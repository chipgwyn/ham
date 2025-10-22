# **DRAFT** Toroid Transformer Design Reference Guide **DRAFT**

This comprehensive reference table provides proven specifications for building HF amateur radio transformers using ferrite toroid cores. The designs cover common impedance transformations including 1:1 common mode chokes (ununs), 4:1 current baluns, 9:1 ununs for random wire antennas, and 49:1 ununs for end-fed half-wave antennas. Power levels range from QRP (5W) to legal limit (2000W) operations, with separate ratings for SSB and continuous-duty digital modes. Core material selection (Mix 43 vs Mix 61) is optimized for frequency range, with Mix 61 preferred for lower bands (160m-40m) due to better permeability at lower frequencies, while Mix 43 offers excellent broadband performance across the entire HF spectrum. Wire gauge recommendations ensure adequate current-carrying capacity and minimize heating, while turn counts are optimized to provide sufficient choking impedance without excessive core saturation. All designs assume proper construction techniques including tight, even winding and adequate wire insulation ratings for high-voltage applications.

## Toroid Transformer Specifications

| Transformer Type | Power Level | Toroid Size | Mix Type | Wire Gauge (AWG) | Turns | SSB Power | Digital Power | Frequency Range | Notes |
|-----------------|-------------|-------------|----------|------------------|-------|-----------|---------------|-----------------|-------|
| **1:1 UnUn (Common Mode Choke)** |
| | 5W | FT82-43 | 43 | 22-24 | 10T twisted pair | 10W | 5W | 160m-10m | QRP applications |
| | 100W | FT240-43 | 43 | 14-16 | 10T twisted pair | 150W | 100W | 160m-10m | Standard HF |
| | 300W | FT240-43 | 43 | 12 | 8T twisted pair | 400W | 300W | 80m-10m | Use thicker wire |
| | 1000W | FT240-61 | 61 | 10 | 7T twisted pair | 1200W | 1000W | 160m-40m | Lower bands |
| | 1000W | 2×FT240-43 | 43 | 10 | 6T twisted pair | 1200W | 1000W | 40m-10m | Stacked cores |
| | 2000W | 2×FT240-61 | 61 | 6-8 | 5-6T twisted pair | 2500W | 2000W | 160m-40m | Heavy wire required |
| **4:1 Balun (Current Type)** |
| | 5W | FT82-43 | 43 | 24 | 12T trifilar | 10W | 5W | 160m-10m | QRP |
| | 100W | FT240-43 | 43 | 16 | 10T trifilar | 150W | 100W | 160m-10m | Standard |
| | 300W | FT240-43 | 43 | 14 | 8T trifilar | 400W | 300W | 80m-10m | Good spacing needed |
| | 1000W | 2×FT240-61 | 61 | 10 | 7T trifilar | 1200W | 1000W | 160m-40m | Stacked cores |
| | 1000W | 2×FT240-43 | 43 | 10 | 6T trifilar | 1200W | 1000W | 40m-10m | Stacked cores |
| | 2000W | 3×FT240-61 | 61 | 8 | 6T trifilar | 2500W | 2000W | 160m-80m | Triple stack |
| **9:1 UnUn (Transmission Line Type)** |
| | 5W | FT82-43 | 43 | 24 | 16T trifilar | 10W | 5W | 160m-10m | QRP |
| | 100W | FT240-43 | 43 | 16 | 12T trifilar | 150W | 100W | 160m-10m | Standard |
| | 300W | FT240-43 | 43 | 14 | 10T trifilar | 400W | 300W | 80m-10m | Random wire |
| | 1000W | 2×FT240-61 | 61 | 10 | 8T trifilar | 1200W | 1000W | 160m-40m | Stacked cores |
| | 1000W | 2×FT240-43 | 43 | 10 | 7T trifilar | 1200W | 1000W | 40m-10m | Stacked cores |
| | 2000W | 3×FT240-61 | 61 | 8 | 7T trifilar | 2500W | 2000W | 160m-80m | Triple stack |
| **49:1 UnUn (Autotransformer or Two-Core)** |
| | 5W | FT82-43 | 43 | 26 | 2:14T bifilar | 10W | 5W | 80m-10m | QRP EFHW |
| | 100W | FT240-43 | 43 | 18 | 2:14T bifilar | 150W | 100W | 80m-10m | Standard EFHW |
| | 300W | FT240-43 | 43 | 14 | 3:21T bifilar | 400W | 300W | 80m-10m | More primary turns |
| | 1000W | 2×FT240-61 | 61 | 12 | 3:21T bifilar | 1200W | 1000W | 80m-40m | Stacked cores |
| | 1000W | 2×FT240-43 | 43 | 10 | 2:14T bifilar | 1200W | 1000W | 40m-10m | Stacked cores |
| | 2000W | 3×FT240-61 | 61 | 10 | 3:21T bifilar | 2500W | 2000W | 80m-40m | Triple stack, heavy duty |

