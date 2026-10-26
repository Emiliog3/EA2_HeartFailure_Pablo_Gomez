# Metadata del dataset – AE2

- **Dataset:** `mstz/heart_failure`
- **Nombre visible:** Heart failure
- **Configuración:** `death`
- **Split:** `train`
- **Fecha de consulta:** 25 de octubre de 2026
- **Tipo:** tabular
- **Formato reportado:** CSV
- **Registros usados:** 299
- **Columnas del DataFrame:** 13
- **Muestra:** no; se utiliza el split completo
- **Hugging Face:** https://huggingface.co/datasets/mstz/heart_failure
- **Fuente subyacente documentada:** UCI Heart Failure Clinical Records
- **DOI UCI:** https://doi.org/10.24432/C5Z89R
- **Artículo asociado:** Chicco & Jurman (2020), https://doi.org/10.1186/s12911-020-1023-5
- **Licencia:** el repositorio de Hugging Face muestra `cc`; UCI identifica el conjunto subyacente como **CC BY 4.0**.
- **Datos sintéticos:** no; las fuentes describen registros clínicos históricos.
- **Valores faltantes:** 0 según el reconocimiento del DataFrame y la documentación UCI.
- **Continuidad con EA1:** el mismo dataset se carga originalmente con 299 × 13; EA1 lo transforma posteriormente a 299 × 15. AE2 trabaja con la versión original 299 × 13 para reconocer la estructura fuente antes del diseño analítico.
- **Repositorio EA1:** https://github.com/Emiliog3/EA1_HeartFailure_Pablo_Gomez

## Unidad de análisis

Cada fila representa un registro individual de un paciente con insuficiencia cardíaca seguido durante un número determinado de días.

## Alcance académico

AE2 utiliza el dataset para formular y documentar una necesidad de analítica descriptiva. No se realizan predicciones, diagnósticos ni inferencias causales.
