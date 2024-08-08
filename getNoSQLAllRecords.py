import requests
import pandas as pd
import json  # Importa el módulo json

# URL de la API
url = "https://66b4e5159f9169621ea4c277.mockapi.io/api/v1/Contactos"

# Realiza la solicitud GET a la API
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Obtiene los datos en formato JSON
    data = response.json()

    # Muestra los registros en formato JSON formateado
    print("Registros en formato JSON:")
    print(json.dumps(data, indent=4))

    # Convierte los datos a un DataFrame
    df = pd.DataFrame(data)

    # Muestra el DataFrame
    print("\nDataFrame:")
    print(df)

    # Exporta el DataFrame a un archivo CSV
    df.to_csv("contactos.csv", index=False)
    print("\nArchivo CSV 'contactos.csv' creado con éxito.")
else:
    print(f"Error en la solicitud: {response.status_code}")