## Core Material Selection Guide

**Mix 43 (Ferrite)**: Permeability μi = 850, frequency range 1-30 MHz
- Best general-purpose choice for HF (80m-10m)
- Lower core losses than Mix 61 on upper bands
- Good broadband performance
- Preferred for 40m and higher frequencies

**Mix 61 (Ferrite)**: Permeability μi = 125, frequency range 200 kHz-25 MHz
- Superior performance on lower bands (160m-80m)
- Higher permeability requires fewer turns
- Lower losses on 160m and 80m
- Preferred for multi-band operation including 160m

**Mix 31 (Ferrite)**: Permeability μi = 1500, frequency range 1-300 MHz
- Alternative for upper HF bands when available
- Can substitute for Mix 43 with reduced turn counts
- Less common in amateur applications

## Construction Notes and Best Practices

**Wire Selection and Preparation:**
- Use magnet wire (enameled copper) or Teflon-insulated wire
- For power levels above 500W, use high-temperature wire (200°C+ rating)
- Teflon or PTFE insulation recommended for legal-limit applications
- For twisted pairs: Twist wires 1-2 twists per inch before winding
- For trifilar: Keep all three wires together and maintain equal tension

**Winding Techniques:**
- **Twisted Pair**: Two wires twisted together, both pass through core as one unit
- **Trifilar**: Three wires bundled and wound together maintaining parallel orientation
- **Bifilar**: Two wires wound together (for 49:1, one is primary, one is secondary)
- Wind turns evenly spaced around the core
- Avoid overlapping turns which increases capacitance
- Leave small gaps between turns when possible for cooling

**Core Stacking for High Power:**
- Stack cores with insulating material between them (kapton tape, electrical tape)
- Wind all cores together as a single unit
- Stacking reduces flux density and heat generation per core
- Essential for sustained digital mode operation above 500W

**Turn Count Notation:**
- "10T twisted pair" = 10 turns of a twisted pair (both wires) through the core
- "12T trifilar" = 12 turns of three wires bundled together
- "2:14T bifilar" = 2 turns primary, 14 turns secondary, wound together

## Warnings and Important Considerations

**⚠️ CRITICAL SAFETY WARNINGS:**

1. **High Voltage**: 49:1 ununs can develop over 1000V at the antenna feedpoint at legal limit power. Use appropriate wire insulation and maintain safe distances. Enclosures must be non-conductive and weatherproof.

2. **Core Temperature**: Ferrite cores can exceed 200°C under high power continuous operation. Never touch cores during or immediately after transmission. Allow 10-15 minutes cooling time. Cores that glow red or smell burnt have failed and must be replaced.

3. **Wire Insulation Breakdown**: Standard magnet wire insulation fails above 150-180°C. For sustained digital mode operation above 300W, use wire rated for 200°C minimum (Teflon, PTFE, or high-temperature polyimide).

4. **Core Saturation**: Operating above rated power causes core saturation, generating extreme heat and harmonic distortion. Core saturation can occur within seconds and cause permanent damage.

**OPERATIONAL CAUTIONS:**

5. **Digital Mode Derating**: FT8, FT4, RTTY, PSK31, and other constant-carrier modes generate continuous power. Always use the "Digital Power" rating, never the SSB rating. Running SSB power levels on digital modes will cause immediate overheating and failure.

6. **SWR and Mismatch**: Transformers assume a matched load. High SWR (>2:1) increases heating and can cause failure even at reduced power. Always check SWR before applying full power.

7. **160m Operation**: 160m requires more turns and larger cores (Mix 61) for adequate choking impedance. Using Mix 43 or insufficient turns on 160m results in poor common-mode rejection and potential RFI issues.

