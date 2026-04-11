#!/usr/bin/env python3
"""
rb_to_eesdr3.py - Convert RepeaterBook CSV export to ExpertSDR3 JSON format.

Usage: python rb_to_eesdr3.py <input.csv> <output.sbj> [--sort {input,freq,distance}] [--kml <file.kml>]
"""

import argparse
import csv
import json
import math
import sys
import xml.etree.ElementTree as ET

# Standard EIA CTCSS tone table, 1-indexed.
# Index 0 is unused; index 1 = 67.0 Hz, index 4 = 77.0 Hz, index 12 = 100.0 Hz.
CTCSS_TONES = [
    None,   # 0 - unused
    67.0,   # 1
    71.9,   # 2
    74.4,   # 3
    77.0,   # 4
    79.7,   # 5
    82.5,   # 6
    85.4,   # 7
    88.5,   # 8
    91.5,   # 9
    94.8,   # 10
    97.4,   # 11
    100.0,  # 12
    103.5,  # 13
    107.2,  # 14
    110.9,  # 15
    114.8,  # 16
    118.8,  # 17
    123.0,  # 18
    127.3,  # 19
    131.8,  # 20
    136.5,  # 21
    141.3,  # 22
    146.2,  # 23
    151.4,  # 24
    156.7,  # 25
    162.2,  # 26
    167.9,  # 27
    173.8,  # 28
    179.9,  # 29
    186.2,  # 30
    192.8,  # 31
    203.5,  # 32
    210.7,  # 33
    218.1,  # 34
    225.7,  # 35
    233.6,  # 36
    241.8,  # 37
    250.3,  # 38
]

# Reverse lookup: Hz value -> 1-based index
TONE_TO_INDEX = {tone: idx for idx, tone in enumerate(CTCSS_TONES) if tone is not None}

# My location: Maidenhead EM73qv center
MY_LAT = 33.896
MY_LON = -84.625


def parse_tone(value):
    """
    Parse a CTCSS tone field from the CSV.
    Returns the float Hz value, or None if empty, invalid, or CSQ.
    CSQ (Carrier Squelch) means no tone is used.
    """
    if not value or value.strip().upper() == "CSQ":
        return None
    try:
        return float(value.strip())
    except ValueError:
        return None


def tone_to_index(hz):
    """
    Map a CTCSS frequency in Hz to its 1-based table index.
    Uses a small tolerance (0.15 Hz) to handle floating point representation.
    Returns None if the tone is not found in the table.
    """
    if hz is None:
        return None
    if hz in TONE_TO_INDEX:
        return TONE_TO_INDEX[hz]
    # Tolerance match for any float precision issues in the CSV
    for tone, idx in TONE_TO_INDEX.items():
        if abs(tone - hz) < 0.15:
            return idx
    return None


def haversine_miles(lat1, lon1, lat2, lon2):
    """Return great-circle distance in miles between two lat/lon points."""
    R = 3958.8
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2
         + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2))
         * math.sin(dlon / 2) ** 2)
    return R * 2 * math.asin(math.sqrt(a))


def load_kml_coords(kml_path):
    """
    Parse a RepeaterBook KML file and return a dict mapping callsign -> (lat, lon).
    Coordinates in the KML are stored as lon,lat,alt.
    """
    ns = {"kml": "http://www.opengis.net/kml/2.2"}
    tree = ET.parse(kml_path)
    root = tree.getroot()

    coords = {}
    for placemark in root.findall(".//kml:Placemark", ns):
        name_el = placemark.find("kml:name", ns)
        coord_el = placemark.find(".//kml:coordinates", ns)
        if name_el is None or coord_el is None:
            continue
        call = name_el.text.strip()
        parts = coord_el.text.strip().split(",")
        if len(parts) >= 2:
            lon, lat = float(parts[0]), float(parts[1])
            coords[call] = (lat, lon)
    return coords


