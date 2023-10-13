# Video
El video presentación puede ser encontrado aquí: https://drive.google.com/file/d/1dxQnlPkiMW8Irmip2oHcveyglzWoY3dx/view?usp=sharing
# ProyectoBedu
Credit Card Fraud Transaction Data

El dataset original que se ha empleado en este proyecto puede ser encontrado aquí:
https://www.kaggle.com/datasets/anurag629/credit-card-fraud-transaction-data

# Introducción
El dataset consiste en una serie de características propias de transacciones bancarias, las cuales pudieron resultar en fraude o no. 
El que una transacción sea fraudulenta o no está determinado por una interrelación entre factores que no son fácilmente modelables empleando métodos habituales de la modelación matemática (el dataset consiste en 16 columnas, por lo que, potencialmente, un modelo de clasificación adecuado podría hacer uso de 16 variables en total). 
Por lo tanto, el uso de Machine Learning es mandatorio.

Nótese que el data set ya está etiquetado en fraude o no; luego, el uso de modelos de aprendizaje supervisado es el enfoque inmediato para la resolución del problema.

# Contenido
Tras la limpieza del dataset, se hace un análisis del mismo, relevando más acerca del segmento población y hábitos de consumo ejemplificados. De esta manera, podemos evitar ser imparciales y erroneamente extrapolar los resultados aquí obtenidos al grueso poblacional.
Posteriormente, dada la disparidad de Fraudes a No Fraudes (aproximadamente un 7% del data set son fraudes), se empleará un undersampling y un oversampling (https://imbalanced-learn.org/stable/) junto con el set de datos sin modificaciones.

El modelo empleado fue un random forest, al cual se le varió el número de 'árboles' junto con el correspondinte sampling, undersampling, y oversampling, y una validación cruzada estándar a 10 folds.

# Resultados
Basado en las métricas obtenidas, en un data set sin modificaciones, el mejor random forest contiene 100 árboles, en contraste con la densidad de árboles inferiores y superiores.

En el caso de undersampling, los resultados fueron ampliamente mejores en promedio, con tendencia a favorecer al bosque de 50 árboles.

Finalmente, en el caso de oversampling, la sensibilidad fue perfecta para todos los árboles, los cuales se desempeñaron casi homogeneamente.

Como parte de la experimentación, y aprovechando la extradimensionalidad del dataset, se probó a emplear un Support Vector Machine con kernel rbf, el cual se desempeño considerablemente peor que el random forest para el caso del data set original.

# Importante
Existe un proyecto anterior entregado que emplea el mismo dataset. Se observará que la limpieza es similar a aquella realizada por el otro equipo puesto que contribuí activamente en esa parte del proyecto. Similarlmente, haré uso de la librería imbalanced-learn (https://imbalanced-learn.org/stable/), pues la idea de usarla fue aportación mía.

*En cuanto al resto del contenido, consiste en ideas originales, las cuales tendrán poca a ninguna semejanza al proyecto paralelo salvo por las ideas arriba mencionadas.*
