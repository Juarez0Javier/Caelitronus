extends Control

@onready var video := $inicio
@onready var audio := $voces

func _ready():
	video.play()
	audio.play()

	video.finished.connect(_on_video_finished)

func _on_video_finished():
	get_tree().change_scene_to_file("res://scenes/juego.tscn")

func _input(event):
	# Saltear con espacio o click
	if event.is_action_pressed("ui_accept") or event is InputEventMouseButton:
		get_tree().change_scene_to_file("res://scenes/juego.tscn")
