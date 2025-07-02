import random
import asyncio

##Limites superiores y menores
RANDATKUP = 20
RANDATKLOW = 1

RANDDMGUP = 4
RANDDMGLOW = 1

#Liimites minimos
BASETOHIT = 10
BASETOLUCK = 10

#Multiplicadores
CRITMULT = 2

#Blueprints de Niveles de Manifestacion
ATKDMN_LV = [
{"StartLv": 1, "EndLv":5},
{"MaxHP": 15, "DEF": 0, "EVS": 1, "ATK": 4, "DAN": 3, "VLC": 1, "SRT": 0},
{"MaxHP": 5, "DEF": 0, "EVS": 0, "ATK": 1, "DAN": 0, "VLC": 0, "SRT": 1},
{"MaxHP": 0, "DEF": 0, "EVS": 0, "ATK": 1, "DAN": 1, "VLC": 1, "SRT": 0},
{"MaxHP": 5, "DEF": 0, "EVS": 1, "ATK": 1, "DAN": 0, "VLC": 0, "SRT": 0},
{"MaxHP": 0, "DEF": 0, "EVS": 1, "ATK": 0, "DAN": 1, "VLC": 1, "SRT": 1}
]
DEFDMN_LV = [
{"StartLv": 1, "EndLv":5},
{"MaxHP": 20, "DEF": 3, "EVS": 2, "ATK": 2, "DAN": 0, "VLC": 0, "SRT": 1},
{"MaxHP": 5, "DEF": 1, "EVS": 0, "ATK": 1, "DAN": 0, "VLC": 0, "SRT": 0},
{"MaxHP": 5, "DEF": 0, "EVS": 1, "ATK": 0, "DAN": 1, "VLC": 0, "SRT": 0},
{"MaxHP": 0, "DEF": 1, "EVS": 1, "ATK": 0, "DAN": 0, "VLC": 0, "SRT": 1},
{"MaxHP": 5, "DEF": 0, "EVS": 1, "ATK": 0, "DAN": 0, "VLC": 1, "SRT": 0}
]
LCKDMN_LV = [
{"StartLv": 1, "EndLv":5},
{"MaxHP": 15, "DEF": 0, "EVS": 4, "ATK": 1, "DAN": 1, "VLC": 2, "SRT": 1},
{"MaxHP": 0, "DEF": 0, "EVS": 1, "ATK": 1, "DAN": 0, "VLC": 0, "SRT": 1},
{"MaxHP": 0, "DEF": 0, "EVS": 1, "ATK": 1, "DAN": 0, "VLC": 1, "SRT": 0},
{"MaxHP": 5, "DEF": 0, "EVS": 0, "ATK": 0, "DAN": 0, "VLC": 1, "SRT": 1},
{"MaxHP": 0, "DEF": 0, "EVS": 0, "ATK": 0, "DAN": 1, "VLC": 1, "SRT": 1}
]

HEALANG_LV = [
{"StartLv": 1, "EndLv": 3},
{"MaxHP": 15, "DEF": 0, "EVS": 2, "ATK": 1, "DAN": 0, "VLC": 2, "SRT": 2},
{"MaxHP": 0, "DEF": 1, "EVS": 1, "ATK": 0, "DAN": 0, "VLC": 0, "SRT": 1},
{"MaxHP": 0, "DEF": 0, "EVS": 1, "ATK": 1, "DAN": 0, "VLC": 1, "SRT": 0},
]
DRAINANG_LV = [
{"StartLv": 1, "EndLv": 3},
{"MaxHP": 15, "DEF": 0, "EVS": 1, "ATK": 0, "DAN": 3, "VLC": 1, "SRT": 2},
{"MaxHP": 0, "DEF": 0, "EVS": 1, "ATK": 1, "DAN": 0, "VLC": 0, "SRT": 1},
{"MaxHP": 5, "DEF": 0, "EVS": 0, "ATK": 0, "DAN": 1, "VLC": 1, "SRT": 0},
]
LAZANG_LV = [
{"MaxHP": 10, "DEF": 1, "EVS": 2, "ATK": 0, "DAN": 0, "VLC": 2, "SRT": 3},
{"MaxHP": 0, "DEF": 0, "EVS": 1, "ATK": 1, "DAN": 0, "VLC": 0, "SRT": 1},
{"MaxHP": 0, "DEF": 0, "EVS": 1, "ATK": 0, "DAN": 0, "VLC": 1, "SRT": 1},
{},
{}
]

