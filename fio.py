import os

# Estructura del nuevo proyecto
base_dir = "disk_io_benchmark"
notebooks_dir = os.path.join(base_dir, "notebooks")
scripts_dir = os.path.join(base_dir, "scripts")
results_dir = os.path.join(base_dir, "results")

# Crear directorios
os.makedirs(notebooks_dir, exist_ok=True)
os.makedirs(scripts_dir, exist_ok=True)
os.makedirs(results_dir, exist_ok=True)

# Crear notebook base
notebook_path = os.path.join(notebooks_dir, "fio_benchmark_analysis.ipynb")
with open(notebook_path, "w", encoding="utf-8") as f:
    f.write("# Notebook for disk I/O benchmark using fio\n")

# Script de setup para VM
vm_script = """#!/bin/bash
echo "🚀 Configurando entorno para benchmark de disco con fio..."
sudo apt update && sudo apt install -y fio python3 python3-pip
pip3 install matplotlib pandas
echo "✅ Setup completado. Ejecuta el notebook en 'notebooks/fio_benchmark_analysis.ipynb'"
"""

# Script de setup para Docker
docker_script = """#!/bin/bash
echo "🐳 Configurando entorno Docker para benchmark con fio..."
sudo apt update && sudo apt install -y fio python3 python3-pip
pip3 install matplotlib pandas
echo "✅ Entorno listo."
"""

# Dockerfile
dockerfile = """FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y fio python3 python3-pip \\
    && pip3 install matplotlib pandas
WORKDIR /workspace
COPY . .
CMD ["bash"]
"""

# README
readme = """# Disk I/O Benchmark (VM vs Docker)

Este proyecto evalúa el rendimiento de disco (lectura/escritura) usando `fio` tanto en una máquina virtual como en un contenedor Docker.

## Estructura
- `notebooks/`: análisis y gráficos de resultados
- `scripts/`: scripts de instalación para VM y Docker
- `results/`: archivos de salida del benchmark

## Requisitos
- `fio`, `python3`, `pip`, `matplotlib`, `pandas`
"""

# Crear archivos
with open(os.path.join(scripts_dir, "vm_setup.sh"), "w", encoding="utf-8") as f:
    f.write(vm_script)

with open(os.path.join(scripts_dir, "docker_setup.sh"), "w", encoding="utf-8") as f:
    f.write(docker_script)

with open(os.path.join(scripts_dir, "Dockerfile"), "w", encoding="utf-8") as f:
    f.write(dockerfile)

with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)

with open(os.path.join(base_dir, ".gitignore"), "w", encoding="utf-8") as f:
    f.write("__pycache__/\n*.pyc\n*.ipynb_checkpoints/\n")

