# NEON CITY: 24 HORAS

Videojuego de gestión y toma de decisiones desarrollado en **Python** con **Pygame**, enfocado en la innovación, la inclusión y el cuidado de los ecosistemas marinos mediante los Objetivos de Desarrollo Sostenible (ODS) 5, 9 y 14.

## Descripción del proyecto

**NEON CITY: 24 HORAS** propone una experiencia interactiva en la que el jugador toma decisiones para responder a diferentes situaciones de una ciudad. Las decisiones pueden afectar el presupuesto y los indicadores de desarrollo, tecnología, bienestar y medio ambiente.

El proyecto combina programación y aprendizaje para reflexionar sobre:

- **ODS 5 — Igualdad de género:** promover la participación equitativa, las oportunidades y el respeto.
- **ODS 9 — Industria, innovación e infraestructura:** explorar soluciones tecnológicas e infraestructura que respondan a necesidades de la comunidad.
- **ODS 14 — Vida submarina:** reconocer los efectos de los residuos y la contaminación del agua y fomentar el cuidado de los ecosistemas marinos.

## Objetivo general

Desarrollar un videojuego en Python que permita experimentar decisiones relacionadas con la igualdad de género, la innovación y la protección de la vida submarina.

## Objetivos específicos

- Diseñar una experiencia interactiva y fácil de comprender.
- Representar situaciones mediante eventos y alternativas de decisión.
- Mostrar las consecuencias de las decisiones en los recursos e indicadores del juego.
- Relacionar las misiones y situaciones con los ODS 5, 9 y 14.
- Probar y mejorar progresivamente el funcionamiento del videojuego.

## Tecnologías

- **Python:** lenguaje principal para la lógica y las reglas del videojuego.
- **Pygame:** biblioteca para crear la ventana, dibujar elementos, manejar eventos de teclado y controlar el ciclo del juego.
- **HTML/CSS (opcional):** podría utilizarse para una página web complementaria. No reemplaza el desarrollo principal del videojuego en Python.

## Estructura del proyecto

```text
NEON_CITY/
├── main.py           # Punto de entrada del juego
├── settings.py       # Configuración y constantes
├── game.py           # Lógica principal, pantallas e interacción
├── events.py         # Eventos y opciones de decisión
├── assets/
│   ├── images/       # Imágenes y recursos gráficos
│   ├── sounds/       # Efectos de sonido y música
│   └── fonts/        # Fuentes tipográficas
└── data/             # Datos auxiliares del proyecto
```

La estructura puede cambiar durante el desarrollo. Las carpetas `assets/` y `data/` pueden estar vacías mientras se incorporan recursos.

## Requisitos

- Python 3 instalado.
- Pygame instalado en el mismo entorno de Python que ejecutará el juego.

## Instalación y ejecución

1. Abre una terminal dentro de la carpeta `NEON_CITY`.
2. Instala Pygame si todavía no está instalado:

   ```bash
   python -m pip install pygame
   ```

3. Ejecuta el juego:

   ```bash
   python main.py
   ```

En Windows, si el comando `python` no funciona, prueba:

```bash
py main.py
```

## Mecánicas previstas

- Explorar las zonas disponibles de la ciudad.
- Recibir eventos con diferentes alternativas.
- Administrar el presupuesto y evaluar los recursos disponibles.
- Modificar indicadores según las decisiones.
- Consultar un resultado final que resuma el estado de la ciudad.

Los controles y las mecánicas definitivas dependen de la versión implementada. Si están habilitados en el código, los controles previstos son **WASD** para moverse, **E** para interactuar y **ESC** para pausar.

## Estado del proyecto

Proyecto académico en desarrollo. Esta fase presenta la idea, el problema, los objetivos, la relación con los ODS y la organización técnica propuesta. Las funciones descritas como previstas deben verificarse en el código antes de considerarlas terminadas.

## Trabajo futuro

- Completar y probar el ciclo de horas y días.
- Mejorar las pantallas y la experiencia de usuario.
- Añadir eventos y decisiones relacionadas claramente con los ODS 5, 9 y 14.
- Incorporar recursos visuales y sonidos propios.
- Probar errores, balance de recursos y condiciones de finalización.
- Documentar las funciones implementadas y preparar una versión funcional para la sustentación.

## Autor

**Daniel Mercado**

Proyecto de aula — videojuego en Python.

---

**Nota:** este README describe el alcance y la estructura propuesta del proyecto. Actualízalo cuando cambien los archivos, controles o funciones realmente disponibles.
