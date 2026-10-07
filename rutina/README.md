# Rutina running + gimnasio → mail diario

Foco: correr más rápido, bajar de peso y sentirse cada vez más cómodo corriendo, sin dejar el gimnasio.

| Día | Sesión |
|---|---|
| Lunes | Gimnasio: tren superior A (fuerza + potencia) + trote suave opcional de 20-25' |
| Martes | Running: pasadas (400 m a 2000 m, según la semana) |
| Miércoles | Gimnasio: tren inferior (sentadilla, rumano, búlgara, nórdico, pliometría) |
| Jueves | Running: rodaje suave (40-55'), con progresivos o tramo a ritmo maratón |
| Viernes | Gimnasio: superior B + core (corto, sin piernas) |
| Sábado o domingo | Running: fondo largo (60' → 100'), el otro día descanso |

Bloque de 8 semanas (semanas 4 y 8 de descarga; semana 8 con test de 5 km) que se repite.
Ritmos de referencia a partir de 21 km a 4:47/km, ajustados para la vuelta:
suave 5:50-6:30/km · maratón ~5:10 · umbral 4:55-5:05 · 1 km 4:30-4:40 · 400 m 1:45-1:50.

Todo el contenido está en `enviar_rutina.py`.

## Envío
Hoy el mail lo manda una tarea programada de Claude (8:55, hora Argentina) que corre
`DRY_RUN=1 python3 rutina/enviar_rutina.py` y agrega un resumen de noticias.

### Alternativa: WhatsApp con GitHub Actions
1. Mandale `I allow callmebot to send me messages` al número de CallMeBot
   (https://www.callmebot.com/blog/free-api-whatsapp-messages/) y guardá la apikey.
2. Cargá los secrets `WHATSAPP_PHONE` y `CALLMEBOT_APIKEY` en GitHub
   (o `WHATSAPP_PROVIDER=twilio` + `TWILIO_SID`, `TWILIO_TOKEN`, `TWILIO_FROM`).
3. Mergeá a `main` (los cron solo corren desde la rama principal).

## Probar localmente
```bash
DRY_RUN=1 RUTINA_FECHA=2026-10-13 python3 rutina/enviar_rutina.py
```
