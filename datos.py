import pandas as pd
import json
import stakeholder as st

with open('datos.json') as file:
    data = json.load(file)

df_requisitos = pd.DataFrame(data['Requisitos'])
df_stakeholders = pd.DataFrame(data['Stakeholder'])
df = pd.json_normalize(data, 'Stakeholder')

print("DATOS RECOGIDOS")
print(df_requisitos)
print(df_stakeholders)



        



st.calcularImportancia()