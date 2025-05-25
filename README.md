# 🧪 Comparación de Rendimiento: Máquina Virtual vs Docker

---

## 📖 1. Introducción

Las **máquinas virtuales (VM)** y los **contenedores Docker** son tecnologías de virtualización. Aunque ambas permiten empaquetar y ejecutar aplicaciones, su funcionamiento es fundamentalmente distinto:

- **Máquina Virtual (VM)**: Emula hardware completo, ejecutando su propio sistema operativo. Ofrece fuerte aislamiento.
- **Contenedor Docker**: Comparte el kernel del sistema host. Es más ligero y arranca más rápido, ideal para microservicios y entornos DevOps.

Este proyecto compara su rendimiento utilizando métricas clave en un entorno controlado.

---

## 🧰 2. Configuración del Entorno de Pruebas

### 💻 Máquina Host

- **CPU**: Intel Core i7-1165G7 @ 2.80GHz  
- **RAM**: 16 GB  
- **Sistema operativo**: Ubuntu 22.04 LTS  

### 🧱 Máquina Virtual

- **Virtualizador**: VirtualBox 7.0  
- **Imagen ISO**: Ubuntu 20.04 Desktop  
- **Recursos asignados**: 2 CPU, 4 GB RAM, 20 GB de disco  

### 🐳 Contenedor Docker

- **Imagen base**: `ubuntu:20.04`  
- **Configuración especial**: docker-in-docker  
- **Recursos límite**: 2 CPU, 4 GB RAM  

---

## 🧪 3. Métricas y Herramientas Utilizadas

| Categoría            | Métricas                             | Herramientas                      |
|----------------------|--------------------------------------|-----------------------------------|
| 🔧 Uso de recursos    | CPU, RAM, Disco                      | `htop`, `top`, `docker stats`, `vmstat` |
| ⚡ Tiempo de arranque | Inicio del sistema                   | `systemd-analyze`, `time`         |
| 🚀 Rendimiento        | CPU, Disco, Red                      | `sysbench`, `fio`, `iperf3`       |
| 📦 Aplicación         | Despliegue, Latencia, Rendimiento    | `ab`, `curl`, `psutil`            |
| 🔒 Seguridad          | Kernel, aislamiento, perfiles        | Evaluación cualitativa            |
| ♻️ Portabilidad       | Exportación, compatibilidad, CI/CD   | Evaluación cualitativa            |

---

## 📊 4. Resultados

### 🔧 Uso de Recursos

| Entorno     | CPU (Idle/Load) | RAM utilizada | Tamaño base |
|-------------|------------------|----------------|-------------|
| VM          | 5% / 95%         | ~1.2 GB        | 8.0 GB      |
| Docker      | 2% / 87%         | ~250 MB        | 1.2 GB      |

### ⚡ Tiempo de Arranque

| Entorno     | Tiempo de arranque |
|-------------|--------------------|
| VM          | 25 segundos        |
| Docker      | 2 segundos         |

### 🚀 Pruebas de Rendimiento: CPU (`sysbench`)

| Entorno     | Tiempo total | Transacciones/s |
|-------------|--------------|-----------------|
| VM          | 6.5 s        | 1538 tps        |
| Docker      | 5.9 s        | 1694 tps        |

### 🚀 Pruebas de Disco (`fio`)

| Entorno     | Lectura (MB/s) | Escritura (MB/s) |
|-------------|----------------|------------------|
| VM          | 340 MB/s       | 290 MB/s         |
| Docker      | 420 MB/s       | 360 MB/s         |

### 📦 Aplicación: Servidor Flask (prueba con Apache Bench)

| Métrica           | VM           | Docker        |
|-------------------|--------------|---------------|
| Tiempo de arranque| 3.8 s        | 1.1 s         |
| Latencia promedio | 82 ms        | 65 ms         |
| Req/s promedio    | 115 req/s    | 162 req/s     |

---

## 🔍 5. Análisis

### ✅ Fortalezas de Docker

- ✅ Arranque casi instantáneo  
- ✅ Bajo uso de recursos (RAM y disco)  
- ✅ Mejor rendimiento en CPU y disco  
- ✅ Ideal para integración continua y despliegues rápidos  

### ✅ Fortalezas de la VM

- ✅ Aislamiento completo del sistema operativo  
- ✅ Simulación precisa de un entorno real  
- ✅ Soporte completo para interfaces gráficas y controladores  

### ❌ Debilidades de Docker

- ❌ Comparte el kernel del host (menor aislamiento)  
- ❌ Menor soporte para interfaces gráficas y entornos complejos  

### ❌ Debilidades de la VM

- ❌ Lento arranque  
- ❌ Alto uso de recursos base  
- ❌ Menor eficiencia para cargas pequeñas  

---

## 🧠 6. Conclusión: ¿Cuándo usar VM vs Docker?

| Escenario                                       | Recomendación     |
|-------------------------------------------------|--------------------|
| Desarrollo ágil / microservicios               | 🐳 Docker           |
| Simulación completa de sistemas operativos     | 🧱 Máquina Virtual  |
| Máxima seguridad y aislamiento del kernel      | 🧱 Máquina Virtual  |
| Automatización DevOps y CI/CD                  | 🐳 Docker           |
| Entornos gráficos o de escritorio complejos    | 🧱 Máquina Virtual  |

---

> En resumen, **Docker es ideal para rendimiento, eficiencia y despliegues rápidos**, mientras que **las máquinas virtuales destacan por su aislamiento y compatibilidad total**.  
> Elegir la mejor opción depende del caso de uso y los requerimientos del entorno.

---



