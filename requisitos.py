import json
class Requisito:
    descripcion = ""
    satisfaccion = 0
    coste= 1

    def __init__(self, descripcion):
        self.descripcion = descripcion
    
    def calcular_satisfaccion(st, req):
        with open('datos.json') as file:
            data = json.load(file)

        for requisito in req:
            for i in range(len(data['Stakeholder'])):
                if data['Stakeholder'][i]['Recomendaciones_R'][requisito.descripcion] == True:
                    requisito.satisfaccion += st[i].importancia

    def calcular_greedy(req, limite):
        cur_limit = 0
        sprints = {}
        req.sort(key=lambda x: x.satisfaccion, reverse=True)
        
        cont = 1
        sprints["Sprint " + str(cont)] = []
        for i in range(len(req)):
            if cur_limit < limite:
                sprints["Sprint " + str(cont)].append(req[i])  
            else:
                cont += 1
                cur_limit = 0
                sprints["Sprint " + str(cont)] = [req[i]]
                
            cur_limit += req[i].coste
 

        for clave, valor in sprints.items():
            print('\n' + clave + ":")
            for descripcion in valor:
                print("- " + descripcion.descripcion)
            print("Satisfaccion total sprint: " + str(sum(x.satisfaccion for x in valor)))

