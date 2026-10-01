# Checklist de pruebas de muestras

Completar una copia por muestra. Anotar el resultado y la evidencia (fotos, videos, logs). Al final, volver a puntuar al proveedor en `proveedores.csv`.

**Datos de la muestra**

| Campo | Valor |
|---|---|
| Proveedor / modelo | |
| Fecha de recepción / días en tránsito | |
| Costo real (muestra + envío + impuestos/courier) | |
| Firmware / versión de SDK | |
| Teléfonos de prueba (mínimo 1 iPhone y 2 Android de marcas distintas) | |
| Tester(s) | |

---

## 1. Recepción y terminación

- [ ] Embalaje sin daños. Incluye cargador, manual y etiqueta con modelo y número de serie.
- [ ] La caja trae marcas o etiquetas de CE, FCC y RoHS. Aplica la etiqueta de batería de litio.
- [ ] El proveedor mandó documentos de UN38.3, MSDS y CE/FCC (o los envió aparte).
- [ ] Terminación de la carcasa: sin rebabas, juntas parejas, botón firme.
- [ ] Malla: material, olor, comodidad tras 8 h de uso, que el broche no se abra solo.
- [ ] Peso medido (g): ______
- [ ] Pantalla (si tiene): brillo al sol, legibilidad, ángulo de visión.
- [ ] Calidad del logo de muestra (si lo mandaron): nitidez y que resista el roce (frotar 50 veces con el dedo y alcohol isopropílico).

## 2. Precisión de pasos

**Preparación:** 2 personas distintas con la pulsera en la muñeca no dominante. Conteo manual con contador de mano (clicker), o filmando los pies y contando después.

| Prueba | Pasos reales | Pulsera | Error % | Celular (Health/Google Fit) | OK (≤ ±5 %) |
|---|---|---|---|---|---|
| Caminata normal en llano, **1.000 pasos** | 1.000 | | | | |
| Caminata normal, repetición 2 | 1.000 | | | | |
| Caminata rápida, 500 pasos | 500 | | | | |
| Trote, 500 pasos | 500 | | | | |
| Subir y bajar escaleras, 200 pasos | 200 | | | | |
| Caminata lenta (adulto mayor), 300 pasos | 300 | | | | |
| Caminata con las manos en los bolsillos o empujando un carrito, 300 pasos | 300 | | | | |

- [ ] Error promedio ≤ 5 % en caminata normal y ≤ 10 % en los demás casos.
- [ ] La pulsera, el SDK y la app del fabricante muestran **el mismo** total.

## 3. Movimiento falso (antitrampa)

Con la pulsera **sin caminar**: anotar los pasos sumados en cada prueba.

| Prueba (3 minutos cada una) | Pasos sumados | Comentario |
|---|---|---|
| Sacudir la pulsera en la mano | | |
| Agitar el brazo sentado | | |
| Pulsera atada a un ventilador, taladro o licuadora (con cuidado) | | |
| Pulsera colgada de una mascota o un péndulo | | |
| Viajar en auto o colectivo por calle con baches (10 min) | | |
| Tipear o lavar platos (5 min) | | |
| Pulsera sobre la mesa, quieta (30 min) | | |

- [ ] Sacudir con la mano suma **menos de 10 %** de lo que sumaría caminar lo mismo. Si no, el riesgo de fraude es alto.
- [ ] ¿La pulsera detecta "no puesta" (sin PPG)? ¿Lo informa el SDK?
- [ ] ¿El SDK expone datos que permitan detectar trampas (FC durante los pasos, tramos de 1 o 5 min, acelerómetro crudo)?

## 4. Batería