8. **Initial Testing**: Always test new transformers at reduced power (10-25%) and check for heating after 30 seconds of transmission. If the core feels warm to touch, it will overheat at full power.

**CONSTRUCTION CAUTIONS:**

9. **Wire Gauge Critical**: Undersized wire causes resistive heating independent of core losses. Wire that's too thin will burn through insulation. At legal limit power, use AWG 8 or larger wire regardless of turn count.

10. **Trifilar/Bifilar Wire Tracking**: When winding multiple wires, they must track together and maintain the same length. Unequal lengths create impedance imbalance and reduce effectiveness.

11. **49:1 Construction Complexity**: 49:1 transformers are the most challenging to build correctly. The 2:14 turn ratio (or 3:21) must be maintained precisely. Poor construction causes high SWR and reduced efficiency. Consider using proven commercial designs for high-power 49:1 applications.

12. **Core Stacking Alignment**: When stacking cores, maintain proper alignment. Offset cores reduce effectiveness and create uneven heating patterns.

**FREQUENCY-SPECIFIC NOTES:**

13. **60m Band (5 MHz)**: 60m is channelized in the US and some other countries. Transformers optimized for 80m/40m work well on 60m.

14. **30m, 17m, 12m (WARC Bands)**: These bands are no-contest zones and often used for digital modes. Use conservative power ratings due to longer transmission periods.

15. **Bandwidth Limitations**: Fewer turns provide wider bandwidth but less choking impedance. For operation on only upper bands (20m-10m), turn counts can be reduced by 20-30% for improved bandwidth.

**MAINTENANCE AND TROUBLESHOOTING:**

16. **Thermal Cycling**: Repeated heating/cooling cycles can crack ferrite cores. Inspect cores periodically for cracks or chips. Damaged cores lose effectiveness and should be replaced.

17. **Wire Insulation Inspection**: After heavy use, inspect wire insulation for discoloration, brittleness, or cracks. These indicate thermal degradation. Replace wire before insulation fails completely.

18. **Moisture Protection**: Ferrite absorbs moisture which increases losses. Always seal transformers in weatherproof enclosures with desiccant for outdoor use.

19. **Testing with Antenna Analyzer**: Before applying transmit power, check impedance transformation with an antenna analyzer. Correct transformation confirms proper construction. Unexpected readings indicate winding errors.

20. **Conservative Approach**: When in doubt, use a larger core, thicker wire, or more cores stacked together. Overbuilding a transformer adds minimal cost but ensures reliable long-term operation.

## Alternative Construction Methods

**Transmission Line Transformers**: The designs shown use conventional wound transformers. Transmission line transformers (using coaxial cable wound on cores) offer alternative construction methods with different characteristics:
- Better high-frequency response
- Lower capacitance between windings
- More difficult to construct properly
- Often preferred for 9:1 and 4:1 designs above 100W

**Split-Core Options**: Some builders use multiple smaller cores instead of one large core:
- Example: Four FT140 cores instead of one FT240
- Distributes heat better
- More complex mounting
- Can improve power handling

## Power Rating Philosophy

The power ratings in this table represent **continuous safe operating power** under the following conditions:
- Ambient temperature: 25°C (77°F)
- Adequate ventilation
- Matched load (SWR < 1.5:1)
- Proper construction technique

**SSB Power Ratings** assume:
- 30% average duty cycle
- Peak envelope power (PEP)
- Typical voice characteristics
- Not suitable for sustained carrier operation

**Digital Power Ratings** assume:
- 100% duty cycle
- Continuous carrier
- Includes safety margin
- Suitable for RTTY, FT8, FT4, PSK31, and other constant-carrier modes

## Source References and Additional Information

These specifications are compiled from multiple sources including:
- ARRL Handbook
- ON4AA Antenna Publications
- W8JI Technical Articles
- Palomar Engineers Application Notes
- Years of amateur radio community experimentation

**Always verify designs with measurement equipment before applying full power. An antenna analyzer and SWR meter are essential tools for transformer validation.**

For additional technical information, consult:
- ARRL Handbook (latest edition, Chapter on Transmission Lines and Antenna Systems)
- Fair-Rite Products Corporation application notes
- Amidon Associates technical specifications
