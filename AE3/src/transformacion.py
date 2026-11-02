"""Transformación y controles de calidad de AE3.

Principio metodológico: no se elimina ni imputa un registro sin evidencia de
error. Los valores extremos estadísticos se identifican para revisión, pero se
conservan porque un valor extremo no es sinónimo de dato incorrecto.
"""

# 1. Activamos anotaciones de tipos modernas.
# 2. Sirve para documentar funciones y colecciones sin alterar su ejecución.
from __future__ import annotations

# 3. Importamos pandas con el alias pd.
# 4. Sirve para convertir tipos, detectar nulos, duplicados y calcular cuartiles.
import pandas as pd

# 5. Importamos NumPy con el alias np.
# 6. Sirve como dependencia numérica explícita del módulo y facilita extensiones reproducibles.
import numpy as np

# 7. Definimos las seis variables que deben conservar únicamente códigos 0/1.
# 8. Sirve para aplicar la misma regla de normalización y validación a todos los indicadores binarios.
BINARIAS = [
    "has_anaemia", "has_diabetes", "has_high_blood_pressure",
    "is_male", "is_smoker", "is_dead"
]

# 9. Definimos las siete variables numéricas sobre las que revisaremos tipos, rangos y extremos.
# 10. Sirve para centralizar la selección y evitar repetir nombres en distintas funciones.
CONTINUAS = [
    "age",
    "creatinine_phosphokinase_concentration_in_blood",
    "heart_ejection_fraction",
    "platelets_concentration_in_blood",
    "serum_creatinine_concentration_in_blood",
    "serum_sodium_concentration_in_blood",
    "days_in_study",
]


def _control_rangos(df: pd.DataFrame) -> dict[str, int]:
    """Cuenta valores que violarían rangos estructurales básicos, no rangos clínicos."""
    # 11. Evaluamos únicamente condiciones estructurales evidentes, como valores negativos imposibles.
    # 12. Sirve para detectar inconsistencias sin inventar límites clínicos no solicitados por la fuente.
    return {
        "edad_no_positiva": int((pd.to_numeric(df["age"], errors="coerce") <= 0).sum()),
        "fraccion_eyeccion_fuera_0_100": int(((pd.to_numeric(df["heart_ejection_fraction"], errors="coerce") < 0) | (pd.to_numeric(df["heart_ejection_fraction"], errors="coerce") > 100)).sum()),
        "plaquetas_negativas": int((pd.to_numeric(df["platelets_concentration_in_blood"], errors="coerce") < 0).sum()),
        "creatinina_serica_negativa": int((pd.to_numeric(df["serum_creatinine_concentration_in_blood"], errors="coerce") < 0).sum()),
        "sodio_serico_negativo": int((pd.to_numeric(df["serum_sodium_concentration_in_blood"], errors="coerce") < 0).sum()),
        "cpk_negativa": int((pd.to_numeric(df["creatinine_phosphokinase_concentration_in_blood"], errors="coerce") < 0).sum()),
        "seguimiento_negativo": int((pd.to_numeric(df["days_in_study"], errors="coerce") < 0).sum()),
    }


