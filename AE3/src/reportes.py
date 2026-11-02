"""Construcción del diccionario y exportaciones automáticas exigidas por AE3."""

# 1. Activamos anotaciones de tipos modernas.
# 2. Sirve para documentar las firmas de funciones sin modificar la ejecución.
from __future__ import annotations

# 3. Importamos Path desde pathlib.
# 4. Sirve para crear rutas relativas compatibles con Windows y GitHub Actions.
from pathlib import Path

# 5. Importamos pandas con el alias pd.
# 6. Sirve para construir diccionarios tabulares y exportar resultados CSV.
import pandas as pd


def construir_diccionario(df: pd.DataFrame) -> pd.DataFrame:
    """Construye el diccionario actualizado a partir de las columnas reales del DataFrame final."""
    # 7. Relacionamos cada variable con un significado y una unidad/codificación documentada.
    # 8. Sirve para que el diccionario sea reproducible y no dependa de una tabla escrita manualmente.
    significados = {
        "age": ("Edad registrada", "años"),
        "has_anaemia": ("Indicador de anemia registrada", "0/1"),
        "creatinine_phosphokinase_concentration_in_blood": ("Concentración de creatina fosfoquinasa en sangre", "mcg/L según documentación fuente"),
        "has_diabetes": ("Indicador de diabetes registrada", "0/1"),
        "heart_ejection_fraction": ("Fracción de eyección cardíaca", "%"),
        "has_high_blood_pressure": ("Indicador de presión arterial alta registrada", "0/1"),
        "platelets_concentration_in_blood": ("Concentración de plaquetas en sangre", "kiloplaquetas/mL según documentación fuente"),
        "serum_creatinine_concentration_in_blood": ("Creatinina sérica", "mg/dL"),
        "serum_sodium_concentration_in_blood": ("Sodio sérico", "mEq/L"),
        "is_male": ("Sexo masculino codificado en la fuente", "0/1"),
        "is_smoker": ("Indicador de tabaquismo registrado", "0/1"),
        "days_in_study": ("Tiempo de seguimiento", "días"),
        "is_dead": ("Muerte registrada durante el seguimiento", "0/1"),
        "estado_seguimiento": ("Etiqueta legible derivada de is_dead", "categoría"),
        "grupo_edad": ("Grupo descriptivo de edad; no es umbral clínico", "categoría"),
        "condiciones_registradas": ("Suma de anemia, diabetes y presión arterial alta registradas", "conteo 0-3"),
        "nivel_condiciones_registradas": ("Agrupación descriptiva del conteo de condiciones", "categoría"),
        "sexo_registrado": ("Etiqueta legible derivada de is_male", "categoría"),
        "tabaquismo_registrado": ("Etiqueta legible derivada de is_smoker", "categoría"),
    }

    # 9. Creamos una lista vacía para reunir una fila por variable real del DataFrame.
    # 10. Sirve para asegurar que el diccionario refleje exactamente la estructura final.
    filas = []

    # 11. Recorremos todas las columnas existentes en el DataFrame final.
    # 12. Sirve para incorporar tanto las 13 variables fuente como las 6 derivadas.
    for c in df.columns:
        # 13. Recuperamos significado y unidad; dejamos una etiqueta genérica solo si aparece una columna inesperada.
        # 14. Sirve para que una ampliación futura no rompa la generación del diccionario.
        sig, unidad = significados.get(c, ("Variable del dataset", "—"))

        # 15. Agregamos nombre, significado, tipo real de pandas y unidad/codificación.
        # 16. Sirve para responder el requisito de diccionario actualizado de AE3.
        filas.append({"variable": c, "significado": sig, "tipo_pandas": str(df[c].dtype), "unidad_o_codificacion": unidad})

    # 17. Convertimos las filas documentadas en DataFrame.
    # 18. Sirve para exportar el diccionario automáticamente a CSV.
    return pd.DataFrame(filas)


