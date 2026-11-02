"""Tablas que responden operacionalmente la pregunta amplia formulada en EA2."""

# 1. Activamos anotaciones de tipos modernas.
# 2. Sirve para documentar entradas y salidas sin afectar la ejecución.
from __future__ import annotations

# 3. Importamos NumPy con el alias np.
# 4. Sirve para representar un coeficiente de variación no calculable cuando la media sea cero.
import numpy as np

# 5. Importamos pandas con el alias pd.
# 6. Sirve para agrupar, resumir y devolver tablas en forma de DataFrame.
import pandas as pd

# 7. Enumeramos las siete variables cuantitativas utilizadas en P2.
# 8. Sirve para que el mismo procedimiento descriptivo se aplique de forma reproducible a todas.
CUANTITATIVAS = [
    "age",
    "creatinine_phosphokinase_concentration_in_blood",
    "heart_ejection_fraction",
    "platelets_concentration_in_blood",
    "serum_creatinine_concentration_in_blood",
    "serum_sodium_concentration_in_blood",
    "days_in_study",
]

# 9. Relacionamos cada indicador binario con una etiqueta comprensible.
# 10. Sirve para producir la tabla P3 sin perder el nombre técnico de la variable.
BINARIAS = {
    "has_anaemia": "Anemia registrada",
    "has_diabetes": "Diabetes registrada",
    "has_high_blood_pressure": "Presión arterial alta registrada",
    "is_male": "Sexo masculino registrado",
    "is_smoker": "Tabaquismo registrado",
}


def tabla_estado(df: pd.DataFrame) -> pd.DataFrame:
    """P1: conteos y porcentajes de los dos estados de seguimiento."""
    # 11. Agrupamos los registros por la etiqueta de estado y contamos filas.
    # 12. Sirve para conocer el tamaño de los dos grupos de comparación.
    t = df.groupby("estado_seguimiento", observed=True).size().reset_index(name="registros")

    # 13. Convertimos cada conteo en porcentaje sobre los 299 registros y redondeamos a dos decimales.
    # 14. Sirve para expresar la distribución relativa sin confundirla con una tasa poblacional.
    t["porcentaje"] = (t["registros"] / len(df) * 100).round(2)

    # 15. Devolvemos la tabla P1 terminada.
    # 16. Sirve para mostrarla en Jupyter, exportarla a CSV y usarla en AE4.
    return t


def tabla_cuantitativas(df: pd.DataFrame) -> pd.DataFrame:
    """P2: medidas de posición y dispersión por estado de seguimiento."""
    # 17. Creamos una lista vacía para reunir una fila por variable y por grupo.
    # 18. Sirve para construir al final un único DataFrame de resultados cuantitativos.
    filas = []

    # 19. Recorremos cada variable cuantitativa definida arriba.
    # 20. Sirve para aplicar exactamente las mismas medidas a todas las variables.
    for variable in CUANTITATIVAS:
        # 21. Dentro de cada variable, separamos los registros por estado de seguimiento.
        # 22. Sirve para realizar la comparación descriptiva solicitada en EA2.
        for estado, grupo in df.groupby("estado_seguimiento", observed=True):
            # 23. Convertimos la variable del grupo actual a números de punto flotante.
            # 24. Sirve para asegurar que las operaciones estadísticas sean numéricas.
            s = grupo[variable].astype(float)

            # 25. Calculamos la media del grupo actual.
            # 26. Sirve como medida de tendencia central, complementada después con mediana.
            media = float(s.mean())

            # 27. Calculamos la desviación estándar muestral con ddof=1.
            # 28. Sirve para describir la dispersión de los valores dentro del grupo.
            std = float(s.std(ddof=1))

            # 29. Agregamos una fila con n, tendencia central, dispersión, cuartiles y rango observado.
            # 30. Sirve para no reducir la comparación a una sola medida.
            filas.append({
                "variable": variable,
                "estado_seguimiento": str(estado),
                "n": int(s.count()),
                "media": round(media, 3),
                "mediana": round(float(s.median()), 3),
                "desviacion_estandar": round(std, 3),
                "coeficiente_variacion_pct": round(std / media * 100, 2) if media != 0 else np.nan,
                "minimo": round(float(s.min()), 3),
                "q1": round(float(s.quantile(.25)), 3),
                "q3": round(float(s.quantile(.75)), 3),
                "maximo": round(float(s.max()), 3),
            })

    # 31. Convertimos la lista de resultados en DataFrame.
    # 32. Sirve para exportar P2 como una tabla estructurada y reutilizable.
    return pd.DataFrame(filas)


