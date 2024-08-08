import logging
import json
import requests
import schedule
import time
from datetime import datetime

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SimulatedService")

# Información del servicio
SERVICE_NAME = "Servicio2"
SERVER_URL = "http://localhost:5000/logs"
API_KEY = "api_key_servicio2"

# Función para generar y enviar un log
def generate_and_send_log():
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "service_name": SERVICE_NAME,
        "log_level": "ERROR",
        "message": "Este es un mensaje de log de ejemplo"
    }

    # Convertir a JSON
    log_data = json.dumps(log_entry)

    # Enviar el log al servidor central
    headers = {
        "Content-Type": "application/json",
        "Authorization": API_KEY
    }
    response = requests.post(SERVER_URL, headers=headers, data=log_data)

    if response.status_code == 200:
        logger.info("Log enviado exitosamente")
    else:
        logger.error(f"Error al enviar log: {response.status_code}")

# Programar la generación de logs cada segundo
schedule.every(30).seconds.do(generate_and_send_log)

# Ejecutar el ciclo de generación de logs
while True:
    schedule.run_pending()
    time.sleep(1)
