"""Envía por WhatsApp la rutina del día (gimnasio + running).

Bloque de 8 semanas que se repite:
  - Semanas 1-3: carga progresiva
  - Semana 4: descarga
  - Semanas 5-7: carga progresiva
  - Semana 8: descarga + test

Variables de entorno:
  WHATSAPP_PROVIDER   "callmebot" (default) o "twilio"
  WHATSAPP_PHONE      tu número con código de país, ej: +5491122334455
  CALLMEBOT_APIKEY    (callmebot) api key que te da el bot
  TWILIO_SID, TWILIO_TOKEN, TWILIO_FROM   (twilio) credenciales y número emisor
  RUTINA_INICIO       fecha de inicio del bloque, YYYY-MM-DD (default 2026-09-28)
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
INICIO = date.fromisoformat(os.environ.get("RUTINA_INICIO", "2026-09-28"))

CALENTAMIENTO_GYM = (
    "🔥 *Entrada en calor (10')*: 5' bici/remo suave + movilidad de cadera, "
    "hombros y tobillos + 2 series livianas del primer básico."
)
CALENTAMIENTO_RUN = (
    "🔥 *Entrada en calor*: 10' trote muy suave + técnica 2x20 m de cada uno: "
    "skipping A, skipping B, taloneo, zancada saltada."
)

# Series/reps de los básicos según la semana del bloque (1-8).
FUERZA = {
    1: "4x6 @RPE7", 2: "4x5 @RPE8", 3: "5x4 @RPE8", 4: "3x5 @RPE6 (descarga)",
    5: "4x5 @RPE8", 6: "5x4 @RPE8", 7: "5x3 @RPE8-9", 8: "3x3 @RPE6 (descarga)",
}
ACCESORIOS = {s: ("2 series" if s in (4, 8) else "3 series") for s in range(1, 9)}

RODAJE = {
    1: "30'", 2: "35'", 3: "40'", 4: "30' (descarga)",
    5: "45'", 6: "50'", 7: "55'", 8: "40' (descarga)",
}

PASADAS = {
    1: "6 x 200 m rápido (RPE 8) · pausa 2' caminando",
    2: "8 x 200 m rápido (RPE 8) · pausa 2' caminando",
    3: "6 x 300 m rápido (RPE 8) · pausa 2'30\" caminando",
    4: "Descarga: 4 x 200 m (RPE 7) · pausa 2'",
    5: "5 x 400 m (RPE 8) · pausa 2'30\" caminando",
    6: "6 x 400 m (RPE 8) · pausa 2'30\" caminando",
    7: "4 x 200 m + 4 x 300 m (RPE 8-9) · pausa 2'30\"",
    8: "TEST: 60 m lanzado cronometrado x2 + 1 km a tope (anotá los tiempos)",
}
SPRINTS = {
    1: "4 x 30 m desde parado", 2: "5 x 30 m desde parado", 3: "4 x 40 m lanzado",
    4: "3 x 30 m desde parado", 5: "5 x 40 m lanzado", 6: "6 x 40 m lanzado",
    7: "4 x 50 m lanzado", 8: "(incluido en el test)",
}


def superior_a(s):
    return [
        "💪 *LUNES · TREN SUPERIOR A (fuerza + potencia)*",
        CALENTAMIENTO_GYM,
        "⚡ *Potencia* (explosivo, sin fatiga):",
        "• Lanzamiento de balón medicinal al pecho contra pared 4x5",
        "• Flexiones pliométricas (con palmada o despegue) 3x5",
        "🏋️ *Fuerza*:",
        f"• Press banca {FUERZA[s]}",
        f"• Remo con barra {FUERZA[s]}",
        "• Press militar de pie 3x6-8",
        "• Dominadas (lastradas si pasás 8) 3x5-8",
        f"🔧 *Accesorios* ({ACCESORIOS[s]}):",
        "• Face pull x12-15 · Curl con barra x10-12 · Extensión tríceps polea x10-12",
    ]


def inferior_a(s):
    return [
        "🦵 *MARTES · TREN INFERIOR A (fuerza + velocidad)*",
        CALENTAMIENTO_GYM,
        "⚡ *Potencia*:",
        "• Salto al cajón 4x3 (bajar caminando)",
        "• Salto horizontal (broad jump) 3x3",
        "🏋️ *Fuerza*:",
        f"• Sentadilla trasera {FUERZA[s]}",
        "• Peso muerto rumano 3x6-8",
        "• Sentadilla búlgara 3x8 c/pierna",
        f"🔧 *Accesorios* ({ACCESORIOS[s]}):",
        "• Gemelos de pie x12-15 · Elevación de tibial x15 · Pallof press x10 c/lado",
    ]


def rodaje(s):
    lineas = [
        "🏃 *MIÉRCOLES · RODAJE SUAVE (base aeróbica)*",
        f"⏱️ *Duración*: {RODAJE[s]} continuos",
        "🎯 *Ritmo*: Zona 2 — tenés que poder hablar en frases completas "
        "(RPE 3-4, ~65-75% FC máx). Si dudás, andá más lento.",
    ]
    if s >= 3 and s not in (4, 8):
        lineas.append("➕ Al final: 4 x 20\" progresivos (strides) con 1' caminando.")
    lineas.append("🧘 Después: 5' de elongación de gemelos, isquios y flexores de cadera.")
    return lineas


def superior_b(s):
    return [
        "💪 *JUEVES · TREN SUPERIOR B (hipertrofia + potencia)*",
        CALENTAMIENTO_GYM,
        "⚡ *Potencia*:",
        "• Push press 4x3 (explosivo)",
        "• Lanzamiento rotacional de balón medicinal 3x5 c/lado",
        "🏋️ *Fuerza / hipertrofia*:",
        "• Press inclinado con mancuernas 4x6-8",
        "• Dominadas o jalón al pecho 4x8",
        "• Fondos en paralelas 3x8-10",
        "• Remo con mancuerna a una mano 3x8-10",
        f"🔧 *Accesorios* ({ACCESORIOS[s]}):",
        "• Elevaciones laterales x12-15 · Curl martillo x10-12 · Face pull x15",
    ]


def inferior_b(s):
    return [
        "🦵 *VIERNES · TREN INFERIOR B (potencia, volumen moderado)*",
        "⚠️ Mañana hay pasadas: nada al fallo, dejá 2-3 reps en reserva.",
        CALENTAMIENTO_GYM,
        "⚡ *Potencia*:",
        "• Hang power clean 5x3 (si no dominás la técnica: swing con kettlebell 5x8)",
        "• Bounds / saltos alternados 3x4 c/pierna",
        "🏋️ *Fuerza*:",
        f"• Peso muerto convencional {FUERZA[s]}",
        "• Hip thrust 3x8",
        "• Curl nórdico 3x4-6 (clave para proteger isquios en los sprints)",
        f"🔧 *Accesorios* ({ACCESORIOS[s]}):",
        "• Step-up al cajón x8 c/pierna · Copenhagen plank 20\" c/lado",
    ]


def pasadas(s):
    return [
        "⚡ *SÁBADO · PASADAS (velocidad)*",
        CALENTAMIENTO_RUN,
        "➕ 3 aceleraciones progresivas de 60 m (al 70-80-90%).",
        f"🚀 *Velocidad máxima*: {SPRINTS[s]} al 95-100% · pausa COMPLETA 2-3' "
        "(la calidad es todo, si te sale más lento cortá).",
        f"🔁 *Pasadas*: {PASADAS[s]}",
        "🧊 *Vuelta a la calma*: 10' trote muy suave + elongación.",
    ]


def descanso(s):
    return [
        "😴 *DOMINGO · DESCANSO*",
        "Recuperación activa opcional: 20-30' caminata, 10' de movilidad, "
        "dormí bien y comé proteína suficiente.",
        "📋 Revisá cómo te sentiste en la semana: si llegaste muy cansado, "
        "bajá un poco el volumen la próxima.",
    ]


DIAS = [superior_a, inferior_a, rodaje, superior_b, inferior_b, pasadas, descanso]


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
