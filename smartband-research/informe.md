# Smartband white-label con SDK para Pasito: informe de proveedores

Fecha: 1 de octubre de 2026. Alcance: Alibaba.com y Made-in-China.com, más la documentación de SDK en GitHub y en los sitios de los fabricantes.

---

## 0. Cómo se hizo y límites (leer primero)

- **Alibaba.com bloqueó el acceso automático** (captcha "punish"). **Made-in-China.com y Global Sources respondieron con error 429.** No pude abrir fichas de producto ni tiendas en vivo.
- Los datos de proveedor salen de otras fuentes:
  - Los directorios públicos de Alibaba (`electronics.alibaba.com/supplier/...`, `alibaba.com/...-suppliers.html`), que muestran años, badge, rating, tiempo de respuesta, entrega a tiempo, precio y MOQ.
  - Las fichas PDF de Global Sources.
  - Los sitios de los fabricantes (por ejemplo jointcorp.com e istarmax.com).
- **Los directorios de Alibaba no son 100 % confiables.** Algunos son guías generadas automáticamente con nombres de proveedor inconsistentes (por ejemplo "Sino-Shanghai Yunnan Manufacturing") y años que no coinciden entre páginas. Usé solo los datos que aparecen de forma coherente en más de un listado. El resto está marcado **A CONFIRMAR**.
- **Revisé los SDK leyendo los repos y la documentación pública** (README, wiki, métodos de la API, fecha del último release). No compilé ni corrí ningún SDK.
- Junté 26 candidatos. 16 quedaron en carrera (preseleccionados, condicionales o reserva) y 10 se descartaron. El detalle completo, con links, está en `proveedores.csv`.
- **Puntaje:** cada criterio va de 1 a 5, con estos pesos: SDK 35 %, proveedor 20 %, precio 20 %, hardware 15 %, certificaciones 10 %. Cuando un dato falta, el puntaje del criterio es bajo (2), para no premiar lo que no se sabe.

---

## 1. Ranking de los 10 mejores

| # | Proveedor | Ecosistema / SDK | Producto de referencia | SDK | Prov. | Precio | HW | Cert. | **Total /5** | Requisitos excluyentes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Shenzhen DO Intelligent Technology (**IDO**) | VeryFit, SDK público iOS/Android/Flutter | Bandas IDO (modelo A CONFIRMAR) | 4 | 5 | 4 | 3 | 3 | **3,95** | SDK ✅ · Logo ✅ · MOQ ≈✅ · Muestra A CONFIRMAR |
| 2 | Shenzhen Youhong Technology (**J-Style / JCVital**) | SDK nativo gratis, a pedido | JCVital 2208A (sin pantalla) | 4 | 4 | 3 | 4 | 3 | **3,70** | ✅ ✅ ✅ ✅ |
| 3 | Shenzhen **Smart Care** Technology | A CONFIRMAR | B10 sin pantalla | 2 | 4 | 5 | 4 | 4 | **3,50** | SDK **A CONFIRMAR** · Logo ✅ · MOQ ✅ · Muestra A CONFIRMAR |
| 4 | Shenzhen **Starmax** Technology | Runmefit, "free SDK guide" | S5 0,96" táctil | 3 | 3 | 4 | 3 | 4 | **3,30** | SDK A CONFIRMAR (anunciado) · ✅ ✅ ✅ |
| 5 | Shenzhen **Veepoo** Technology | H Band, SDK público Apache-2.0 | Banda Veepoo (modelo A CONFIRMAR) | 5 | 2 | 2 | 3 | 2 | **3,20** | SDK ✅ · resto A CONFIRMAR |
| 6 | Shenzhen **Yawell** Intelligent | QRing/QWatch (Colmi) | Y25 / Y28C sin pantalla | 2 | 4 | 4 | 3 | 4 | **3,15** | SDK **A CONFIRMAR** (solo comunidad) · ✅ ✅ |
| 7 | Ecosistema **FitCloudPro** (Topstep) vía fabricante socio | SDK público iOS (MIT) y Android | Banda FitCloudPro (A CONFIRMAR) | 4 | 3 | 2 | 3 | 2 | **3,05** | SDK ✅ · Logo ✅ · MOQ/muestra A CONFIRMAR |
| 8 | Shenzhen **Yiqun** Technology | "with SDK and API" (¿FitCloudPro?) | ES02 / tracker con SDK | 3 | 3 | 3 | 3 | 3 | **3,00** | SDK A CONFIRMAR · ✅ ✅ |
| 9 | Shenzhen **Vivistar** Technology | A CONFIRMAR | VY25 / VY26 | 2 | 3 | 4 | 3 | 3 | **2,85** | SDK A CONFIRMAR · ✅ ✅ ✅ |
| 10 | Shenzhen **Simple Fun** Technology | "OEM Free SDK" (anuncio) | Y25 / S01 | 2 | 3 | 4 | 3 | 2 | **2,75** | SDK A CONFIRMAR · ✅ ✅ |

