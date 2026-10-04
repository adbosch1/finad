# Opciones recomendadas: contacto, análisis y cronograma

Complementa `informe.md`. Los contactos salen de los sitios oficiales de cada fabricante (consultados el 4-oct-2026) y de sus tiendas en Alibaba. No contacté a nadie.

> **Recomendación de canal:** hacer el primer contacto y el pago de las muestras **dentro de Alibaba** (chat de la tienda + Trade Assurance), así hay registro y protección del pago. Usar email o WhatsApp para la parte técnica (SDK, documentación) y para acelerar respuestas.

---

## 1. Ficha de cada opción

### Opción A: J-Style / JCVital 2208A (Shenzhen Youhong Technology / Joint Chinese Ltd)

| | |
|---|---|
| **Qué es** | Fabricante especializado en wearables de salud (pulseras sin pantalla, anillos, relojes con ECG). Marcas J-Style y JCVital. Apunta a clientes B2B: salud, telemedicina, programas corporativos. |
| **Producto** | 2208A, pulsera **sin pantalla**: chip Nordic, PPG Maxim, acelerómetro Bosch 6D, batería de 90-95 mAh, **7-10 días**, IP68, BLE 5.0, OTA, **30 días de memoria**. Mide pasos, FC, HRV, SpO2, sueño y temperatura. |
| **SDK** | Android/iOS (y Windows/macOS). Gratis según la web. Lo entregan a pedido (no hay repo público). Dicen tener Flutter/RN y acceso a datos crudos (A CONFIRMAR). |
| **OEM** | Logo serigrafiado en malla o hebilla, animación de arranque, packaging. |
| **Proveedor** | 14 años en Alibaba, Verified Manufacturer, rating 4.5-4.6, responde en ≤6-7 h, entrega a tiempo 90-92 %, recompra 52-54 %. |
| **Precio de referencia** | USD 9,90-13,90 por unidad (listados); muestra USD 13,90-37 + envío. A CONFIRMAR con cotización. |
| **Plazos** | Muestra despachada en ~3 días hábiles. Producción: 15-25 días hábiles con 30 % de anticipo (ficha) o 6-8 semanas (FAQ). |

**Dónde hablarles:**
- Web: https://www.jointcorp.com (contacto: https://www.jointcorp.com/contact-us/, SDK: https://www.jointcorp.com/sdk-api/)
- Producto: https://www.jointcorp.com/product/2208a-smart-health-band/
- Email: **info@jointcorp.com**
- WhatsApp: **+86 186 8039 0477** y **+86 135 3828 0575** (publicados en su web)
- Alibaba: https://jointcorp.en.alibaba.com
- Dirección: Unit 2, Building 4, No. 3 Nanshan Road, Songshanhu District, Dongguan, Guangdong, China

---

### Opción B: IDO (Shenzhen DO Intelligent Technology)

| | |
|---|---|
| **Qué es** | Uno de los fabricantes grandes de wearables de China: desde 2014, ~1.300 empleados, 21 líneas de producción propias. Hace la app **VeryFit**, que usan muchas marcas blancas. |
| **Producto** | Bandas: Veryfit Pulse Band, IDB05, KR05, KR01; también relojes y anillos. **Modelo y specs a definir** con ellos. |
| **SDK** | **Público y verificado:** iOS, Android, Flutter y HarmonyOS, con documentación en inglés y demos en GitHub (actualizado en 2026). Pasos en tiempo real e histórico, FC, sueño, SpO2, PA, estrés. |
| **OEM** | Logo en pulsera, caja y manual; personalización de app. |
| **Proveedor** | Verified Manufacturer, más de 12 años (directorio de Alibaba). Tienda oficial en Alibaba A CONFIRMAR. |
| **Precio de referencia** | Desde USD 10,99-11,79, MOQ 10 (directorio). A CONFIRMAR. |
| **Riesgo clave** | Reporte público de **falta de autenticación BLE**: cualquiera puede conectarse a la pulsera. Hay que exigir bonding/cifrado. |

**Dónde hablarles:**
- Web: https://www.idoosmart.com (contacto: https://www.idoosmart.com/contact.html)
- **OEM/ODM (Mr. Zeng) y ventas:** **sales@idoocn.com**
- Soporte técnico y seguridad (Mr. Wang): **ido@idoocn.com**. Útil para las preguntas del SDK y del BLE.
- Teléfono: 0755-82529675 (es el de RR.HH.; para ventas usar el email)
- SDK: https://github.com/idoosmart · https://idoosmart.github.io/Flutter_GitBook/en/

---

### Opción C: Veepoo (Shenzhen Veepoo Technology, 维亿魄科技)

