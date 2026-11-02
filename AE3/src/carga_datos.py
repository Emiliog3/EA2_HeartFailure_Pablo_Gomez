"""Carga reproducible del dataset usado desde EA1 y EA2.

La primera opción es Hugging Face (`mstz/heart_failure`, configuración `death`,
split `train`). Para que el proyecto también pueda revisarse si temporalmente
no hay conexión, se conserva una copia reproducible en `AE3/datos`.
"""

# 1. Activamos anotaciones de tipos modernas sin evaluarlas inmediatamente.
# 2. Sirve para documentar tipos de retorno sin afectar la ejecución normal.
from __future__ import annotations

# 3. Importamos Path desde pathlib.
# 4. Sirve para construir rutas relativas compatibles con Windows y GitHub Actions.
from pathlib import Path

# 5. Importamos pandas con el alias pd.
# 6. Sirve para leer la copia CSV y trabajar con los datos como DataFrame.
import pandas as pd

# 7. Guardamos el identificador exacto del dataset en Hugging Face.
# 8. Sirve para mantener continuidad y trazabilidad con EA1 y EA2.
DATASET_ID = "mstz/heart_failure"

# 9. Guardamos la configuración utilizada por el proyecto.
# 10. Sirve para seleccionar la variante `death` del dataset.
CONFIG = "death"

# 11. Guardamos el split que contiene los 299 registros.
# 12. Sirve para cargar la misma partición usada en las entregas anteriores.
SPLIT = "train"

# 13. Declaramos, en el mismo orden, las 13 columnas que esperamos recibir.
# 14. Sirve para detectar cambios accidentales de esquema antes de analizar datos.
COLUMNAS_ESPERADAS = [
    "age",
    "has_anaemia",
    "creatinine_phosphokinase_concentration_in_blood",
    "has_diabetes",
    "heart_ejection_fraction",
    "has_high_blood_pressure",
    "platelets_concentration_in_blood",
    "serum_creatinine_concentration_in_blood",
    "serum_sodium_concentration_in_blood",
    "is_male",
    "is_smoker",
    "days_in_study",
    "is_dead",
]


def _raiz_proyecto() -> Path:
    """Localiza la raíz aunque el notebook se ejecute desde AE3/notebooks."""
    # 15. Tomamos la carpeta actual y la convertimos en una ruta absoluta.
    # 16. Sirve como punto de partida para buscar la raíz del repositorio.
    actual = Path.cwd().resolve()

    # 17. Construimos una lista con la carpeta actual y todos sus directorios padre.
    # 18. Sirve para que la búsqueda funcione desde la raíz o desde una subcarpeta.
    candidatos = [actual, *actual.parents]

    # 19. Recorremos cada carpeta candidata.
    # 20. Sirve para identificar cuál contiene la estructura `AE3/src`.
    for candidato in candidatos:
        # 21. Preguntamos si en la carpeta candidata existe `AE3/src`.
        # 22. Sirve para reconocer de manera portable la raíz del proyecto.
        if (candidato / "AE3" / "src").exists():
            # 23. Devolvemos la primera carpeta que cumple la condición.
            # 24. Sirve para construir después rutas sin escribir `G:\...` en el código.
            return candidato

    # 25. Generamos un error claro si no encontramos la estructura esperada.
    # 26. Sirve para evitar que el programa escriba archivos en una ubicación equivocada.
    raise FileNotFoundError("No fue posible localizar la raíz del proyecto AE3.")


