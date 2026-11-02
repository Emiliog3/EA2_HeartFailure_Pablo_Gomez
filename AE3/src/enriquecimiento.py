"""Variables derivadas de AE3.

Las categorías son operativas para analítica descriptiva. No constituyen
diagnósticos ni umbrales clínicos y se documentan como tales.
"""

# 1. Activamos anotaciones de tipos modernas.
# 2. Sirve para documentar las funciones sin cambiar su comportamiento.
from __future__ import annotations

# 3. Importamos pandas con el alias pd.
# 4. Sirve para crear categorías, transformar columnas y devolver tablas de documentación.
import pandas as pd


def enriquecer(df_transformado: pd.DataFrame):
    """Crea seis variables derivadas transparentes y devuelve su documentación."""
    # 5. Creamos una copia profunda del DataFrame ya transformado.
    # 6. Sirve para que el enriquecimiento no modifique el objeto recibido por referencia.
    df = df_transformado.copy(deep=True)

    # 7. Creamos una lista vacía donde documentaremos cada variable derivada.
    # 8. Sirve para construir automáticamente `variables_enriquecidas.csv`.
    cambios = []

    # 9. Traducimos el código 0/1 de is_dead a una etiqueta legible.
    # 10. Sirve para que tablas, filtros y futuras visualizaciones no muestren códigos crudos.
    df["estado_seguimiento"] = df["is_dead"].map({1: "Registró muerte", 0: "No registró muerte"}).astype("category")

    # 11. Documentamos regla, significado, utilidad y cantidad de registros etiquetados.
    # 12. Sirve para cumplir la exigencia de justificar cada enriquecimiento.
    cambios.append({"variable": "estado_seguimiento", "regla": "is_dead: 1=Registró muerte; 0=No registró muerte", "significado": "Etiqueta legible del desenlace registrado durante el seguimiento.", "utilidad": "Facilita tablas, filtros y futura visualización en Streamlit.", "afectados": len(df)})

    # 13. Agrupamos la edad en cinco intervalos descriptivos.
    # 14. Sirve para comparar grupos de forma legible sin declarar umbrales clínicos.
    df["grupo_edad"] = pd.cut(
        df["age"],
        bins=[-float("inf"), 49, 59, 69, 79, float("inf")],
        labels=["<50", "50-59", "60-69", "70-79", "80+"],
        ordered=True,
    )

    # 15. Documentamos la regla de agrupación de edad.
    # 16. Sirve para dejar explícito que la categoría es analítica y no diagnóstica.
    cambios.append({"variable": "grupo_edad", "regla": "<50; 50-59; 60-69; 70-79; 80+ años", "significado": "Agrupación descriptiva de edad.", "utilidad": "Permite comparar la distribución del evento por grupos de edad sin interpretar los cortes como umbrales clínicos.", "afectados": len(df)})

    # 17. Guardamos las tres condiciones binarias que se pueden sumar de manera transparente.
    # 18. Sirve para crear un conteo simple sin inventar un índice clínico.
    condiciones = ["has_anaemia", "has_diabetes", "has_high_blood_pressure"]

    # 19. Sumamos las tres condiciones 0/1 fila por fila y guardamos el resultado como entero pequeño.
    # 20. Sirve para saber si cada registro presenta 0, 1, 2 o 3 de esas condiciones documentadas.
    df["condiciones_registradas"] = df[condiciones].sum(axis=1).astype("int8")

    # 21. Documentamos el conteo de condiciones.
    # 22. Sirve para evitar interpretarlo erróneamente como una escala de comorbilidad validada.
    cambios.append({"variable": "condiciones_registradas", "regla": "anemia + diabetes + presión arterial alta (cada indicador 0/1)", "significado": "Número de las tres condiciones binarias registradas en cada fila.", "utilidad": "Resume simultáneamente las condiciones disponibles sin crear un índice clínico.", "afectados": len(df)})

    # 23. Agrupamos el conteo anterior en tres niveles descriptivos.
    # 24. Sirve para producir una tabla compacta que pueda reutilizarse en AE4.
    df["nivel_condiciones_registradas"] = pd.cut(
        df["condiciones_registradas"],
        bins=[-1, 0, 1, 3],
        labels=["0 condiciones", "1 condición", "2 o 3 condiciones"],
        ordered=True,
    )

    # 25. Documentamos la categoría derivada del conteo.
    # 26. Sirve para mantener trazabilidad entre regla, significado y salida analítica.
    cambios.append({"variable": "nivel_condiciones_registradas", "regla": "0; 1; 2 o 3 condiciones registradas", "significado": "Categoría descriptiva derivada del conteo anterior.", "utilidad": "Facilita la comparación de proporciones en tablas y en AE4.", "afectados": len(df)})

    # 27. Traducimos is_male a una etiqueta legible.
    # 28. Sirve para evitar códigos 0/1 en tablas y filtros.
    df["sexo_registrado"] = df["is_male"].map({1: "Masculino", 0: "Femenino"}).astype("category")

    # 29. Documentamos la etiqueta de sexo codificado en la fuente.
    # 30. Sirve para aclarar que se conserva la definición disponible en el dataset.
    cambios.append({"variable": "sexo_registrado", "regla": "is_male: 1=Masculino; 0=Femenino", "significado": "Etiqueta legible del sexo codificado en la fuente.", "utilidad": "Evita mostrar códigos 0/1 en resultados y filtros.", "afectados": len(df)})

    # 31. Traducimos is_smoker a Sí/No.
    # 32. Sirve para facilitar la lectura humana del indicador de tabaquismo.
    df["tabaquismo_registrado"] = df["is_smoker"].map({1: "Sí", 0: "No"}).astype("category")

    # 33. Documentamos la etiqueta legible de tabaquismo.
    # 34. Sirve para preparar tablas y visualizaciones posteriores.
    cambios.append({"variable": "tabaquismo_registrado", "regla": "is_smoker: 1=Sí; 0=No", "significado": "Etiqueta legible del indicador de tabaquismo registrado.", "utilidad": "Facilita lectura de tablas y futura visualización.", "afectados": len(df)})

    # 35. Verificamos que el enriquecimiento no haya eliminado filas.
    # 36. Sirve para demostrar que se conservan los 299 registros originales.
    assert df.shape[0] == 299

    # 37. Verificamos que ninguna variable derivada haya creado valores faltantes.
    # 38. Sirve para validar la integridad del DataFrame final.
    assert df.isna().sum().sum() == 0

    # 39. Devolvemos el DataFrame enriquecido y la tabla que documenta sus seis nuevas variables.
    # 40. Sirve para continuar el análisis y exportar evidencia verificable.
    return df, pd.DataFrame(cambios)
