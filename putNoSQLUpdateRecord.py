import requests
import json

# URL base de la API
url = "https://66b4e5159f9169621ea4c277.mockapi.io/api/v1/Contactos"

# ID del registro que quieres modificar
registro_id = "1"  # Cambia este valor al ID del registro que deseas modificar

# Datos que deseas actualizar en el registro
actualizacion_registro = {
    "nombre": "Juan Pérez Modificado",
    "email": "juan.perez.modificado@example.com",
    "telefono": "0987654321",
    "direccion": "Avenida Siempre Viva 742",
    "ciudad": "Ciudad Actualizada"
}

# Construye la URL completa para el registro específico
url_completa = f"{url}/{registro_id}"

# Realiza la solicitud PUT para modificar el registro
response = requests.put(url_completa, json=actualizacion_registro)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Obtiene los datos del registro actualizado en formato JSON
    data = response.json()

    # Muestra los datos del registro actualizado
    print("Registro modificado exitosamente:")
    print(json.dumps(data, indent=4))
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response.text)
