import requests
import json

# URL de la API
url = "https://66b4e5159f9169621ea4c277.mockapi.io/api/v1/Contactos"

# Datos del nuevo registro
nuevo_registro = {
    "nombre": "Juan Pérez",
    "pais": "México",
    "estado": "Hidalgo",
    "ciudad": "Pachuca",
    "Imagen": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/555.jpg",
    "genero": "No binario"
}

# Realiza la solicitud POST para agregar el nuevo registro
response = requests.post(url, json=nuevo_registro)

# Verifica si la solicitud fue exitosa
if response.status_code == 201:
    # Obtiene los datos del nuevo registro en formato JSON
    data = response.json()

    # Muestra los datos del nuevo registro
    print("Nuevo registro agregado exitosamente:")
    print(json.dumps(data, indent=4))
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response.text)
