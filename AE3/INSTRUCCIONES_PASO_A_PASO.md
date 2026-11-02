# AE3 - Instrucciones de ejecucion y verificacion

## Repositorio oficial

https://github.com/Emiliog3/EA2_HeartFailure_Pablo_Gomez

AE3 continua la entrega EA2 dentro del mismo repositorio.

## Estructura

- AE3/datos
- AE3/documento
- AE3/notebooks
- AE3/resultados
- AE3/src

## Preparacion

Clonar el repositorio y abrir su carpeta raiz.

Usar Python 3.12 para reproducir el entorno de GitHub Actions.

Instalar dependencias desde la raiz:

```powershell
python -m pip install -r AE3/requirements-ci.txt
```

## Ejecucion

Ejecutar el notebook completo:

```powershell
python -m nbconvert --to notebook --execute AE3/notebooks/PABLO_GOMEZ_AE3_TRANSFORMACION_ENRIQUECIMIENTO.ipynb --inplace --ExecutePreprocessor.timeout=600 --ExecutePreprocessor.kernel_name=python3
```

## Validacion

Ejecutar:

```powershell
python validar_entrega_ae3.py
```

Comprobar:

- 299 registros.
- 19 columnas finales.
- Cero valores nulos.
- Cinco tablas descriptivas.
- CSV preparado.
- TXT generado automaticamente.
- Documento Word presente.

## Ejecucion remota

Consultar GitHub Actions y verificar el workflow:

Validacion automatica AE3

GitHub Actions instala las dependencias, ejecuta el notebook
y valida las evidencias automaticamente.

## Versionamiento

EA1 y EA2 conservan su historia. AE3 se desarrolla sobre
la misma historia Git y se incorpora en la carpeta AE3.

No ejecutar git init ni crear un nuevo repositorio.

## Alcance

Los resultados son descriptivos y no constituyen
diagnosticos clinicos ni inferencias causales.