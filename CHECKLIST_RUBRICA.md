# Checklist de la rúbrica AE2

## Puntualidad y enlace de entrega – 10 puntos
- [ ] Entregar antes de las 23:59 del 25 de octubre de 2026.
- [ ] Compartir un enlace válido y accesible al repositorio de GitHub.

## 1. Documento — Definición y diseño de la necesidad – 30 puntos
- [x] Contexto y escenario identificados como hipotéticos.
- [x] Beneficiario definido.
- [x] Necesidad de información formulada sin afirmar un problema no comprobado.
- [x] Pregunta descriptiva coherente con las variables.
- [x] Objetivo general y objetivos específicos verificables.
- [x] Alcance y limitaciones expresos.
- [x] Continuidad con EA1 documentada: mismo dataset, configuración y split; se diferencia con claridad el DataFrame original 299 × 13 del transformado 299 × 15 de EA1.

## 2. Documento — Estructura y avance documentado – 25 puntos
- [x] Portada.
- [x] Tabla de contenido.
- [x] Índice de tablas; no se crean índices vacíos de gráficas/ilustraciones.
- [x] Introducción.
- [x] Planteamiento de la necesidad.
- [x] Justificación.
- [x] Objetivos.
- [x] Marco teórico inicial con fuentes.
- [x] Metodología de la etapa 1.
- [x] Ficha del dataset.
- [x] Unidad de análisis.
- [x] Diccionario inicial de las 13 variables.
- [x] Alcance, limitaciones y diseño inicial.
- [x] Reconocimiento del dataset.
- [x] Referencias APA 7.

## 3. Código — Jupyter y resumen automático .txt – 25 puntos
- [x] Código para obtener el dataset desde Hugging Face.
- [x] Conversión a DataFrame de Pandas.
- [x] `head()`.
- [x] Filas y columnas.
- [x] Nombres de columnas.
- [x] Tipos de datos.
- [x] Nulos por columna.
- [x] Explicación de qué representa una fila.
- [x] Explicación de variables relacionadas con la necesidad.
- [x] Generación automática de `resultados/resumen_dataframe.txt` en UTF-8.
- [x] Creación automática de la carpeta si no existe.
- [x] Verificación final mediante `assert`.
- [ ] Ejecutar el notebook en el equipo del estudiante y guardar las salidas antes del commit final.

## 4. Versionamiento en GitHub – 10 puntos
- [x] README incluido.
- [x] Dependencias incluidas.
- [x] Documento, notebook y .txt organizados.
- [x] `.gitignore` evita publicar el entorno virtual.
- [ ] Crear/publicar el repositorio y realizar commits descriptivos desde el equipo del estudiante.

**Observación:** los únicos puntos que dependen todavía de una acción externa son la ejecución final en el entorno local, los commits/publicación en GitHub y la entrega puntual en Canvas.
