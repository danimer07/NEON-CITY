import pygame
import sys
import random

# ============================================================
# INICIALIZACIÓN
# ============================================================

pygame.init()

ANCHO = 1000
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("NEON CITY: 24 HORAS")

reloj = pygame.time.Clock()

# ============================================================
# COLORES
# ============================================================

FONDO = (15, 18, 30)
NEGRO = (5, 8, 15)
BLANCO = (255, 255, 255)
GRIS = (150, 155, 165)
GRIS_OSCURO = (35, 40, 55)

VERDE = (50, 220, 120)
VERDE_OSCURO = (25, 120, 75)

AZUL = (50, 150, 255)
AZUL_OSCURO = (25, 75, 130)

AMARILLO = (255, 210, 70)
NARANJA = (255, 145, 50)

ROJO = (240, 70, 80)
MORADO = (170, 90, 255)

CYAN = (50, 230, 240)

# ============================================================
# FUENTES
# ============================================================

fuente_titulo = pygame.font.SysFont("arial", 52, bold=True)
fuente_grande = pygame.font.SysFont("arial", 34, bold=True)
fuente_mediana = pygame.font.SysFont("arial", 25, bold=True)
fuente_normal = pygame.font.SysFont("arial", 20)
fuente_pequena = pygame.font.SysFont("arial", 16)

# ============================================================
# ESTADOS DEL JUEGO
# ============================================================

MENU = "menu"
JUEGO = "juego"
ODS = "ods"
INSTRUCCIONES = "instrucciones"
PAUSA = "pausa"
FINAL = "final"
VICTORIA = "victoria"

estado = MENU

# ============================================================
# DATOS DE LA PARTIDA
# ============================================================

hora = 1
presupuesto = 100000

desarrollo = 50
tecnologia = 50
medio_ambiente = 50
bienestar = 50

puntos = 0
acciones_realizadas = 0

mensaje = "La ciudad necesita tu ayuda."

evento_actual = None
opciones_evento = []

# ============================================================
# JUGADOR
# ============================================================

jugador = pygame.Rect(470, 390, 35, 35)

velocidad = 5

# ============================================================
# ZONAS DE LA CIUDAD
# ============================================================

parque = pygame.Rect(100, 150, 180, 110)
panel_solar = pygame.Rect(400, 130, 180, 90)
centro_tecnologia = pygame.Rect(700, 140, 180, 100)
zona_reciclaje = pygame.Rect(690, 350, 180, 100)
fuente_agua = pygame.Rect(110, 360, 160, 100)

# ============================================================
# BOTONES
# ============================================================

boton_jugar = pygame.Rect(350, 250, 300, 65)
boton_ods = pygame.Rect(350, 330, 300, 65)
boton_instrucciones = pygame.Rect(350, 410, 300, 65)
boton_salir = pygame.Rect(350, 490, 300, 55)

boton_evento_1 = pygame.Rect(170, 450, 250, 60)
boton_evento_2 = pygame.Rect(470, 450, 250, 60)

boton_volver = pygame.Rect(30, 530, 180, 45)

# ============================================================
# FUNCIONES GENERALES
# ============================================================

def texto(texto, fuente, color, x, y, centro=False):
    superficie = fuente.render(texto, True, color)

    if centro:
        rect = superficie.get_rect(center=(x, y))
    else:
        rect = superficie.get_rect(topleft=(x, y))

    pantalla.blit(superficie, rect)


def dibujar_boton(rect, texto_boton, color=VERDE):
    pygame.draw.rect(pantalla, color, rect, border_radius=12)
    pygame.draw.rect(pantalla, BLANCO, rect, 2, border_radius=12)

    texto(
        texto_boton,
        fuente_normal,
        NEGRO,
        rect.centerx,
        rect.centery,
        True
    )


def reiniciar_partida():
    global hora
    global presupuesto
    global desarrollo
    global tecnologia
    global medio_ambiente
    global bienestar
    global puntos
    global acciones_realizadas
    global mensaje
    global evento_actual
    global opciones_evento

    hora = 1
    presupuesto = 100000

    desarrollo = 50
    tecnologia = 50
    medio_ambiente = 50
    bienestar = 50

    puntos = 0
    acciones_realizadas = 0

    mensaje = "La ciudad necesita tu ayuda."

    evento_actual = None
    opciones_evento = []

    jugador.x = 470
    jugador.y = 390


# ============================================================
# ESTADÍSTICAS
# ============================================================

