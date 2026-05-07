# Project Blueprint: The "Silicone 106" POTA Doublet

# WARNING!  THIS IS ALL AI DRIVEN AND IS PROBABLY INCORRECT IN SOME PLACES!!

# THIS IS AN UNFINISHED DRAFT!

**Target Use:** High-Efficiency Portable / POTA Operations  
**Design Philosophy:** Minimal weight, zero solder points, and high flexibility for rapid deployment.

---

## 1. System Specifications

### Physical Dimensions
- **Element Length:** 32.7 ft per leg (half-wave at 7.150 MHz; cut from ~33 ft and trimmed to resonance)
- **Feedline Length:** 43 ft (optimized to avoid "tuning holes" across 40–10m)
- **Configuration:** Inverted-V, 33 ft apex
- **Element wire ends:** 27.6 ft horizontal / 15.5 ft AGL from mast center
- **String (wire end to stake):** ~29 ft per side
- **Stake positions:** 52 ft horizontal from mast base (standard POTA33H setup)
- **Stake-to-stake footprint:** 104 ft

### Materials
- **Wire:** 20 AWG Silicone-coated, individual strands (250 ft spool)
- **Spacers:** 3D-Printed PETG (2.0-inch/50.8mm wire-to-wire spacing, 10-inch intervals)
- **Mast:** POTA33H Heavy Duty (33 ft Carbon Fiber)
- **Tuner:** MFJ-945C (Manual T-Network with internal 4:1 balun)
- **Jumper:** 5-ft RG-316 or RG-8X (Tuner to Radio)
- **Guy string:** ~29 ft lightweight string per side (wire tip to ground stake)

### Power & Impedance
- **Max Power (MFJ-945C):** 300W PEP SSB / 150W CW. POTA ops typically 5–100W.
- **Feedpoint Impedance:** Varies widely by band (50Ω–5000Ω+). Elements are resonant on 40m; tuner handles matching on all other bands.
- **Ladder Line Characteristic Impedance:** ~579Ω at 2-inch wire spacing with 20 AWG wire. Note: MFJ-945C balanced output tops out near 600Ω — verify match on high-impedance bands.
- **Tuner Balanced Output Range:** ~25–600Ω. The 43 ft feedline was chosen to keep common HF bands inside this window. If a tuning hole is encountered, adjust feedline length in 1-foot increments.
- **Coax Jumper Impedance:** 50Ω unbalanced (radio to tuner input).
- **Target Bands:** 40m (resonant), 20m, 17m, 15m, 12m, 10m (tuner-matched). Higher bands will exhibit multi-lobe radiation patterns as the elements become multiple half-wavelengths long.

---

## 2. Fabrication Guide

### Wire Cuts

Elements and feedline are **separate pieces** — this is intentional for portability and field management.

| Piece | Qty | Length | Notes |
|---|---|---|---|
| Element wire | 2 | ~33 ft | Cut long; trim to resonance at 7.150 MHz |
| Feedline wire | 2 | 43 ft | Cut to length; no trimming needed |

All four pieces come from one 250 ft spool with wire to spare.

### Ladder Line Construction

1. Lay the two 43 ft feedline wires parallel.
2. Thread **~52 spacers** at **10-inch intervals** along the pair.
3. Secure each spacer with small zip ties cinched firmly against the silicone jacket to prevent sliding.
4. The 2-inch wire-to-wire spacing gives a characteristic impedance of ~579Ω.

### Element Wire Length Tuning

Elements are cut for 40m resonance, not for multi-band starting length. Trim carefully:

1. Cut each element to **33 ft** (a few inches over the calculated 32.7 ft).
2. Deploy at full operating height before any trimming — ground proximity shifts impedance.
3. Connect an antenna analyzer to the balanced terminals on the MFJ-945C rear (bypassing tuner circuits), or use a balun + analyzer at the feedpoint.
4. Target **7.150 MHz** with R near 50–100Ω and X near zero. The inverted-V configuration will shift resonance slightly lower than a flat dipole — trim in 1-inch increments from both legs equally.
5. Once 40m resonance is confirmed, verify 20m, 15m, and 10m are tunable with the MFJ-945C. If a band is a tuning hole, adjust feedline length in 1-foot increments rather than retrimming the elements.
6. Record final element length in your kit notes.

