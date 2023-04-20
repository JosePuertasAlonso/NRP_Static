import json
class Requisito:
    descripcion = ""
    satisfaccion = 0
    coste= 1

    def __init__(self, descripcion):
        self.descripcion = descripcion
    
    def calcularsatisfaccion(st, req):
        with open('datos.json') as file:
            data = json.load(file)

        cont = 0
        for requisito in req:
            for i in range(len(data['Stakeholder'])):
                if data['Stakeholder'][i]['Recomendaciones_R'][requisito.descripcion] == True:
                    requisito.satisfaccion += st[i].importancia