| | |
|---|---|
| **Qué es** | **Casa de soluciones**, no una fábrica de producto terminado: desde 2012, más de 100 personas (80 % I+D), centros de I+D en Shenzhen y Fuzhou, más de 30 patentes. Vende **placas PCBA + firmware + algoritmos + app H Band** a fabricantes, y también hace desarrollo a medida. Dicen tener más de 60M usuarios finales. |
| **Producto** | No tiene catálogo propio en Alibaba. La pulsera la fabrica un **socio** suyo. Hay que pedirle a Veepoo que recomiende 2-3 fabricantes que entreguen una banda con su firmware y logo propio. |
| **SDK** | **El mejor que revisé:** público, licencia Apache-2.0, activo en sep-2026. Pasos en tiempo real, histórico cada 5 min, FC, sueño, SpO2, PPG/ECG crudo, **idioma español por API**. Chips Nordic, JieLi o Goodix. |
| **Precio / MOQ** | A CONFIRMAR (depende del fabricante socio). |
| **Riesgo clave** | Hay dos partes (Veepoo hace el firmware y otra empresa fabrica), así que el soporte y la garantía se reparten. El README del SDK dice "para clientes que cooperan": puede requerir acuerdo. |

**Dónde hablarles:**
- Web: https://www.veepoo.cn (en chino; tiene formulario "在线给我们留言")
- Email: **Hi@veepoo.cn**
- Dirección: Kexing Science Park A1-505, Gaoxin Zhong 1st Rd., Yuehai, Nanshan, Shenzhen
- SDK: https://github.com/HBandSDK
- Alternativa: buscar en Alibaba bandas que usen la app "H Band" y preguntar al vendedor si el firmware es Veepoo.

---

### Opciones opcionales (muestras 4 y 5)

**D. Starmax S5 (Shenzhen Starmax Technology).** Es la opción **con pantalla** de 0,96".
- Producto: IP68, 105 mAh.
- Proveedor: 11 años en Alibaba, CE/RoHS/FCC, ISO9001/BSCI, responde en ≤1 h.
- Precio: USD 9,39-11,05.
- Personalización: logo en hebilla o caja gratis desde 100 unidades; **logo de arranque recién desde 5.000 unidades**.
- Contacto: https://istarmax.com/contact-us/ · **sales@istarmax.com** · info@istarmax.com · +86-755-21016803 · Alibaba: https://istarmax.en.alibaba.com

**E. Smart Care B10 (Shenzhen Smart Care Technology).** La **más barata**.
- Precio: USD 7,42-8,43 con MOQ 1.000.
- Producto: 12 días de batería, 3ATM, BLE 5.3.
- **SDK no verificado:** pedir documentación antes de cualquier pago.
- Contacto: solo por Alibaba, https://smartcare.en.alibaba.com (chat de la tienda).

---

## 2. Análisis: ¿cuál es la mejor opción?

| Criterio | J-Style 2208A | IDO | Veepoo |
|---|---|---|---|
| Cumple los 4 requisitos excluyentes con evidencia | **Sí** | 3 de 4 (falta confirmar muestra suelta) | 1 de 4 (solo SDK) |
| Calidad del SDK verificada | Media (a pedido) | **Alta** (pública) | **Muy alta** (pública) |
| Flutter/RN | Anunciado | **Flutter oficial** | No |
| Hardware para contar pasos | **Nordic, 30 días de memoria, 7-10 días de batería** | A definir | Según el socio |
| Riesgo de fraude o seguridad | Medio | **Alto** (sin autenticación BLE) | Medio (usa contraseña de dispositivo) |
| Un solo responsable (fábrica + SDK) | **Sí** | **Sí** | No |
| Velocidad para tener muestra | **Alta** (despacho en ~3 días) | Media | Baja (falta ubicar socio) |

### Veredicto

**La mejor opción hoy es J-Style / JCVital 2208A.**
- Es la única que cumple los cuatro requisitos con evidencia.
- La misma empresa fabrica y da el SDK, así que hay un solo responsable.
- Hardware de calidad (chip Nordic, sensores Bosch/Maxim) y 30 días de memoria: el usuario no pierde pasos aunque tarde en abrir la app.
- Batería de 7-10 días, que baja la fricción.
- SDK gratuito.
- Su foco es B2B de salud: están acostumbrados a integraciones con apps de terceros, que es exactamente nuestro caso.

**Condición para confirmarlo:** que antes de pagar la muestra entreguen documentación y demo del SDK, y que la prueba confirme que se leen pasos en tiempo real e históricos sin su app.

**IDO es la mejor alternativa**, y conviene correrla en paralelo. Tiene el SDK más fácil de evaluar ya mismo (público, con Flutter) y es el proveedor más grande y con mejor precio. **Su punto débil es la seguridad BLE**: si no la resuelven, el riesgo de fraude en un programa de premios es real.