Quedaron como reserva **UTE / GloryFit** (2,70), **IUTECH / Iwown** (2,70), Nanchang Nafan, Letine, Tianpengyu y VALDUS.

**Descartados:**
- Minew y Moko: son beacons y no cuentan pasos.
- XZT/ZTX y Kingstar: no tienen SDK.
- Moyoung: no fabrica y no tiene SDK verificable.
- Yucheng: no encontré un canal de compra.
- Chileaf: se especializa en frecuencia cardíaca y es caro.
- Fitcare: precio de USD 59.
- Eternity: sin SDK y con poca trayectoria.
- Vanzone: es el único candidato de Made-in-China, pero vende sobre todo auriculares.

> **El primer requisito excluyente (SDK) lo pude verificar con documentación pública solo para cinco ecosistemas:** Veepoo, IDO, FitCloudPro, J-Style (en su web) e Iwown (solo iOS). Los demás (Smart Care, Yawell, Vivistar, Simple Fun y otros) dicen tener SDK o no dicen nada. **Si no muestran documentación antes de comprar, quedan descartados.**

---

## 2. Top 3 recomendado para pedir muestras

El top 3 de muestras no sigue al pie de la letra el top 3 por puntaje. Smart Care (3.º) sube por precio, pero el SDK, que es excluyente, **no está verificado**. Pedir esa muestra antes de ver la documentación sería gastar a ciegas. Por eso priorizo los tres con SDK verificado y hardware o proveedor fuertes.

### Muestra 1: J-Style / JCVital 2208A (Shenzhen Youhong Technology)

**Por qué:**
- Es el único candidato que cumple **los 4 requisitos excluyentes** con evidencia.
- Usa chip **Nordic** (nRF52 en todas las fichas de la marca), PPG Maxim y acelerómetro Bosch.
- Es IP68, tiene 7 a 10 días de batería y **guarda 30 días de datos** en la pulsera. Si el usuario no abre la app, no pierde pasos.
- El SDK es **gratuito**, según el fabricante, y anuncian acceso a datos **crudos** del acelerómetro. Con eso podríamos armar nuestro propio filtro antitrampa.
- Fabricante con 14 años en Alibaba, 52 a 54 % de recompra y despacho de muestras en unos 3 días hábiles.
- Ofrecen logo serigrafiado y animación de arranque OEM.

**Riesgos:**
- El SDK no es público: hay que ver la documentación y la demo antes de comprometerse.
- No tiene pantalla: el usuario no ve sus pasos en la muñeca (UX y "gamificación" pasan 100 % por la app).
- Hay precios muy dispares en los listados (USD 9,90 a 37). Una guía de Alibaba menciona USD 1.200/año por soporte prioritario del SDK.
- Los plazos de producción no coinciden (15 a 25 días hábiles en la ficha y 6 a 8 semanas en las FAQ).

**A CONFIRMAR:** precio a 1.000 unidades, costo de logo y packaging, si hay costo o licencia del SDK, Flutter/RN, certificaciones (CE, FCC, RoHS, BQB, UN38.3, MSDS) y peso.

### Muestra 2: IDO (Shenzhen DO Intelligent Technology)

