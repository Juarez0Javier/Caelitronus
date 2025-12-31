extends Control

@onready var btn_continuar = $menubotones/btncontinuar
@onready var botones = $menubotones.get_children()
@onready var hover_sound = $HoverSound

const FONT_NORMAL := 45
const FONT_HOVER := 35
const COLOR_NORMAL := Color("#251b07")
const COLOR_HOVER := Color("#f8f5cb")

func _ready():
	AudioSettings.aplicar()


	if hay_partida_guardada():
		btn_continuar.visible = true
	else:
		btn_continuar.visible = false

	for btn in botones:
		if btn is Button:
			btn.mouse_entered.connect(func(): _on_hover(btn))
			btn.mouse_exited.connect(func(): _on_hover_exit(btn))

func aplicar_audio():
	if not FileAccess.file_exists("user://settings.dat"):
		return

	var file = FileAccess.open("user://settings.dat", FileAccess.READ)
	var data: Dictionary = file.get_var()
	file.close()

	set_bus_volume("Music", data.get("music", 100))
	set_bus_volume("SFX", data.get("sfx", 100))
	set_bus_volume("Voces", data.get("voces", 100))

func set_bus_volume(bus_name: String, value: float):
	var bus := AudioServer.get_bus_index(bus_name)
	if bus == -1:
		push_warning("Bus no encontrado: " + bus_name)
		return

	AudioServer.set_bus_volume_db(
		bus,
		linear_to_db(value / 100.0)
	)

func _on_hover(btn: Button):
	btn.add_theme_font_size_override("font_size", FONT_HOVER)
	btn.add_theme_color_override("font_color", COLOR_HOVER)

	if hover_sound:
		hover_sound.play()

func _on_hover_exit(btn: Button):
	btn.add_theme_font_size_override("font_size", FONT_NORMAL)
	btn.add_theme_color_override("font_color", COLOR_NORMAL)

func hay_partida_guardada() -> bool:
	return FileAccess.file_exists("user://save.dat")

func _on_btncontinuar_pressed():
	get_tree().change_scene_to_file("res://scenes/juego.tscn")

func _on_bntcomenzar_pressed():
	if FileAccess.file_exists("user://save.dat"):
		DirAccess.remove_absolute("user://save.dat")
	get_tree().change_scene_to_file("res://scenes/juego.tscn")

func _on_bntajustes_pressed():
	get_tree().change_scene_to_file("res://scenes/ajustes.tscn")

func _on_btnglosario_pressed():
	get_tree().change_scene_to_file("res://scenes/glosario.tscn")

func _on_btncreditos_pressed():
	get_tree().change_scene_to_file("res://scenes/creditos.tscn")

func _on_btnsalir_pressed():
	get_tree().change_scene_to_file("res://scenes/salir.tscn")
