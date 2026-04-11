# eesdr3-repeaterbook

Tools for importing [RepeaterBook](https://www.repeaterbook.com) repeater data into [ExpertSDR3](https://www.expertelectronics.ru/software/expertsdr3/).

## Background

ExpertSDR3 stores station memory lists in a proprietary JSON format (`.sbj`). RepeaterBook — the community-maintained repeater directory — exports data as CSV and KML. This repo contains a conversion script and sample data files for 2-meter (144–148 MHz) FM repeaters.

## Files

| File | Description |
|------|-------------|
| `rb_to_eesdr3.py` | Conversion script (Python 3, stdlib only) |
| `RB_*.csv` | RepeaterBook CSV export(s) |
| `repeaters_*.kml` | RepeaterBook KML export(s) — used for distance sorting |
| `2m-stations.sbj` | Reference ExpertSDR3 station file |
| `ADR-001-rb-to-eesdr3-converter.md` | Architecture Decision Record documenting converter design |

## Requirements

- Python 3.6 or later
- No third-party packages

## Usage

### Basic conversion (preserves CSV row order)

```
python rb_to_eesdr3.py RB_export.csv output.sbj
```

### Sort by output frequency

```
python rb_to_eesdr3.py RB_export.csv output.sbj --sort freq
```

### Sort by distance from your location (closest first)

```
python rb_to_eesdr3.py RB_export.csv output.sbj --sort distance --kml repeaters_export.kml
```

Distance sorting requires a KML export from the same RepeaterBook query. The KML provides the lat/lon coordinates that the CSV omits.

### Full argument reference

```
usage: rb_to_eesdr3.py [-h] [--sort {input,freq,distance}] [--kml KML] input output

positional arguments:
  input                     Input RepeaterBook CSV file
  output                    Output ExpertSDR3 .sbj file

optional arguments:
  --sort {input,freq,distance}
                            Output sort order (default: input)
                              input     - preserve CSV row order
                              freq      - ascending by output frequency
                              distance  - closest to furthest from operator location
  --kml KML                 KML file with repeater coordinates (required for --sort distance)
```

## Exporting from RepeaterBook

1. Go to [repeaterbook.com](https://www.repeaterbook.com) and run a search (e.g., by state or proximity).
2. Export **CSV** — used as the primary input file.
3. Export **KML** (Google Earth) — used only when sorting by distance.

Both exports should come from the same search query so the callsigns match between files.

## Importing into ExpertSDR3

1. Run the conversion script to produce a `.sbj` file.
2. In ExpertSDR3, open the Station List manager.
3. Use **Import** to load the `.sbj` file, or replace an existing station list file directly.

## Operator Location

Distance sorting is computed from Maidenhead grid square **EM73qv** (33.896°N, 84.625°W). To use your own location, edit the `MY_LAT` and `MY_LON` constants near the top of `rb_to_eesdr3.py`.

## Data Conventions

### Offset calculation

The standard 2-meter offset is 600 kHz. Direction follows the RepeaterBook `Offset` column:

- `-` → −600,000 Hz
- `+` → +600,000 Hz
- `s` → calculated from `(Input Freq − Output Freq)` to capture non-standard offsets

### CTCSS tones

Tones are mapped using the standard EIA 38-tone table (1-indexed). If only one of uplink/downlink tone is specified, the same index is used for both Tx and Rx. `CSQ` (carrier squelch) is treated as no tone.

### Station label format

```
CALL - Location    (e.g., "NF4GA - Sandy Springs")
```

### Skipped rows

Rows with an unrecognized CTCSS tone (not in the EIA table) are skipped and reported as warnings on stdout.

## Architecture

Design decisions are documented in [ADR-001-rb-to-eesdr3-converter.md](ADR-001-rb-to-eesdr3-converter.md).
