extends Control


func _ready():
	for button in get_tree().get_nodes_in_group("LinkPersonal"):
		button.pressed.connect(_on_link_pressed.bind(button.get_parent().name))


func _on_atras_pressed() -> void:
	get_tree().change_scene_to_file("res://scenes/menu_principal.tscn")


func _on_links_pressed() -> void:
	OS.shell_open("https://linktr.ee/ServentesioStudios")


func _on_button_der_pressed() -> void:
	$Tipo.text = "ACTORES DE VOZ"
	$ButtonDer.hide()
	$Desarrolladores.hide()
	$Voces.show()
	$ButtonIzq.show()


func _on_button_izq_pressed() -> void:
	$Tipo.text = "DESARROLLADORES"
	$ButtonIzq.hide()
	$Voces.hide()
	$ButtonDer.show()
	$Desarrolladores.show()


func _on_link_pressed(id) -> void:
	match id:
		"Javier":
			OS.shell_open("https://linktr.ee/ServentesioStudios")
		"Matias":
			OS.shell_open("https://linktr.ee/ServentesioStudios")
		"Adrian":
			OS.shell_open("https://linktr.ee/ServentesioStudios")
		"Matute":
			OS.shell_open("https://linktr.ee/ServentesioStudios")
		"Uriel":
			OS.shell_open("https://linktr.ee/ServentesioStudios")
		"Anto":
			OS.shell_open("https://linktr.ee/ServentesioStudios")
		"Lucio":
			OS.shell_open("https://linktr.ee/ServentesioStudios")
		"Thiago":
			OS.shell_open("https://linktr.ee/ServentesioStudios")
		"Joaquin":
			OS.shell_open("https://linktr.ee/ServentesioStudios")
		"Uriel":
			OS.shell_open("https://linktr.ee/ServentesioStudios")

			
func _on_link_mouse_entered() -> void:
	$HoverSound.play()
