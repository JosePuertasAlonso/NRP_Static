import pandas as pd
import json
import stakeholder as st
import requisitos as req

with open('datos.json') as file:
    data = json.load(file)

df_requisitos = pd.DataFrame(data['Requisitos'])
df_stakeholders = pd.DataFrame(data['Stakeholder'])
limite = 3

st_array = []
req_array = []

for i in range(len(data['Stakeholder'])):
    st_array.append(st.Stakeholder(data['Stakeholder'][i]['Nombre']))
    st.Stakeholder.calcularImportancia(st_array[i])

for i in range(len(data['Requisitos'])):
    req_array.append(req.Requisito(data['Requisitos'][i]['Descripcion']))

req.Requisito.calcularsatisfaccion(st_array, req_array)


print("DATOS RECOGIDOS\n")
print(df_requisitos)
print(df_stakeholders)

print("\nIMPORTANCIA DE CADA STAKEHOLDER")
for i in range(len(st_array)):
    print(st_array[i].nombre + " -> " + str(st_array[i].importancia))

print("\nSATISFACCION DE CADA REQUISITO")
for i in range(len(req_array)):
    print(req_array[i].descripcion + " -> " + str(req_array[i].satisfaccion))



