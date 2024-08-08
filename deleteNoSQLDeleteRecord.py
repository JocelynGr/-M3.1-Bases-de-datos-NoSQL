import requests

# URL base de la API
url = "https://66b4e5159f9169621ea4c277.mockapi.io/api/v1/Contactos"

# ID del registro que quieres eliminar
registro_id = "1"  # Cambia este valor al ID del registro que deseas eliminar

# Construye la URL completa para el registro específico
url_completa = f"{url}/{registro_id}"

# Realiza la solicitud DELETE para eliminar el registro
response = requests.delete(url_completa)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    print(f"Registro con ID {registro_id} eliminado exitosamente.")
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response.text)
