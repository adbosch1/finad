"""Envía la rutina del día (running + gimnasio).

Plan de 6 días con foco en correr más rápido y bajar de peso:
  Lun  Gimnasio: tren superior A (+ trote suave opcional)
  Mar  Running: pasadas (calidad)
  Mié  Gimnasio: tren inferior (fuerza + potencia)
  Jue  Running: rodaje suave / progresivo
  Vie  Gimnasio: superior B + core (corto, sin piernas)
  Sáb o Dom  Running: fondo largo (el otro día, descanso)

Bloque de 8 semanas que se repite:
  - Semanas 1-3: carga progresiva
  - Semana 4: descarga
  - Semanas 5-7: carga progresiva
  - Semana 8: descarga + test de 5 km

Ritmos de referencia (21 km a 4:47/km el año pasado, ajustados porque
venís oxidado; se recalculan con el test de la semana 8).

Variables de entorno:
  WHATSAPP_PROVIDER   "callmebot" (default) o "twilio"
  WHATSAPP_PHONE      tu número con código de país, ej: +5491122334455
  CALLMEBOT_APIKEY    (callmebot) api key que te da el bot
  TWILIO_SID, TWILIO_TOKEN, TWILIO_FROM   (twilio) credenciales y número emisor
  RUTINA_INICIO       fecha de inicio del bloque, YYYY-MM-DD (default 2026-10-05)
  RUTINA_FECHA        fuerza una fecha (para probar), YYYY-MM-DD
  DRY_RUN=1           imprime el mensaje sin enviarlo
"""

import os
import sys
import urllib.parse
import urllib.request
from base64 import b64encode
from datetime import date, datetime
from zoneinfo import ZoneInfo

TZ = ZoneInfo("America/Argentina/Buenos_Aires")
INICIO = date.fromisoformat(os.environ.get("RUTINA_INICIO", "2026-10-05"))

RITMOS = (
    "📏 *Ritmos de referencia*: suave 5:50-6:30/km · maratón ~5:10 · "
    "umbral 4:55-5:05 · pasadas de 1 km 4:30-4:40 · 400 m en 1:45-1:50"
)
CALENTAMIENTO_GYM = (
    "🔥 *Entrada en calor (10')*: 5' bici/remo suave + movilidad de cadera, "
    "hombros y tobillos + 2 series livianas del primer básico."
)
CALENTAMIENTO_RUN = (
    "🔥 *Entrada en calor*: 15' trote suave + técnica 2x20 m (skipping A, "
    "skipping B, taloneo) + 4 aceleraciones de 60 m al 80-90%."
)
DESCARGA = (4, 8)

# Series/reps de los básicos según la semana del bloque (1-8).
FUERZA = {
    1: "4x6 @RPE7", 2: "4x5 @RPE8", 3: "5x4 @RPE8", 4: "3x5 @RPE6 (descarga)",
    5: "4x5 @RPE8", 6: "5x4 @RPE8", 7: "5x3 @RPE8", 8: "3x3 @RPE6 (descarga)",
}
ACCESORIOS = {s: ("2 series" if s in DESCARGA else "3 series") for s in range(1, 9)}

PASADAS = {
    1: "8 x 400 m en 1:48-1:52 · pausa 1'30\" trotando",
    2: "6 x 800 m a 4:35-4:40/km · pausa 2' trotando",
    3: "5 x 1000 m a 4:35/km · pausa 2' trotando",
    4: "Descarga: 6 x 400 m cómodos (1:52-1:55) · pausa 1'30\"",
    5: "3 x 2000 m a umbral (4:55-5:00/km) · pausa 2' trotando",
    6: "10 x 400 m en 1:45-1:48 · pausa 1'15\" trotando",
    7: "5 x 1000 m a 4:30/km · pausa 1'45\" trotando",
    8: "TEST: 5 km a tope (anotá el tiempo, con eso recalculamos los ritmos)",
}

