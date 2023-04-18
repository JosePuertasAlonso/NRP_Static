import pandas as pd
import json

class Stakeholder:
    nombre = ""
    importancia = 0

    def __init__(self, nombre):
        self.nombre = nombre
    
    def calcularImportancia(st):

        with open('datos.json') as file:
            data = json.load(file)
        for stakeholder in data['Stakeholder']:
            if stakeholder['Recomendaciones_S'][st.nombre] == True:
                st.importancia += 1

        
    