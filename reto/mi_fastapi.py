# FastAPI.py
import random
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field

app = FastAPI()

# Creamos una lista de 10 generadores inicialmente
generadores = [
    {"id": i, "potencia": random.randint(-100, 100), "estado": "activo"}
    for i in range(1, 11)
]

class GeneradorIn(BaseModel):
    potencia: int 
    estado: str

@app.get("/generador/{generador_id}")
def get_generador_info(generador_id: int = Path(..., title="ID del Generador", ge=1, le=len(generadores))):
    generador = generadores[generador_id - 1]  # Obtiene el generador correspondiente al ID proporcionado
    if generador["potencia"] <= 0:  # Verifica si la potencia del generador es menor o igual a 0
        raise HTTPException(status_code=404, detail="Generador no encontrado")  # Si la potencia es 0 o menor, lanza una excepción indicando que el generador no fue encontrado
    return generador  # Devuelve la información del generador


@app.post("/generador/")
def create_generador(generador: GeneradorIn):
    new_id = len(generadores) + 1  # Calcula el nuevo ID para el generador
    generador_dict = generador.dict()  # Convierte el objeto Pydantic GeneradorIn a un diccionario
    generador_dict["id"] = new_id  # Agrega el nuevo ID al diccionario del generador
    generadores.append(generador_dict)  # Agrega el nuevo generador a la lista de generadores
    return {"id": new_id}  # Devuelve el ID del nuevo generador creado


@app.get("/concentrador/")
def get_all_generadores():
    # Filtrar los generadores para mostrar solo aquellos con potencia mayor que 0
    generadores_con_potencia_positiva = [generador for generador in generadores if generador["potencia"] > 0]
    return {"generadores": generadores_con_potencia_positiva}


@app.get("/pconcentrador/media_potencia")
def get_media_potencia_parque():
    # Filtrar los generadores con potencia mayor que 0
    generadores_con_potencia_positiva = [generador for generador in generadores if generador["potencia"] > 0]
    
    # Calcular la suma de la potencia solo para los generadores con potencia mayor que 0
    total_potencia = sum(generador["potencia"] for generador in generadores_con_potencia_positiva)
    
    # Calcular el número de generadores con potencia mayor que 0
    num_generadores_positivos = len(generadores_con_potencia_positiva)
    
    # Calcular la media de la potencia solo para los generadores con potencia mayor que 0
    if num_generadores_positivos > 0:
        media_potencia = total_potencia / num_generadores_positivos
    else:
        media_potencia = 0  # Si no hay generadores con potencia mayor que 0, la media es 0
    
    return {"media_potencia_parque": media_potencia}