RODAJE = {
    1: "40' suaves + 4 x 20\" progresivos",
    2: "45' suaves + 6 x 20\" progresivos",
    3: "45': 35' suaves + 10' a ritmo maratón (~5:10/km)",
    4: "35' suaves (descarga)",
    5: "50': 35' suaves + 15' a ritmo maratón (~5:10/km)",
    6: "50' suaves + 6 x 20\" progresivos",
    7: "55': 35' suaves + 20' a ritmo maratón (~5:10/km)",
    8: "35' suaves + 4 x 20\" progresivos (descarga)",
}

FONDO = {
    1: "60' continuos suaves", 2: "70' continuos suaves", 3: "80' continuos suaves",
    4: "60' continuos suaves (descarga)", 5: "85' continuos suaves",
    6: "90': 75' suaves + últimos 15' a ritmo maratón (~5:10/km)",
    7: "100' continuos suaves", 8: "50' suaves (semana de test, sin exigirte)",
}

# Trote opcional después del gimnasio del lunes (desde semana 2, no en descarga).
TROTE_EXTRA = {s: (None if s in (1, 4, 8) else "20-25' suaves") for s in range(1, 9)}


def superior_a(s):
    lineas = [
        "💪 *LUNES · GIMNASIO: TREN SUPERIOR A (fuerza + potencia)*",
        CALENTAMIENTO_GYM,
        "⚡ *Potencia* (explosivo, sin fatiga):",
        "• Lanzamiento de balón medicinal al pecho contra pared 4x5",
        "• Flexiones pliométricas 3x5",
        "🏋️ *Fuerza*:",
        f"• Press banca {FUERZA[s]}",
        f"• Remo con barra {FUERZA[s]}",
        "• Press militar de pie 3x6-8",
        "• Dominadas 3x5-8",
        f"🔧 *Accesorios* ({ACCESORIOS[s]}):",
        "• Face pull x12-15 · Curl con barra x10-12 · Extensión tríceps polea x10-12",
    ]
    if TROTE_EXTRA[s]:
        lineas.append(
            f"🏃 *Opcional (suma para bajar de peso)*: {TROTE_EXTRA[s]} en cinta o "
            "afuera después de las pesas, Zona 2."
        )
    return lineas


def pasadas(s):
    return [
        "⚡ *MARTES · RUNNING: PASADAS (velocidad)*",
        CALENTAMIENTO_RUN,
        f"🔁 *Bloque principal*: {PASADAS[s]}",
        "🧊 *Vuelta a la calma*: 10' trote muy suave + elongación.",
        RITMOS,
        "💡 Si la última repetición sale más lenta que la primera, arrancaste muy rápido.",
    ]


def inferior(s):
    return [
        "🦵 *MIÉRCOLES · GIMNASIO: TREN INFERIOR (fuerza + potencia)*",
        "⚠️ Mañana corrés: dejá 2 reps en reserva, nada al fallo.",
        CALENTAMIENTO_GYM,
        "⚡ *Potencia*:",
        "• Salto al cajón 4x3 (bajar caminando)",
        "• Saltos alternados (bounds) 3x4 c/pierna",
        "🏋️ *Fuerza*:",
        f"• Sentadilla trasera {FUERZA[s]}",
        "• Peso muerto rumano 3x6-8",
        "• Sentadilla búlgara 3x8 c/pierna",
        "• Curl nórdico 3x4-6 (protege isquios)",
        f"🔧 *Accesorios* ({ACCESORIOS[s]}):",
        "• Gemelos a una pierna x12-15 · Elevación de tibial x15 · Copenhagen plank 20\" c/lado",
    ]


def rodaje(s):
    return [
        "🏃 *JUEVES · RUNNING: RODAJE (base aeróbica)*",
        f"⏱️ *Sesión*: {RODAJE[s]}",
        "🎯 *Suave* = Zona 2, podés hablar en frases completas (5:50-6:30/km). "
        "Si dudás, más lento.",
        "🧘 Después: 5' de elongación de gemelos, isquios y flexores de cadera.",
    ]


