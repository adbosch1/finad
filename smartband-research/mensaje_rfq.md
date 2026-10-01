# Mensaje RFQ (en inglés): pedido de cotización y muestras

**Cómo usarlo:**
- Reemplazar los campos `{{...}}`.
- El bloque "Supplier-specific questions" del final tiene preguntas extra por proveedor: pegar solo las que correspondan.
- Mandarlo por el chat o el formulario de Alibaba/MIC (Trade Assurance) o por email.
- **No pagar la muestra hasta recibir la documentación del SDK.**

---

**Subject:** RFQ – White-label fitness band with BLE SDK (samples + ~1,000 pcs, custom logo) – {{Model}}

Hello {{Contact name}},

I am {{Your name}}, {{Your role}} at **Pasito** (Argentina, {{website}}). Our mobile app (iOS and Android) rewards users for walking: every 1,000 steps earns points they can redeem at partner stores. We are launching our own branded fitness band. Its data must sync **directly into our app via your SDK**, with no dependency on your companion app.

We are interested in **{{Model / link to listing}}**.

**Plan:**
1. Buy **1–2 samples** now for testing (accuracy, battery, BLE stability and SDK integration).
2. If the samples pass, place a first order of about **1,000 units** with our logo on the band and the packaging. Destination: **Argentina**.

Please answer the questions below. A short answer per item is fine.

### A. SDK & data
1. Do you provide an SDK for **both iOS and Android**? Please name the languages (Swift/Obj-C, Kotlin/Java) and say whether **Flutter or React Native** is supported.
2. Please share the **SDK documentation and a demo app** (or a GitHub/download link) **before we buy the samples**. Which SDK version applies to this model?
3. Can our app read **real-time steps** and **historical step data**?
   - What is the history granularity (e.g. per 5 min / per hour / per day)?
   - How many days of data does the band store when it is not synced?
4. Which other data can we read: distance, calories, heart rate, sleep, SpO2? Is any **raw data** available (accelerometer / PPG)?
5. Is there any **cost, license fee, annual fee, per-device royalty or NDA** for the SDK? Is technical support included, and in which language and time zone?
6. Does the SDK, or the band itself, require **any connection to your servers / cloud (in China or elsewhere)** to work? We need BLE-only, local data access.
7. How is the BLE connection **secured** (pairing/bonding, encryption, device password)? Can another app connect to the band and read or write data without authorization?

### B. Step accuracy & anti-cheating (important: we reward steps)
8. What is the step accuracy of your algorithm, and do you have a test report?
9. Does the firmware **filter fake movements**, such as shaking the band by hand, arm swinging while seated, or the band attached to a fan or drill? Can this filter be enabled or tuned?
10. Can the band report whether it is **worn** (wear detection / PPG contact)?

### C. Customization (OEM)
11. Our **logo on the band** (print or laser): what is the cost and the MOQ?
12. **Custom packaging** (box, manual in Spanish): what is the cost and the MOQ?
13. Firmware: can you set **Spanish** as the default language on the screen, and show **our logo on the boot screen**? What is the cost, and what is the MOQ for each?
14. Can the **BLE advertised name** be customized (e.g. "Pasito Band")?

### D. Price, samples & lead time
15. **Sample price** (1–2 units) plus **shipping cost to Argentina** (courier, DDU). Which courier, and how long does it take?
16. **Unit price for 1,000 pcs**, with and without logo and custom packaging. Please also quote 3,000 and 5,000 pcs for reference.
17. **MOQ** for this model, with and without customization.
18. **Production lead time** for 1,000 pcs after artwork approval, and **payment terms**. Do you accept Alibaba **Trade Assurance**?
19. Warranty period and defect policy (DOA replacement rate, spare units).

### E. Hardware specs (please confirm)
20. Chipset / BLE SoC (e.g. Nordic nRF52xxx, Realtek, JieLi, Telink), accelerometer model and BLE version.
21. Battery capacity (mAh), real battery life with HR monitoring on, charging type and charging time.
22. Water resistance (IP67 / IP68 / 5ATM): is there a test report?
23. Screen (size/type) or screenless; net weight; strap material.

### F. Certifications & import to Argentina
24. Please send copies of: **CE (RED), FCC ID, RoHS, Bluetooth SIG (QDID/BQB)** and **battery UN38.3 test summary + MSDS**. Which are issued for this exact model?
25. In Argentina, Bluetooth devices need **ENACOM type approval**. Is this model, or another one of yours, already **certified in Latin America** (ENACOM Argentina, ANATEL Brazil, IFT Mexico, etc.)? Can you share the **RF test reports** (EN 300 328 / FCC Part 15) so we can file the approval?
26. Can you ship lithium-battery products to Argentina, with the correct dangerous-goods documents (UN3481), for both the samples and the bulk order?

### G. Company
27. Are you the **manufacturer** or a trading company? Please share your business license. Can we do a short **video call of the factory**?
28. Which **brands or markets** use this SDK today? Any clients in Latin America?

Thank you. We are comparing a few suppliers and will choose our sample partners within **{{N}} days**. Fast and complete answers will be prioritized.

Best regards,
{{Your name}}
{{Role}} – Pasito
{{Email}} | {{WhatsApp}}
{{Company address, Argentina}}

---

## Supplier-specific questions (pegar las que correspondan)

**J-Style / JCVital (Shenzhen Youhong), 2208A:**
- Your site says the SDK is free. Is there any annual fee for priority support (we saw a mention of ~USD 1,200/year)?
- Do you provide **raw accelerometer data** via the SDK?
- Is a native **Flutter** plugin available today?
- Which Nordic SoC does the 2208A use (nRF52832 / nRF52840)?
- Your FAQ says lead time is 6–8 weeks and the spec sheet says 15–25 working days. Which applies to 1,000 pcs with logo?

**IDO (Shenzhen DO Intelligent), VeryFit models:**
- Which band model do you recommend for a step-reward program?
- Is any **registration or key** needed for the IDO protocol library (Flutter/native)?
- A 2025 security write-up reported that IDO devices accept BLE connections **without authentication**. Do you offer a firmware option with **bonding/encryption** or a custom authentication handshake for our app?

**Veepoo-based (H Band) bands, any seller:**
- Please confirm this model runs **Veepoo firmware** and is compatible with the public SDK at github.com/HBandSDK (Android/iOS). Which SDK version applies?
- Is a cooperation agreement needed to use the SDK commercially?
- Can the **boot logo** be customized, and at what MOQ?

**Starmax, S5:**
- Your OEM page states the boot-screen logo MOQ is 5,000. Is there any option at 1,000 pcs (with a setup fee)?
- Please send the "free SDK guide" and the demo app for the S5.

**Smart Care, B10:**
- Is there an SDK for the B10 (iOS/Android)? Please send the docs before we decide on samples.
- Can you sell **1–2 sample units** even though the MOQ is 1,000?

**FitCloudPro-based bands (e.g. Azhuo / Yiqun):**
- Confirm the model uses **FitCloudPro firmware** (Topstep SDK at github.com/htangsmart).
- Who provides SDK support: you or Topstep?
- Can the Android SDK be delivered as files or from an HTTPS repository?