def convert_row(row, row_num):
    """
    Convert a single RepeaterBook CSV row to an ExpertSDR3 station dict.
    row_num is used only for error reporting.
    """
    output_freq_mhz = float(row["Output Freq"])
    input_freq_mhz = float(row["Input Freq"])
    offset_dir = row["Offset"].strip()

    output_freq_hz = round(output_freq_mhz * 1_000_000)

    if offset_dir == "-":
        repeater_offset_hz = -600000
    elif offset_dir == "+":
        repeater_offset_hz = 600000
    else:
        # Non-standard offset (marked 's'): calculate from actual frequencies
        repeater_offset_hz = round((input_freq_mhz - output_freq_mhz) * 1_000_000)

    uplink_hz = parse_tone(row.get("Uplink Tone", ""))
    downlink_hz = parse_tone(row.get("Downlink Tone", ""))

    # If one tone is present and the other is missing, use the same for both
    if uplink_hz is not None and downlink_hz is None:
        downlink_hz = uplink_hz
    elif downlink_hz is not None and uplink_hz is None:
        uplink_hz = downlink_hz

    tx_index = tone_to_index(uplink_hz)
    rx_index = tone_to_index(downlink_hz)

    if tx_index is None and uplink_hz is not None:
        raise ValueError(f"Unknown Uplink Tone {uplink_hz} Hz — not in CTCSS table")
    if rx_index is None and downlink_hz is not None:
        raise ValueError(f"Unknown Downlink Tone {downlink_hz} Hz — not in CTCSS table")

    ctcss_enabled = tx_index is not None

    call = row.get("Call", "").strip()
    location = row.get("Location", "").strip()
    comment = f"{call} - {location}" if location else call

    return {
        "comment": comment,
        "ctcss": ctcss_enabled,
        "ctcssMode": 2,
        "ctcssRxIndex": rx_index if rx_index is not None else 0,
        "ctcssTxIndex": tx_index if tx_index is not None else 0,
        "editComment": False,
        "freq": output_freq_hz,
        "modulation": "NFM",
        "repeater": True,
        "repeaterOffset": repeater_offset_hz,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Convert a RepeaterBook CSV export to ExpertSDR3 JSON (.sbj) format."
    )
    parser.add_argument("input", help="Input RepeaterBook CSV file")
    parser.add_argument("output", help="Output ExpertSDR3 .sbj file")
    parser.add_argument(
        "--sort",
        choices=["input", "freq", "distance"],
        default="input",
        help=(
            "Output sort order: 'input' preserves CSV order (default), "
            "'freq' sorts by output frequency, "
            "'distance' sorts by distance from EM73qv (requires --kml)"
        ),
    )
    parser.add_argument(
        "--kml",
        help="RepeaterBook KML file for coordinates (required when --sort distance)",
    )
    args = parser.parse_args()

    if args.sort == "distance" and not args.kml:
        parser.error("--kml is required when using --sort distance")

    kml_coords = {}
    if args.kml:
        kml_coords = load_kml_coords(args.kml)

    # Collect as list of (entry, call) to allow sorting before re-indexing
    rows = []
    warnings = []

    with open(args.input, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row_num, row in enumerate(reader, start=2):  # row 1 is the header
            try:
                entry = convert_row(row, row_num)
                call = row.get("Call", "").strip()
                rows.append((entry, call))
            except Exception as exc:
                warnings.append(f"  Row {row_num} ({row.get('Call', '?')}): {exc}")

    if args.sort == "freq":
        rows.sort(key=lambda x: x[0]["freq"])
    elif args.sort == "distance":
        missing = set()

        def distance_key(item):
            entry, call = item
            if call in kml_coords:
                lat, lon = kml_coords[call]
                return haversine_miles(MY_LAT, MY_LON, lat, lon)
            missing.add(call)
            return float("inf")  # unknown coords sort to the end

        rows.sort(key=distance_key)
        if missing:
            print(f"  Note: {len(missing)} station(s) not found in KML (sorted to end): {', '.join(sorted(missing))}")

    stations = {str(i): entry for i, (entry, _) in enumerate(rows)}

    with open(args.output, "w", encoding="utf-8") as outfile:
        json.dump(stations, outfile, indent=4)

    print(f"Converted {len(stations)} station(s) -> {args.output}")
    if warnings:
        print(f"\n{len(warnings)} warning(s) — rows skipped:")
        for w in warnings:
            print(w)


if __name__ == "__main__":
    main()
