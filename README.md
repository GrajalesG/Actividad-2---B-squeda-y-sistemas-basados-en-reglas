# Sistema Inteligente de Rutas con A*

## Descripción

Este proyecto consiste en el desarrollo de un sistema inteligente que permite encontrar la mejor ruta entre dos puntos dentro de un sistema de transporte.

## Enfoque del sistema

El sistema se basa en los siguientes elementos:

* **Base de conocimiento**: Representada como un grafo.
* **Nodos**: Representan estaciones del sistema de transporte.
* **Aristas**: Representan conexiones entre estaciones.
* **Costo**: Tiempo de desplazamiento entre estaciones.
* **Algoritmo**: A* para encontrar la mejor ruta.


## Tecnologías utilizadas

* Python 3
* Librería estándar `heapq`

---

## Instrucciones de ejecución

### Requisitos

* Tener instalado Python 3.x
---

### Pasos para ejecutar

1. Clonar el repositorio:

```bash
git clone https://github.com/tuusuario/tu-repo.git
```

2. Ingresar a la carpeta del proyecto:

```bash
cd tu-repo
```

3. Ejecutar el programa:

```bash
python sistema_transporte.py
```

---

## Uso 

1. El sistema solicitará:

   * Punto de inicio
   * Punto de destino

2. El usuario debe ingresar las estaciones en mayúscula (Ejemplo: A, B, C, etc.)

3. El sistema calculará automáticamente la mejor ruta utilizando el algoritmo A*

4. Se mostrará:

   * La ruta óptima
   * El tiempo total del recorrido

---


## Notas importantes

* Las estaciones válidas están definidas dentro del código
* El sistema no requiere librerías externas adicionales
* Funciona completamente en consola
* Si se ingresa una estación inválida, el sistema mostrará un mensaje de error

