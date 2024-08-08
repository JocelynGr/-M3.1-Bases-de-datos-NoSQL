import requests
import json

# URL de la API
url = "https://66b4e5159f9169621ea4c277.mockapi.io/api/v1/Contactos"

# ID del registro que quieres mostrar
registro_id = "5"  # Cambia este valor al ID del registro que quieres consultar

# Realiza la solicitud GET a la API para obtener todos los registros
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Obtiene los datos en formato JSON
    data = response.json()

    # Busca el registro con el ID especificado
    registro = next((item for item in data if item['id'] == registro_id), None)

    if registro:
        # Muestra el registro en formato plano
        print("Registro en formato plano:")
        for campo, valor in registro.items():
            print(f"{campo}: {valor}")
    else:
        print(f"Registro con ID {registro_id} no encontrado.")
else:
    print(f"Error en la solicitud: {response.status_code}")
