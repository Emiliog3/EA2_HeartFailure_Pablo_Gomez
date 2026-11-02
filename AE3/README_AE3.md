# AE3 - Transformacion y enriquecimiento de datos

## Proyecto Integrador III

Esta actividad continua EA1 y EA2 mediante un estudio
descriptivo del dataset `mstz/heart_failure`.

## Fuente

- Plataforma: Hugging Face.
- Dataset: mstz/heart_failure.
- Configuracion: death.
- Split: train.
- Registros originales: 299.
- Variables originales: 13.

## Proceso realizado

Se revisan los tipos de datos, valores nulos, duplicados,
rangos, indicadores binarios y valores extremos.

El procesamiento mantiene los 299 registros y produce
un conjunto preparado de 19 columnas.

Se incorporan seis variables derivadas para facilitar
la agrupacion y la interpretacion descriptiva.

## Estructura

- datos: conjunto original y dataset preparado.
- documento: informe academico.
- notebooks: ejecucion reproducible.
- resultados: tablas, controles y TXT automatico.
- src: modulos Python del procesamiento.

## Resultados

La carpeta resultados contiene cinco tablas descriptivas,
el diccionario actualizado, controles de calidad y un resumen
TXT construido automaticamente desde el DataFrame final.

## Reproducibilidad

GitHub Actions ejecuta el notebook con Python 3.12 y valida
las evidencias generadas.

Workflow:

`.github/workflows/validacion_ae3.yml`

## Continuidad

Repositorio oficial:

https://github.com/Emiliog3/EA2_HeartFailure_Pablo_Gomez

La entrega AE3 forma parte del mismo historial de Git.

## Alcance

El trabajo presenta asociaciones descriptivas internas
del dataset, sin atribuir causalidad ni producir
diagnosticos individuales.