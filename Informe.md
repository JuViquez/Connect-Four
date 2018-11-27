## Algoritmo genético

Cada agente genera su siguiente jugada dependiendo de un arreglo de posibilidades que controla sus decisiones. El problema radica en que no se conoce la configuración con mejores resultados. Es por ello que se implementó un algoritmo genético que resuelve esta incógnita. 

### Cromosomas

Cada agente automático posee su propio arreglo de porcentajes como un atributo de la clase. Este arreglo, llamado en el código como "strategies_probs", es la representación del cromosoma de un agente. Su estructura consta de  un arreglo de tamaño fijo 8, con números flotantes en el rango de 0 a 1 incluidos ambos y que sumados todos los números, el resultado sea 1. Cada posición del arreglo es significativa, es decir, la posición de un número fija la probabilidad de escogencia de la estrategia correspondiente a esa posición. Las posiciones para cada estrategia establecida son las siguientes: "Secuencia", "Espacios", "Centros", "Extremos", "Fila Impar", "Fila Par", "Columna Impar", "Columna Par".  Así por ejemplo, un agente con un cromosoma [0, 0.5, 0, 0, 0.5, 0, 0, 0] tiene 50% de probabilidad de escoger "Espacios" como estrategia y 50% de probabilidad de escoger "Fila Impar".

### Población

El tamaño de la población, el tamaño de los hijos y la cantidad de generaciones son parámetros que se configuran desde el main. La población se inicializa con cromosomas aleatorios. La población es alamacenada en el array bidimensional llamada population en la clase GeneticAlgorithm, la primer posición de cada elemento es el agente y la segunda un entero que corresponde a la puntuación.


