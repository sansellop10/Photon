# Photon

Photon es un widget de escritorio flotante, minimalista y de alto rendimiento desarrollado en Python 3 y PyQt6. Diseñado con un enfoque estético Cyber-Vibrant de alto contraste, actúa como un overlay translúcido e interactivo que monitoriza en tiempo real las métricas críticas del sistema sin interferir con el espacio de trabajo.

---

## Características Principales

* **Estética Cyber-Vibrant:** Interfaz translúcida integrada con bordes suavizados (`border-radius: 18px`).
* **Always-on-Top Nativo:** Configurado con flags de nivel de sistema gráfico (`X11BypassWindowManagerHint`) para ignorar las restricciones del gestor de ventanas y flotar siempre encima.
* **Barras de Progreso ASCII:** Indicadores de carga visuales optimizados usando caracteres de bloque sólido (`████░░░░`).
* **Interactividad Completa:** Soporte nativo para arrastrar, mover y reposicionar el HUD dinámicamente con el ratón por toda la pantalla.
* **Consumo Eficiente:** Monitorización asíncrona controlada por hardware mediante un ciclo `QTimer` optimizado a 1Hz (1000ms).

---

## Telemetría en Tiempo Real

1. **CPU:** Porcentaje de uso global acompañado de su respectiva barra de progreso.
2. **RAM:** Consumo y asignación de memoria volátil del sistema.
3. **RED:** Monitorización de ancho de banda simétrico (Velocidades de bajada `↓` y subida `↑` calculadas en KB/s).
4. **TEMP:** Captura automática de sensores térmicos de la CPU principal (con soporte de fallback dinámico en hardware compatible).

---

## Arquitectura y Requisitos

El core de Photon está ese estructurado como un paquete modular de Python que interactúa directamente con el subsistema gráfico X11/XCB y el kernel de Linux.

* **Python** >= 3.10
* **PyQt6** >= 6.4.0 (Motor de renderizado de interfaz y bucle de eventos)
* **psutil** >= 5.9.0 (Capa de abstracción de hardware para la lectura de métricas)

---

## Instalación y Despliegue (Modo Desarrollo)

Para instalar el proyecto localmente de forma modular utilizando la estructura del manifiesto moderno:

1. **Clona el repositorio y entra al directorio:**
   ```bash
   git clone [https://github.com/tu-usuario/photon.git](https://github.com/tu-usuario/photon.git)
   cd photon

2. **Instala el paquete en modo editable:**
    ```bash
    pip install -e

3. **Ejecuta el HUD desde cualquier lugar de tu sistema:**
    ```bash
    photon

---
