'''
Aquí se encuentran las funciones de apoyo usadas a lo largo del proyecto. Basadas en los módulos estudiados anteriormente.
'''
# Packages




def fit_predict_score_matrix(model, X_train, y_train, X_test, y_test):
  x= model
  x.fit(X_train, y_train)
  y_pred = x.predict(X_test)
  score = x.score(X_test, y_test)
  cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
  print("Score sin validación cruzada: ", score)
  return y_pred, score, cnf_matrix