**Veepoo conviene como plan B técnico.** Su SDK es el mejor, pero cada paso es más lento porque hay que sumar un fabricante socio. Recomiendo escribirles igual: con un solo email se sabe si tienen un socio con banda lista y logo propio.

**Sobre la pantalla:** la 2208A no tiene. Si para Pasito es clave que el usuario vea sus pasos en la muñeca, la muestra de Starmax S5 permite comparar. El costo es que el logo de arranque exige 5.000 unidades.

---

## 3. Cronograma estimado (de hoy al lanzamiento con 1.000 unidades)

Los plazos de producción salen de los proveedores. **Aduana argentina, courier y ENACOM son estimaciones a validar con el despachante.**

| Semana | Etapa | Detalle | Responsable |
|---|---|---|---|
| **0-1** | Contacto y RFQ | Enviar `mensaje_rfq.md` a J-Style, IDO y Veepoo (y opcionalmente a Starmax y Smart Care). Pedir documentación y demo del SDK. Respuesta típica: 1-5 días. | Pasito (compras) |
| **1-2** | Evaluar SDK sin hardware | Compilar las demos públicas (IDO, Veepoo) y la de J-Style cuando llegue. Revisar costos, licencias y dependencia de servidores. **Filtro: quien no muestre SDK queda afuera.** | Pasito (dev móvil) |
| **1-2** | Consulta al despachante | Régimen para muestras por courier y para 1.000 unidades, posición arancelaria, homologación ENACOM, seguridad eléctrica del cargador. | Pasito + despachante |
| **2** | Pagar muestras | 1-2 unidades por proveedor, vía Trade Assurance. Exigir UN38.3 y MSDS para el envío. | Pasito |
| **2-5** | Envío de muestras | Despacho en 3-7 días + courier internacional 5-10 días + aduana argentina (**A CONFIRMAR**, puede sumar 1-3 semanas). | Proveedor / courier |
| **4-8** | Pruebas (`checklist_muestras.md`) | Precisión y antitrampa: 2-3 días. Batería: 1-2 semanas, que es el cuello de botella. Uso real: 1 semana. Integración del SDK en la app de prueba iOS/Android: 2-3 semanas en paralelo. | Pasito (QA + dev) |
| **8** | Decisión y negociación | Elegir proveedor. Negociar precio a 1.000 unidades, logo, caja y garantía. Aprobar el arte del logo. Proforma y anticipo del 30 %. | Pasito |
| **8-16** | **Homologación ENACOM** (en paralelo) | Arrancar apenas se elige el modelo, con los reportes de ensayo RF del proveedor. **Duración A CONFIRMAR con el despachante o gestor:** puede ser el camino crítico. | Despachante / gestor |
| **9-14** | Producción | 15-25 días hábiles (J-Style) hasta 6-8 semanas, más una muestra de preproducción con logo para aprobar (~1 semana). | Proveedor |
| **14-15** | Inspección | Inspección antes del embarque (propia o de un tercero, p. ej. SGS/QIMA) y pago del saldo. | Pasito / inspector |
| **15-18** | Envío de 1.000 unidades | **Aéreo** (recomendado por el volumen): ~1-2 semanas + aduana. Marítimo: ~6-8 semanas, más barato pero lento. | Forwarder + despachante |
| **paralelo 8-16** | Integración en la app de Pasito | SDK en producción, vinculación pulsera-cuenta, sync en background, reglas antifraude en el backend, pruebas en beta con 20-50 usuarios. | Pasito (dev) |
| **~18-20** | **Lanzamiento** | Con pulseras liberadas y la app lista. | |

### Resumen de tiempos

- **Escenario optimista:** unas **14 semanas (~3,5 meses)**. Se da si el SDK responde rápido, la aduana de las muestras es ágil, ENACOM sale en paralelo sin demoras y el envío es aéreo.
- **Escenario realista:** **18-22 semanas (~4,5-5 meses)**.
- **Caminos críticos:**
  1. Que el proveedor entregue el SDK rápido.
  2. Aduana de las muestras.
  3. **Homologación de ENACOM**: si no puede correr en paralelo con la producción, suma su duración completa.
  4. Prueba de batería (no se puede acortar).

### Lo que conviene hacer esta semana

1. Mandar el RFQ a **J-Style (info@jointcorp.com + WhatsApp), IDO (sales@idoocn.com, con copia a ido@idoocn.com para lo técnico) y Veepoo (Hi@veepoo.cn)**.
2. Que el equipo móvil empiece a compilar las demos públicas de IDO y Veepoo (no requiere hardware).
3. Agendar la consulta con un despachante sobre ENACOM y el régimen de importación.