**Por qué:**
- Es el fabricante más grande del grupo: unos 1.300 empleados, 21 líneas propias y operación desde 2014.
- **SDK público para iOS, Android y Flutter**, con documentación en inglés (GitBook) y demos nativas y en Flutter en GitHub. La documentación se actualizó en 2026.
- Datos: pasos en tiempo real e histórico, FC, sueño, SpO2, PA, estrés y más.
- Aparece desde USD 10,99 a 11,79 con MOQ de 10. Hace OEM de logo en pulsera, caja y manual.

**Riesgos:**
- **Seguridad:** un investigador (sprocketfox.io, febrero de 2025) mostró que los dispositivos IDO **no tienen autenticación BLE**. Cualquiera puede conectarse, leer y enviar comandos. Para Pasito importa doblemente: es privacidad, y además facilita emular o manipular la pulsera para inflar pasos. Hay que exigir bonding/cifrado o un desafío-respuesta propio.
- La documentación menciona "registro" de la librería: puede haber clave o licencia.
- No encontré su tienda oficial en Alibaba. Muchos revendedores usan firmware IDO (VeryFit), así que hay que comprar al fabricante o confirmar el origen del firmware.

**A CONFIRMAR:** modelo de banda concreto, chipset, batería, IP, certificaciones, precio de muestra y costo del SDK.

### Muestra 3: banda con firmware Veepoo (H Band)

**Por qué:**
- Es **el mejor SDK que revisé**:
  - Repos públicos con licencia **Apache-2.0** y actividad en septiembre de 2026.
  - Wiki en inglés con métodos concretos: pasos en tiempo real (`veepooSDKGetStepDataWithDate`), histórico en tramos de **5 minutos**, FC, sueño, SpO2 y arrays crudos de PPG/ECG.
  - Configuración de **idioma español** por API (código 7).
  - Soporta chips Nordic, JieLi y Goodix.
  - Los datos de salud no dependen de servidores (solo el mercado de esferas usa su nube).

**Riesgos:**
- **No identifiqué una tienda de Veepoo en Alibaba ni en MIC.** Veepoo trabaja con fabricantes socios.
- Para la muestra, en el RFQ hay que pedir a 2 o 3 vendedores de bandas "H Band" que confirmen que el firmware es Veepoo, que entregan SDK y que el SDK de GitHub funciona con su modelo.
- El README aclara que el SDK es "solo para clientes que cooperan", así que puede haber un acuerdo de por medio.

**A CONFIRMAR:** todo lo comercial (proveedor, precio, MOQ, logo, certificaciones, hardware).

### Muestras opcionales (4.ª y 5.ª, ya que el plan prevé de 3 a 5)