def limitar_estadisticas():
    global desarrollo
    global tecnologia
    global medio_ambiente
    global bienestar

    desarrollo = max(0, min(100, desarrollo))
    tecnologia = max(0, min(100, tecnologia))
    medio_ambiente = max(0, min(100, medio_ambiente))
    bienestar = max(0, min(100, bienestar))


def promedio_ciudad():
    return (
        desarrollo +
        tecnologia +
        medio_ambiente +
        bienestar
    ) // 4


# ============================================================
# EVENTOS
# ============================================================

def crear_evento():
    global evento_actual
    global opciones_evento

    eventos = [
        {
            "titulo": "Fallo en el sistema eléctrico",
            "descripcion": "Una zona de la ciudad quedó sin energía.",
            "opcion1": "Instalar tecnología",
            "opcion2": "Ahorrar presupuesto",
            "costo1": 18000,
            "costo2": 0,
            "efecto1": "tech",
            "efecto2": "bienestar"
        },
        {
            "titulo": "Parque abandonado",
            "descripcion": "Los habitantes piden recuperar una zona verde.",
            "opcion1": "Recuperar el parque",
            "opcion2": "No intervenir",
            "costo1": 12000,
            "costo2": 0,
            "efecto1": "ambiente",
            "efecto2": "desarrollo"
        },
        {
            "titulo": "Problema con el agua",
            "descripcion": "Se detectó un desperdicio importante de agua.",
            "opcion1": "Reparar tuberías",
            "opcion2": "Esperar",
            "costo1": 15000,
            "costo2": 0,
            "efecto1": "ambiente",
            "efecto2": "bienestar"
        },
        {
            "titulo": "Nueva oportunidad tecnológica",
            "descripcion": "Una empresa ofrece instalar sensores inteligentes.",
            "opcion1": "Aceptar proyecto",
            "opcion2": "Rechazar",
            "costo1": 20000,
            "costo2": 0,
            "efecto1": "tech",
            "efecto2": "desarrollo"
        }
    ]

    evento_actual = random.choice(eventos)

    opciones_evento = [
        evento_actual["opcion1"],
        evento_actual["opcion2"]
    ]


def aplicar_evento(opcion):
    global presupuesto
    global desarrollo
    global tecnologia
    global medio_ambiente
    global bienestar
    global puntos
    global acciones_realizadas
    global mensaje
    global evento_actual

    if evento_actual is None:
        return

    if opcion == 1:

        costo = evento_actual["costo1"]

        if presupuesto < costo:
            mensaje = "No tienes suficiente presupuesto."
            return

        presupuesto -= costo

        efecto = evento_actual["efecto1"]

        if efecto == "tech":
            tecnologia += 12
            bienestar += 5
            mensaje = "La tecnología de la ciudad mejoró."

        elif efecto == "ambiente":
            medio_ambiente += 15
            bienestar += 8
            mensaje = "El medio ambiente mejoró."

        elif efecto == "bienestar":
            bienestar += 15
            mensaje = "El bienestar ciudadano mejoró."

        elif efecto == "desarrollo":
            desarrollo += 15
            mensaje = "El desarrollo de la ciudad mejoró."

        puntos += 20

    else:

        efecto = evento_actual["efecto2"]

        if efecto == "tech":
            tecnologia -= 8
            mensaje = "La ciudad perdió oportunidades tecnológicas."

        elif efecto == "ambiente":
            medio_ambiente -= 10
            mensaje = "El medio ambiente empeoró."

        elif efecto == "bienestar":
            bienestar -= 8
            mensaje = "El bienestar ciudadano disminuyó."

        elif efecto == "desarrollo":
            desarrollo -= 8
            mensaje = "El desarrollo de la ciudad se frenó."

        puntos += 5

    acciones_realizadas += 1

    limitar_estadisticas()

    evento_actual = None


# ============================================================
# CIUDAD
# ============================================================

