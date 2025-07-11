# Caelitronus

**Caelitronus** es un juego de batallas automáticas desarrollado en Python con la librería Pygame. En él, los jugadores eligen un personaje único y se enfrentan a enemigos poderosos en un sistema de combate por turnos con estadísticas, habilidades y progresión de nivel.

---

##Estructura del Proyecto

El proyecto se compone de distintos módulos organizados por funcionalidad:

| Archivo        | Función Principal                                         |
|----------------|------------------------------------------------------------|
| `main.py`      | Punto de entrada. Coordina menús, progreso, niveles, audio, etc. |
| `Battle.py`    | Lógica del sistema de combate y renderización visual.     |
| `Characters.py`| Sistema de clases para personajes, enemigos, estadísticas y progresión. |
| `Levels.py`    | Gestión de secuencia de niveles y generación de enemigos. |
| `Menus.py`     | Menús interactivos del juego (inicio, selección, victoria, derrota, etc.). |
| `Button.py`    | Clase auxiliar para crear botones interactivos con Pygame. |

---

##Módulos y Funcionalidades

### `main.py`
Controla todo el flujo del juego: carga de recursos, configuración, cinemáticas, menús y bucle principal.

- `Game`: clase principal. Contiene métodos para cargar/guardar configuración y progreso, aplicar desenfoque, renderizar texto multilineal, reproducir cinemáticas y correr el juego.
- Menús integrados como clases anidadas:
  - `MenuScreen`, `AjustesScreen`, `ConfirmQuitScreen`, etc.

### `Battle.py`
Contiene la lógica de combate y animaciones.

- Clase `Battle`: gestiona batallas automáticas entre personajes, aplica animaciones, efectos, estadísticas, y control del flujo de combate.

### `Characters.py`
Define personajes jugables y enemigos, junto a su sistema de progresión.

- Clase base: `Manifest`
- Subclases de Ángeles:
  - `HealManifest`, `DrainManifest`, `LazManifest`
- Subclases de Fauste de Fe (jugadores):
  - `AtkDmnManifest`, `DefDmnManifest`, `LckDmnManifest`
- Jefes:
  - `SpnBossManifest`, `FnBossManifest`, `PssBossManifest`, `FnlBossManifest`

Incluye blueprint de niveles, progresión de experiencia, habilidades especiales, buffs, curaciones, muerte, ataques críticos, etc.

### `Levels.py`
Secuencia de niveles, selección aleatoria de enemigos y jefes, control de victoria/derrota.

- `Level`: ejecuta batallas en secuencia, genera enemigos, reproduce música según el tipo de enemigo y transiciona entre pantallas.

### `Menus.py`
Maneja todas las pantallas del juego.

- Menús:
  - `CharSelectScreen`: selección de personaje.
  - `LevelSelectScreen`: selección de nivel/jefe.
  - `WScreen`, `LScreen`, `GWScreen`: victoria, derrota, gran victoria.
  - `LvUpScreen`: mejora de estadísticas al subir de nivel.
  - `Creditos`, `Instruct`: créditos e instrucciones del juego.

Los menús están construidos sobre una clase base (`BinaryMenu`) con botones interactivos y lógica personalizada según el tipo de pantalla.

---

##Características Clave

- ✔️ Combate automático con lógica estratégica.
- ✔️ Selección de personajes con habilidades y estilos de juego únicos.
- ✔️ Progresión de niveles, experiencia y mejora de estadísticas.
- ✔️ Enemigos variados: ángeles con habilidades especiales y jefes demoníacos.
- ✔️ Menús interactivos con diseño visual personalizado.
- ✔️ Cinemáticas y efectos visuales/audio integrados.

---

##Requisitos

- Python 3.9+
- [Pygame](https://www.pygame.org/)
- [pygame_widgets](https://github.com/PygameCommunityFund/pygame-widgets)
- [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) (para cinemáticas)
- `moviepy` (si usás video, aunque puede ser opcional)

Instalación de dependencias:

```bash
pip install -r requirements.txt
