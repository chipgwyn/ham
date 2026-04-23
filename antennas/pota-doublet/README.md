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

---

## 🏗 2. Fabrication Guide

### **The "Continuous Wire" Method**
1.  **Cut:** Two (2) identical lengths of **96 feet** each (53ft for the leg + 43ft for the feed).
2.  **Center Transition:** Pass each wire through the 3D-printed Center Insulator at the 53ft mark.
3.  **Ladder Line Construction:** 
    *   Thread **35 spacers** onto the 43ft feedline sections.
    *   Set spacer interval to **15 inches**.
    *   Secure with small zip ties; cinch firmly against the silicone jacket to prevent sliding.

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

## ⚠️ 4. Maintenance Notes
*   **Silicone Care:** Wipe down wire after muddy activations; silicone attracts debris but cleans easily.
*   **Zip Tie Check:** Inspect zip ties on spacers periodically; PETG is durable, but soft silicone wire can shift under heavy wind load.
*   **Storage:** Always use a **Figure-8 wrap** when winding. Do NOT coil in circles, or the ladder line will become a tangled nightmare for your next activation.

