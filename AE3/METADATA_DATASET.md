# Metadata del dataset

- **Proyecto:** Proyecto Integrador III – Analítica de Datos
- **Actividad:** AE3 – Transformación y Enriquecimiento de Datos
- **Dataset de continuidad:** `mstz/heart_failure`
- **Configuración:** `death`
- **Split:** `train`
- **Registros:** 299
- **Variables originales:** 13
- **Fuente de consulta del proyecto:** Hugging Face
- **Fuente subyacente:** UCI Heart Failure Clinical Records
- **DOI:** https://doi.org/10.24432/C5Z89R
- **Licencia UCI:** CC BY 4.0

## Decisión de reproducibilidad

El código intenta obtener el dataset directamente desde Hugging Face. Además, el repositorio conserva `AE3/datos/fuente_original_heart_failure.csv` como copia reproducible de los mismos registros, para evitar que una caída de red impida revisar el flujo. La copia no reemplaza la atribución a Hugging Face/UCI.

## Alcance

Los resultados son descriptivos. Las variables derivadas (`grupo_edad`, `condiciones_registradas`, entre otras) son construcciones analíticas para esta actividad y no deben interpretarse como criterios clínicos.