def detectar_extremos_iqr(df: pd.DataFrame) -> pd.DataFrame:
    """Identifica extremos por IQR y los documenta sin eliminarlos."""
    # 13. Creamos una lista vacía para reunir una fila de diagnóstico por variable cuantitativa.
    # 14. Sirve para exportar posteriormente `valores_extremos_iqr.csv`.
    filas = []

    # 15. Recorremos cada variable cuantitativa definida en CONTINUAS.
    # 16. Sirve para aplicar una regla uniforme y auditable de detección estadística de extremos.
    for columna in CONTINUAS:
        # 17. Convertimos temporalmente la columna a numérica.
        # 18. Sirve para garantizar que cuantiles y comparaciones se calculen sobre números.
        serie = pd.to_numeric(df[columna], errors="coerce")

        # 19. Calculamos primer cuartil, tercer cuartil y rango intercuartílico.
        # 20. Sirve para definir límites descriptivos sin declarar que un valor fuera de ellos sea erróneo.
        q1 = float(serie.quantile(0.25))
        q3 = float(serie.quantile(0.75))
        iqr = q3 - q1

        # 21. Calculamos los límites IQR de 1.5 veces el rango intercuartílico.
        # 22. Sirve para identificar observaciones estadísticamente alejadas de la zona central.
        inferior = q1 - 1.5 * iqr
        superior = q3 + 1.5 * iqr

        # 23. Contamos cuántos valores están por debajo o por encima de esos límites.
        # 24. Sirve para documentar la presencia de extremos sin borrarlos automáticamente.
        cantidad = int(((serie < inferior) | (serie > superior)).sum())

        # 25. Guardamos cálculos, cantidad y decisión metodológica.
        # 26. Sirve para dejar trazabilidad explícita del control de valores extremos.
        filas.append({
            "variable": columna,
            "q1": q1,
            "q3": q3,
            "iqr": iqr,
            "limite_inferior_iqr": inferior,
            "limite_superior_iqr": superior,
            "valores_extremos_iqr": cantidad,
            "tratamiento": "Se conservan; son extremos estadísticos, no errores demostrados.",
        })

    # 27. Convertimos el diagnóstico acumulado en DataFrame.
    # 28. Sirve para mostrarlo en el notebook y exportarlo como evidencia.
    return pd.DataFrame(filas)