def dibujar_ciudad():

    # Fondo
    pantalla.fill(FONDO)

    # Carreteras
    pygame.draw.rect(
        pantalla,
        GRIS_OSCURO,
        (0, 280, ANCHO, 100)
    )

    pygame.draw.rect(
        pantalla,
        GRIS_OSCURO,
        (300, 80, 100, 520)
    )

    # Líneas de carretera
    for x in range(0, ANCHO, 80):
        pygame.draw.rect(
            pantalla,
            AMARILLO,
            (x, 325, 45, 6)
        )

    # Parque
    pygame.draw.rect(
        pantalla,
        VERDE_OSCURO,
        parque,
        border_radius=10
    )

    texto(
        "PARQUE",
        fuente_normal,
        BLANCO,
        parque.centerx,
        parque.y + 15,
        True
    )

    # Árboles
    for x, y in [
        (130, 200),
        (180, 220),
        (230, 190),
        (150, 245),
        (250, 235)
    ]:
        pygame.draw.circle(
            pantalla,
            VERDE,
            (x, y),
            15
        )

    # Panel solar
    pygame.draw.rect(
        pantalla,
        AZUL_OSCURO,
        panel_solar,
        border_radius=8
    )

    pygame.draw.rect(
        pantalla,
        CYAN,
        (425, 150, 130, 50),
        2
    )

    texto(
        "ENERGÍA SOLAR",
        fuente_pequena,
        BLANCO,
        panel_solar.centerx,
        115,
        True
    )

    # Centro tecnológico
    pygame.draw.rect(
        pantalla,
        MORADO,
        centro_tecnologia,
        border_radius=10
    )

    texto(
        "CENTRO",
        fuente_normal,
        BLANCO,
        centro_tecnologia.centerx,
        centro_tecnologia.y + 25,
        True
    )

    texto(
        "TECNOLÓGICO",
        fuente_pequena,
        BLANCO,
        centro_tecnologia.centerx,
        centro_tecnologia.y + 55,
        True
    )

    # Reciclaje
    pygame.draw.rect(
        pantalla,
        VERDE,
        zona_reciclaje,
        border_radius=10
    )

    texto(
        "RECICLAJE",
        fuente_normal,
        NEGRO,
        zona_reciclaje.centerx,
        zona_reciclaje.centery,
        True
    )

    # Agua
    pygame.draw.rect(
        pantalla,
        AZUL,
        fuente_agua,
        border_radius=10
    )

    texto(
        "AGUA",
        fuente_normal,
        BLANCO,
        fuente_agua.centerx,
        fuente_agua.centery,
        True
    )

    # Edificios
    edificios = [
        (50, 80, 100, 60),
        (600, 70, 70, 80),
        (800, 80, 80, 50),
        (50, 500, 100, 50),
        (800, 500, 120, 50)
    ]

    for edificio in edificios:
        pygame.draw.rect(
            pantalla,
            (55, 60, 80),
            edificio,
            border_radius=5
        )

    # Jugador
    pygame.draw.rect(
        pantalla,
        AMARILLO,
        jugador,
        border_radius=8
    )

    # Panel superior
    pygame.draw.rect(
        pantalla,
        NEGRO,
        (0, 0, ANCHO, 70)
    )

    texto(
        f"HORA {hora}/24",
        fuente_mediana,
        BLANCO,
        25,
        18
    )

    texto(
        f"${presupuesto:,}",
        fuente_mediana,
        VERDE,
        190,
        18
    )

    texto(
        f"PUNTOS: {puntos}",
        fuente_mediana,
        AMARILLO,
        390,
        18
    )

    texto(
        f"ESTADO: {promedio_ciudad()}%",
        fuente_mediana,
        CYAN,
        620,
        18
    )


# ============================================================
# BARRAS DE ESTADÍSTICAS
# ============================================================

def barra_estadistica(nombre, valor, x, y, color):

    texto(
        f"{nombre}: {valor}%",
        fuente_pequena,
        BLANCO,
        x,
        y
    )

    pygame.draw.rect(
        pantalla,
        GRIS_OSCURO,
        (x, y + 23, 150, 12),
        border_radius=5
    )

    pygame.draw.rect(
        pantalla,
        color,
        (x, y + 23, int(150 * valor / 100), 12),
        border_radius=5
    )


def dibujar_estadisticas():

    pygame.draw.rect(
        pantalla,
        NEGRO,
        (15, 90, 175, 250),
        border_radius=10
    )

    texto(
        "CIUDAD",
        fuente_mediana,
        BLANCO,
        30,
        105
    )

    barra_estadistica(
        "Desarrollo",
        desarrollo,
        30,
        150,
        AMARILLO
    )

    barra_estadistica(
        "Tecnología",
        tecnologia,
        30,
        205,
        MORADO
    )

    barra_estadistica(
        "Ambiente",
        medio_ambiente,
        30,
        260,
        VERDE
    )

    barra_estadistica(
        "Bienestar",
        bienestar,
        30,
        315,
        CYAN
    )


