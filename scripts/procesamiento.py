import pandas as pd

datos = {
    "agente": ["Juan", "Maria", "Carlos"],
    "llamadas": [120, 110, 130],
    "adherencia": [95, 92, 97]
}

df = pd.DataFrame(datos)

print("Reporte WFM - GTR")
print(df)

print("Total llamadas:", df["llamadas"].sum())
print("Adherencia promedio:", df["adherencia"].mean())