> **Rule of thumb:** If 40m tunes but a harmonic band is a hole, change feedline length. If 40m won't tune at all, retrim the elements.

### 3D Printing Queue (Prusa Mini / PETG)

- **Center Insulator (x1):** Sourced from Printables, MakerWorld, or Thingiverse — many suitable doublet/dipole center insulators exist. Needs a top mast attachment point and four wire entry points (two elements, two feedline). (5 perimeters, 40% infill.)
- **Feedline Spacers (x55):** 2-inch "dog-bone" design with zip-tie channels. Print 55 for a 43 ft run at 10-inch intervals (~52 needed + spares). (3 perimeters.)
- **End Insulators (x2):** Lightweight 2-hole dog-bones for element-wire-to-string connection at the wire tips.
- **Wire Winder (x1):** Large figure-8 or H-frame winder. Essential for silicone wire — do not skip.

---

## 3. Deployment & Operating Guide

### The Setup

1. **Prep:** Attach the T-shaped center insulator to the POTA33H mast's paracord loop via S-Biner.
2. **Raise:** Extend mast to full 33 ft while walking out the 43 ft ladder line toward the operating position.
3. **Elements:** Run each element wire outward from the center insulator at the apex.
4. **String:** Attach ~29 ft of lightweight string to each element wire end (via end insulator).
5. **Stake:** Run string to ground stakes at ~52 ft horizontal from the mast base. This gives an apex angle of ~115° and element wire ends floating at ~15.5 ft AGL.
6. **Connect:** Plug the two ladder line ends into the **balanced binding posts** on the rear of the MFJ-945C.
7. **Clearance:** Ensure the ladder line drops away from the conductive carbon fiber mast at a slight angle — ladder line must not touch the mast.

### Tuning Procedures

- **40m:** Elements are resonant here. The MFJ-945C should find a 1:1 match easily.
- **20m / 15m / 10m:** Harmonic bands — feedpoint impedance is more predictable but may still need tuner adjustment.
- **17m / 12m:** Non-harmonic bands — tuner will work harder; the 43 ft feedline was chosen to keep these within the tuner's range.
- **RFI Check:** If the tuner chassis feels "hot" or the radio resets, ensure the 5 ft coax jumper is away from the ladder line. Use a snap-on ferrite on the coax jumper if needed.

---

## 4. Maintenance Notes

- **Silicone Care:** Wipe down wire after muddy activations; silicone attracts debris but cleans easily.
- **Zip Tie Check:** Inspect zip ties on spacers periodically; PETG is durable but soft silicone wire can shift under heavy wind load.
- **Storage:** Always use a **Figure-8 wrap** when winding. Do NOT coil in circles — the ladder line will become a tangled nightmare for your next activation.

---

## 5. Geometry & Deployment Coordinates

### Modeled Configuration

- **Apex height:** 33 ft
- **Element leg length:** 32.7 ft each
- **Apex angle:** ~115° (57.5° each leg from vertical)
- **Element wire end height AGL:** ~15.5 ft
- **Element wire end horizontal reach:** 27.6 ft from mast
- **String per side:** ~29 ft (element tip to ground stake)
- **Stake distance from mast:** 52 ft (existing standard POTA33H setup)
- **Stake-to-stake footprint:** 104 ft

### Coordinate Reference Points

**Origin:** Ground level directly below the apex. X = along antenna legs, Y = perpendicular (feedline/operator direction), Z = vertical up.

| Point | X (ft) | Y (ft) | Z (ft) | Description |
|---|---|---|---|---|
| Stake 1 | -52 | 0 | 0 | Ground stake — string anchors here |
| Wire tip 1 | -27.6 | 0 | 15.5 | Element wire end / string attaches here |
| Apex | 0 | 0 | 33.0 | Center insulator / mast top |
| Wire tip 2 | +27.6 | 0 | 15.5 | Element wire end / string attaches here |
| Stake 2 | +52 | 0 | 0 | Ground stake — string anchors here |
| Feedline ground | 0 | 0 | 0 | Feedline reaches ground at mast base |
| Tuner | 0 | +10 | 0 | ~10 ft of feedline slack runs to operator position |

The feedline (43 ft) is 10 ft longer than the mast height; the excess lies on the ground toward the operating position. Orient the Y axis toward your operating position when deploying.
