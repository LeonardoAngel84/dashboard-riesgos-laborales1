import pandas as pd
import matplotlib.pyplot as plt

# Cargar Excel
df = pd.read_excel("Dashboard_Pro.xlsx", sheet_name="Matriz_de_Riesgos")

# Calcular Nivel de Riesgo
df["Nivel_Riesgo"] = df["Probabilidad"] * df["Consecuencia"]

# Clasificación automática
def clasificar(valor):
    if valor <= 8:
        return "Tolerable"
    elif valor <= 16:
        return "Moderado"
    elif valor <= 24:
        return "Importante"
    else:
        return "Intolerable"

df["Clasificación"] = df["Nivel_Riesgo"].apply(clasificar)

# Conteo de riesgos
conteo = df["Clasificación"].value_counts()

print(conteo)

# Gráfico
conteo.plot(kind="bar")
plt.title("Distribución de Riesgos")
plt.xlabel("Nivel de Riesgo")
plt.ylabel("Cantidad")
plt.show()