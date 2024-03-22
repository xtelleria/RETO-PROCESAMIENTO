# RETO-PROCESAMIENTO
## Objetivo del Proyecto:

El objetivo de este proyecto es simular el funcionamiento de un parque eólico mediante la implementación de un sistema que consta de 10 generadores de energía eólica y un concentrador. Este sistema tiene como propósito principal validar los datos generados por cada generador, realizar agregaciones de datos, como la media de producción del parque, y gestionar la posibilidad de que haya datos erróneos con una probabilidad N.

El sistema está desarrollado utilizando FastAPI, un framework web rápido para construir APIs con Python. Cada generador de energía eólica es representado por un programa individual que genera datos sintéticos de forma diferente. El concentrador, implementado con FastAPI, valida los datos recibidos de los generadores y proporciona funcionalidades de agregación de datos, como calcular la media de producción del parque y agregados minutales.
## Explicación de los Pasos Seguidos:

1. **Leer la Documentación de FastAPI:** Se realizó una lectura detallada de la documentación oficial de FastAPI para comprender su funcionamiento y características principales. Se prestaron especial atención a los conceptos relacionados con la creación de APIs, manejo de rutas, validación de datos, y manejo de errores.

2. **Hacer Pruebas Simples del Tutorial de FastAPI:** Se siguieron los ejemplos simples proporcionados en el tutorial de FastAPI para entender cómo funciona el framework en la práctica. Se realizaron pruebas básicas de creación de rutas, definición de modelos de datos, y manejo de solicitudes HTTP.

3. **Diseñar el Modelo de Datos:** Se diseñó un modelo de datos que representara adecuadamente la estructura de un parque eólico, incluyendo la información de los generadores y del concentrador. Se decidió utilizar clases de Pydantic para definir modelos de datos que facilitaran la validación y serialización de los datos.

4. **Implementar GET y POST:** Se implementaron las rutas GET y POST utilizando FastAPI. La ruta GET se utilizó para obtener información sobre los generadores individuales y el concentrador, mientras que la ruta POST se utilizó para crear nuevos generadores en el parque.

5. **Manejar Errores Potenciales:** Se identificaron posibles escenarios de error en el sistema, como datos erróneos provenientes de los generadores o solicitudes incorrectas por parte de los clientes. Se implementaron mecanismos para manejar estos errores de manera adecuada, utilizando excepciones HTTP y validaciones de datos.

6. **Añadir la Media de la Potencia de los Generadores:** Se agregó una funcionalidad adicional para calcular la media de la potencia de los generadores en el parque. Se diseñó una ruta específica para este propósito y se implementó la lógica necesaria para calcular la media de manera eficiente.

## Ejecución del Proyecto:

1. **Ejecutar el Servidor FastAPI:** Desde una terminal, ejecutar el siguiente comando para iniciar el servidor FastAPI:
    uvicorn mi_fastapi:app --reload --port 8080
2. **Enviar Datos a través de POST:** Desde otra terminal, ejecutar el siguiente comando para enviar datos a través de POST al servidor FastAPI:
    python3 post.py

## Retos Encontrados:

1. **Manejo del Error:** Uno de los principales retos encontrados fue el adecuado manejo de errores en el sistema. Se debió identificar los posibles escenarios de error y diseñar mecanismos para manejarlos de manera eficiente y proporcionar retroalimentación adecuada al usuario o cliente de la API.

2. **Entender el Objetivo del Reto:** Otra dificultad fue comprender completamente el objetivo del reto y diseñar una solución que cumpliera con todos los requisitos especificados, incluyendo la validación de datos, la agregación de información y el manejo de errores potenciales.

## Alternativas Posibles: Flask

Como alternativa a FastAPI, se consideró el uso del framework Flask para la implementación de la API. Flask es un microframework web para Python que es fácil de aprender y utilizar, y ofrece una gran flexibilidad para construir aplicaciones web.

Sin embargo, se optó por FastAPI debido a su rendimiento superior y su capacidad integrada de validación de datos y generación de documentación automática. FastAPI es especialmente adecuado para aplicaciones que requieren alta velocidad y eficiencia, como en el caso de este proyecto de procesamiento de datos en un parque eólico.
