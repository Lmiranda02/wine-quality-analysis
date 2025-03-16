from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import seaborn as sns

import matplotlib.pyplot as plt

# Función para evaluar modelos de clasificación
def evaluate_model(model, X_test, y_test, labels):
    """
    Evalúa un modelo de clasificación y muestra métricas clave.

    Parámetros:
        model: Modelo entrenado de sklearn.
        X_test (DataFrame): Conjunto de prueba.
        y_test (Series): Etiquetas verdaderas.
        labels (list): Lista de etiquetas de las clases.

    Retorna:
        dict: Resultados de las métricas.
    """
    y_pred = model.predict(X_test)
    
    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, average="weighted"),
        "Recall": recall_score(y_test, y_pred, average="weighted"),
        "F1-Score": f1_score(y_test, y_pred, average="weighted")
    }
    
    conf_matrix = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 7))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(f'Confusion Matrix - {model.__class__.__name__}')
    plt.show()
    
    print("\n🔹 Reporte de Clasificación:\n", classification_report(y_test, y_pred, target_names=labels))
    
    return metrics