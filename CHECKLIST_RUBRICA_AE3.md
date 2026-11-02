# Lista de verificación de entrega — S30, AE3

**Proyecto Integrador III · Transformación y Enriquecimiento de Datos**

## 1. Acceso y entrega (10 puntos)
- [x] Repositorio público de continuidad con EA2.
- [x] Carpeta `AE3/` integrada en la rama principal `main`.
- [x] Historial de commits conservado.
- [ ] Adjuntar el Word en Canvas, incluir enlace público y confirmar el envío dentro del plazo.

## 2. Transformación y enriquecimiento (30 puntos)
- [x] Fuente identificada: `mstz/heart_failure`, configuración `death`, partición `train`.
- [x] 299 registros y 13 variables originales conservados.
- [x] Controles de tipos, valores faltantes, duplicados, rangos y extremos documentados.
- [x] Seis columnas derivadas, con reglas y significado en `AE3/resultados/variables_enriquecidas.csv`.
- [x] Dataset final de 299 filas por 19 columnas, sin valores nulos.
- [x] Diccionario de las 19 variables en `AE3/resultados/diccionario_datos_ae3.csv`.
- [x] Informe Word revisado y condensado con metodología, transformaciones y diccionario.

## 3. Resultados y preguntas (25 puntos)
- [x] Se mantiene la pregunta descriptiva formulada en EA2.
- [x] P1: `AE3/resultados/tabla_01_estado_seguimiento.csv`.
- [x] P2: `AE3/resultados/tabla_02_cuantitativas_por_estado.csv` (siete variables, incluidas CPK y plaquetas).
- [x] P3: `AE3/resultados/tabla_03_binarias_por_estado.csv`.
- [x] P4: `AE3/resultados/tabla_04_grupo_edad_por_estado.csv`.
- [x] P5: `AE3/resultados/tabla_05_condiciones_registradas_por_estado.csv`.
- [x] Interpretaciones descriptivas y limitaciones incorporadas al documento.

## 4. Notebook, datos y TXT (25 puntos)
- [x] Notebook Jupyter reproducible: `AE3/notebooks/PABLO_GOMEZ_AE3_TRANSFORMACION_ENRIQUECIMIENTO.ipynb`.
- [x] CSV de origen y CSV preparado en `AE3/datos/`.
- [x] Tablas, controles, diccionario y archivo `resumen_dataframe_final.txt` exportados.
- [x] Validador canónico: `validar_entrega_ae3.py` en la raíz.
- [x] Ejecución anterior de AE3 comprobada en GitHub Actions.

## 5. GitHub y README (10 puntos)
- [x] README principal y `AE3/README_AE3.md` disponibles.
- [x] Dependencias y workflow `.github/workflows/validacion_ae3.yml` incluidos.
- [x] Las ejecuciones de AE2 y AE3 aprobaron en `main` el 2 de noviembre de 2026.
- [ ] Confirmar el resultado de GitHub Actions correspondiente al último commit documental, después de publicarlo.

## Documento académico
`AE3/documento/S30_AE3_Transformacion_Enriquecimiento_PG.docx`

En Canvas puede adjuntarse una copia con el nombre `S30_AE3_Transformacion_Enriquecimiento_Pablo_Gomez.docx`.

**Repositorio oficial:** https://github.com/Emiliog3/EA2_HeartFailure_Pablo_Gomez/tree/main/AE3

Este checklist es un apoyo para verificar la entrega; la puntuación final corresponde exclusivamente al docente.