SPNBOSS_LV = [
{"StartLv": 3, "EndLv": 5},
{"MaxHP": 25, "DEF": 2, "EVS": 3, "ATK": 3, "DAN": 3, "VLC": 2, "SRT": 2},
{"MaxHP": 0, "DEF": 0, "EVS": 0, "ATK": 1, "DAN": 0, "VLC": 1, "SRT": 1},
{"MaxHP": 5, "DEF": 1, "EVS": 0, "ATK": 1, "DAN": 0, "VLC": 1, "SRT": 0}
]
FNBOSS_LV = [
{"StartLv": 3, "EndLv": 5},
{"MaxHP": 20, "DEF": 0, "EVS": 1, "ATK": 4, "DAN": 3, "VLC": 1, "SRT": 0},
{"MaxHP": 5, "DEF": 0, "EVS": 0, "ATK": 1, "DAN": 0, "VLC": 0, "SRT": 1},
{"MaxHP": 0, "DEF": 0, "EVS": 0, "ATK": 1, "DAN": 1, "VLC": 1, "SRT": 0}
]
PSSBOSS_LV = [
{"StartLv": 3, "EndLv": 5},
{"MaxHP": 25, "DEF": 4, "EVS": 2, "ATK": 2, "DAN": 4, "VLC": 1, "SRT": 2},
{"MaxHP": 0, "DEF": 0, "EVS": 0, "ATK": 0, "DAN": 1, "VLC": 1, "SRT": 1},
{"MaxHP": 0, "DEF": 0, "EVS": 0, "ATK": 1, "DAN": 1, "VLC": 1, "SRT": 0}
]
FNLBOSS_LV = [
{"StartLv": 6, "EndLv": 6},
{"MaxHP": 35, "DEF": 3, "EVS": 4, "ATK": 4, "DAN": 5, "VLC": 3, "SRT": 3}
]