def cargar_heart_failure(preferir_huggingface: bool = True):
    """Devuelve `(DataFrame, metadatos_de_carga)` sin transformar los datos."""
    # 27. Registramos inicialmente que la fuente será la copia reproducible local.
    # 28. Sirve como valor de respaldo si Hugging Face no está disponible.
    fuente = "copia reproducible local"

    # 29. Creamos una variable vacía para conservar cualquier error de conexión a Hugging Face.
    # 30. Sirve para informar el fallback sin ocultar por qué ocurrió.
    error_hf = None

    # 31. Inicializamos el DataFrame como vacío.
    # 32. Sirve para saber si la carga remota tuvo éxito o debemos usar la copia local.
    df = None

    # 33. Preguntamos si el flujo debe intentar primero la fuente oficial del proyecto en Hugging Face.
    # 34. Sirve para que la ejecución normal mantenga la procedencia acordada desde EA1.
    if preferir_huggingface:
        try:
            # 35. Importamos load_dataset únicamente cuando se necesita la descarga.
            # 36. Sirve para obtener el dataset desde Hugging Face.
            from datasets import load_dataset

            # 37. Descargamos el dataset usando identificador, configuración y split definidos arriba.
            # 38. Sirve para recuperar los mismos 299 registros trabajados en EA1 y EA2.
            dataset_hf = load_dataset(DATASET_ID, CONFIG, split=SPLIT)

            # 39. Convertimos el objeto de Hugging Face en DataFrame de pandas.
            # 40. Sirve para aplicar controles, transformaciones y tablas descriptivas.
            df = dataset_hf.to_pandas()

            # 41. Registramos que la fuente usada fue Hugging Face.
            # 42. Sirve para dejar trazabilidad en el TXT final.
            fuente = "Hugging Face"
        except Exception as exc:
            # 43. Convertimos el error de la descarga en un texto legible.
            # 44. Sirve para documentar la razón del fallback sin detener la reproducibilidad.
            error_hf = f"{type(exc).__name__}: {exc}"

    # 45. Si la carga remota no produjo un DataFrame, usamos la copia reproducible incluida.
    # 46. Sirve para que la revisión técnica pueda continuar aun cuando no exista conexión de red.
    if df is None:
        # 47. Construimos la ruta relativa de la copia del conjunto original.
        # 48. Sirve para evitar rutas personales y mantener portabilidad.
        ruta = _raiz_proyecto() / "AE3" / "datos" / "fuente_original_heart_failure.csv"

        # 49. Leemos la copia CSV como DataFrame.
        # 50. Sirve para reconstruir el mismo esquema fuente sin modificarlo.
        df = pd.read_csv(ruta)

        # 51. Recorremos los cinco indicadores que Hugging Face presenta como booleanos.
        # 52. Sirve para que la copia local conserve tipos equivalentes a la versión remota.
        for columna in ["has_anaemia", "has_diabetes", "has_high_blood_pressure", "is_male", "is_smoker"]:
            # 53. Normalizamos representaciones booleanas comunes a True/False.
            # 54. Sirve para evitar diferencias de tipo entre la carga remota y la carga local.
            df[columna] = df[columna].map({True: True, False: False, "True": True, "False": False, 1: True, 0: False})

    # 55. Identificamos si falta alguna de las columnas esperadas.
    # 56. Sirve para validar el esquema antes de ejecutar transformaciones.
    faltantes = [c for c in COLUMNAS_ESPERADAS if c not in df.columns]

    # 57. Detenemos la ejecución si la estructura recibida no corresponde al proyecto.
    # 58. Sirve para evitar resultados construidos sobre un dataset incompleto o distinto.
    assert not faltantes, f"Faltan columnas esperadas: {faltantes}"

    # 59. Verificamos que se conserven exactamente los 299 registros documentados.
    # 60. Sirve para comprobar continuidad con EA1, EA2 y la ficha del dataset.
    assert df.shape[0] == 299, f"Se esperaban 299 registros y llegaron {df.shape[0]}."

    # 61. Seleccionamos las 13 columnas en el orden documentado y creamos una copia profunda.
    # 62. Sirve para preservar una versión de entrada independiente de las transformaciones posteriores.
    df = df[COLUMNAS_ESPERADAS].copy(deep=True)

    # 63. Reunimos la procedencia técnica de esta ejecución en un diccionario.
    # 64. Sirve para trasladar esa trazabilidad al TXT y a otras evidencias.
    metadatos = {
        "dataset": DATASET_ID,
        "configuracion": CONFIG,
        "split": SPLIT,
        "fuente_usada": fuente,
        "error_huggingface": error_hf,
    }

    # 65. Devolvemos el DataFrame fuente y sus metadatos de carga.
    # 66. Sirve para que el notebook continúe con una entrada validada y documentada.
    return df, metadatos