def superior_b(s):
    return [
        "💪 *VIERNES · GIMNASIO: SUPERIOR B + CORE (corto, sin piernas)*",
        "⚠️ El fin de semana va el fondo largo: piernas descansadas.",
        CALENTAMIENTO_GYM,
        "⚡ *Potencia*: Lanzamiento rotacional de balón medicinal 3x5 c/lado",
        "🏋️ *Fuerza / hipertrofia*:",
        "• Press inclinado con mancuernas 4x6-8",
        "• Dominadas o jalón al pecho 4x8",
        "• Fondos en paralelas 3x8-10",
        "• Remo con mancuerna a una mano 3x8-10",
        f"🧱 *Core* ({ACCESORIOS[s]}):",
        "• Plancha 40\" · Dead bug x10 c/lado · Pallof press x10 c/lado",
    ]


def _fondo(s):
    return [
        f"⏱️ *Sesión*: {FONDO[s]}",
        "🎯 *Suave* = 5:50-6:30/km o más lento si hay desnivel.",
        "⛰️ Si podés, hacelo en trail o con desnivel: mismo tiempo, ritmo por sensación.",
        "💧 Más de 75': llevá agua y un gel o algo de azúcar a partir de los 45'.",
        "🎯 La idea es terminar con la sensación de que podrías haber seguido.",
    ]


def sabado(s):
    return [
        "🏞️ *SÁBADO · FONDO LARGO (hoy o mañana)*",
        "Elegí el día: el fondo hoy y mañana descanso, o al revés.",
    ] + _fondo(s)


def domingo(s):
    return [
        "🏞️ *DOMINGO · FONDO LARGO o DESCANSO*",
        "👉 Si ayer no hiciste el fondo, hoy toca:",
    ] + _fondo(s) + [
        "",
        "😴 Si ya lo hiciste: descanso total o 30' de caminata + movilidad.",
        "🍽️ Para bajar de peso: déficit moderado (300-500 kcal/día), proteína "
        "1,6-2 g por kg de peso y no recortes carbohidratos los días de pasadas y fondo.",
    ]


DIAS = [superior_a, pasadas, inferior, rodaje, superior_b, sabado, domingo]


def mensaje(hoy: date) -> str:
    semana = ((hoy - INICIO).days // 7) % 8 + 1
    cuerpo = DIAS[hoy.weekday()](semana)
    encabezado = f"🗓️ *{hoy.strftime('%d/%m')}* · Semana {semana}/8 del bloque"
    return "\n".join([encabezado, ""] + cuerpo + ["", "¡Vamos! 💥"])


def enviar(texto: str) -> None:
    proveedor = os.environ.get("WHATSAPP_PROVIDER", "callmebot").lower()
    telefono = os.environ["WHATSAPP_PHONE"]

    if proveedor == "callmebot":
        params = urllib.parse.urlencode({
            "phone": telefono,
            "text": texto,
            "apikey": os.environ["CALLMEBOT_APIKEY"],
        })
        req = urllib.request.Request(f"https://api.callmebot.com/whatsapp.php?{params}")
    elif proveedor == "twilio":
        sid = os.environ["TWILIO_SID"]
        auth = b64encode(f"{sid}:{os.environ['TWILIO_TOKEN']}".encode()).decode()
        data = urllib.parse.urlencode({
            "From": f"whatsapp:{os.environ['TWILIO_FROM']}",
            "To": f"whatsapp:{telefono}",
            "Body": texto,
        }).encode()
        req = urllib.request.Request(
            f"https://api.twilio.com/2010-04-01/Accounts/{sid}/Messages.json",
            data=data,
            headers={"Authorization": f"Basic {auth}"},
        )
    else:
        sys.exit(f"Proveedor desconocido: {proveedor}")

    with urllib.request.urlopen(req, timeout=30) as resp:
        print(f"Enviado ({proveedor}): HTTP {resp.status}")


if __name__ == "__main__":
    fecha = os.environ.get("RUTINA_FECHA")
    hoy = date.fromisoformat(fecha) if fecha else datetime.now(TZ).date()
    texto = mensaje(hoy)
    print(texto)
    if os.environ.get("DRY_RUN") != "1":
        enviar(texto)