- [ ] Carga completa de 0 a 100 %: tiempo ______ h.
- [ ] Autonomía con la configuración que usaría Pasito (FC automática cada X min, notificaciones apagadas, sync 2 a 3 veces por día): ______ días. Comparar con lo prometido.
- [ ] Autonomía en el peor caso (FC continua, pantalla al máximo): ______ días.
- [ ] Al llegar a 0 %, ¿se pierden datos? Recargar y comprobar si el histórico sigue.
- [ ] Temperatura durante la carga (no debe estar caliente al tacto) y estado del cargador o pines después de 10 cargas.

## 5. Estabilidad de la conexión BLE

- [ ] Primer emparejamiento desde **nuestra app de prueba** en iOS y Android: tiempo y cantidad de intentos.
- [ ] Reconexión automática después de: alejarse 15 m y volver, apagar y prender el Bluetooth, reiniciar el teléfono, matar la app.
- [ ] Sync en segundo plano: ¿iOS y Android sincronizan con la app cerrada o en background? Medir cada cuánto.
- [ ] Sync del histórico después de **3 días y después de 7 días** sin conectar: ¿llegan todos los tramos? ¿Cuánto tarda?
- [ ] 50 ciclos de conectar, sincronizar y desconectar sin cuelgues ni datos duplicados.
- [ ] Alcance útil en interiores: ______ m.
- [ ] **Seguridad:** desde otro teléfono con nRF Connect, ¿se puede conectar y leer o escribir sin autorización mientras la pulsera está vinculada a nuestra app? Documentarlo.
- [ ] Cambio de teléfono: desvincular, vincular a otra cuenta y comprobar que el histórico no se mezcla.

## 6. Integración del SDK (app de prueba iOS y Android)

**Preparación:** app mínima (nativa o Flutter/RN, según el SDK) con estas funciones: escanear, conectar, leer pasos en tiempo real, sincronizar histórico, leer FC y batería, configurar idioma y hora.

| Ítem | iOS | Android |
|---|---|---|
| Instalación del SDK (CocoaPods/SPM/.framework, Gradle/.aar): tiempo hasta compilar | | |
| Compila con Xcode y Android Gradle Plugin actuales y targetSdk vigente (Play Store) | | |
| Demo oficial corre sin cambios | | |
| Escanear y conectar | | |
| Pasos **en tiempo real** (latencia: ___ s) | | |
| Histórico de pasos (granularidad: ___ min; días: ___) | | |
| Distancia / calorías | | |
| FC, sueño, SpO2 | | |
| Configurar hora, unidad e **idioma español** | | |
| Batería y versión de firmware | | |
| OTA de firmware desde nuestra app | | |
| Funciona **sin internet** (modo avión + BT) | | |
| Tráfico de red del SDK (proxy Charles/mitmproxy): ¿llama a servidores? ¿cuáles? | | |
| Permisos que pide (ubicación, contactos, SMS…): ¿son razonables? | | |
| Tamaño agregado a la app (MB) | | |
| Licencias de terceros incluidas (revisar GPL u otras incompatibles) | | |
| Calidad de la doc (1-5) y respuesta del soporte técnico (horas) | | |

- [ ] **No requiere la app del fabricante** en ningún paso.
- [ ] Sin crashes en 1 hora de uso con conexión y desconexión repetidas.

## 7. Resistencia al agua y uso diario

- [ ] Lavarse las manos y ducharse (si es IP67 o mejor): funciona y conserva los datos.
- [ ] Si es IP68 o 5ATM: 30 minutos sumergida a 1 m (balde). Después revisar pantalla, carga y sensores.
- [ ] Uso real de 7 días por 2 personas: comodidad, irritación de la piel, desgaste.

## 8. Resultado

| Criterio | Puntaje 1-5 | Comentario |
|---|---|---|
| Precisión de pasos | | |
| Antitrampa | | |
| Batería | | |
| BLE | | |
| SDK iOS | | |
| SDK Android | | |
| Terminación | | |
| **Decisión** (Avanzar / Avanzar con cambios / Descartar) | | |

**Cambios a pedir al proveedor antes del pedido de 1.000 unidades:**

-
