from grafo import Grafo

# Instanciamos el grafo como no dirigido
grafo_casa = Grafo(dirigido=False)

# Creamos los vértices representando los ambientes de la casa
ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
             "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]

for ambiente in ambientes:
    grafo_casa.insert_vertice(ambiente)

# Agregar aristas con pesos (distancias en metros)
grafo_casa.insert_arista("cocina", "comedor", 5)
grafo_casa.insert_arista("cocina", "baño 1", 8)
grafo_casa.insert_arista("cocina", "habitación 1", 12)
grafo_casa.insert_arista("comedor", "sala de estar", 7)
grafo_casa.insert_arista("comedor", "baño 1", 4)
grafo_casa.insert_arista("comedor", "quincho", 10)
grafo_casa.insert_arista("cochera", "patio", 6)
grafo_casa.insert_arista("cochera", "quincho", 9)
grafo_casa.insert_arista("cochera", "habitación 2", 15)
grafo_casa.insert_arista("quincho", "terraza", 11)
grafo_casa.insert_arista("quincho", "baño 2", 7)
grafo_casa.insert_arista("baño 1", "baño 2", 3)
grafo_casa.insert_arista("baño 2", "habitación 2", 5)
grafo_casa.insert_arista("habitación 1", "habitación 2", 6)
grafo_casa.insert_arista("habitación 2", "sala de estar", 8)
grafo_casa.insert_arista("terraza", "patio", 10)
grafo_casa.insert_arista("sala de estar", "terraza", 4)

# Añadimos aristas adicionales para cumplir con el requisito de cinco aristas en dos vértices
grafo_casa.insert_arista("cocina", "terraza", 15)
grafo_casa.insert_arista("cochera", "baño 1", 10)
grafo_casa.insert_arista("cochera", "sala de estar", 14)
grafo_casa.insert_arista("quincho", "habitación 1", 13)

# Generar el árbol de expansión mínima y calcular la longitud total
arbol_expansion_minima = grafo_casa.kruskal("cocina")

# Calcular la longitud total de cables del árbol de expansión mínima
total_metros_cable = 0
for arbol in arbol_expansion_minima:
    segmentos = arbol.split(';')
    for segmento in segmentos:
        partes = segmento.split('-')
        if len(partes) == 3:  # Confirmar que contiene origen, destino y distancia
            distancia = int(partes[2])
            total_metros_cable += distancia

print("Árbol de expansión mínima:", arbol_expansion_minima)
print("Metros de cable necesarios para conectar todos los ambientes:", total_metros_cable)


# Ejecutar Dijkstra desde "habitación 1"
camino_minimo = grafo_casa.dijkstra("habitación 1")

# Encontrar la distancia a la "sala de estar" y el camino específico
distancia_sala_estar = 0
ruta = []

# Usar una lista para simular la pila o verificar el tamaño
while not camino_minimo:  # Cambiado para usar la lista directamente
    nodo = camino_minimo.pop()
    if nodo[1][0] == "sala de estar":
        distancia_sala_estar = nodo[0]
        # Reconstruir la ruta desde "habitación 1" a "sala de estar"
        while nodo:
            ruta.insert(0, nodo[1][0])
            # Asegúrate de que el índice 2 sea correcto y que exista
            nodo = next((n for n in camino_minimo if n[1][0] == nodo[1][2]), None)
        break

print("Ruta más corta desde 'habitación 1' a 'sala de estar':", " -> ".join(ruta))
print("Metros de cable de red necesarios:", distancia_sala_estar)
