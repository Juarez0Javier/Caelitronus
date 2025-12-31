extends Control

@onready var fondo = $fondo
@onready var cuadro = $Cuadro
@onready var texto = $Cuadro/Texto

@onready var btnsi = $HBox/btnsi
@onready var btnno = $HBox/btnno

@onready var musica = $MusicaSalir
@onready var hover_sound = $HoverSound
@onready var label_final = $LabelFinal

const FONT_NORMAL := 56
const FONT_HOVER := 40
const COLOR_NORMAL := Color("#f8f5cb")
const COLOR_HOVER := Color("#afad95")

var estado := 0
var esperando_input := false

func _ready():
	texto.text = "estas seguro???"
	label_final.visible = false

	btnsi.mouse_entered.connect(func(): _on_hover(btnsi))
	btnsi.mouse_exited.connect(func(): _on_hover_exit(btnsi))
	btnno.mouse_entered.connect(func(): _on_hover(btnno))
	btnno.mouse_exited.connect(func(): _on_hover_exit(btnno))

func _on_hover(btn: Button):
	btn.add_theme_font_size_override("font_size", FONT_HOVER)
	btn.add_theme_color_override("font_color", COLOR_HOVER)
	btn.scale = Vector2(0.9, 0.9)

	if hover_sound:
		hover_sound.play()

func _on_hover_exit(btn: Button):
	btn.add_theme_font_size_override("font_size", FONT_NORMAL)
	btn.add_theme_color_override("font_color", COLOR_NORMAL)
	btn.scale = Vector2.ONE

func _on_btnsi_pressed():
	estado += 1
	saturar_musica()

	match estado:
		1:
			texto.text = "seguro????????"
			btnsi.scale = Vector2(0.7, 0.7)
			btnno.scale = Vector2(1.2, 1.2)
			fondo.modulate = Color("#200000")

		2:
			fondo.modulate = Color.BLACK
			cuadro.visible = false
			musica.stop()

			label_final.text = "no eres digno de luchar por en 
			el conclave marica"
			label_final.visible = true

			await get_tree().create_timer(4.0).timeout
			get_tree().quit()

func _on_btnno_pressed():
	cuadro.visible = false
	label_final.text = "eso ve toma el trono a la fuerza"
	label_final.visible = true
	esperando_input = true

func saturar_musica():
	var bus := AudioServer.get_bus_index("Music")
	if bus == -1:
		return

	var vol := AudioServer.get_bus_volume_db(bus)
	AudioServer.set_bus_volume_db(bus, vol + 4)

# -------------------------
# VOLVER AL MENU
# -------------------------
func _input(event):
	if esperando_input and (
		event.is_action_pressed("ui_accept")
		or event is InputEventMouseButton
	):
		get_tree().change_scene_to_file("res://scenes/menu_principal.tscn")
