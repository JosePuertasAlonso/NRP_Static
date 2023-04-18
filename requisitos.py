import json
class Requisito:
    descripcion = ""



    def __init__(self, descripcion):
        self.descripcion = descripcion

    def getDescripcion():
        with open('datos.json') as file:
            data = json.load(file)

        for i in data['Requisitos']:
            print(i['Descripcion'][0])
            