class Manifest:

    #Nombre y Sprite
    _name = None
    _sprite = None

    #Nivel y Experiencia
    _lv = 1
    _xp = 0

    #Opponente
    _opp = None

    #Blueprint de Nivel
    _lvBp = None

    _minLv = None
    _maxLv = None

    def __init__(self,lv):
        
        # Stats siendo Vida (hp), Vida Maxima (maxHp), Defensa (defn), Evasion (evd), Ataque (atk),
        # Daño (atkDmg), Velocidad (spd), y Suerte (luck)

        self._lv = self._lvBp[0]['StartLv']

        self._hp = self._lvBp[1]['MaxHP']
        self._maxHp = self._lvBp[1]['MaxHP']
        self._defn = self._lvBp[1]['DEF']
        self._evd = self._lvBp[1]['EVS']
        self._atk = self._lvBp[1]['ATK']
        self._atkDmg = self._lvBp[1]['DAN']
        self._spd = self._lvBp[1]['VLC']
        self._luck = self._lvBp[1]['SRT']

        effmxLv = lv 

        if effmxLv > self._lvBp[0]['EndLv']:
            effmxLv = self._lvBp[0]['EndLv']

        for i in range (self._lvBp[0]['StartLv'],effmxLv):
            self.lvUp()

    ##Funciones de Set y Get

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_sprite(self):
        return self._sprite
    def set_sprite(self, sprite):
        self._sprite = sprite
    
    def get_lv(self):
        return self._lv
    def set_lv(self, lv):
        self._lv = lv

    def get_xp(self):
        return self._xp
    def set_xp(self, xp):
        self._xp = xp
    
    def get_hp(self):
        return self._hp
    def set_hp(self, hp):
        self._hp = hp

    def get_maxHp(self):
        return self._maxHp
    def set_maxHp(self, maxHp):
        self._maxHp = maxHp     

    def get_defn(self):
        return self._defn
    def set_defn(self, defn):
        self._defn = defn   

    def get_evd(self):
        return self._evd
    def set_evd(self, evd):
        self._evd = evd 

    def get_atk(self):
        return self._atk
    def set_atk(self, atk):
        self._atk = atk

    def get_atkDmg(self):
        return self._atkDmg
    def set_atkDmg(self, atkDmg):
        self._atkDmg = atkDmg

    def get_spd(self):
        return self._spd
    def set_spd(self, spd):
        self._spd = spd

    def get_luck(self):
        return self._luck
    def set_luck(self, luck):
        self._luck = luck

    def get_opp(self):
        return self._opp
    def set_opp(self, opp):
        self._opp = opp

    ##Funciones de Atacar y Ser Atacado
    ##Las funciones siempre retornan los mensajes de acciones

    def act(self):
        if random.randrange(self.get_luck(),(BASETOLUCK + 1)) == BASETOLUCK:
            return self.callAbility()
        else:
            return self.attack()

    def attack (self):
        btlMssg = self.get_name()
        mult = 1
        if (random.randrange(RANDATKLOW,RANDATKUP) + self.get_atk()) >= (BASETOHIT + self.get_opp().get_evd()):
            #Animacion de Ataque - Golpea
            btlMssg+= " golpea a " + self.get_opp().get_name() + "."
            if random.randrange(self.get_luck(),(BASETOLUCK + 1)) >= BASETOLUCK:
                 mult = CRITMULT
                 btlMssg+= " Ataque Critico!"
            btlMssg+= "\n" + self.get_opp().takeDamage((random.randrange(RANDDMGLOW,RANDDMGUP) + self.get_atkDmg()) * mult)
        else:
            #Animacion de Ataque - Erra
            btlMssg+= " le erra a " + self.get_opp().get_name() + "."
        return btlMssg

    def takeDamage(self, dmg):
        rdDmg = dmg - self.get_defn()
        if(self.get_defn() > dmg ):
            rdDmg = 0
        btlMssg = self.get_name() + " recibe " + str(rdDmg) + " de daño."
        #Animacion de recibir daño
        if rdDmg >= self.get_hp():
            self.set_hp(0)
            btlMssg+= "\n" + self.death()
        else:
            self.set_hp(self.get_hp() - rdDmg) 
        return btlMssg
        
    def callAbility(self):
        return self.get_name()  + " usa su habilidad especial."
    
    def heal(self,heal):
        btlMssg = self.get_name() + " se cura "
        effHeal = self.get_maxHp() - self.get_hp()
        if heal >= effHeal:
            self.set_hp(self.get_hp() + effHeal)
            btlMssg += str(effHeal)
        else:
            self.set_hp(self.get_hp() + heal)
            btlMssg += str(heal)
        btlMssg += " de vida."
        return btlMssg

    def death(self):
        #Animacion Muerte
        return self.get_name() + " muere."
    
    def xpUp(self,xp):
        Mss = self.get_name() + " gana " + str(xp) + " puntos de experiencia."
        xpToLv = self.get_lv() * 10
        self.set_xp(self.get_xp() + xp)
        if self.get_xp() >= xpToLv:
            self.set_xp(self.get_xp() - xpToLv)
            Mss += self.lvUp()
        return Mss


    def lvUp(self):
        self.set_lv(self.get_lv() + 1)

        Offset = self.get_lv() - self._lvBp[0]['StartLv']  + 1

        self.set_maxHp(self.get_maxHp() + self._lvBp[Offset]['MaxHP'])
        self.set_hp(self.get_hp() + self._lvBp[Offset]['MaxHP'])
        self.set_defn(self.get_defn() + self._lvBp[Offset]['DEF'])
        self.set_evd(self.get_evd() + self._lvBp[Offset]['EVS'])
        self.set_atk(self.get_atk() + self._lvBp[Offset]['ATK'])
        self.set_atkDmg(self.get_atkDmg() + self._lvBp[Offset]['DAN'])
        self.set_spd(self.get_spd() + self._lvBp[Offset]['VLC'])
        self.set_luck(self.get_luck() + self._lvBp[Offset]['SRT'])

        return "\n" + self.get_name() + " sube a nivel " + str(self.get_lv()) + "!"

#Clases de Angeles

class HealManifest (Manifest):

    _name = "Angel Sagrado"
    _sprite =""

    _lvBp = HEALANG_LV

    def act(self):
        btlMssg = self.attack()
        if random.randrange(self.get_luck(),(BASETOLUCK + 1)) == BASETOLUCK:
            btlMssg += "\n" + self.callAbility()
        return btlMssg 

    def callAbility(self):
        heal = int(self.get_maxHp() * 0.25)
        return self.get_name()  + " usa su habilidad especial." + "\n" +  self.heal(heal)
    