def tabla_binarias(df: pd.DataFrame) -> pd.DataFrame:
    """P3: frecuencia y porcentaje de cinco indicadores binarios por grupo."""
    # 33. Creamos una lista vacía para reunir los resultados.
    # 34. Sirve para construir una fila por indicador y estado.
    filas = []

    # 35. Recorremos cada variable binaria y su etiqueta legible.
    # 36. Sirve para mantener juntas la identificación técnica y la presentación humana.
    for variable, etiqueta in BINARIAS.items():
        # 37. Dividimos los registros por estado de seguimiento.
        # 38. Sirve para calcular frecuencias dentro de cada grupo y no sobre toda la base mezclada.
        for estado, grupo in df.groupby("estado_seguimiento", observed=True):
            # 39. Sumamos los 1 de la variable binaria.
            # 40. Sirve para contar cuántos registros presentan el indicador dentro del grupo.
            casos = int(grupo[variable].sum())

            # 41. Contamos cuántos registros contiene el grupo.
            # 42. Sirve como denominador del porcentaje.
            n = len(grupo)

            # 43. Guardamos conteo y porcentaje redondeado a dos decimales.
            # 44. Sirve para comparar la composición de los dos grupos descriptivamente.
            filas.append({
                "variable": variable,
                "indicador": etiqueta,
                "estado_seguimiento": str(estado),
                "n_grupo": n,
                "registros_con_indicador_1": casos,
                "porcentaje_en_grupo": round(casos / n * 100, 2),
            })

    # 45. Convertimos la lista de resultados P3 en DataFrame.
    # 46. Sirve para mostrarla, exportarla y reutilizarla en Streamlit.
    return pd.DataFrame(filas)


def tabla_grupo_edad(df: pd.DataFrame) -> pd.DataFrame:
    """P4: total y porcentaje con muerte registrada por grupo descriptivo de edad."""
    # 47. Agrupamos por grupo de edad y calculamos total de filas y suma de is_dead.
    # 48. Sirve para obtener total de registros y muertes registradas por categoría.
    t = df.groupby("grupo_edad", observed=True)["is_dead"].agg(total_registros="size", muertes_registradas="sum").reset_index()

    # 49. Restamos las muertes registradas al total de cada categoría.
    # 50. Sirve para calcular los registros sin muerte documentada en cada grupo.
    t["sin_muerte_registrada"] = t["total_registros"] - t["muertes_registradas"]

    # 51. Calculamos el porcentaje con muerte registrada dentro de cada grupo de edad.
    # 52. Sirve para comparar categorías sin presentarlas como umbrales clínicos ni riesgo causal.
    t["porcentaje_con_muerte_registrada"] = (t["muertes_registradas"] / t["total_registros"] * 100).round(2)

    # 53. Devolvemos la tabla P4.
    # 54. Sirve como evidencia de resultados y futuro insumo gráfico de AE4.
    return t


def tabla_condiciones(df: pd.DataFrame) -> pd.DataFrame:
    """P5: total y porcentaje con muerte registrada por nivel descriptivo de condiciones."""
    # 55. Agrupamos por nivel de condiciones y calculamos total y muertes registradas.
    # 56. Sirve para resumir la variable derivada sin convertirla en un índice clínico.
    t = df.groupby("nivel_condiciones_registradas", observed=True)["is_dead"].agg(total_registros="size", muertes_registradas="sum").reset_index()

    # 57. Calculamos los registros sin muerte documentada por nivel.
    # 58. Sirve para completar la distribución dentro de cada categoría.
    t["sin_muerte_registrada"] = t["total_registros"] - t["muertes_registradas"]

    # 59. Calculamos el porcentaje con muerte registrada dentro de cada nivel.
    # 60. Sirve para responder P5 mediante una proporción descriptiva verificable.
    t["porcentaje_con_muerte_registrada"] = (t["muertes_registradas"] / t["total_registros"] * 100).round(2)

    # 61. Devolvemos la tabla P5.
    # 62. Sirve para exportarla a CSV y reutilizarla posteriormente.
    return t


def construir_tablas(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Ejecuta P1–P5 y devuelve todas las tablas bajo nombres de archivo estables."""
    # 63. Ejecutamos las cinco funciones y las reunimos en un diccionario.
    # 64. Sirve para que el notebook pueda recorrer y exportar las respuestas de manera automática.
    return {
        "tabla_01_estado_seguimiento": tabla_estado(df),
        "tabla_02_cuantitativas_por_estado": tabla_cuantitativas(df),
        "tabla_03_binarias_por_estado": tabla_binarias(df),
        "tabla_04_grupo_edad_por_estado": tabla_grupo_edad(df),
        "tabla_05_condiciones_registradas_por_estado": tabla_condiciones(df),
    }
