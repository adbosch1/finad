# Estudio de fábricas en Alibaba y Made-in-China con SDK abierto

Fecha: 4 de octubre de 2026. Tabla completa (21 fábricas, con URL de tienda y métricas): `fabricas_alibaba_mic.csv`.

## Cómo se armó

- **Alibaba** bloquea la navegación automática con captcha. Usé sus **directorios públicos**:
  - `electronics.alibaba.com/supplier/smart-bracelet-with-open-sdk`
  - `.../smart-bracelet-programmable-with-api-and-sdk`
  - `.../wearable-fitness-tracker-manufacturer`
  - `.../no-screen-fitness-tracker-producer`
  - `.../smart-band-watch-producer`
  - `.../product/fit-cloud-pro-watch`

  Estos directorios muestran los mismos datos que la tienda: años, badge, rating, cantidad de reseñas, tiempo de respuesta, entrega a tiempo, recompra, precio y MOQ.
- **Made-in-China** sí se pudo leer: búsquedas "Smart Bracelet SDK", "Smart Band SDK", "Fitness Tracker Smart Bracelet" y showrooms de cada fábrica.
- Cada dato de SDK se clasificó en uno de cuatro niveles:
  1. **Público verificado:** repositorio y documentación abiertos. Es el nivel más alto.
  2. **Gratis a pedido en la web del fabricante.**
  3. **Solo anunciado en el listado.**
  4. **Sin mención.**
- **Puntaje (1 a 5):** SDK abierto 40 %, reseñas (rating y volumen) 25 %, solidez de la fábrica (años, badge, entrega, recompra) 20 %, producto adecuado (pulsera, precio, MOQ ≤ 1.000) 15 %.
- **Advertencia:** algunas métricas de los directorios varían entre páginas (por ejemplo, años 6 contra 8). Puse los rangos. Las métricas definitivas hay que verlas en la tienda real antes de pagar.

## Ranking

