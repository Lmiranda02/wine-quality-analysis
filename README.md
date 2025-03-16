# 🍷 Wine Quality Analysis

## 📌 Introducción

El análisis de la calidad del vino es un desafío clave en la industria vinícola, donde diversos factores fisicoquímicos influyen en la percepción sensorial de los consumidores. Este proyecto tiene como objetivo explorar, modelar y visualizar datos sobre vinos tintos y blancos de la región portuguesa **"Vinho Verde"**, utilizando técnicas de **ciencia de datos y machine learning** para comprender qué características impactan más en la calidad del vino.

A través de este estudio, se busca responder preguntas como:
- ¿Cuáles son los factores más influyentes en la calidad del vino?
- ¿Es posible predecir la calidad de un vino a partir de sus propiedades químicas?
- ¿Existen diferencias significativas entre vinos tintos y blancos?
- ¿Cómo se pueden utilizar estos datos para optimizar la producción y selección de vinos?

---

## 📊 Dataset

Este proyecto utiliza el dataset público **Wine Quality Dataset**, disponible en el **UCI Machine Learning Repository**. Los datos fueron recopilados por **Cortez et al. (2009)** y contienen **1599 muestras de vino tinto** y **4898 de vino blanco** con 11 atributos fisicoquímicos y una variable objetivo de calidad (score de 0 a 10).

### 🔹 **Atributos del dataset:**
- **Propiedades fisicoquímicas (input variables)**:
  1. Fixed acidity
  2. Volatile acidity
  3. Citric acid
  4. Residual sugar
  5. Chlorides
  6. Free sulfur dioxide
  7. Total sulfur dioxide
  8. Density
  9. pH
  10. Sulphates
  11. Alcohol

- **Variable objetivo (output variable)**:
  - **Quality**: Puntuación entre **0 (muy mala)** y **10 (excelente)** basada en la evaluación de expertos.

📂 **Archivos en el dataset:**
- `winequality-red.csv` → Vinos tintos (1599 muestras)
- `winequality-white.csv` → Vinos blancos (4898 muestras)

---

## 🏆 Objetivos del Proyecto

✅ Realizar un **análisis exploratorio de datos (EDA)** para identificar patrones y tendencias.  
✅ Aplicar **técnicas de machine learning** para predecir la calidad del vino.  
✅ Construir **visualizaciones avanzadas** para comunicar insights clave.  
✅ Implementar un **dashboard interactivo** para mostrar resultados.  
✅ Documentar todo el proceso.  

---

## 📌 Enfoque Metodológico

Este proyecto sigue un **flujo estructurado** basado en el proceso de **Ciencia de Datos**, incluyendo:

1️⃣ **Análisis exploratorio (EDA)** 📊  
   - Inspección y limpieza de datos.  
   - Visualización de distribuciones y correlaciones.  
   - Comparación entre vinos tintos y blancos.  

2️⃣ **Modelado Predictivo** 🤖  
   - Selección de características más relevantes.  
   - Entrenamiento de modelos como **Random Forest, XGBoost y SVM**.  
   - Evaluación del desempeño con métricas como **RMSE y F1-score**.  

3️⃣ **Desarrollo de Aplicación** 🌍  
   - Creación de un **dashboard interactivo** en Power BI.    

4️⃣ **Publicación y Presentación Profesional** 🚀  
   - Documentación clara con gráficos explicativos.  
   - Publicación en GitHub con un README detallado.  

---

## 📂 Estructura del Proyecto
```
wine-quality-analysis/
├── data/               # Datos crudos y procesados
│   ├── raw/            # Datos originales descargados
│   ├── processed/      # Datos limpios y transformados
├── notebooks/          # Jupyter Notebooks con análisis detallado
├── models/             # Modelos entrenados
├── scripts/            # Código reutilizable
│   ├── download-dataset.py  # Script para descargar los datos
├── dashboard/          # Dashboard interactivo en Streamlit
├── api/                # API con FastAPI para predicciones
├── reports/            # Reportes y visualizaciones finales
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Documentación principal
├── .gitignore          # Archivos a ignorar en Git
└── LICENSE  
```

---

## 🔧 Tecnologías Utilizadas
✅ **Python** (Pandas, NumPy, Scikit-Learn, XGBoost)  
✅ **Jupyter Notebooks** para análisis interactivo  
✅ **Matplotlib, Seaborn, Plotly** para visualización 
✅ **Power BI** para reportes interactivos.
✅ **Git & GitHub** para control de versiones  

---

## 📌 Referencias
- **Cortez et al. (2009)** - Modeling wine preferences by data mining from physicochemical properties. *Decision Support Systems*. [DOI](http://dx.doi.org/10.1016/j.dss.2009.05.016)
- **UCI Machine Learning Repository** - [Wine Quality Dataset](https://archive.ics.uci.edu/dataset/186/wine+quality)
- Documentación de **Scikit-Learn** y **XGBoost**.

---

## 🚀 Siguientes Pasos
1. **Desarrollar una API o Dashboard interactivo.**
2. **Publicar el proyecto con documentación completa en GitHub.**

---

