## Algoritmo genético

Cada agente genera su siguiente jugada dependiendo de un arreglo de posibilidades que controla sus decisiones. El problema radica en que no se conoce la configuración con mejores resultados. Es por ello que se implementó un algoritmo genético que resuelve esta incógnita. 

### Cromosomas

Cada agente automático posee su propio arreglo de porcentajes como un atributo de la clase. Este arreglo, llamado en el código como "strategies_probs", es la representación del cromosoma de un agente. Su estructura consta de  un arreglo de tamaño fijo 8, con números flotantes en el rango de 0 a 1 incluidos ambos y que sumados todos los números, el resultado sea 1. Cada posición del arreglo es significativa, es decir, la posición de un número fija la probabilidad de escogencia de la estrategia correspondiente a esa posición. Las posiciones para cada estrategia establecida son las siguientes: "Secuencia", "Espacios", "Centros", "Extremos", "Fila Impar", "Fila Par", "Columna Impar", "Columna Par".  Así por ejemplo, un agente con un cromosoma [0, 0.5, 0, 0, 0.5, 0, 0, 0] tiene 50% de probabilidad de escoger "Espacios" como estrategia y 50% de probabilidad de escoger "Fila Impar".

### Población

El tamaño de la población, el tamaño de los hijos y la cantidad de generaciones son parámetros que se configuran desde el main. La población se inicializa con cromosomas aleatorios. La población es alamacenada en el array bidimensional llamada population en la clase GeneticAlgorithm, la primer posición de cada elemento es el agente y la segunda un entero que corresponde a la puntuación de ese agente.

### Simulación de partidas

El controlador del algoritmo genético se encarga de generar un round-robin doble para que todos los agentes se enfrenten dos veces con cada enemigo. En el archivo settings.py de la carpeta utilities, se encuentra un parámetro para definir cuál color de ficha empieza el primer turno. El motivo de enfrentarse dos veces es alternar el color de la ficha correspondiente, ya que en principio, existe una leve ventaja en ejecutar el primer turno. 

### Función de evaluación

El sistema de puntuación consiste en repartir 2 puntos en cada partido efectuado, si un agente gana se lleva los los puntos, si empata se reparte uno y uno con su enemigo, en caso de perder no se le suma nada a su puntuación. Después de finalizar la ronda de partidas se compara el puntaje de todos los agentes y se ordena el arreglo de forma ascendente, quedando en los primeros indices los agentes con peor puntuación yq eu luego serán reemplazados.

### Cruce de agentes

La probabilidad de escoger un agente es directamente proporcional  a la puntuación que obtuevieron, por lo tanto, se espera que los agentes con mayor puntuación sean escogidos más veces para reproducirse. Cuando se escogen dos agentes distintos, se escoge un punto de quiebre de forma aleatoria en el arreglo de probabilidades y se crea un nuevo agente con la unión de las partes de cada progenitor. Se reajustan los valores de porcentajes para que la suma de ellos siempre de 1.



### Mutación

Todos los hijos de cada generación se redirigen a un proceso de mutación. La mutación consiste en cambiar de forma aleatoria un gen de los hijos. La probabilidad de mutación se encuentra en torno al 10% ó 15% dependiendo de la configuración del programa. Si un hijo entra a mutar, se ecoge un gen aleatorio  de su arreglo, se le otorga un nuevo valor aleatorio del uno al cero incluidos, y se ajustan de nueva cuenta todos los pesos para que sumados de 1.



### Reemplazo

Tal y como se comentó antes, el arreglo es ordenado de forma ascendente. Los hijos son insertados a este arreglo en las primeras posiciones, sustituyendo a los agentes con peor rendimiento y siendo participes de la siguiente generación del algoritmo.



## Resultados

Se ejecutaron numerosas veces el algoritmo genético con distintas configuraciones de número de generaciones, tamaño de población y cantidad de hijos. Se obtuvieron los siguientes resultados ("Secuencia", "Espacios", "Centros", "Extremos", "Fila Impar", "Fila Par", "Columna Impar", "Columna Par"):

- Población: 60, hijos: 15, generaciones: 20, resultado: 0.00247947, 0.00054656, 0.01820531, 0.25123566, 0.48210063, 0.01736479, 0.02902593, 0.19904165

- Población: 50, hijos: 15, generaciones: 25, resultado: 3.48722626e-04, 5.33369811e-03, 4.40077406e-02, 4.05673066e-02, 5.93002717e-01, 1.79300240e-01, 2.90529597e-02, 1.08386616e-01

- Población: 50, hijos: 15, generaciones: 35, resultado: 2.29603586e-04, 1.19437515e-02, 1.32712678e-02, 3.48560198e-03, 3.15585049e-01, 3.00640005e-03, 2.34902697e-01, 4.17575629e-01

- Población: 65, hijos: 20, generaciones: 35, resultado 0.00548696, 0.00773916, 0.0093209,  0.02215657, 0.08894724, 0.00555274, 0.44035399, 0.42044244

Dados estos resultados, las estrategias con mayor peso son Fila Impar, Columna Impar y Columna Par.



## Distribución de trabajo:

El trabajo de ambos integrantes fue equivalente, por lo tanto se recomienda repartir la nota en partes iguales.

**Julio Víquez Murillo 2015013680:**

- Implementación de Algoritmos de Search y Score.

- Implementación de los métodos de cruzar y mutar.

- Implementación del random provider.

- Implementación de las estrategias Secuenciales, Centros, Extremos, Columna par.



**José Antonio Salas 2015013633:**

- Implementación del algoritmo de Checker, Win, Block.

- Implementación del controlador de algoritmo genético.

- Implementación de las estrategia Espacios, Columna Impar, Fila Par e Impar.

- Implementación del controlador del juego.
