# EA2 – Ideación, diseño y documentación de la necesidad

**Proyecto Integrador III – Analítica de Datos**  
**Estudiante:** Pablo Emilio Gómez Gómez  
**Docente:** Andrés Felipe Callejas Jaramillo  
**Institución:** Institución Universitaria Digital de Antioquia  
**Código:** PREICA2602B020038  
**Fecha:** 25 de octubre de 2026

## Propósito

Esta carpeta desarrolla la Actividad 2 utilizando el mismo dataset de continuidad del proyecto: `mstz/heart_failure`, configuración `death`, split `train`.

La continuidad con la **Actividad 1 (EA1)** se conserva de forma explícita. EA1 carga inicialmente el mismo dataset con **299 filas y 13 columnas** y luego aplica cinco transformaciones hasta obtener un DataFrame de **299 × 15**. AE2 vuelve deliberadamente al **DataFrame original de 299 × 13**, antes de esas transformaciones, porque esta etapa pide reconocer los datos fuente y formular una necesidad descriptiva coherente con las variables originales. No existe contradicción entre ambos resultados: corresponden a momentos distintos del mismo flujo.

- Repositorio público de EA1: https://github.com/Emiliog3/EA1_HeartFailure_Pablo_Gomez
- Perfil de GitHub: https://github.com/Emiliog3

La necesidad propuesta es **descriptiva**: caracterizar los 299 registros y comparar las variables disponibles entre pacientes que registraron y que no registraron muerte durante el seguimiento. El proyecto no formula diagnósticos, predicciones ni conclusiones causales.

## Dataset

- Identificador: `mstz/heart_failure`
- Configuración: `death`
- Split: `train`
- Registros: 299
- Columnas: 13
- Muestra: no se utiliza muestra; se trabaja con el split completo.
- Hugging Face: https://huggingface.co/datasets/mstz/heart_failure
- Fuente subyacente documentada: UCI Heart Failure Clinical Records — https://doi.org/10.24432/C5Z89R
- Licencia: Hugging Face muestra la etiqueta `cc`; UCI identifica el dataset subyacente como CC BY 4.0.

## Estructura

```text
EA2_HeartFailure_Pablo_Gomez/
├── .gitignore
├── CHECKLIST_RUBRICA.md
├── METADATA_DATASET.md
├── README.md
├── requirements.txt
├── documento/
│   └── PABLO_GOMEZ_EA2_IDEACION_DISENO_NECESIDAD.docx
├── notebooks/
│   └── PABLO_GOMEZ_EA2_RECONOCIMIENTO_DATASET.ipynb
└── resultados/
    └── resumen_dataframe.txt
```

## Pregunta de análisis

**¿Cómo se caracterizan y qué diferencias descriptivas se observan en las variables demográficas, clínicas y de estilo de vida disponibles entre los pacientes que registraron y los que no registraron muerte durante el seguimiento del dataset `mstz/heart_failure`?**

## Preparación del entorno

Desde la carpeta raíz del proyecto, en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

En Visual Studio Code, abra `notebooks/PABLO_GOMEZ_EA2_RECONOCIMIENTO_DATASET.ipynb` y seleccione como kernel el Python ubicado en `.venv`.

## Ejecución

Ejecute todas las celdas de arriba hacia abajo. El notebook debe mostrar:

- algunos registros;
- 299 filas y 13 columnas;
- nombres de columnas;
- tipos de datos;
- valores nulos por columna;
- creación automática de `resultados/resumen_dataframe.txt`;
- verificación final sin errores.

El archivo `.txt` se regenera en cada ejecución y se construye a partir del mismo DataFrame cargado en el notebook.

## Código explicado

Cada instrucción importante del notebook está precedida por dos comentarios:

1. **Cómo se lee:** traduce la sintaxis a lenguaje natural.
2. **Para qué sirve:** explica la función de esa línea dentro del flujo.

Se conserva así un estilo pedagógico y comprensible sin modificar el comportamiento de Python.

## Antes de publicar en GitHub

1. Ejecute el notebook completo y guarde las salidas visibles.
2. Verifique que `resultados/resumen_dataframe.txt` se haya regenerado.
3. Abra el documento Word y confirme el contenido final.
4. No suba `.venv`, cachés ni credenciales.
5. Use commits descriptivos que evidencien avances.

## Archivos evaluados

- Documento inicial: `documento/PABLO_GOMEZ_EA2_IDEACION_DISENO_NECESIDAD.docx`
- Notebook: `notebooks/PABLO_GOMEZ_EA2_RECONOCIMIENTO_DATASET.ipynb`
- Resumen automático: `resultados/resumen_dataframe.txt`
- Documentación del repositorio: `README.md`, `METADATA_DATASET.md`, `requirements.txt`

## Nota de alcance

Los datos son históricos y corresponden a una población específica. Las comparaciones futuras serán descriptivas y no deberán interpretarse como prueba de causalidad, diagnóstico individual o recomendación médica.
