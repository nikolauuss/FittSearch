# REPOSITORIO APT122

Estructura base del repositorio para las evidencias del Proyecto APT.

## Importante

- Los apellidos y nombres de cada estudiante deben escribirse en MAYÚSCULAS y sin tildes.
- Reemplace `APELLIDO_NOMBRE` en los archivos individuales por el nombre real del estudiante.
- Debe existir un conjunto de archivos individuales por cada integrante del equipo.
- Los documentos en inglés están marcados como optativos.
- Las planillas de evaluación y las guías oficiales deben reemplazarse por los archivos enviados por el docente.
- No elimine las carpetas de evidencias, aunque todavía estén vacías.
- Los archivos `.gitkeep` permiten que GitHub conserve las carpetas vacías.

## Formato recomendado para los nombres

Ejemplo:

`GONZALEZ_JUAN_1.1_APT122_AutoevaluacionCompetenciasFase1.docx`

No use tildes, eñes, minúsculas ni caracteres especiales en la parte correspondiente al nombre del estudiante.

## Personalización automática

1. Abra `NOMBRES_EQUIPO.txt`.
2. Escriba un integrante por línea con el formato `APELLIDO_NOMBRE`.
3. Ejecute:

```bash
python HERRAMIENTAS/generar_archivos_individuales.py
```

El programa copiará los archivos individuales para cada integrante y eliminará los marcadores `APELLIDO_NOMBRE`.