| # | Fábrica | Plataforma / tienda | Reputación | Pulsera destacada | Precio USD / MOQ | SDK | Puntaje |
|---|---|---|---|---|---|---|---|
| 1 | **Shenzhen Youhong (J-Style / JCVital)** | [jointcorp.en.alibaba.com](https://jointcorp.en.alibaba.com) | 14 años, Verified Manufacturer, 4,6★ (~100 reseñas), entrega a tiempo 92 %, **recompra 52 %** | "API/SDK Opened Smart Bracelet **1810**" · **2208A** sin pantalla (Nordic) | 1810: 11,50-14 / 100 · 2208A: 13,90-32 / 1 | **Gratis a pedido** (su web) | **4,35** |
| 2 | **Shenzhen DO Intelligent (IDO / VeryFit)** | [MIC: showroom/ninatang](https://www.made-in-china.com/showroom/ninatang/) · Alibaba (tienda A CONFIRMAR) | Fábrica de 500+ personas, ISO 9001, CE, RoHS, FCC, BSCI | Heart Rate Intelligent Tracker | 13,80-15 / **1.000** | **Público** (GitHub, Flutter) | **4,10** |
| 3 | Shenzhen Xunchitong | [xusiton.en.alibaba.com](https://xusiton.en.alibaba.com) | 6-7 años, Verified Manufacturer, 4,5★ (**458-614 reseñas**), entrega a tiempo 98 % | S01 sin pantalla (menciona SDK); relojes FitCloudPro | 11,60-12,99 / 1 | Anunciado + FitCloudPro | 3,85 |
| 4 | Shenzhen Simple Fun | [simplefun.en.alibaba.com](https://simplefun.en.alibaba.com) | 6-8 años, Verified Manufacturer, 4,8★ (104-185), entrega a tiempo 97 % | ZW65 (**FitCloudPro**, es reloj) · Y25/S01 | 7,55-12,30 / 10 | **Público** vía FitCloudPro (solo en ese modelo) | 3,80 |
| 5 | Shenzhen Shunxiang | [dykj.en.alibaba.com](https://dykj.en.alibaba.com) | **15 años**, Verified Manufacturer, 4,7★ (154), entrega a tiempo 97 %, recompra 39 % | G69 sin pantalla "SDK" | 9,80-10,80 / 5 | Anunciado | 3,65 |
| 6 | Shenzhen Yawell (QRing/Colmi) | [yawell.en.alibaba.com](https://yawell.en.alibaba.com) | 6 años, Verified Manufacturer, 4,7-4,8★ (~60), ISO/BSCI, CE/FCC/RoHS | Y25 / Y28C sin pantalla | 10,93-11,55 / 100-1.000 | Anunciado ("Custom OEM SDK") + protocolo de comunidad | 3,60 |
| 7 | Shenzhen Tianpengyu (Spovan) | [spovan.en.alibaba.com](https://spovan.en.alibaba.com) | **13 años**, Verified Manufacturer, 4,5★ (71-222), entrega a tiempo 97 %, recompra 34-49 % | OEM PPG/ECG Smart Band (SDK/API) | 18-19 / 5 | Anunciado | 3,40 |
| 8 | Shenzhen Starmax | [istarmax.en.alibaba.com](https://istarmax.en.alibaba.com) · [MIC](https://www.made-in-china.com/showroom/fitnesstracker) | 11 años, Verified Manufacturer, 4,3-4,5★ (~40), ISO 9001/14001, CE/FCC/RoHS/MSDS, **entrega a tiempo 75-83 %** | "SDK API Fitness Tracker S5" (pantalla 0,96") | 9,39-11,05 / 22 | Gratis a pedido | 3,30 |
| 9 | Shenzhen Staranb | [staranb.en.made-in-china.com](https://staranb.en.made-in-china.com) | **Diamond + Audited** en MIC, I+D propio, 6 líneas | "**Nordic** Chip Custom SDK Screenless Tracker" | 9,80-24,50 / 10-1.000 | Anunciado | 3,25 |
| 10 | Shenzhen Yiqun | [shenzhenyq.en.alibaba.com](https://shenzhenyq.en.alibaba.com) | 11 años, 4,6★ (159) | Tracker "with SDK and API" | 17-17,90 / 100 | Anunciado (¿FitCloudPro?) | 3,25 |

Del 11 al 21 (en el CSV): Ovesse, Karen M (gran reputación pero sin SDK), Vivistar, Smart Care (barata pero sin SDK), Eternity, Lida, Yuanzhou, Blackrhino, Tianyu Zhixing, Risinno y Maikodi.

## Conclusiones

1. **Muy pocas fábricas tienen un SDK abierto de verdad.** La mayoría dice "SDK" en el título del producto para posicionarse en la búsqueda. Solo encontré tres caminos con documentación pública o del fabricante:
   - **IDO**: SDK público, fábrica propia.
   - **J-Style (Youhong)**: SDK gratis, fábrica propia.
   - **FitCloudPro (Topstep)**: SDK público, pero lo usan otras fábricas, casi siempre en relojes y no en pulseras.

   El cuarto, **Veepoo**, tiene el mejor SDK público pero **no tiene tienda propia**. Vende placas a otras fábricas, así que no figura en el ranking.
2. **Mejor balance entre producto, reseñas y SDK: Shenzhen Youhong (J-Style).** Tiene 14 años en Alibaba, 52 % de recompra (la más alta entre los fabricantes serios) y un modelo que el propio listado llama "API/SDK Opened" (1810), además de la 2208A con chip Nordic.
3. **Mejor SDK verificable con fábrica grande: IDO.** En Made-in-China tiene MOQ de 1.000, justo lo que necesitamos, y certificaciones CE, FCC y RoHS declaradas. Sigue pendiente el riesgo de seguridad Bluetooth que ya señalamos.
4. **Mejores reseñas, con SDK por confirmar:** Xunchitong (más de 600 reseñas), Shunxiang (15 años, 4,7★) y Tianpengyu (13 años, recompra de hasta 49 %). Vale la pena mandarles el RFQ, porque si muestran documentación del SDK suben al podio.
5. **En Made-in-China, la mejor es Staranb**: Diamond + Audited y anuncia SDK con chip Nordic. Falta ver documentación y no hay reseñas visibles.

## A quién escribirle

| Prioridad | Fábrica | Por qué |
|---|---|---|
| 1 | J-Style (jointcorp.en.alibaba.com, modelos 1810 y 2208A) | Mejor puntaje general |
| 1 | IDO (MIC: Nina Tang, Sales Manager · sales@idoocn.com) | SDK público + fábrica grande |
| 2 | Xunchitong, Shunxiang, Tianpengyu | Mejores reseñas; deben demostrar el SDK |
| 2 | Staranb (MIC) | Mejor perfil en Made-in-China |
| 3 | Simple Fun, Yiqun | Preguntar si tienen pulseras con firmware FitCloudPro |
| 3 | Veepoo (Hi@veepoo.cn) | Pedirles que recomienden una fábrica socia con pulsera H Band |

**Filtro común:** pedir **documentación y demo del SDK antes de cualquier pago**. Usar el `mensaje_rfq.md`.

## Cómo verificar cada tienda (lo tiene que hacer una persona, porque Alibaba bloquea los bots)

1. Abrir la tienda y confirmar el badge **Verified** ("Verified Manufacturer" en Alibaba, "Audited Supplier" en MIC) y el informe de auditoría (TÜV/SGS/BV).
2. Revisar **Company Profile**: años, empleados, superficie de la fábrica, líneas de producción, mercados (si hay Latinoamérica, mejor).
3. Leer **reseñas de 1-3★**, que muestran los problemas reales (envíos, fallas, soporte).
4. Confirmar en la ficha de la pulsera: chip, batería, IP, app asociada (VeryFit, JCVital, FitCloudPro, H Band, etc.). **La app indica de quién es el firmware y, por lo tanto, qué SDK es.**
5. Comprar y pagar las muestras con **Trade Assurance**.