def _resumen_txt(df: pd.DataFrame, metadatos: dict) -> str:
    """Genera el contenido textual del resumen exigido a partir del DataFrame final."""
    # 19. Creamos las primeras líneas con trazabilidad, dimensiones y total de nulos.
    # 20. Sirve para que el TXT se regenere desde los datos y no sea una evidencia escrita a mano.
    lineas = [
        "AE3 - RESUMEN AUTOMÁTICO DEL DATAFRAME TRANSFORMADO Y ENRIQUECIDO",
        "=" * 76,
        f"Dataset: {metadatos['dataset']}",
        f"Configuración: {metadatos['configuracion']}",
        f"Split: {metadatos['split']}",
        f"Fuente utilizada en esta ejecución: {metadatos['fuente_usada']}",
        f"Filas: {df.shape[0]}",
        f"Columnas: {df.shape[1]}",
        f"Valores nulos totales: {int(df.isna().sum().sum())}",
        "",
        "COLUMNAS, TIPOS Y NULOS",
        "-" * 76,
    ]

    # 21. Recorremos cada columna del DataFrame final.
    # 22. Sirve para registrar automáticamente nombre, tipo y nulos de las 19 variables.
    for c in df.columns:
        lineas.append(f"{c} | tipo: {df[c].dtype} | nulos: {int(df[c].isna().sum())}")

    # 23. Añadimos un encabezado para las estadísticas numéricas.
    # 24. Sirve para separar claramente la parte estructural de la parte descriptiva.
    lineas += ["", "ESTADÍSTICAS DESCRIPTIVAS NUMÉRICAS", "-" * 76]

    # 25. Calculamos describe únicamente sobre columnas numéricas y transponemos la tabla.
    # 26. Sirve para incluir conteo, media, desviación, cuartiles, mínimo y máximo pertinentes.
    desc = df.select_dtypes(include="number").describe().T.round(3)

    # 27. Convertimos las estadísticas en texto y las incorporamos al resumen.
    # 28. Sirve para que el TXT pueda revisarse sin abrir Jupyter.
    lineas.append(desc.to_string())

    # 29. Añadimos un encabezado para frecuencias de variables derivadas legibles.
    # 30. Sirve para complementar las estadísticas numéricas con categorías de AE3.
    lineas += ["", "FRECUENCIAS DE VARIABLES DERIVADAS", "-" * 76]

    # 31. Recorremos cinco variables categóricas derivadas.
    # 32. Sirve para registrar sus frecuencias sin mezclar códigos técnicos con etiquetas humanas.
    for c in ["estado_seguimiento", "grupo_edad", "nivel_condiciones_registradas", "sexo_registrado", "tabaquismo_registrado"]:
        lineas.append(f"\n{c}:")
        lineas.append(df[c].value_counts(dropna=False).to_string())

    # 33. Unimos todas las líneas con saltos de línea y añadimos un salto final.
    # 34. Sirve para producir un archivo TXT legible y estable en UTF-8.
    return "\n".join(lineas) + "\n"


def exportar_evidencias(
    df_final: pd.DataFrame,
    tablas: dict[str, pd.DataFrame],
    control: pd.DataFrame,
    comparacion: pd.DataFrame,
    tipos: pd.DataFrame,
    extremos: pd.DataFrame,
    enriquecimiento: pd.DataFrame,
    metadatos: dict,
    raiz: Path,
) -> dict[str, Path]:
    """Exporta dataset preparado, tablas, controles, diccionario y TXT final."""
    # 35. Construimos las rutas de las carpetas de datos y resultados.
    # 36. Sirve para guardar todas las evidencias dentro del repositorio mediante rutas relativas.
    datos = raiz / "AE3" / "datos"
    resultados = raiz / "AE3" / "resultados"

    # 37. Creamos ambas carpetas y permitimos que ya existan.
    # 38. Sirve para que una ejecución limpia no dependa de carpetas creadas manualmente.
    datos.mkdir(parents=True, exist_ok=True)
    resultados.mkdir(parents=True, exist_ok=True)

    # 39. Creamos un diccionario donde registraremos cada archivo generado y su ruta.
    # 40. Sirve para validar después que todas las evidencias existan.
    rutas = {}

    # 41. Definimos la ruta estable del dataset preparado.
    # 42. Sirve para que AE4/Streamlit pueda consumir siempre el mismo archivo.
    rutas["dataset_preparado"] = datos / "heart_failure_preparado.csv"

    # 43. Exportamos el DataFrame final sin el índice de pandas y en UTF-8.
    # 44. Sirve para conservar las 299 filas y 19 columnas en un formato reutilizable.
    df_final.to_csv(rutas["dataset_preparado"], index=False, encoding="utf-8")

    # 45. Recorremos las cinco tablas que responden P1–P5.
    # 46. Sirve para generar un CSV independiente por pregunta.
    for nombre, tabla in tablas.items():
        ruta = resultados / f"{nombre}.csv"
        tabla.to_csv(ruta, index=False, encoding="utf-8")
        rutas[nombre] = ruta

    # 47. Reunimos las evidencias auxiliares de transformación, calidad y documentación.
    # 48. Sirve para que la revisión del docente pueda rastrear cada decisión del flujo.
    extras = {
        "control_calidad": control,
        "comparacion_antes_despues": comparacion,
        "comparacion_tipos": tipos,
        "valores_extremos_iqr": extremos,
        "variables_enriquecidas": enriquecimiento,
        "diccionario_datos_ae3": construir_diccionario(df_final),
    }

    # 49. Exportamos cada evidencia auxiliar como CSV.
    # 50. Sirve para mantener resultados estructurados y reutilizables fuera del notebook.
    for nombre, tabla in extras.items():
        ruta = resultados / f"{nombre}.csv"
        tabla.to_csv(ruta, index=False, encoding="utf-8")
        rutas[nombre] = ruta

    # 51. Definimos la ruta estable del resumen textual obligatorio.
    # 52. Sirve para regenerar siempre el mismo archivo exigido por la actividad.
    rutas["resumen_txt"] = resultados / "resumen_dataframe_final.txt"

    # 53. Generamos el contenido desde el DataFrame final y lo escribimos en UTF-8.
    # 54. Sirve para que el TXT represente exactamente el estado transformado y enriquecido.
    rutas["resumen_txt"].write_text(_resumen_txt(df_final, metadatos), encoding="utf-8")

    # 55. Devolvemos todas las rutas generadas.
    # 56. Sirve para que el notebook valide su existencia y muestre dónde quedaron.
    return rutas
