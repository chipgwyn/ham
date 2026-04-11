#!/usr/bin/env python3
"""
postprocess.py - Post-process an ExpertSDR3 .sbj file with custom station edits.

Edits applied (in order):
  1. Insert 146.520 MHz simplex calling frequency as the first entry.
  2. Move the WX4PCA 146.955 repeater to the second slot and rename it 'SCARS',
     removing it from its original position.

Usage: python postprocess.py <input.sbj> <output.sbj>
"""

import argparse
import json
import sys

# --- Entry definitions ---

SIMPLEX_146520 = {
    "comment": "146.520 Simplex",
    "ctcss": False,
    "ctcssMode": 2,
    "ctcssRxIndex": 0,
    "ctcssTxIndex": 0,
    "editComment": False,
    "freq": 146520000,
    "modulation": "NFM",
    "repeater": False,
    "repeaterOffset": 0,
}

SCARS_FREQ = 146955000


def find_wx4pca(stations):
    """Return the entry dict for the WX4PCA 146.955 repeater, or None."""
    for entry in stations:
        if entry["freq"] == SCARS_FREQ and "WX4PCA" in entry.get("comment", ""):
            return entry
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Post-process an ExpertSDR3 .sbj file with custom station edits."
    )
    parser.add_argument("input", help="Input .sbj file")
    parser.add_argument("output", help="Output .sbj file")
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as f:
        raw = json.load(f)

    # .sbj files are dicts keyed "0", "1", ... — convert to an ordered list
    stations = [raw[k] for k in sorted(raw, key=lambda k: int(k))]

    # --- Edit 1: locate WX4PCA 146.955 and pull it out ---
    scars_entry = find_wx4pca(stations)
    if scars_entry is None:
        print("WARNING: WX4PCA 146.955 not found in input — it will not be inserted at slot 2.")
    else:
        stations.remove(scars_entry)
        scars_entry = dict(scars_entry)   # copy before mutating
        scars_entry["comment"] = "SCARS"

    # --- Edit 2: build final ordered list ---
    result = [SIMPLEX_146520]
    if scars_entry is not None:
        result.append(scars_entry)
    result.extend(stations)

    # Re-key as "0", "1", ...
    output = {str(i): entry for i, entry in enumerate(result)}

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print(f"Written {len(output)} station(s) -> {args.output}")


if __name__ == "__main__":
    main()
