grafo = {"A":["B","C","D"],
   "B":["E"],
   "C":["F","G"],
   "D":["H"],
   "E":["I"],
   "F":["J"]}

def dfs(grafo, inicio):

       if inicio is None or inicio not in grafo:
           return "No existe el nodo"

       camino = []
       stack = [inicio]

       while(len(stack) != 0):

           s = stack.pop()

           if s not in camino:
               camino.append(s)

           if s not in grafo:
               continue

           for neighbor in grafo[s]:
               stack.append(neighbor)

       return " ".join(camino)

print(dfs(grafo, "A"))
