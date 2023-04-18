import pandas as pd
import json
import stakeholder as st

with open('datos.json') as file:
    data = json.load(file)

df_requisitos = pd.DataFrame(data['Requisitos'])
df_stakeholders = pd.DataFrame(data['Stakeholder'])

st_array = []
for i in range(len(data['Stakeholder'])):
    st_array.append(st.Stakeholder(data['Stakeholder'][i]['Nombre']))
    st.Stakeholder.calcularImportancia(st_array[i])

print("DATOS RECOGIDOS\n")
print(df_requisitos)
print(df_stakeholders)

print("\nIMPORTANCIA DE CADA STAKEHOLDER")
for i in range(len(st_array)):
    print(st_array[i].nombre + " " + str(st_array[i].importancia))