# ============================================================
# EVENTO EN PANTALLA
# ============================================================

def dibujar_evento():

    if evento_actual is None:
        return

    # Fondo oscuro
    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(210)
    overlay.fill(NEGRO)

    pantalla.blit(overlay, (0, 0))

    caja = pygame.Rect(
        100,
        110,
        800,
        400
    )

    pygame.draw.rect(
        pantalla,
        (30, 35, 50),
        caja,
        border_radius=15
    )

    pygame.draw.rect(
        pantalla,
        CYAN,
        caja,
        3,
        border_radius=15
    )

    texto(
        evento_actual["titulo"],
        fuente_grande,
        CYAN,
        500,
        160,
        True
    )

    texto(
        evento_actual["descripcion"],
        fuente_normal,
        BLANCO,
        500,
        220,
        True
    )

    dibujar_boton(
        boton_evento_1,
        evento_actual["opcion1"],
        VERDE
    )

    dibujar_boton(
        boton_evento_2,
        evento_actual["opcion2"],
        ROJO
    )


# ============================================================
# PANTALLA DEL JUEGO
# ============================================================

def dibujar_juego():

    dibujar_ciudad()
    dibujar_estadisticas()

    # Mensaje
    pygame.draw.rect(
        pantalla,
        NEGRO,
        (220, 520, 750, 55),
        border_radius=10
    )

    texto(
        mensaje,
        fuente_pequena,
        BLANCO,
        240,
        538
    )

    # Ayuda
    texto(
        "WASD: mover | E: interactuar | ESC: pausa",
        fuente_pequena,
        GRIS,
        25,
        570
    )

    # Evento
    dibujar_evento()


# ============================================================
# MENÚ
# ============================================================

def dibujar_menu():

    pantalla.fill(FONDO)

    # Decoración
    for x in range(0, ANCHO, 50):
        pygame.draw.line(
            pantalla,
            (25, 30, 45),
            (x, 0),
            (x, ALTO)
        )

    for y in range(0, ALTO, 50):
        pygame.draw.line(
            pantalla,
            (25, 30, 45),
            (0, y),
            (ANCHO, y)
        )

    texto(
        "NEON CITY",
        fuente_titulo,
        CYAN,
        500,
        100,
        True
    )

    texto(
        "24 HORAS",
        fuente_grande,
        VERDE,
        500,
        155,
        True
    )

    texto(
        "Construye una ciudad sostenible",
        fuente_normal,
        GRIS,
        500,
        195,
        True
    )

    dibujar_boton(
        boton_jugar,
        "JUGAR",
        VERDE
    )

    dibujar_boton(
        boton_ods,
        "ODS",
        AZUL
    )

    dibujar_boton(
        boton_instrucciones,
        "INSTRUCCIONES",
        MORADO
    )

    dibujar_boton(
        boton_salir,
        "SALIR",
        ROJO
    )


# ============================================================
# PANTALLA ODS
# ============================================================

def dibujar_ods():

    pantalla.fill(FONDO)

    texto(
        "OBJETIVOS DE DESARROLLO SOSTENIBLE",
        fuente_grande,
        CYAN,
        500,
        55,
        True
    )

    ods = [
        ("ODS 3", "Salud y bienestar", VERDE),
        ("ODS 4", "Educación de calidad", AZUL),
        ("ODS 6", "Agua limpia", CYAN),
        ("ODS 7", "Energía limpia", AMARILLO),
        ("ODS 9", "Innovación y tecnología", MORADO),
        ("ODS 11", "Ciudades sostenibles", VERDE),
        ("ODS 12", "Producción responsable", NARANJA),
        ("ODS 13", "Acción por el clima", VERDE)
    ]

    posiciones = [
        (100, 140),
        (350, 140),
        (600, 140),
        (100, 270),
        (350, 270),
        (600, 270),
        (225, 400),
        (475, 400)
    ]

    for i in range(len(ods)):

        numero, nombre, color = ods[i]

        x, y = posiciones[i]

        caja = pygame.Rect(
            x,
            y,
            200,
            95
        )

        pygame.draw.rect(
            pantalla,
            (30, 35, 50),
            caja,
            border_radius=10
        )

        pygame.draw.rect(
            pantalla,
            color,
            caja,
            2,
            border_radius=10
        )

        texto(
            numero,
            fuente_mediana,
            color,
            x + 15,
            y + 15
        )

        texto(
            nombre,
            fuente_pequena,
            BLANCO,
            x + 15,
            y + 55
        )

    dibujar_boton(
        boton_volver,
        "VOLVER",
        ROJO
    )