class DrainManifest (Manifest):

    _name = "Angel Oscuro"
    _sprite =""

    _lvBp = DRAINANG_LV

    def callAbility(self):
        drainDmg = int (random.randrange(RANDDMGLOW,RANDDMGUP) * 2 + self.get_atkDmg())
        btlMssg = self.get_name()  + " usa su habilidad especial." + "\n"
        btlMssg += self.get_name() + " le absorbe vida a " + self.get_opp().get_name() + "."
        btlMssg += "\n" + self.get_opp().takeDamage(drainDmg)
        btlMssg += "\n" + self.heal(int(drainDmg * 0.5))
        return btlMssg

class LazManifest (Manifest):

    _name = "Angel Lazar"
    _sprite =""

    _lvBp = LAZANG_LV
    
    _abilityUse = 1

    def act(self):
        return self.attack()
    
    def death(self):
        btlMssg = self.get_name() + " muere."
        if self._abilityUse > 0:
            self._abilityUse -= 1
            btlMssg += "\n" + self.callAbility()
        return btlMssg
    
    def callAbility(self):
        btlMssg = ""
        rvHeal = int(random.randrange(self.get_luck(),((BASETOLUCK + 1))) * 0.75 * self.get_maxHp())
        btlMssg = self.get_name()  + " usa su habilidad especial." + "\n"
        btlMssg += self.get_name()  + " revive!" + "\n"
        btlMssg += self.heal(rvHeal)
        return btlMssg

#Clases de Demonio Principal

class AtkDmnManifest(Manifest):
    _name = "Fauste de Fe"
    _sprite =""

    _lvBp = ATKDMN_LV

    #Special BUff Ability
        #Calls a Buff Manager, that checks the time, and once its over, calls end

class DefDmnManifest(Manifest):
    _name = "Fauste de Fe"
    _sprite =""

    _lvBp = DEFDMN_LV

class LckDmnManifest(Manifest):
    _name = "Fauste de Fe"
    _sprite =""

    _lvBp = LCKDMN_LV

#Clases de Jefes

class SpnBossManifest(Manifest):
    _name = "Kamathra"
    _sprite =""

    _lvBp = SPNBOSS_LV

    def act(self):
        return self.attack()

    def takeDamage(self, dmg):
        rdDmg = dmg - self.get_defn()
        if(self.get_defn() > dmg ):
            rdDmg = 0
        btlMssg = self.get_name() + " recibe " + str(rdDmg) + " de daño."
        #Animacion de recibir daño
        if rdDmg >= self.get_hp():
            self.set_hp(0)
            btlMssg+= "\n" + self.death()
        else:
            self.set_hp(self.get_hp() - rdDmg) 
            if random.randrange(self.get_luck(),(BASETOLUCK + 1)) == BASETOLUCK:
                btlMssg += "\n" + self.callAbility()
        return btlMssg

    def callAbility (self):
        counterDmg = int (random.randrange(RANDDMGLOW,RANDDMGUP) * 2 + self.get_atkDmg())
        btlMssg = self.get_name()  + " usa su habilidad especial." + "\n"
        btlMssg += self.get_name() + " contrataca!"
        btlMssg += "\n" + self.get_opp().takeDamage(counterDmg)
        return btlMssg

class FnBossManifest(Manifest):
    _name = "Vahruksha"
    _sprite =""

    _lvBp = FNBOSS_LV

class PssBossDmnManifest(Manifest):
    _name = "Nzolukaya"
    _sprite =""

    _lvBp = PSSBOSS_LV

class FnlBossDmnManifest(Manifest):
    _name = "Eliadran"
    _sprite =""

    _lvBp = FNLBOSS_LV


M1 = AtkDmnManifest(5)
M2 = FnlBossDmnManifest(6)

M1.set_opp(M2)
M2.set_opp(M1)

i = 0
while M1.get_hp() > 0 and M2.get_hp() > 0:
    print("##################################")
    print(M1.act())
    print("----------------------------------")
    print(M2.act())
    print("----------------------------------")
    print(M1.get_name() + " le queda " + str(M1.get_hp()) + " de vida.")
    print(M2.get_name() + " le queda " + str(M2.get_hp()) + " de vida.")
    i+=1
print("Turnos Totales: " + str(i))