4. **Starmax S5** (con pantalla de 0,96"): sirve si queremos que el usuario vea sus pasos en la muñeca.
   - A favor: CE, RoHS y FCC; ISO9001 y BSCI; responde en 1 hora o menos; USD 9,39 a 11,05.
   - Riesgos: **logo de arranque solo desde 5.000 unidades**, entrega a tiempo baja (75 a 83 %) y SDK no público.
5. **Smart Care B10**: el más barato (USD 7,42 a 8,43 a 1.000 unidades), con 12 días de batería y 3ATM.
   - **Pedirla solo si mandan la documentación del SDK antes de comprar** y si venden una unidad suelta (el MOQ publicado es 1.000).

---

## 3. Riesgos por candidato (top 10)

| Proveedor | Riesgos principales |
|---|---|
| IDO | No tiene autenticación BLE (privacidad y emulación). Posible registro o licencia del SDK. No encontré su tienda oficial. Muchos revendedores usan su firmware. |
| J-Style 2208A | El SDK no es público. No tiene pantalla. Precios y plazos inconsistentes. Posible costo de soporte (USD 1.200/año, A CONFIRMAR). |
| Smart Care B10 | No hay evidencia de SDK. El MOQ de 1.000 puede impedir comprar una muestra suelta. |
| Starmax S5 | Logo de arranque recién desde 5.000 unidades. Entrega a tiempo de 75 a 83 %. SDK a pedido. |
| Veepoo | Canal de compra no identificado. SDK "para clientes que cooperan". Hardware depende del fabricante socio. |
| Yawell | Solo protocolo documentado por la comunidad (Gadgetbridge), sin SDK oficial verificado. Depender de ingeniería inversa no es viable para producción. |
| FitCloudPro | El SDK es de Topstep y el hardware de otro: ¿quién da soporte? El SDK Android se descarga **por HTTP inseguro desde una IP china** (120.78.153.20), así que hay que espejarlo en un repositorio propio. Está orientado a smartwatches con muchas funciones extra. |
| Yiqun | No está claro qué SDK usa (¿FitCloudPro?). Datos de directorio viejos. |
| Vivistar | Sin SDK verificado. Entrega a tiempo de 81 %. |
| Simple Fun | Probable revendedor de firmware de terceros (el Y25 lo venden muchos). Años en la plataforma inconsistentes (1 u 8). |

**Riesgos comunes a todos:**
- **Ningún fabricante documenta un filtro contra sacudidas** para que no sumen pasos. Ver la sección 4.
- **Todos sincronizan por BLE sin autenticación fuerte demostrada**, así que una pulsera se puede emular. Las validaciones antifraude tienen que hacerse en nuestro backend.
- Los listados de Alibaba mezclan fabricantes y tradings con el mismo modelo genérico (Y25, H59, G69). **Siempre pedir la licencia de negocio y una videollamada de la fábrica**, y verificar el badge Verified/Audited y Trade Assurance en la tienda real.

---

## 4. Detección de movimiento falso (sacudir la pulsera)

No encontré documentación pública de ningún proveedor sobre filtros antitrampa. Propuesta:

1. **Preguntar en el RFQ** si el algoritmo de pasos del firmware filtra sacudidas, movimientos con un solo eje o cadencias imposibles, y si se puede activar. Probarlo con la checklist.
2. **Preferir SDKs con datos granulares o crudos.** Veepoo da tramos de 5 minutos y PPG crudo; J-Style anuncia acelerómetro crudo; FitCloud da pasos cada ~5 minutos.
3. **Reglas en el backend de Pasito:**
   - cadencia plausible (aproximadamente 60 a 200 pasos por minuto sostenidos);
   - pasos sin aumento de la frecuencia cardíaca;
   - ráfagas uniformes durante horas o con la pulsera quieta de noche;
   - topes diarios;
   - pasos con la pulsera "no puesta" (sensor de contacto o PPG sin señal);
   - un solo dispositivo por cuenta, vinculado por MAC o número de serie.
4. Si el volumen lo justifica: **firmware a medida** con nuestro filtro. Esto se da en chips Nordic (J-Style, Veepoo), pero el acceso al código fuente suele exigir MOQ altos (A CONFIRMAR).

---

## 5. Certificaciones e importación a Argentina

- **Pedir a cada proveedor:** CE (RED), FCC ID, RoHS, Bluetooth SIG (QDID/BQB), **UN38.3 y MSDS de la batería** (sin estos no se pueden transportar baterías de litio por aire), y el informe de prueba de caída (1,2 m).
- **Transporte:** una pulsera con batería de litio integrada va como "batería en equipo" (UN3481). El courier va a pedir el resumen de ensayo UN38.3. Confirmar con el forwarder.
- **ENACOM:** en Argentina los equipos con Bluetooth requieren **homologación de ENACOM**. Preguntar a cada proveedor si ya tiene productos homologados en Latinoamérica (ENACOM, ANATEL, IFT, etc.) y pedir los **reportes de ensayo RF** (EN 300 328, FCC Part 15.247) y los de SAR, si aplican, para facilitar el trámite. VALDUS dice exportar a México, Brasil, Perú y Colombia, lo que podría ayudar (A CONFIRMAR).
- **Régimen de importación:** hay que validarlo con un **despachante de aduana**: posición arancelaria, licencias, envíos courier frente a carga general para las muestras y el pedido de 1.000 unidades, y si se exige certificación de seguridad eléctrica para el cargador o cable. Todo esto está A CONFIRMAR porque la normativa cambia seguido.

---

## 6. Datos "A CONFIRMAR" prioritarios (por proveedor del top 3 de muestras)

| Dato | J-Style 2208A | IDO | Veepoo (vía socio) |
|---|---|---|---|
| Acceso, licencia y costo del SDK | Gratis según la web; ¿soporte USD 1.200/año? | ¿Registro o clave? | Apache-2.0; ¿acuerdo de cooperación? |
| Documentación y demo antes de comprar | Pedir | Pública | Pública |
| Flutter / React Native | Anunciado, sin verificar | Flutter ✅ | No (nativo) |
| Precio de muestra + envío a Argentina | ? | ? | ? |
| Precio a 1.000 u (con logo y caja) | ? (USD 9,90 a 13,90 de referencia) | ? (USD 10,99 a 11,79 de referencia) | ? |
| Costo de logo en pulsera, arranque y caja | ? | ? | ? |
| Español en pantalla / logo de arranque | No aplica (sin pantalla) | ? | Español ✅ por API; logo ? |
| Filtro antisacudida | ? | ? | ? |
| Servidores en China | Nube opcional | No (según la doc) | Solo esferas |
| Chipset exacto | Nordic (¿nRF52832/52840?) | ? | Según modelo |
| CE / FCC / RoHS / BQB / UN38.3 / MSDS | ? | ? | ? |
| Homologaciones en LATAM | ? | ? | ? |
| Tiempo de producción | 15-25 días hábiles o 6-8 semanas | ? | ? |
| Seguridad BLE (bonding/cifrado) | ? | **No tiene (reportado)** | Contraseña de dispositivo (`confirmDevicePwd`) |

---

## 7. Próximos pasos sugeridos

1. Mandar `mensaje_rfq.md` a J-Style, IDO y 2 o 3 vendedores de bandas con firmware Veepoo (H Band). Como alternativa, a Starmax y Smart Care.
2. **No pagar ninguna muestra sin recibir antes la documentación o demo del SDK.** Pedir el .aar/.framework o el acceso al repo.
3. Mientras llegan las muestras, compilar la demo pública de Veepoo, IDO o FitCloud en un proyecto de prueba (iOS y Android) para medir la calidad del SDK.
4. Con las muestras: correr `checklist_muestras.md` y volver a puntuar.
5. Consultar a un despachante sobre ENACOM y el régimen de importación antes del pedido de 1.000 unidades.

---

## Fuentes principales

- SDK de Veepoo: https://github.com/HBandSDK · Wiki iOS: https://github.com/HBandSDK/iOS_Ble_SDK/wiki/VeepooSDK-iOS-API-Document
- SDK de IDO: https://github.com/idoosmart · https://idoosmart.github.io/Flutter_GitBook/en/ · Seguridad: https://sprocketfox.io/xssfox/2025/02/09/ido/
- SDK de FitCloudPro: https://github.com/htangsmart/FitCloudPro-SDK-Android · https://github.com/htangsmart/FitCloudPro-SDK-iOS
- SDK de Iwown (iOS): https://github.com/iwown/Lib3Framework-iOS
- UTE/GloryFit (wrapper comunitario): https://pub.dev/packages/flutter_band_fit
- J-Style: https://www.jointcorp.com/sdk-api/ · https://www.jointcorp.com/product/2208a-smart-health-band/ · https://www.jointcorp.com/faqs/
- Starmax OEM: https://istarmax.com/service/oem-and-odm/
- Directorios de Alibaba: https://electronics.alibaba.com/supplier/wearable-fitness-tracker-manufacturer · https://electronics.alibaba.com/supplier/no-screen-fitness-tracker-producer · https://electronics.alibaba.com/supplier/smart-band-watch-producer · https://www.alibaba.com/smart-bracelet-with-sdk-suppliers.html · https://electronics.alibaba.com/product/smart-bracelet-with-open-sdk
- Protocolos de comunidad: https://gadgetbridge.org/internals/specifics/moyoung-protocol/ · https://gadgetbridge.org/gadgets/rings/yawell/
- Fichas de Global Sources (J-Style 1755/1963, Starmax GTR2): p.globalsources.com/IMAGES/PDT/SPEC/...