# ============================================================
# INSTRUCCIONES
# ============================================================

def dibujar_instrucciones():

    pantalla.fill(FONDO)

    texto(
        "INSTRUCCIONES",
        fuente_titulo,
        CYAN,
        500,
        70,
        True
    )

    instrucciones = [
        "WASD  →  Mover al personaje",
        "E     →  Interactuar con la ciudad",
        "ESC   →  Pausar el juego",
        "",
        "Durante 24 horas deberás tomar decisiones.",
        "Cada decisión afecta el desarrollo de la ciudad.",
        "",
        "Administra el presupuesto.",
        "Mejora la tecnología.",
        "Protege el medio ambiente.",
        "Aumenta el bienestar ciudadano.",
        "",
        "Tu objetivo es conseguir una ciudad sostenible."
    ]

    y = 150

    for linea in instrucciones:

        texto(
            linea,
            fuente_normal,
            BLANCO,
            500,
            y,
            True
        )

        y += 30

    dibujar_boton(
        boton_volver,
        "VOLVER",
        ROJO
    )


# ============================================================
# PAUSA
# ============================================================

def dibujar_pausa():

    dibujar_juego()

    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(220)
    overlay.fill(NEGRO)

    pantalla.blit(
        overlay,
        (0, 0)
    )

    texto(
        "PAUSA",
        fuente_titulo,
        CYAN,
        500,
        180,
        True
    )

    texto(
        "Presiona ESC para continuar",
        fuente_normal,
        BLANCO,
        500,
        260,
        True
    )

    texto(
        "Presiona M para volver al menú",
        fuente_normal,
        GRIS,
        500,
        300,
        True
    )


# ============================================================
# FINAL
# ============================================================

def dibujar_final():

    pantalla.fill(FONDO)

    promedio = promedio_ciudad()

    texto(
        "24 HORAS COMPLETADAS",
        fuente_titulo,
        CYAN,
        500,
        80,
        True
    )

    texto(
        f"Estado final de la ciudad: {promedio}%",
        fuente_grande,
        VERDE,
        500,
        160,
        True
    )

    texto(
        f"Puntuación: {puntos}",
        fuente_mediana,
        AMARILLO,
        500,
        220,
        True
    )

    texto(
        f"Presupuesto restante: ${presupuesto:,}",
        fuente_normal,
        BLANCO,
        500,
        260,
        True
    )

    texto(
        f"Desarrollo: {desarrollo}%",
        fuente_normal,
        BLANCO,
        500,
        310,
        True
    )

    texto(
        f"Tecnología: {tecnologia}%",
        fuente_normal,
        BLANCO,
        500,
        345,
        True
    )

    texto(
        f"Medio ambiente: {medio_ambiente}%",
        fuente_normal,
        BLANCO,
        500,
        380,
        True
    )

    texto(
        f"Bienestar: {bienestar}%",
        fuente_normal,
        BLANCO,
        500,
        415,
        True
    )

    if promedio >= 70:

        texto(
            "¡MISIÓN COMPLETADA!",
            fuente_grande,
            VERDE,
            500,
            470,
            True
        )

    else:

        texto(
            "La ciudad necesita seguir mejorando.",
            fuente_normal,
            NARANJA,
            500,
            470,
            True
        )

    dibujar_boton(
        boton_volver,
        "MENÚ PRINCIPAL",
        AZUL
    )


# ============================================================
# MOVIMIENTO
# ============================================================

def mover_jugador(teclas):

    if evento_actual is not None:
        return

    dx = 0
    dy = 0

    if teclas[pygame.K_w]:
        dy -= velocidad

    if teclas[pygame.K_s]:
        dy += velocidad

    if teclas[pygame.K_a]:
        dx -= velocidad

    if teclas[pygame.K_d]:
        dx += velocidad

    jugador.x += dx
    jugador.y += dy

    # Límites
    if jugador.left < 0:
        jugador.left = 0

    if jugador.right > ANCHO:
        jugador.right = ANCHO

    if jugador.top < 75:
        jugador.top = 75

    if jugador.bottom > ALTO:
        jugador.bottom = ALTO


