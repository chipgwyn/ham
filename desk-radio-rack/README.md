# HAM Radio Shelf Stack

I have several pieces of ham radio gear I want to stack on top of each other.  The goal being to take up less desk space, consolidate wiring,
and maintain good airflow.

## Stack items:

| Device | Width | Depth | Height | Notes |
|---|---|---|---|---|
| SunSDR2Pro Radio | 165 mm (6.5") | 165 mm (6.5") | 35 mm (1.4") | Official manual; one source lists depth as 100 mm — may vary by version. Noctua NF-S12B fan mounted on top: 120 × 120 × 25 mm — adds 25 mm to effective height |
| RM Italy BLA350 Plus | 358 mm (14.1") | 270 mm (10.6") | 160 mm (6.3") | 13.5 kg / 29.7 lbs |
| LDG AT-600 Pro II Tuner | 267 mm (10.5") | 216 mm (8.5") | 70 mm (2.75") | 1.5 kg / 3 lbs 6 oz |
| CN-801 Power Meter | 150 mm (5.9") | 120 mm (4.7") | 115 mm (4.5") | Daiwa CN-801HP; ~0.9 kg |
| Mirage B1016 Amplifier | 140 mm (5.5") | 305 mm (12") | 76 mm (3") | 13.6 VDC @ 20–25A |

## Power Supplies

| Device | Width | Depth | Height | Notes |
|---|---|---|---|---|
| Yaesu FP-1023A | 178 mm (7") | 210 mm (8.25") | 56 mm (2.2") | 13.8V / 23A switching; 1.6 kg / 3.5 lbs |
| Mean Well LRS-100-15 | 129 mm (5.08") | 97 mm (3.82") | 30 mm (1.18") | 15V / 7A (105W max); fanless, open-frame enclosed |
| LM2596 Buck Converter | 66 mm (2.6") | 35 mm (1.4") | ~14 mm | PCB module; 4–40V in, 1.25–37V adjustable out; LED voltmeter display |

## Notable Items

- The SunSDR2Pro has a fan attached Noctua NF-S12B attached to the top
- The LDG tuner has a 100W Dummy Load plugged into Antenna Port 2, basically this: https://a.co/d/0abaO3BB

## Airflow

Both the SunSDR2Pro and RM Italy Amplifier need good airflow, that is a requirement

---

## Stack Configuration

### Tier Layout (bottom → top)

| Tier | Devices | Arrangement | Width | Depth | Height |
|---|---|---|---|---|---|
| Bottom | RM Italy BLA350 Plus | single | 358 mm | 270 mm | 160 mm |
| — | *airflow gap* | — | — | — | 50 mm |
| Middle | LDG AT-600 Pro II | bottom | 267 mm | 216 mm | 70 mm |
| Middle | Mirage B1016 | stacked on LDG | 140 mm | 305 mm | 76 mm |
| — | *shelf* | — | — | — | ~5 mm |
| Top | SunSDR2Pro + CN-801 | side by side | 315 mm | 165 mm | 115 mm |
| — | *airflow gap (SunSDR fan)* | — | — | — | 50 mm |

### Full Stack Outer Dimensions

| Dimension | Value | Constraint |
|---|---|---|
| **Width** | ~375 mm (14.8") | BLA350 (358 mm) |
| **Depth** | ~325 mm (12.8") | Mirage (305 mm) + 20 mm cable clearance |
| **Height** | ~535 mm (21.1") | Sum of tiers + airflow gaps + shelf material |

### Height Breakdown

```
 50 mm  — airflow clearance above SunSDR fan
115 mm  — top tier: SunSDR2Pro + CN-801 (CN-801 height drives this)
  5 mm  — shelf
 76 mm  — Mirage B1016 (on top of LDG)
 70 mm  — LDG AT-600 Pro II
 50 mm  — airflow clearance above BLA350
160 mm  — RM Italy BLA350 Plus
──────
526 mm + ~10 mm base/structure = ~535 mm
```

---

## Diagrams

### Front View

```
      ←————————————————— 375 mm —————————————————→
      ┌─────────────────────────────────────────────┐ ╌╌ top
      │              [ airflow space ]              │      50 mm
      ├──────────────────┬──────────────────────────┤
      │   SunSDR2Pro     │        CN-801            │      115 mm
      │   165 mm wide    │       150 mm wide        │
      ├──────────────────┴──────────────────────────┤
      │          ┌──────────────┐                   │      76 mm
      │          │ Mirage B1016 │                   │
      │          │  140 mm wide │                   │
      ├──────────┴──────────────┴───────────────────┤
      │           LDG AT-600 Pro II                 │      70 mm
      │              267 mm wide                    │
      ├─────────────────────────────────────────────┤
      │              [ airflow space ]              │      50 mm
      ├─────────────────────────────────────────────┤
      │                                             │
      │           RM Italy BLA350 Plus              │      160 mm
      │               358 mm wide                  │
      │                                             │
      └─────────────────────────────────────────────┘ ╌╌ base
```

### Side View (left side, front → back)

```
  ←————————————————— 325 mm —————————————————→
  ┌─────────────────────────────────────────────┐ ╌╌ top
  │            [ airflow space ]                │      50 mm
  ├──────────────────┐                          │
  │     CN-801       │                          │      115 mm
  │    120 mm deep   │  (SunSDR: 165 mm deep)   │
  ├──────────────────┴──────────────────────────┤
  │                  ┌──────────────────────────┤      76 mm
  │                  │       Mirage B1016       │
  │                  │       305 mm deep        │
  ├──────────────────┤                          │      70 mm
  │  LDG AT-600      │                          │
  │   216 mm deep    │                          │
  ├──────────────────┴──────────────────────────┤
  │            [ airflow space ]                │      50 mm
  ├─────────────────────────────────────────────┤
  │                                             │
  │           RM Italy BLA350 Plus              │      160 mm
  │               270 mm deep                  │
  │                                             │
  └─────────────────────────────────────────────┘ ╌╌ base
```

