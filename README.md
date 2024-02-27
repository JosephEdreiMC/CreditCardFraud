# Note: Language
This project was a requirement for a certification taught in Spanish; therefore, comments on the code will not be in English.

# Video
Video of the presentation of this project can be found here (in Spanish)/ El video presentación puede ser encontrado aquí: https://drive.google.com/file/d/1dxQnlPkiMW8Irmip2oHcveyglzWoY3dx/view?usp=sharing
# Bedu Project / ProyectoBedu
Credit Card Fraud Transaction Data

The original dataset can be found here / El dataset original que se ha empleado en este proyecto puede ser encontrado aquí:
https://www.kaggle.com/datasets/anurag629/credit-card-fraud-transaction-data

# Introduction / Introducción

The dataset consists of different characteristics of several bank transactions, which may have been fraudulent.
Whether a transaction is fraudulent can be determined by an unknown relationship between different factors that cannot be easily modeled using typical methods (16 features per transaction potentially require a classification model with 16 variables in total);
therefore, we need to use a Machine-Learning approach.

Note that the original dataset is already labeled as fraud/not fraud; thus, supervised learning techniques are used.
/
El dataset consiste en una serie de características propias de transacciones bancarias, las cuales pudieron resultar en fraude o no. 
El que una transacción sea fraudulenta o no está determinado por una interrelación entre factores que no son fácilmente modelables empleando métodos habituales de la modelación matemática (el dataset consiste en 16 columnas, por lo que, potencialmente, un modelo de clasificación adecuado podría hacer uso de 16 variables en total). 
Por lo tanto, el uso de Machine Learning es mandatorio.

Nótese que el data set ya está etiquetado en fraude o no; luego, el uso de modelos de aprendizaje supervisado es el enfoque inmediato para la resolución del problema.

# Content / Contenido
After data cleaning, an analysis of the main characteristics of the data set was made, resulting in insight into the demographic characteristics and consumer habits of the sampled population. This was done to avoid possible bias and wrongly extrapolate the results to other populations.
Subsequently, due to the disparity between Frauds and Not Frauds (about 7% of the dataset consists of fraudulent transactions), undersampling and oversampling approaches were implemented (based on https://imbalanced-learn.org/stable/) together with the imbalanced data set as a control.
A random forest classification was used on the undersampled, oversampled, and control data sets, varying the number of trees and using a 10-fold cross-validation.
/
Tras la limpieza del dataset, se hace un análisis del mismo, relevando más acerca del segmento población y hábitos de consumo ejemplificados. De esta manera, podemos evitar ser imparciales y erroneamente extrapolar los resultados aquí obtenidos al grueso poblacional.
Posteriormente, dada la disparidad de Fraudes a No Fraudes (aproximadamente un 7% del data set son fraudes), se empleará un undersampling y un oversampling (https://imbalanced-learn.org/stable/) junto con el set de datos sin modificaciones.

El modelo empleado fue un random forest, al cual se le varió el número de 'árboles' junto con el correspondinte sampling, undersampling, y oversampling, y una validación cruzada estándar a 10 folds.

# Results / Resultados
In the case of the imbalanced data set, the best result was achieved by the 100-tree random forest, in contrast with those forests with more and fewer trees, according to the resulting metrics.

As for the undersampled data set, the results were mostly better in comparison with the other two datasets, and the 50-tree forest obtained the best metrics.

Finally, in the case of the oversampled dataset, the sensitivity score was perfect regardless of the number of trees in the random forest, which performed homogeneously.

As an experiment, and taking advantage of the high dimensionality of the dataset, a rbf-kernel Support Vector Machine implementation was used, which delivered poorly when compared against the random forest implementation both on the imbalanced data set.
/
Basado en las métricas obtenidas, en un data set sin modificaciones, el mejor random forest contiene 100 árboles, en contraste con la densidad de árboles inferiores y superiores.

En el caso de undersampling, los resultados fueron ampliamente mejores en promedio, con tendencia a favorecer al bosque de 50 árboles.

Finalmente, en el caso de oversampling, la sensibilidad fue perfecta para todos los árboles, los cuales se desempeñaron casi homogeneamente.

Como parte de la experimentación, y aprovechando la extradimensionalidad del dataset, se probó a emplear un Support Vector Machine con kernel rbf, el cual se desempeño considerablemente peor que el random forest para el caso del data set original.
