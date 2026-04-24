# 📡 Project Blueprint: The "Silicone 106" POTA Doublet
**Target Use:** High-Efficiency Portable / POTA Operations  
**Design Philosophy:** Minimal weight, zero solder points, and high flexibility for rapid deployment.

---

## 🛠 1. System Specifications

### **Physical Dimensions**
*   **Antenna Span:** 106 feet (Two 53-foot legs).
*   **Feedline Length:** 43 feet (Optimized to avoid "tuning holes").
*   **Configuration:** Inverted-V (33ft center height).
*   **Ground Footprint:** ~82 feet tip-to-tip.

### **Materials**
*   **Wire:** 20 AWG Silicone-coated, individual strands (250ft spool).
*   **Spacers:** 3D-Printed PETG (1.0-inch/25.4mm spacing).
*   **Mast:** POTA33H Heavy Duty (33ft Carbon Fiber).
*   **Tuner:** MFJ-945C (Manual T-Network with internal 4:1 balun).
*   **Jumper:** 5-ft RG-316 or RG-8X (Tuner to Radio).

### **Power & Impedance**
*   **Max Power (MFJ-945C):** 300W PEP SSB / 150W CW. POTA ops typically 5–100W.
*   **Feedpoint Impedance:** Varies widely by band (50Ω–5000Ω+). Not resonant by design — the tuner handles matching.
*   **Ladder Line Characteristic Impedance:** ~450Ω at 1-inch spacing with 20 AWG wire.
*   **Tuner Balanced Output Range:** ~25–600Ω. Bands where the feedpoint impedance falls outside this window are "tuning holes" — the 43ft feedline was chosen to keep common HF bands inside this range.
*   **Coax Jumper Impedance:** 50Ω unbalanced (radio to tuner input).

---

## 🏗 2. Fabrication Guide

### **The "Continuous Wire" Method**
1.  **Cut:** Two (2) identical lengths of **96 feet** each (53ft for the leg + 43ft for the feed).
2.  **Center Transition:** Pass each wire through the 3D-printed Center Insulator at the 53ft mark.
3.  **Ladder Line Construction:** 
    *   Thread **35 spacers** onto the 43ft feedline sections.
    *   Set spacer interval to **15 inches**.
    *   Secure with small zip ties; cinch firmly against the silicone jacket to prevent sliding.

### **Initial Wire Length Tuning**

The doublet's legs don't need to be cut to resonance — the tuner handles that — but the leg length determines which bands are reachable and how gracefully the tuner can match each one. Cut long, then trim.

1.  **Start Long:** Cut legs to **55–56 feet** (2–3 feet over target). Leave the feedline at the full 43 feet.
2.  **First Deployment:** Raise the antenna to operating height. All trimming should be done at the actual operating angle and height, as ground proximity shifts impedance.
3.  **Connect an Antenna Analyzer:** Attach directly to the balanced binding posts on the MFJ-945C's rear (bypassing the tuner circuits) or use a balun + analyzer at the feedpoint.
4.  **Check 40m First (primary band):** Look for a resistance (R) near 50–100Ω and reactance (X) near zero at 7.1–7.3 MHz. The legs are close to a half-wave on 40m at 53ft, so this is your reference point.
5.  **Trim in 1-Inch Increments:** Remove equal lengths from both legs. After each trim, re-measure resistance and reactance. You're moving the half-wave resonance point, not chasing a perfect SWR — just confirm the tuner can match it (SWR < 3:1 before the tuner is a good target).
6.  **Check All Target Bands:** After settling on a leg length, verify 80m, 40m, 20m, 17m, 15m, 10m all produce a match with the MFJ-945C. If a band is a tuning hole (tuner maxes out without reaching 1:1), adjust the feedline length in 1-foot increments rather than retrimming the legs.
7.  **Final Cut:** Once satisfied, trim the excess and melt the silicone jacket tip slightly to prevent fraying. Record the final leg and feedline lengths for your kit notes.

> **Rule of thumb:** If 40m tunes but 20m is a hole, change feedline length. If 40m won't tune, adjust leg length.

### **3D Printing Queue (Prusa Mini / PETG)**
*   **Center Insulator (x1):** Hanging-style plate with top loop hole, two outer leg anchors, and two bottom 1-inch feedline guides. (5 perimeters, 40% infill).
*   **Feedline Spacers (x40):** 1-inch "Dog-bone" design with zip-tie channels. (3 perimeters).
*   **End Insulators (x2):** Lightweight 2-hole dog-bones for leg-to-paracord connection.
*   **Wire Winder (x1):** Large figure-8 or H-frame winder (essential for silicone wire management).

---

## 🚀 3. Deployment & Operating Guide

### **The Setup**
1.  **Prep:** Attach the center insulator to the POTA33H mast’s paracord loop (use an S-Biner).
2.  **Raise:** Extend the mast while walking out the 43ft ladder line.
3.  **Stake:** Anchor the 53ft legs to form an Inverted-V. Maintain a **90° to 120° apex angle**. Ensure the ladder line drops away from the conductive carbon fiber mast at a slight angle.
4.  **Connect:** Plug the two ladder line ends directly into the **balanced binding posts** on the rear of the MFJ-945C.

### **Tuning Procedures**
*   **Low Bands (80m/40m):** The antenna is highly efficient here. Use the MFJ-945C to find a 1:1 match.
*   **High Bands (20m–10m):** The antenna will present multiple lobes (cloverleaf). If you encounter a "touchy" match on 20m, add or subtract 2-3 feet of ladder line "slack" on the ground to shift the impedance.
*   **RFI Check:** If the tuner chassis feels "hot" or the radio resets, ensure the 5ft coax jumper is away from the ladder line. Use a snap-on ferrite on the coax jumper if needed.

---

## 📐 5. Geometry & Deployment Coordinates

### Modeled Configuration
- **Apex height:** 33 ft
- **Leg length:** 53 ft each
- **Apex angle:** 115°
- **Half apex angle:** 57.5° (each leg from vertical)
- **Tip height AGL:** ~4.5 ft (tips staked to ground via paracord)
- **Horizontal reach per leg:** 44.7 ft
- **Tip-to-tip footprint:** ~89.4 ft

> Note: The ~82 ft figure in the specs corresponds to a tighter ~101° apex angle. At the recommended 115°, expect ~89 ft tip-to-tip.

### Coordinate Reference Points

**Origin:** Ground level directly below the apex. X = along antenna legs, Y = perpendicular (feedline/operator direction), Z = vertical up.

| Point | X (ft) | Y (ft) | Z (ft) | Description |
|---|---|---|---|---|
| Tip 1 | -44.7 | 0 | 4.5 | Leg end — stake with paracord |
| Apex | 0 | 0 | 33.0 | Center insulator / mast top |
| Tip 2 | +44.7 | 0 | 4.5 | Leg end — stake with paracord |
| Feedline ground | 0 | 0 | 0 | Feedline reaches ground at mast base |
| Tuner | 0 | +10 | 0 | 10 ft of feedline slack runs to operator position |

The feedline (43 ft) is 10 ft longer than the mast height; the excess lies on the ground toward the operating position. Orient the Y axis toward your operating position when deploying.

---

## ⚠️ 4. Maintenance Notes
*   **Silicone Care:** Wipe down wire after muddy activations; silicone attracts debris but cleans easily.
*   **Zip Tie Check:** Inspect zip ties on spacers periodically; PETG is durable, but soft silicone wire can shift under heavy wind load.
*   **Storage:** Always use a **Figure-8 wrap** when winding. Do NOT coil in circles, or the ladder line will become a tangled nightmare for your next activation.

