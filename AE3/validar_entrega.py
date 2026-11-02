"""Validación local final de la estructura y resultados de AE3."""

# 1. Importamos json, Path y pandas.
# 2. Sirve para revisar notebook, archivos, dimensiones y contenidos de la entrega.
import json
from pathlib import Path
import pandas as pd

# 3. Tomamos como raíz la carpeta donde se encuentra este archivo.
# 4. Sirve para evitar rutas personales del computador.
RAIZ = Path(__file__).resolve().parent

# 5. Abrimos el notebook entregable y leemos su estructura JSON.
# 6. Sirve para verificar que todas las celdas de código hayan sido ejecutadas y no tengan errores.
ruta_nb = RAIZ / "AE3" / "notebooks" / "PABLO_GOMEZ_AE3_TRANSFORMACION_ENRIQUECIMIENTO.ipynb"
nb = json.loads(ruta_nb.read_text(encoding="utf-8"))
codigo = [c for c in nb["cells"] if c.get("cell_type") == "code"]
errores = [o for c in codigo for o in c.get("outputs", []) if o.get("output_type") == "error"]
assert codigo and all(c.get("execution_count") is not None for c in codigo), "Hay celdas sin ejecutar."
assert not errores, f"El notebook contiene errores: {errores}"

# 7. Leemos el dataset preparado.
# 8. Sirve para comprobar la salida final que alimentará AE4.
df = pd.read_csv(RAIZ / "AE3" / "datos" / "heart_failure_preparado.csv")
assert df.shape == (299, 19), f"Dimensión final inesperada: {df.shape}"
assert int(df.isna().sum().sum()) == 0, "El dataset preparado contiene valores nulos."

# 9. Enumeramos las evidencias mínimas que deben existir antes de publicar.
# 10. Sirve para detectar omisiones de archivos de forma automática.
obligatorios = [
    "README.md",
    "requirements.txt",
    "CHECKLIST_RUBRICA_AE3.md",
    ".github/workflows/validacion_ae3.yml",
    "AE3/documento/PABLO_GOMEZ_AE3_TRANSFORMACION_ENRIQUECIMIENTO.docx",
    "AE3/resultados/resumen_dataframe_final.txt",
    "AE3/resultados/control_calidad.csv",
    "AE3/resultados/comparacion_antes_despues.csv",
    "AE3/resultados/diccionario_datos_ae3.csv",
    "AE3/resultados/tabla_01_estado_seguimiento.csv",
    "AE3/resultados/tabla_02_cuantitativas_por_estado.csv",
    "AE3/resultados/tabla_03_binarias_por_estado.csv",
    "AE3/resultados/tabla_04_grupo_edad_por_estado.csv",
    "AE3/resultados/tabla_05_condiciones_registradas_por_estado.csv",
]
for relativo in obligatorios:
    ruta = RAIZ / relativo
    assert ruta.exists() and ruta.stat().st_size > 0, f"Falta evidencia: {relativo}"

# 11. Comprobamos que P1 conserve los 299 registros y aproximadamente 100 %.
# 12. Sirve como control básico de consistencia entre el dataset y su primera tabla de resultados.
t1 = pd.read_csv(RAIZ / "AE3" / "resultados" / "tabla_01_estado_seguimiento.csv")
assert int(t1["registros"].sum()) == 299
assert abs(float(t1["porcentaje"].sum()) - 100.0) < 0.02

# 13. Mostramos un cierre visible cuando todos los controles pasan.
# 14. Sirve para saber que el paquete está listo para GitHub y para la entrega.
print("[OK] Notebook completamente ejecutado y sin errores.")
print("[OK] Dataset final: 299 filas x 19 columnas, 0 nulos.")
print("[OK] Archivos obligatorios presentes.")
print("[OK] Tablas de resultados coherentes.")
print("[OK] AE3 lista para publicar.")
