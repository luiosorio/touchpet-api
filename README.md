# touchpet-api
Api in Python with Firebase to manage Touch Pet Data

## Pasos para ejecutar la Api

1. Clonar el repositorio
2. Abrir la terminal en la carpeta del proyecto
3. Ejecutar en la terminal el comando **.apirest\Scripts\activate**
4. Si sale una excepcion o error "PSSecurityException" se debe ejecutar el comando  **Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process**  
5. Despues de superar la excepcion, ejecutar en la terminal el comando **.apirest\Scripts\activate**, si no salio la excepcion saltar al paso 6.
6. Instalar los paquetes necesarios ejecutando el comando **pip install -r requirements.txt**
7. Ejecutar la API con el comando **python .\aplicacion.py**
8. Se pueden probar los endpoints desde postman, instalando POSTMAN e importando la coleccion del archivo **./API TouchPet.postman_collection.json**
