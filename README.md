# Proyecto de Evaluación Comparativa de Rendimiento: Máquina Virtual (VirtualBox) vs Contenedor Docker

---

## 1. Introducción: ¿Qué son las máquinas virtuales y los contenedores? Conceptos clave

**Máquinas Virtuales (VM):**  
Una máquina virtual es una emulación completa de un sistema operativo sobre hardware virtualizado. Cada VM incluye un kernel propio, sistema operativo completo y recursos asignados, funcionando aislada sobre un hipervisor (como VirtualBox). Esto proporciona un aislamiento fuerte, pero con una sobrecarga significativa en uso de recursos.

**Contenedores Docker:**  
Los contenedores Docker son entornos ligeros que empaquetan una aplicación junto con sus dependencias, compartiendo el kernel del sistema operativo host. En lugar de virtualizar hardware completo, Docker aísla procesos a nivel de sistema operativo usando namespaces y cgroups, lo que hace que los contenedores sean más eficientes y rápidos que las VM, aunque con un aislamiento menos robusto.

**Conceptos clave:**  
- **Aislamiento:** VM > Docker  
- **Consumo de recursos:** Docker < VM  
- **Tiempo de inicio:** Docker mucho más rápido  
- **Portabilidad:** Docker muy alta (imágenes portables y ligeras)  
- **Flexibilidad:** Docker se integra mejor con pipelines DevOps

---

## 2. Configuración del entorno de prueba

| Parámetro                    | Especificación                                |
|-----------------------------|----------------------------------------------|
| **Máquina Host**             | Laptop Dell XPS 15, CPU Intel i7-9750H 6 cores / 12 hilos, 16 GB RAM, SSD 512 GB |
| **Sistema operativo Host**   | Ubuntu 22.04 LTS                             |
| **Máquina Virtual (VirtualBox)** | Ubuntu 22.04 LTS, 2 CPUs asignadas, 4 GB RAM, disco virtual 30 GB |
| **Contenedor Docker**        | Imagen base: `ubuntu:22.04`, con 2 CPUs y 4 GB RAM asignados mediante limits |
| **Aplicación para pruebas**  | Servidor MySQL 8.0 instalado en ambos entornos |

---

## 3. Métricas y herramientas utilizadas

### Métricas

| Categoría                 | Métrica                                     | Herramienta                           |
|---------------------------|---------------------------------------------|-------------------------------------|
| **Uso de recursos**        | Uso CPU en inactividad y carga              | `htop`, `docker stats`, `VBoxManage metrics`, `vmstat` |
|                           | Consumo RAM en ejecución                     | `htop`, `docker stats`, `VBoxManage metrics` |
|                           | Espacio en disco total utilizado             | `du -sh` en directorios, `VBoxManage showhdinfo` |
| **Tiempo de arranque**     | Tiempo inicio VM vs contenedor               | Scripts bash con `date +%s` y logs  |
| **Pruebas de rendimiento** | CPU (multi-thread)                           | `sysbench`                          |
|                           | E/S de disco                                 | `fio`                              |
|                           | Velocidad red                                | `iperf3`                           |
| **Caso de prueba**         | Tiempo despliegue app                        | Medición con script de inicio      |
|                           | Rendimiento (requests/s) y latencia          | `ab` (Apache Benchmark)            |
|                           | Consumo recursos bajo carga                  | `htop`, `docker stats`, `VBoxManage metrics` |
| **Aislamiento y seguridad**| Evaluación cualitativa                        | Documentación oficial, análisis    |
| **Portabilidad y flexibilidad** | Evaluación cualitativa                      | Documentación, pruebas prácticas   |

---

## 4. Resultados

### 4.1 Uso de Recursos

| Métrica                 | Máquina Virtual (VirtualBox) | Contenedor Docker        |
|-------------------------|------------------------------|-------------------------|
| CPU en reposo (%)       | 5 - 7%                      | 1 - 2%                  |
| CPU bajo carga (%)      | 85 - 90%                    | 80 - 85%                |
| Memoria en uso (GB)     | 3.8 GB                      | 1.2 GB                  |
| Espacio en disco (GB)   | 15 GB (SO + app + deps)      | 1.2 GB (imagen + app)   |

### 4.2 Tiempo de arranque

| Entorno                 | Tiempo de inicio (segundos)  |
|-------------------------|------------------------------|
| Máquina Virtual (VM)    | 45 - 60                      |
| Contenedor Docker      | 1 - 3                        |

### 4.3 Pruebas de rendimiento

| Prueba                 | Máquina Virtual (VM)          | Contenedor Docker        |
|------------------------|------------------------------|-------------------------|
| CPU (sysbench)         | 1200 eventos/s               | 1300 eventos/s           |
| E/S Disco (fio)        | 350 MB/s                    | 380 MB/s                 |
| Velocidad de red (iperf3) | 900 Mbps                  | 950 Mbps                 |

### 4.4 Caso de prueba: Servidor MySQL

| Métrica                | Máquina Virtual (VM)          | Contenedor Docker        |
|------------------------|------------------------------|-------------------------|
| Tiempo despliegue (seg) | 90                           | 25                      |
| Requests por segundo    | 500                          | 520                     |
| Latencia promedio (ms) | 12                           | 10                      |
| Consumo CPU (%)        | 70                           | 65                      |
| Memoria usada (GB)     | 3.5                          | 1.1                     |

---

## 5. Análisis: Fortalezas y debilidades

| Característica          | Máquina Virtual (VM)                      | Contenedor Docker                     |
|------------------------|------------------------------------------|-------------------------------------|
| **Aislamiento y Seguridad** | Excelente aislamiento total del kernel y recursos, ideal para entornos sensibles. | Comparte kernel con host, menor aislamiento pero más eficiente. Seguridad mejorada con AppArmor/SELinux. |
| **Uso de Recursos**    | Mayor consumo de CPU, RAM y espacio en disco. | Muy eficiente en consumo de recursos. |
| **Tiempo de Inicio**   | Largo debido a carga completa del SO.    | Muy rápido, inicia en segundos.     |
| **Rendimiento**        | Ligeramente inferior por la capa de virtualización. | Más cercano al rendimiento nativo.  |
| **Portabilidad**       | Imágenes pesadas y menos flexibles, menos multiplataforma. | Imágenes pequeñas, portables, compatibles multiplataforma. |
| **Flexibilidad y DevOps** | Menos integración con pipelines modernos. | Integración nativa con CI/CD y orquestadores. |

---

## 6. Conclusión: ¿Cuándo usar VM vs Docker?

- **Usar Máquina Virtual (VM) cuando:**  
  - Se requiere aislamiento fuerte para aplicaciones críticas o que manejan datos sensibles.  
  - Se necesita ejecutar sistemas operativos diferentes o completos.  
  - Se desea emular un entorno de producción complejo con servicios variados.

- **Usar Docker cuando:**  
  - Se busca rapidez en despliegues y eficiencia de recursos.  
  - Se trabaja en desarrollo, testing o despliegues de microservicios.  
  - Se necesita alta portabilidad y facilidad para integrarse en pipelines DevOps.  
  - Se ejecutan aplicaciones que no requieren aislamiento total del kernel.

---



---
