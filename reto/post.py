import requests
import json
import random

# Generar datos aleatorios para el nuevo generador
potencia_aleatoria = random.randint(-100, 200)  # Permitir valores negativos
estado = "activo"

# Verificar si la potencia es negativa
if potencia_aleatoria < 0:
    print("Error: Potencia negativa. No se puede crear el generador.")
else:
    # Definir los datos del generador a crear
    generador_data = {
        "potencia": potencia_aleatoria,
        "estado": estado
    }

    # Definir la URL del endpoint POST /generador/
    url = "http://localhost:8080/generador/"

    # Realizar la solicitud POST
    response = requests.post(url, json=generador_data)

    # Verificar la respuesta
    if response.status_code == 200:
        print("Generador creado exitosamente. ID del generador:", response.json()["id"])
    else:
        print("Error al crear el generador. Código de estado:", response.status_code)