def transformar_y_validar(df_original: pd.DataFrame):
    """Normaliza tipos, ejecuta controles y devuelve evidencias antes/después."""
    # 29. Conservamos una copia independiente del estado de entrada.
    # 30. Sirve para comparar antes/después sin alterar la evidencia original.
    antes = df_original.copy(deep=True)

    # 31. Creamos una segunda copia que sí será transformada.
    # 32. Sirve para separar conceptualmente preservación y procesamiento.
    df = df_original.copy(deep=True)

    # 33. Creamos una lista para documentar cada control de calidad.
    # 34. Sirve para registrar también controles cuyo resultado sea cero.
    control = []

    # 35. Contamos nulos totales y filas afectadas antes de transformar.
    # 36. Sirve para justificar si se requiere o no imputación.
    control.append({"control": "Valores nulos antes", "resultado": int(antes.isna().sum().sum()), "afectados": int(antes.isna().any(axis=1).sum()), "decision": "No imputar si el resultado es 0."})

    # 37. Contamos filas duplicadas exactas antes de transformar.
    # 38. Sirve para justificar si se requiere o no eliminar duplicados.
    control.append({"control": "Filas duplicadas exactas antes", "resultado": int(antes.duplicated().sum()), "afectados": int(antes.duplicated().sum()), "decision": "No eliminar si el resultado es 0."})

    # 39. Recorremos las siete columnas cuantitativas y las convertimos explícitamente a número.
    # 40. Sirve para estandarizar tipos y convertir en nulo cualquier valor no interpretable como número.
    for columna in CONTINUAS:
        df[columna] = pd.to_numeric(df[columna], errors="coerce")

    # 41. Recorremos los seis indicadores binarios.
    # 42. Sirve para normalizarlos a códigos 0/1 que facilitan sumas y proporciones.
    for columna in BINARIAS:
        # 43. Si la columna viene como bool, la convertimos directamente a entero de 8 bits.
        # 44. Sirve para representar False=0 y True=1 sin perder información.
        if df[columna].dtype == bool:
            df[columna] = df[columna].astype("int8")
        else:
            # 45. Si no viene como bool, intentamos convertirla a número y luego a entero anulable.
            # 46. Sirve para detectar códigos no numéricos como posibles faltantes en el control posterior.
            df[columna] = pd.to_numeric(df[columna], errors="coerce").astype("Int8")

    # 47. Convertimos edad a entero porque la versión de Hugging Face usada en EA2 la reporta como int64.
    # 48. Sirve para conservar coherencia de esquema con la entrega anterior.
    df["age"] = df["age"].astype("int64")

    # 49. Convertimos days_in_study a entero porque representa días completos en la fuente usada.
    # 50. Sirve para mantener un tipo consistente con EA2.
    df["days_in_study"] = df["days_in_study"].astype("int64")

    # 51. Inicializamos el conteo de valores binarios que no sean 0 ni 1.
    # 52. Sirve para consolidar en un único control los seis indicadores.
    invalidos_binarios = 0

    # 53. Recorremos las columnas binarias y acumulamos códigos inválidos.
    # 54. Sirve para comprobar que la normalización produjo solamente 0/1.
    for columna in BINARIAS:
        invalidos_binarios += int((~df[columna].isin([0, 1])).sum())

    # 55. Registramos el resultado y la decisión asociada al control binario.
    # 56. Sirve para demostrar que no se modifica ningún registro si el resultado es cero.
    control.append({"control": "Valores fuera de 0/1 en indicadores binarios", "resultado": invalidos_binarios, "afectados": invalidos_binarios, "decision": "No se modifica ningún registro si el resultado es 0."})

    # 57. Ejecutamos los controles de rangos estructurales definidos arriba.
    # 58. Sirve para detectar valores imposibles básicos sin convertirlos automáticamente en errores clínicos.
    rangos = _control_rangos(df)

    # 59. Recorremos cada control de rango y lo añadimos a la bitácora.
    # 60. Sirve para informar explícitamente incluso los resultados iguales a cero.
    for nombre, cantidad in rangos.items():
        control.append({"control": f"Rango estructural: {nombre}", "resultado": cantidad, "afectados": cantidad, "decision": "Revisar únicamente si el resultado es mayor que 0."})

    # 61. Volvemos a contar nulos después de las conversiones de tipo.
    # 62. Sirve para verificar que la transformación no haya creado faltantes nuevos.
    control.append({"control": "Valores nulos después de conversión", "resultado": int(df.isna().sum().sum()), "afectados": int(df.isna().any(axis=1).sum()), "decision": "La conversión no debe crear faltantes."})

    # 63. Calculamos la diferencia de filas entre antes y después.
    # 64. Sirve para demostrar que AE3 no eliminó ningún registro.
    control.append({"control": "Filas eliminadas", "resultado": int(len(antes) - len(df)), "afectados": int(len(antes) - len(df)), "decision": "AE3 conserva los 299 registros."})

    # 65. Construimos una tabla compacta con filas, columnas, nulos y duplicados antes/después.
    # 66. Sirve para cumplir la comparación estructural solicitada explícitamente por la actividad.
    comparacion = pd.DataFrame([
        {"indicador": "filas", "antes": antes.shape[0], "despues_transformacion": df.shape[0]},
        {"indicador": "columnas", "antes": antes.shape[1], "despues_transformacion": df.shape[1]},
        {"indicador": "nulos_totales", "antes": int(antes.isna().sum().sum()), "despues_transformacion": int(df.isna().sum().sum())},
        {"indicador": "duplicados_exactos", "antes": int(antes.duplicated().sum()), "despues_transformacion": int(df.duplicated().sum())},
    ])

    # 67. Construimos una tabla con el tipo de cada variable antes y después de transformar.
    # 68. Sirve para evidenciar exactamente qué tipos cambiaron.
    tipos = pd.DataFrame({
        "variable": antes.columns,
        "tipo_antes": [str(antes[c].dtype) for c in antes.columns],
        "tipo_despues_transformacion": [str(df[c].dtype) for c in antes.columns],
    })

    # 69. Ejecutamos la detección IQR sobre el DataFrame ya normalizado.
    # 70. Sirve para documentar extremos estadísticos sin eliminar observaciones válidas por defecto.
    extremos = detectar_extremos_iqr(df)

    # 71. Devolvemos el DataFrame transformado y cuatro evidencias de control.
    # 72. Sirve para que el notebook muestre, exporte y documente cada etapa de la transformación.
    return df, pd.DataFrame(control), comparacion, tipos, extremos
