import os
import json

import Characters as Char

#Save Route
SVFILE = ""

#Player Save
def plyr_save(MC):
    dicc = {
    "tipoMC": type(MC).__name__[:3],
    "nivelMC": MC.get_lv(),
    "xpMC": MC.get_xp(),
    "pvMC": MC.get_bsStatByKey("PV"),
    "defMC": MC.get_bsStatByKey("DEF"),
    "esqMC": MC.get_bsStatByKey("ESQ"),
    "atkMC": MC.get_bsStatByKey("ATK"),
    "danMC": MC.get_bsStatByKey("DAN"),
    "vlcMC": MC.get_bsStatByKey("VLC"),
    "srtMC": MC.get_bsStatByKey("SRT")
    }
    guardar_file(SVFILE + "plyr.json",dicc)
def plyr_load():
    dicc = cargar_file(SVFILE + "plyr.json")
    if dicc:
        MC = getattr(Char,dicc["tipoMC"] + "DmnManifest")(1)
        MC.set_lv(dicc["nivelMC"])
        MC.set_xp(dicc["xpMC"])
        MC.set_bsStatByKey("PV",dicc["pvMC"])
        MC.set_bsStatByKey("DEF",dicc["defMC"])
        MC.set_bsStatByKey("ESQ",dicc["esqMC"])
        MC.set_bsStatByKey("ATK",dicc["atkMC"])
        MC.set_bsStatByKey("DAN",dicc["danMC"])
        MC.set_bsStatByKey("VLC",dicc["vlcMC"])
        MC.set_bsStatByKey("SRT",dicc["srtMC"])
        return MC
    return None

# Stage Save
def stg_save(Stage, Diff):
     dicc = {
        "jefesCant": Stage.jefesderrotados,
        "espinaFlag":Stage.flag_espina,
        "espinaDif": Diff["Spn"],
        "serpicoFlag": Stage.flag_serpico,
        "serpicoDif": Diff["Fn"],
        "corvusFlag": Stage.flag_corvus,
        "corvusDif": Diff["Pss"],
        "galaadFlag": Stage.flag_galaad,
        "galaadDif": Diff["Fnl"],
        "missFlag": Stage.flag_misionero,
        "missDif": Diff["Miss"]
     }
     guardar_file(SVFILE + "stage.json",dicc)
def stg_load(Stage, Diff):
    dicc = cargar_file(SVFILE + "stage.json")
    if dicc:
        Stage.jefesderrotados = dicc["jefesCant"] 
        Stage.flag_espina = dicc["espinaFlag"] 
        Diff["Spn"] = dicc["espinaDif"] 
        Stage.flag_serpico = dicc["serpicoFlag"] 
        Diff["Fn"] = dicc["serpicoDif"] 
        Stage.flag_corvus = dicc["corvusFlag"] 
        Diff["Pss"] = dicc["corvusDif"] 
        Stage.flag_galaad = dicc["galaadFlag"] 
        Diff["Fnl"] = dicc["galaadDif"] 
        Stage.flag_misionero = dicc["missFlag"] 
        Diff["Miss"] = dicc["missDif"]
    pass

# Collection Save
# Endings Save
# Settings Save


#General Load and Save Functions
def cargar_file(file):
        if os.path.exists(file):
            with open(file, "r") as f:
                return json.load(f)
        return None
def guardar_file(file,dicc):
    with open(file, "w") as f:
        json.dump(dicc, f)
