# HAM Radio Shelf Stack — HomeRacker Bill of Materials

## Frame Geometry

| Dimension | Base Units | mm | Notes |
|-----------|-----------|-----|-------|
| Interior clear width | 24u | 360mm | Clears BLA350 (358mm) with 1mm per side |
| Interior clear depth | 22u | 330mm | Clears Mirage (305mm) with 25mm cable clearance |
| Total structural height | 36u | 540mm | Includes 4 connector rows |

### Bay Layout (bottom → top)

| Bay | Units | Height | Contents | Clearance check |
|-----|-------|--------|----------|-----------------|
| Bay 1 | 14u | 210mm | RM Italy BLA350 Plus | 160mm device + 50mm airflow = 210mm ✓ |
| _connector row_ | 1u | 15mm | Shelf 1 connectors | — |
| Bay 2 | 10u | 150mm | LDG AT-600 Pro II + Mirage B1016 | 70+76=146mm, 4mm spare ✓ |
| _connector row_ | 1u | 15mm | Shelf 2 connectors | — |
| Bay 3 | 8u | 120mm | SunSDR2Pro + CN-801 side by side | CN-801=115mm, 5mm spare; SunSDR fan at 60mm has 60mm clearance (>50mm req) ✓ |
| _connector row_ | 1u | 15mm | Top frame connectors | — |

> **Note:** The BLA350 (13.5 kg) sits directly on the desk floor inside Bay 1 — the frame stands around it. It does not rest on a 3D-printed shelf.

> **Airflow:** 50mm open clearance above the top frame for the Noctua fan on the SunSDR2Pro is satisfied by leaving 50mm between the top of the rack and any overhead obstruction.

---

## 3D-Printed Parts

All parts use the [HomeRacker Core](https://github.com/kellerlabs/homeracker/tree/main/models/core) parametric OpenSCAD models.

### Vertical Supports (Corner Posts)

| Qty | `support(units)` | Height | Location |
|-----|-----------------|--------|----------|
| 4 | `support(14)` | 210mm | Bay 1 corner posts |
| 4 | `support(10)` | 150mm | Bay 2 corner posts |
| 4 | `support(8)` | 120mm | Bay 3 corner posts |
| **12 total** | | | |

### Horizontal Supports (Rails)

| Qty | `support(units)` | Length | Location |
|-----|-----------------|--------|----------|
| 8 | `support(24)` | 360mm | Front & back rails at all 4 levels |
| 8 | `support(22)` | 330mm | Left & right side rails at all 4 levels |
| **16 total** | | | |

### Connectors

All connectors are standard (no pull-through). Use `connector(dimensions, directions, "none")`.

| Qty | OpenSCAD call | Arms | Location |
|-----|--------------|------|----------|
| 4 | `connector(3, 3, "none")` | up + front + side | Base (floor level), 1 per corner |
| 4 | `connector(3, 4, "none")` | up + down + front + side | Shelf 1 (LDG level), 1 per corner |
| 4 | `connector(3, 4, "none")` | up + down + front + side | Shelf 2 (SunSDR level), 1 per corner |
| 4 | `connector(3, 3, "none")` | down + front + side | Top frame, 1 per corner |
| **16 total** | | 8× 3-arm, 8× 4-arm | |

### Feet

| Qty | Part | Notes |
|-----|------|-------|
| 4 | `foot()` | Plugs into base connector arms. Print in **TPU** for grip and load distribution. |

### Lock Pins

| Level | Connectors | Arms each | Pins |
|-------|-----------|-----------|------|
| Base | 4 | 3 | 12 |
| Shelf 1 | 4 | 4 | 16 |
| Shelf 2 | 4 | 4 | 16 |
| Top | 4 | 3 | 12 |
| **Total** | | | **56 pins** |

Print the **100-pin plate** from [MakerWorld](https://makerworld.com/en/models/1317298-homeracker-core) — you'll have spares for inevitable losses.

---

## Non-Printed Parts (Shelves)

The shelf panels span 360 × 330mm — too large for most print beds and load-bearing for HAM gear.

| Qty | Item | Size | Purpose | Notes |
|-----|------|------|---------|-------|
| 1 | Shelf board (Shelf 1) | 360 × 330mm | Holds LDG + Mirage (~3kg) | 12mm Baltic birch plywood recommended. Cut to fit inside the horizontal rails. |
| 1 | Shelf board (Shelf 2) | 360 × 330mm | Holds SunSDR2Pro + CN-801 (~1.5kg) | 6mm plywood or 3mm aluminum plate. Alternatively, print the HomeRacker Panel in sections (`panel_type=1`, `units_x=24`, `units_y=22`). |

---

## Optional / Recommended Extras

| Qty | Part | Purpose |
|-----|------|---------|
| 1 | [Pinpusher](https://github.com/kellerlabs/homeracker/tree/main/models/pinpusher) | Makes removing lock pins fast without damaging parts |
| 4–8 | [Racklink](https://github.com/kellerlabs/homeracker/tree/main/models/racklink) | Lateral bracing between front/back column pairs on each side — adds rigidity to the 540mm-tall frame |

---

## Print Summary

| Category | Qty |
|----------|-----|
| Vertical supports | 12 |
| Horizontal supports | 16 |
| Connectors | 16 |
| Feet | 4 |
| Lock pins | 56 (print 100-pin plate) |
| **Total structural parts** | **48** (excl. pins) |

### Filament Notes

- **Supports & connectors:** PLA Matte or PETG (rigid)
- **Feet:** TPU (grip/load distribution)
- **Lock pins:** Any rigid PLA/PETG
- All filament types are cross-compatible in assembly per the HomeRacker documentation

---

## Frame Diagram (HomeRacker layout)

```
      ←——————————— 390mm outer ———————————→
      ←—————— 360mm interior clear —————→

      ┌─────────────────────────────────────┐  ← top frame connectors (36u / 540mm)
      │       [ 50mm Noctua fan             │
      │         clearance above this ]      │
      ├──────────────────┬──────────────────┤  ← shelf 2 connectors (28u / 420mm)
      │   SunSDR2Pro     │    CN-801        │    Bay 3: 8u = 120mm
      │   165mm wide     │    150mm wide    │
      │   (fan on top)   │    115mm tall    │
      ├──────────────────┴──────────────────┤  ← shelf 1 connectors (18u / 270mm)
      │  LDG AT-600 Pro II (bottom)         │    Bay 2: 10u = 150mm
      │  Mirage B1016 (stacked on top)      │
      ├─────────────────────────────────────┤  ← base connectors (0u / 0mm)
      │                                     │    Bay 1: 14u = 210mm
      │   RM Italy BLA350 Plus              │
      │   (sits on desk inside frame)       │
      │                                     │
      └─────────────────────────────────────┘  ← desk surface / feet
```

---

## Source Files

- HomeRacker Core (GitHub): https://github.com/kellerlabs/homeracker/tree/main/models/core
- HomeRacker Core (MakerWorld, pre-sliced): https://makerworld.com/en/models/1317298-homeracker-core
- Foot insert: https://github.com/kellerlabs/homeracker/tree/main/models/foot
- Panel (optional shelves): https://github.com/kellerlabs/homeracker/tree/main/models/panel
- Pinpusher: https://github.com/kellerlabs/homeracker/tree/main/models/pinpusher
- Racklink: https://github.com/kellerlabs/homeracker/tree/main/models/racklink
