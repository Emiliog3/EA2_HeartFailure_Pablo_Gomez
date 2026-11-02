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

## Validación automática con GitHub Actions

El repositorio incluye el workflow `.github/workflows/validacion_ae2.yml`, que ejecuta automáticamente una validación técnica al publicar cambios en la rama `main`.

La automatización instala las dependencias en un entorno limpio de GitHub, ejecuta el notebook completo, verifica que las celdas no presenten errores, comprueba la estructura original de 299 registros y 13 columnas y valida la generación de `resultados/resumen_dataframe.txt`.

Esta verificación complementa la ejecución local y permite comprobar públicamente la reproducibilidad técnica de AE2.


## Documento académico entregado en Canvas

El documento académico correspondiente a AE2 se entrega directamente como archivo adjunto en Canvas, de forma separada al repositorio técnico.

El repositorio conserva las evidencias reproducibles del componente de datos: notebook ejecutado, resumen automático `.txt`, dependencias, metadata, documentación técnica e integración continua mediante GitHub Actions.


<!-- INICIO_AE3_2026 -->

---

## Actividad 3 - Transformación y enriquecimiento de datos

### Continuidad del proyecto

Esta entrega continúa el estudio descriptivo de insuficiencia
cardíaca desarrollado en EA1 y EA2. Se conserva la misma
fuente de información y se amplía el tratamiento de los datos
para responder las preguntas planteadas en la segunda etapa.

**Fuente:** Hugging Face, `mstz/heart_failure`.

**Configuración:** `death`.

**Partición:** `train`.

**Registros originales:** 299.

**Columnas originales:** 13.

**Columnas después del procesamiento:** 19.

El análisis conserva los 299 registros y realiza verificaciones
para detectar valores faltantes, inconsistencias y problemas
de calidad antes de producir las tablas de resultados.

### Organización de la Actividad 3

La carpeta `AE3` contiene los siguientes directorios:

- `datos`: conjunto original y datos preparados.
- `src`: funciones de transformación y análisis.
- `notebooks`: desarrollo ejecutable en Jupyter.
- `resultados`: tablas, controles y archivos TXT.
- `documento`: informe académico de la tercera entrega.

El notebook principal es:

`AE3/notebooks/PABLO_GOMEZ_AE3_TRANSFORMACION_ENRIQUECIMIENTO.ipynb`

### Transformación y enriquecimiento

El procesamiento incluye la revisión de los tipos de datos,
la identificación de inconsistencias, la aplicación de reglas
de calidad y la construcción de variables descriptivas.

Las variables incorporadas permiten organizar las
observaciones por estado de seguimiento, grupos de edad
y condiciones registradas, entre otros criterios presentes
en el análisis.

Se mantiene la distinción entre información original,
variables derivadas y resultados descriptivos.

### Resultados

Los resultados se exportan a `AE3/resultados/`.

Entre las evidencias se encuentran:

- Comparación de datos antes y después.
- Diccionario de datos actualizado.
- Controles de calidad.
- Tablas descriptivas por estado de seguimiento.
- Análisis de variables cuantitativas.
- Análisis de condiciones registradas.
- Distribución por grupos de edad.
- Interpretaciones de los resultados.
- Resumen automático del DataFrame final.

Las tablas se generan a partir de los datos procesados
y deben coincidir con los resultados del notebook.

### Reproducción del proyecto

El entorno de GitHub Actions utiliza Python 3.12.

Para preparar las dependencias:

```bash
python -m pip install -r AE3/requirements-ci.txt
```

Para ejecutar el notebook:

```bash
python -m nbconvert --to notebook --execute AE3/notebooks/PABLO_GOMEZ_AE3_TRANSFORMACION_ENRIQUECIMIENTO.ipynb --inplace --ExecutePreprocessor.kernel_name=python3 --ExecutePreprocessor.timeout=600
```

Para ejecutar el validador:

```bash
python validar_entrega_ae3.py
```

El flujo automatizado se encuentra en:

`.github/workflows/validacion_ae3.yml`

La publicación de una nueva versión permite que GitHub Actions
ejecute el notebook y compruebe los resultados de forma
independiente del computador utilizado para desarrollarlo.

### Alcance y limitaciones

Los resultados tienen carácter descriptivo y exploratorio.
Las asociaciones observadas no permiten establecer relaciones
causales ni sustituir la valoración clínica individual.

El enriquecimiento de datos busca mejorar la organización,
interpretación y presentación de la información disponible,
sin incorporar observaciones clínicas que no existan en
la fuente original.

### Proyección hacia la Actividad 4

Esta tercera etapa proporciona datos preparados,
tablas verificables y métricas descriptivas que servirán
de base para desarrollar una aplicación Streamlit.

La aplicación deberá utilizar las mismas definiciones
y reglas de cálculo para mantener coherencia entre
notebook, visualizaciones e informe final.

<!-- FIN_AE3_2026 -->