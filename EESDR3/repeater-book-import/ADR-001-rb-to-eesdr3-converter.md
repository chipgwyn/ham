# ADR-001: RepeaterBook CSV to ExpertSDR3 JSON Converter

**Status:** Accepted  
**Date:** 2026-04-11

## Context

ExpertSDR3 stores station lists in a proprietary JSON format (`.sbj`). RepeaterBook exports repeater data as CSV. A conversion tool was needed to import RepeaterBook data into ExpertSDR3 without manual re-entry.

## Decisions

### 1. Offset Calculation

**Rule:** Use the `Offset` direction column as a hint, not as the sole source of truth.

- If `Offset` is `-`: use the standard 2-meter offset of **-600000 Hz**
- If `Offset` is `+`: use the standard 2-meter offset of **+600000 Hz**
- If `Offset` is `s`: the repeater uses a non-standard offset — **calculate from `(Input Freq - Output Freq) × 1,000,000`**, rounded to the nearest integer Hz

**Rationale:** Some entries marked `s` (simplex) actually have distinct input and output frequencies with non-standard offsets (e.g., WC4RAV at -940 kHz, WX4AUX at +2260 kHz). The `Offset` column direction alone is insufficient for these cases.

### 2. CTCSS Tone Handling

**Rule:** Use the standard EIA CTCSS tone table, **1-indexed** (index 1 = 67.0 Hz, index 4 = 77.0 Hz, index 12 = 100.0 Hz).

- If both Uplink and Downlink tones are present: map each independently to `ctcssTxIndex` and `ctcssRxIndex`
- If only one tone is present: use the same index for both Tx and Rx
- If neither tone is present: set `ctcss: false`, `ctcssTxIndex: 0`, `ctcssRxIndex: 0`

**Rationale:** ExpertSDR3 requires separate Tx/Rx indices. Using the available tone for both sides is the safest default when one is absent.

### 3. CSQ (Carrier Squelch) Tone Values

**Rule:** Treat `CSQ` in a tone field the same as an empty value — no tone is assigned.

Apply decision 2 (same index for both) when the other tone field has a valid Hz value.

**Rationale:** CSQ indicates the repeater uses no CTCSS tone on that side. Since ExpertSDR3 needs an index, the paired tone (if present) is used for both.

### 4. Modulation

**Rule:** Set `modulation: "NFM"` for all entries.

**Rationale:** The target use case is FM voice operation. Repeaters listed with digital modes (DSTAR, DMR, P-25, Fusion, etc.) also support FM. Digital-specific columns are ignored entirely.

### 5. Comment / Station Label Format

**Rule:** Format as `"CALL - Location"` (e.g., `"NF4GA - Sandy Springs"`).

**Rationale:** Matches the convention already used in existing `.sbj` station files. Callsign-first aids quick visual scanning of the station list in the ExpertSDR3 UI.

### 6. Repeater Flag

**Rule:** Set `repeater: true` for all entries.

**Rationale:** All entries in a RepeaterBook export are repeaters by definition. Even entries marked `s` in the Offset column have distinct input/output frequencies and are operated as repeaters.

### 7. Fixed Fields

The following fields are set to constant values for all entries, matching the pattern observed in existing `.sbj` files:

| Field | Value |
|-------|-------|
| `ctcssMode` | `2` |
| `editComment` | `false` |
| `modulation` | `"NFM"` |

### 8. Dependencies

**Rule:** Use Python standard library only (`csv`, `json`, `argparse`, `math`, `xml.etree.ElementTree`).

**Rationale:** Minimizes installation friction. No third-party packages required.

### 9. Output Sort Order

**Rule:** Provide three sort modes via `--sort {input,freq,distance}`, defaulting to `input`.

- `input`: preserves CSV row order (original behavior, default)
- `freq`: ascending by output frequency (`freq` field in Hz)
- `distance`: ascending by great-circle distance from the operator's location, closest first

**Rationale:** Different workflows call for different orderings. Frequency order matches how a traditional memory scanner steps through channels. Distance order is useful when operating mobile or evaluating which repeaters are most accessible from a given location.

### 10. Distance Sorting and KML Coordinates

**Rule:** For `--sort distance`, require a `--kml` argument pointing to a RepeaterBook KML export. Parse coordinates from the KML `<Placemark>` elements (callsign from `<name>`, position from `<coordinates>` in lon,lat,alt order). Distance is computed using the Haversine formula in miles. Stations whose callsign is not found in the KML sort to the end.

**Rationale:** The RepeaterBook CSV does not include coordinates. The KML export from the same query contains per-repeater lat/lon. Matching by callsign links the two files without requiring a separate geocoding API call.

### 11. Operator Home Location

**Rule:** The operator's home coordinates are stored as module-level constants `MY_LAT` / `MY_LON`, computed once from Maidenhead grid square EM73qv (center: 33.896°N, 84.625°W).

**Rationale:** Maidenhead is the standard amateur radio location reference. Computing the center at write-time avoids a runtime lookup and keeps the script dependency-free. The constants are clearly labeled so any operator can substitute their own grid square.

## Output Format

The `.sbj` output is a JSON object with sequential integer string keys (`"0"`, `"1"`, ...), matching the ExpertSDR3 native format. Fields within each entry are sorted alphabetically to match existing file conventions.

## Consequences

- Non-standard CTCSS tones not present in the EIA table will cause that row to be skipped with a warning printed to stdout.
- All digital-mode metadata (Digital Access codes, mode flags) is discarded in the output.
- The `Offset` direction column (`s`/`-`/`+`) from RepeaterBook is not written to the output; offset is always stored as a signed Hz integer.
