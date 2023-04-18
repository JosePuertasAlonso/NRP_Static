import pandas as pd
import json

class Stakeholder:
    nombre = ""
    importancia = 0
    recomendaciones = []

    def __init__(self, nombre, importancia, recomendaciones):
        self.nombre = nombre
        self.importancia = importancia
        self.recomendaciones = recomendaciones
    
def calcularImportancia():

    with open('datos.json') as file:
        data = json.load(file)
        df_requisitos = pd.DataFrame(data['Requisitos'])

    st0 = 0
    st1 = 0
    st2 = 0
    st3 = 0
    for stakeholder in data['Stakeholder']:

        if stakeholder['Recomendaciones_S']['Stakeholder_0'] == True:
            st0 += 1
        if stakeholder['Recomendaciones_S']['Stakeholder_1'] == True:
            st1 += 1
        if stakeholder['Recomendaciones_S']['Stakeholder_2'] == True:
            st2 += 1
        if stakeholder['Recomendaciones_S']['Stakeholder_3'] == True:
            st3 += 1
    print("Stakeholder 0 importancia: " + str(st0))
    print("Stakeholder 1 importancia: " + str(st1))
    print("Stakeholder 2 importancia: " + str(st2))
    print("Stakeholder 3 importancia: " + str(st3))

        
    