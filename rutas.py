# SISTEMA DE RUTAS CON INTELIGENCIA ARTIFICIAL
# Algoritmo A* (A estrella)

import heapq


# BASE DE CONOCIMIENTO

# Representamos el sistema de transporte como un grafo
# Cada letra que vemos es una estación y los valores son las conexiones con su costo (tiempo)
grafo = {
    "A": {"B": 5, "C": 10},
    "B": {"A": 5, "D": 3, "E": 7},
    "C": {"A": 10, "F": 2},
    "D": {"B": 3, "G": 6},
    "E": {"B": 7, "F": 1, "G": 3},
    "F": {"C": 2, "E": 1, "H": 4},
    "G": {"D": 6, "E": 3, "H": 2},
    "H": {"F": 4, "G": 2}
}

# Esta es la heurística, una estimación de que tan lejos esta cada nodo del destino.
# IMPORTANTE: valores aproximados, sirve para guiar la busqueda.
heuristica = {
    "A": 10,
    "B": 8,
    "C": 5,
    "D": 7,
    "E": 3,
    "F": 6,
    "G": 2,
    "H": 0  # destino final 
}

# REGLAS LÓGICAS

def es_conectado(nodo, vecino):
    return vecino in grafo[nodo]

def costo_camino(actual, vecino):
    return grafo[actual][vecino]


# ALGORITMO A*

def a_estrella(inicio, destino):
    abiertos = []
    heapq.heappush(abiertos, (0, inicio))

    # Costos
    g_costos = {nodo: float("inf") for nodo in grafo}
    g_costos[inicio] = 0

    padres = {}

    while abiertos:
        _, actual = heapq.heappop(abiertos)

        # Si llego al destino, ya terminé
        if actual == destino:
            return reconstruir_ruta(padres, actual), g_costos[destino]

        # Expandir nodos vecinos
        for vecino in grafo[actual]:
            if es_conectado(actual, vecino):

                nuevo_costo = g_costos[actual] + costo_camino(actual, vecino)

                # Regla: elegir camino con menor costo
                if nuevo_costo < g_costos[vecino]:
                    padres[vecino] = actual
                    g_costos[vecino] = nuevo_costo

                    f = nuevo_costo + heuristica[vecino]

                    heapq.heappush(abiertos, (f, vecino))

    return None, float("inf")


# RECONSTRUIR LA RUTA

def reconstruir_ruta(padres, nodo):
    ruta = [nodo]
    while nodo in padres:
        nodo = padres[nodo]
        ruta.append(nodo)
    ruta.reverse()
    return ruta


# ENTRADA POR CONSOLA

def sistema_transporte():
    print(" SISTEMA DE RUTAS ")

    inicio = input("Ingrese punto de inicio: ").upper()
    destino = input("Ingrese punto de destino: ").upper()

    if inicio not in grafo or destino not in grafo:
        print("Estación inválida")
        return
    #Llamamos al algoritmo
    ruta, costo = a_estrella(inicio, destino)
    #Resultados
    if ruta:
        print("\n Mejor ruta encontrada:")
        print(" ➜ ".join(ruta))
        print(f"Costo total: {costo} minutos")
    else:
        print("No se encontró una ruta")


# EJECUCIÓN
if __name__ == "__main__":
    sistema_transporte()