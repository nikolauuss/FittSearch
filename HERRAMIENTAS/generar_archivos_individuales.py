from pathlib import Path
import shutil
import unicodedata
import re

ROOT = Path(__file__).resolve().parents[1]
NAMES_FILE = ROOT / "NOMBRES_EQUIPO.txt"

def normalize_name(value: str) -> str:
    value = value.strip().upper()
    value = "".join(
        ch for ch in unicodedata.normalize("NFD", value)
        if unicodedata.category(ch) != "Mn"
    )
    value = value.replace("Ñ", "N")
    value = re.sub(r"[^A-Z0-9]+", "_", value)
    return value.strip("_")

names = []
for line in NAMES_FILE.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    normalized = normalize_name(line)
    if normalized:
        names.append(normalized)

if not names:
    raise SystemExit(
        "No hay integrantes en NOMBRES_EQUIPO.txt. "
        "Agregue uno por línea con el formato APELLIDO_NOMBRE."
    )

templates = list(ROOT.rglob("APELLIDO_NOMBRE_*.docx"))
if not templates:
    raise SystemExit("No se encontraron archivos individuales de plantilla.")

created = 0
for template in templates:
    for name in names:
        destination = template.with_name(template.name.replace("APELLIDO_NOMBRE", name))
        shutil.copy2(template, destination)
        created += 1

for template in templates:
    template.unlink()

print(f"Se crearon {created} archivos individuales para {len(names)} integrante(s).")
