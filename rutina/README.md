# Rutina gimnasio + running → WhatsApp diario

| Día | Sesión |
|---|---|
| Lunes | Tren superior A: fuerza + potencia (balón medicinal, flexiones pliométricas, banca, remo, militar, dominadas) |
| Martes | Tren inferior A: fuerza + velocidad (saltos al cajón, broad jump, sentadilla, rumano, búlgara) |
| Miércoles | Rodaje suave en Zona 2 (30' → 55' a lo largo del bloque) |
| Jueves | Tren superior B: hipertrofia + potencia (push press, lanzamiento rotacional, inclinado, fondos) |
| Viernes | Tren inferior B: potencia con volumen moderado (hang clean, bounds, peso muerto, curl nórdico) |
| Sábado | Pasadas: sprints cortos a velocidad máxima + pasadas de 200–400 m |
| Domingo | Descanso |

Bloque de 8 semanas (semanas 4 y 8 de descarga; semana 8 con test) que se repite.
Todo el contenido está en `enviar_rutina.py`.

## Activar el envío por WhatsApp (CallMeBot, gratis)

1. Agendá el número de CallMeBot (lo tenés en https://www.callmebot.com/blog/free-api-whatsapp-messages/)
   y mandale por WhatsApp: `I allow callmebot to send me messages`. Te responde con tu **apikey**.
2. En GitHub: *Settings → Secrets and variables → Actions → New repository secret*:
   - `WHATSAPP_PHONE` = tu número con código de país (ej. `+5491122334455`)
   - `CALLMEBOT_APIKEY` = la apikey que te dio el bot
3. Mergeá esta rama a `main` (los cron de GitHub solo corren desde la rama principal).
4. Probá ya mismo desde *Actions → Rutina diaria por WhatsApp → Run workflow*.

### Alternativa: Twilio
Creá la variable `WHATSAPP_PROVIDER=twilio` y los secrets `TWILIO_SID`, `TWILIO_TOKEN`, `TWILIO_FROM`.

## Probar localmente
```bash
DRY_RUN=1 RUTINA_FECHA=2026-10-03 python3 rutina/enviar_rutina.py
```
