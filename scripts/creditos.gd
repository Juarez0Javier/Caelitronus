extends Control


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