# ============================================================
# INTERACCIÓN
# ============================================================
def interactuar():
    global mensaje
    global puntos
    global medio_ambiente
    global tecnologia
    global bienestar
    global desarrollo
    global presupuesto
    zonas = [
        (parque, "Parque", "Recuperar el parque mejora el ambiente."),
        (panel_solar, "Panel solar", "La energía limpia mejora la tecnología."),
        (centro_tecnologia, "Centro tecnológico", "La innovación impulsa el desarrollo."),
        (zona_reciclaje, "Reciclaje", "Reciclar mejora el medio ambiente."),
        (fuente_agua, "Agua", "Cuidar el agua mejora el bienestar.")
    ]

    for zona, nombre, descripcion in zonas:
        if jugador.colliderect(zona):
            if nombre == "Parque":
                medio_ambiente += 5
                bienestar += 3
                puntos += 5
                mensaje = descripcion

            elif nombre == "Panel solar":
                tecnologia += 5
                medio_ambiente += 5
                puntos += 5
                mensaje = descripcion

            elif nombre == "Centro tecnológico":
                tecnologia += 6
                desarrollo += 5
                puntos += 5
                mensaje = descripcion

            elif nombre == "Reciclaje":
                medio_ambiente += 7
                puntos += 5
                mensaje = descripcion

            elif nombre == "Agua":
                bienestar += 6
                medio_ambiente += 4
                puntos += 5
                mensaje = descripcion
            limitar_estadisticas()
            return
    mensaje = "No hay nada para interactuar aquí."


# ============================================================
# AVANZAR HORA
# ============================================================
def avanzar_hora():
    global hora
    global mensaje
    global evento_actual
    if evento_actual is not None:
        return
    hora += 1
    if hora > 24:
        cambiar_estado(FINAL)
        return
    # Cada hora aparece un evento
    crear_evento()
    mensaje = "Ha comenzado una nueva hora."


# ============================================================
# CAMBIO DE ESTADO
# ============================================================
def cambiar_estado(nuevo_estado):
    global estado
    estado = nuevo_estado


# ============================================================
# BUCLE PRINCIPAL
# ============================================================
ejecutando = True
while ejecutando:
    reloj.tick(60)
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        # ====================================================
        # MENÚ
        # ====================================================
        elif estado == MENU:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    reiniciar_partida()
                    cambiar_estado(JUEGO)
                elif boton_ods.collidepoint(evento.pos):
                    cambiar_estado(ODS)
                elif boton_instrucciones.collidepoint(evento.pos):
                    cambiar_estado(INSTRUCCIONES)
                elif boton_salir.collidepoint(evento.pos):
                    ejecutando = False

        # ====================================================
        # JUEGO
        # ====================================================
        elif estado == JUEGO:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    cambiar_estado(PAUSA)
                elif evento.key == pygame.K_e:
                    if evento_actual is None:
                        interactuar()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento_actual is not None:
                    if boton_evento_1.collidepoint(evento.pos):
                        aplicar_evento(1)
                        avanzar_hora()
                    elif boton_evento_2.collidepoint(evento.pos):
                        aplicar_evento(2)
                        avanzar_hora()

        # ====================================================
        # PAUSA
        # ====================================================
        elif estado == PAUSA:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    cambiar_estado(JUEGO)
                elif evento.key == pygame.K_m:
                    cambiar_estado(MENU)

        # ====================================================
        # ODS
        # ====================================================
        elif estado == ODS:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.collidepoint(evento.pos):
                    cambiar_estado(MENU)

        # ====================================================
        # INSTRUCCIONES
        # ====================================================
        elif estado == INSTRUCCIONES:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.collidepoint(evento.pos):
                    cambiar_estado(MENU)

        # ====================================================
        # FINAL
        # ====================================================
        elif estado == FINAL:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.collidepoint(evento.pos):
                    cambiar_estado(MENU)

    # ========================================================
    # ACTUALIZACIÓN
    # ========================================================
    if estado == JUEGO:
        teclas = pygame.key.get_pressed()
        mover_jugador(teclas)

    # ========================================================
    # DIBUJADO
    # ========================================================
    if estado == MENU:
        dibujar_menu()
    elif estado == JUEGO:
        dibujar_juego()
    elif estado == PAUSA:
        dibujar_pausa()
    elif estado == ODS:
        dibujar_ods()
    elif estado == INSTRUCCIONES:
         dibujar_instrucciones()
    elif estado == FINAL:
        dibujar_final()
    pygame.display.flip()

# ============================================================
# CERRAR
# ============================================================
pygame.quit()
sys.exit()