# Instrucciones paso a paso – AE3 Heart Failure

Estas instrucciones están pensadas para ejecutar el proyecto en bloques pequeños y verificables.

## Bloque 1 – Ubicar el proyecto

1. Descomprima `EA3_HeartFailure_Pablo_Gomez` dentro de:
   `G:\Mi unidad\15. ING. DE SOFTWARE Y DATOS\05. PROYECTO INTEGRADOR III\ACTIVIDADES\ACTIVIDAD 03`
2. En Visual Studio Code seleccione **Archivo > Abrir carpeta** y abra `EA3_HeartFailure_Pablo_Gomez`.
3. Abra **Terminal > Nuevo terminal** y confirme que la terminal se encuentra en la raíz del proyecto.

## Bloque 2 – Preparar el entorno

1. Ejecute `powershell -ExecutionPolicy Bypass -File .\PREPARAR_ENTORNO.ps1`.
2. Espere a que finalice la instalación y verificación de dependencias.
3. En Jupyter seleccione el kernel **Python (EA3 HeartFailure)** o el intérprete `.venv\Scripts\python.exe`.

## Bloque 3 – Ejecutar AE3

1. Abra `AE3/notebooks/PABLO_GOMEZ_AE3_TRANSFORMACION_ENRIQUECIMIENTO.ipynb`.
2. Use **Run All** desde la primera celda hasta la última.
3. Confirme al final: 299 filas, 19 columnas, 0 nulos y mensaje `[OK] AE3 ejecutada completamente`.

## Bloque 4 – Validación local

1. Guarde el notebook después de ejecutar todas las celdas.
2. Ejecute `powershell -ExecutionPolicy Bypass -File .\VALIDAR_LOCAL.ps1`.
3. No continúe a GitHub si alguna validación aparece como error.

## Bloque 5 – Crear el repositorio nuevo de AE3

> El docente escribió literalmente “mismo repositorio”. Por decisión del estudiante, esta entrega se prepara como repositorio nuevo para proteger EA2. El paquete conserva `AE2_CONTINUIDAD` y enlaza el repositorio anterior. Esta decisión debe mantenerse consciente del criterio literal de la guía.

1. En GitHub cree un repositorio público vacío llamado `EA3_HeartFailure_Pablo_Gomez`.
2. No marque README, `.gitignore` ni licencia al crearlo, porque el proyecto ya contiene esos archivos.
3. Copie la URL HTTPS del repositorio nuevo.

## Bloque 6 – Publicar con Git

Ejecute, desde la raíz del proyecto, sustituyendo únicamente la URL si GitHub muestra una diferente:

```powershell
git init
git branch -M main
git add .
git commit -m "feat: estructura inicial y continuidad de AE3"
git remote add origin https://github.com/Emiliog3/EA3_HeartFailure_Pablo_Gomez.git
git push -u origin main
```

Después de cualquier ajuste realice commits descriptivos, por ejemplo:

```powershell
git add .
git commit -m "feat: transforma y enriquece dataset heart failure"
git push
```

```powershell
git add .
git commit -m "docs: actualiza resultados documento y README de AE3"
git push
```

## Bloque 7 – Verificar GitHub Actions

1. Abra la pestaña **Actions** del repositorio.
2. Entre al workflow **Validacion automatica AE3**.
3. Confirme que la ejecución final aparece en verde antes de entregar el enlace.
