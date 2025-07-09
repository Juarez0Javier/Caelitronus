import random
import asyncio

##Limites superiores y menores
RANDATKUP = 200
RANDATKLOW = 10

RANDDMGUP = 40
RANDDMGLOW = 10

#Liimites minimos
BASETOHIT = 100
BASETOLUCK = 100

#Multiplicadores
CRITMULT = 2

#Blueprints de Niveles de Manifestacion
ATKDMN_LV = [
{"StartLv": 1, "EndLv":5},
{"MaxHP": 150, "DEF": 0, "EVS": 10, "ATK": 40, "DAN": 30, "VLC": 10, "SRT": 10},
{"MaxHP": 50, "DEF": 0, "EVS": 0, "ATK": 10, "DAN": 00, "VLC": 0, "SRT": 10},
{"MaxHP": 00, "DEF": 0, "EVS": 0, "ATK": 10, "DAN": 10, "VLC": 10, "SRT": 0},
{"MaxHP": 50, "DEF": 0, "EVS": 10, "ATK": 10, "DAN": 0, "VLC": 0, "SRT": 0},
{"MaxHP": 00, "DEF": 0, "EVS": 10, "ATK": 0, "DAN": 10, "VLC": 10, "SRT": 10}
]
DEFDMN_LV = [
{"StartLv": 1, "EndLv":5},
{"MaxHP": 200, "DEF": 30, "EVS": 20, "ATK": 20, "DAN": 0, "VLC": 0, "SRT": 10},
{"MaxHP": 50, "DEF": 10, "EVS": 0, "ATK": 10, "DAN": 0, "VLC": 0, "SRT": 0},
{"MaxHP": 50, "DEF": 0, "EVS": 10, "ATK": 0, "DAN": 10, "VLC": 0, "SRT": 0},
{"MaxHP": 0, "DEF": 10, "EVS": 10, "ATK": 0, "DAN": 0, "VLC": 0, "SRT": 10},
{"MaxHP": 50, "DEF": 0, "EVS": 10, "ATK": 0, "DAN": 0, "VLC": 10, "SRT": 0}
]
LCKDMN_LV = [
{"StartLv": 1, "EndLv":5},
{"MaxHP": 150, "DEF": 0, "EVS":40, "ATK": 10, "DAN": 10, "VLC": 20, "SRT": 10},
{"MaxHP": 0, "DEF": 0, "EVS": 10, "ATK": 10, "DAN": 00, "VLC": 00, "SRT": 10},
{"MaxHP": 0, "DEF": 0, "EVS": 10, "ATK": 10, "DAN": 00, "VLC": 10, "SRT": 00},
{"MaxHP": 50, "DEF": 0, "EVS": 0, "ATK": 0, "DAN": 00, "VLC": 10, "SRT": 10},
{"MaxHP": 00, "DEF": 0, "EVS": 0, "ATK": 0, "DAN": 10, "VLC": 10, "SRT": 10}
]

HEALANG_LV = [
{"StartLv": 1, "EndLv": 3},
{"MaxHP": 150, "DEF": 0, "EVS": 20, "ATK": 10, "DAN": 0, "VLC": 20, "SRT": 20},
{"MaxHP": 0, "DEF": 10, "EVS": 10, "ATK": 0, "DAN": 0, "VLC": 0, "SRT": 10},
{"MaxHP": 0, "DEF": 0, "EVS": 10, "ATK": 10, "DAN": 0, "VLC": 10, "SRT": 0},
]
DRAINANG_LV = [
{"StartLv": 1, "EndLv": 3},
{"MaxHP": 150, "DEF": 0, "EVS": 10, "ATK": 0, "DAN": 30, "VLC": 10, "SRT": 20},
{"MaxHP": 0, "DEF": 0, "EVS": 10, "ATK": 10, "DAN": 0, "VLC": 0, "SRT": 10},
{"MaxHP": 50, "DEF": 0, "EVS": 0, "ATK": 0, "DAN": 10, "VLC": 10, "SRT": 0},
]
LAZANG_LV = [
{"StartLv": 1, "EndLv": 3},
{"MaxHP": 100, "DEF": 10, "EVS": 20, "ATK": 0, "DAN": 0, "VLC": 20, "SRT": 30},
{"MaxHP": 0, "DEF": 0, "EVS": 10, "ATK": 10, "DAN": 0, "VLC": 0, "SRT": 10},
{"MaxHP": 0, "DEF": 0, "EVS": 10, "ATK": 0, "DAN": 0, "VLC": 10, "SRT": 10}
]

SPNBOSS_LV = [
{"StartLv": 3, "EndLv": 5},
{"MaxHP": 250, "DEF": 20, "EVS": 30, "ATK": 30, "DAN": 30, "VLC": 20, "SRT": 20},
{"MaxHP": 0, "DEF": 0, "EVS": 0, "ATK": 10, "DAN": 0, "VLC": 10, "SRT": 1},
{"MaxHP": 50, "DEF": 10, "EVS": 0, "ATK": 10, "DAN": 0, "VLC": 10, "SRT": 0}
]
FNBOSS_LV = [
{"StartLv": 3, "EndLv": 5},
{"MaxHP": 200, "DEF": 0, "EVS": 10, "ATK": 40, "DAN": 30, "VLC": 10, "SRT": 0},
{"MaxHP": 50, "DEF": 0, "EVS": 0, "ATK": 10, "DAN": 0, "VLC": 0, "SRT": 10},
{"MaxHP": 0, "DEF": 0, "EVS": 0, "ATK": 10, "DAN": 10, "VLC": 10, "SRT": 0}
]
PSSBOSS_LV = [
{"StartLv": 3, "EndLv": 5},
{"MaxHP": 250, "DEF": 40, "EVS": 20, "ATK": 20, "DAN": 40, "VLC": 10, "SRT": 20},
{"MaxHP": 0, "DEF": 0, "EVS": 0, "ATK": 0, "DAN": 10, "VLC": 10, "SRT": 10},
{"MaxHP": 0, "DEF": 0, "EVS": 0, "ATK": 10, "DAN": 10, "VLC": 10, "SRT": 0}
]
FNLBOSS_LV = [
{"StartLv": 6, "EndLv": 6},
{"MaxHP": 350, "DEF": 30, "EVS": 40, "ATK": 40, "DAN": 50, "VLC": 30, "SRT": 30}
]

#Bluprint de Experiencia para Subir de Nivel
XPPROG = [10,30,60,100]

class Manifest:
    #Nombre y Sprite
    _name = None
    _sprite = None

    #Nivel y Experiencia
    _lv = None
    _xp = 0

    #Opponente
    _opp = None

    #Blueprint de Nivel Y Exp
    _lvBp = None 
    _xpBp = XPPROG

    #Variables de Abilidad
    _abilityUse = 1
    _actvBuff = [5,False]

    def __init__(self,lv):
        
        #Definiendo Nivel
        self._lv = self._lvBp[0]["StartLv"]

        #Definiendo Stats Base
        self._hp = self._lvBp[1]['MaxHP']
        self._maxHp = self._lvBp[1]['MaxHP']
        self._defnBs = self._lvBp[1]['DEF']
        self._evdBs = self._lvBp[1]['EVS']
        self._atkBs = self._lvBp[1]['ATK']
        self._atkDmgBs = self._lvBp[1]['DAN']
        self._spdBs = self._lvBp[1]['VLC']
        self._luckBs = self._lvBp[1]['SRT']

        #Definiendo Stats Bonus    

        self._defnBn = 0
        self._evdBn = 0
        self._atkBn = 0
        self._atkDmgBn = 0
        self._spdBn = 0
        self._luckBn = 0

        #Definiendo Stats Totales

        self._defn = self._defnBs + self._defnBn
        self._evd = self._evdBs + self._evdBn
        self._atk = self._atkBs + self._atkBn
        self._atkDmg = self._atkDmgBs + self._atkDmgBn
        self._spd = self._spdBs + self._spdBn
        self._luck = self._luckBs + self._luckBn

        #Ritina para Subir de Nivel en caso de comenzar
        #en un nivel mayor al inicial

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

    def get_actvBuff(self):
        return self._actvBuff


    ##Funciones de Atacar y Ser Atacado
    ##Las funciones siempre retornan los mensajes de acciones

    def act(self):
        Mss = ""
        if (random.randrange(1,BASETOLUCK) + self._luck >= BASETOLUCK) and (self._actvBuff[1] == False):  
            Mss = self.callAbility() + "\n" + self.attack()
        else:
            Mss = self.attack()
        return Mss

    def attack (self):
        Mss = self.get_name()
        mult = 1
        if (random.randrange(RANDATKLOW,RANDATKUP) + self.get_atk()) >= (BASETOHIT + self.get_opp().get_evd()):
            Mss+= " golpea a " + self.get_opp().get_name() + "."
            if random.randrange(1,BASETOLUCK) + self._luck >= BASETOLUCK:
                 mult = CRITMULT
                 Mss+= " Ataque Critico!"
            Mss+= "\n" + self.get_opp().takeDamage((random.randrange(RANDDMGLOW,RANDDMGUP) + self.get_atkDmg()) * mult)
        else:
            Mss+= " le erra a " + self.get_opp().get_name() + "."
        return Mss

    def takeDamage(self, dmg):
        rdDmg = dmg - self.get_defn()
        if(self.get_defn() > dmg ):
            rdDmg = 0
        Mss = self.get_name() + " recibe " + str(rdDmg) + " de daño."

        if rdDmg >= self.get_hp():
            self.set_hp(0)
            Mss+= '\n' + self.death()
        else:
            self.set_hp(self.get_hp() - rdDmg) 
        return Mss
    
    def death(self):
        return self.get_name() + " muere."
        
    def heal(self,heal):
        Mss = self.get_name() + " se cura "
        effHeal = self.get_maxHp() - self.get_hp()
        if heal >= effHeal:
            self.set_hp(self.get_hp() + effHeal)
            Mss += str(effHeal)
        else:
            self.set_hp(self.get_hp() + heal)
            Mss += str(heal)
        Mss += " de vida."
        return Mss
    
    #Metodos de Abilidades
    
    def callAbility(self):
        return self.get_name()  + " usa su habilidad especial."
    
    def endBuff(self):
        self._defnBn = 0
        self._evdBn = 0
        self._atkBn = 0
        self._atkDmgBn = 0
        self._spdBn = 0
        self._luckBn = 0

        self._actvBuff[1] = False

        return self.get_name()  + " pierde el incremento a sus estadísticas."
    
    #Metodos 'Ganar Experiencia' y 'Subir de Nivel'

    def xpUp(self,xp):
        Mss = self.get_name() 
        if self._xp == self._xpBp[-1]:
            Mss += "no puede ganar mas experiencia."   
        else:
            Mss += " gana " + str(xp) + " puntos de experiencia."
            self.set_xp(self.get_xp() + xp)
        return Mss
    
    def checkXp (self):
        if self._lv <= len(self._xpBp):
            if self._xp >= self._xpBp[self._lv - 1]:
                return True
        return False


    def lvUp(self):
        self.set_lv(self.get_lv() + 1)

        Offset = self.get_lv() - self._lvBp[0]['StartLv']  + 1

        self.set_maxHp(self.get_maxHp() + self._lvBp[Offset]['MaxHP'])
        self.set_hp(self.get_hp() + self._lvBp[Offset]['MaxHP'])

        self._defnBs += self._lvBp[Offset]['DEF']
        self._evdBs += self._lvBp[Offset]['EVS']
        self._atkBs += self._lvBp[Offset]['ATK']
        self._atkDmgBs += self._lvBp[Offset]['DAN']
        self._spdBs += self._lvBp[Offset]['VLC']
        self._luckBs += self._lvBp[Offset]['SRT']

        return "\n" + self.get_name() + " sube a nivel " + str(self.get_lv()) + "!"

#Clases de Angeles

class HealManifest (Manifest):
    def __init__(self, lv):
        self._name = "Angel Sagrado"
        self._sprite =r"Assets\BttlSprit\AnSag.gif"
        self. _lvBp = HEALANG_LV

        super().__init__(lv)
           
    def callAbility(self):
        heal = int(self.get_maxHp() * 0.25)
        return self.get_name()  + " usa su habilidad especial." + "\n" +  self.heal(heal)
    
class DrainManifest (Manifest):
    def __init__(self, lv):
        self._name = "Angel Oscuro"
        self._sprite =r"Assets\BttlSprit\AnOsc.gif"
        self._lvBp = DRAINANG_LV

        super().__init__(lv)        

    def act(self):
        Mss = None
        if random.randrange(1,BASETOLUCK) + self._luck >= BASETOLUCK:  
            Mss = self.callAbility()
        else:
            Mss = self.attack()
        return Mss

    def callAbility(self):
        drainDmg = int(random.randrange(RANDDMGLOW,RANDDMGUP) * 2 + self.get_atkDmg())
        Mss = self.get_name()  + " usa su habilidad especial." + "\n"
        Mss += self.get_name() + " le absorbe vida a " + self.get_opp().get_name() + "."
        Mss += "\n" + self.get_opp().takeDamage(drainDmg)
        Mss += "\n" + self.heal(int(drainDmg * 0.5))
        return Mss

class LazManifest (Manifest):
    def __init__(self, lv):
        self._name = "Angel Lázaro"
        self._sprite =r"Assets\BttlSprit\AnLaz.gif"
        self._lvBp = LAZANG_LV

        super().__init__(lv)
        
    def act(self):
        return self.attack()
    
    def death(self):
        Mss = self.get_name() + " muere."
        if self._abilityUse > 0:
            self._abilityUse -= 1
            Mss += "\n" + self.callAbility()
        return Mss
    
    def callAbility(self):
        Mss = ""
        rvHeal = int(random.randrange(self._luck,BASETOLUCK) * 0.0075 * self.get_maxHp())
        Mss = self.get_name()  + " usa su habilidad especial." + "\n"
        Mss += self.get_name()  + " revive!" + "\n"
        Mss += self.heal(rvHeal)
        return Mss

#Clases de Demonio Principal

class AtkDmnManifest(Manifest):
    def __init__(self, lv):
        self._name = "Fauste de Fe"
        self._sprite =r"Assets\BttlSprit\Fause.png"
        self._lvBp = ATKDMN_LV

        super().__init__(lv)    

    def callAbility(self):
        Mss = self.get_name()  + " usa su habilidad especial."

        self._atkBn += int(self._atkBs * 0.3)
        self._atkDmgBn += int(self._atkDmgBs * 0.3)

        Mss += "\n" + self.get_name()  + " incrementa su ATK y DAN."

        self._actvBuff[1] = True

        return Mss

class DefDmnManifest(Manifest):
    def __init__(self, lv):
        self._name = "Fauste de Fe"
        self._sprite =r"Assets\BttlSprit\Fause.gif"
        self._lvBp = DEFDMN_LV

        super().__init__(lv)     

    def callAbility(self):
        Mss = self.get_name()  + " usa su habilidad especial."

        self._dfnBn += int(self._atkBs * 0.4)

        Mss += "\n" + self.get_name()  + " incrementa su DEF."
        Mss += "\n" + str(self.heal(int(self.get_maxHp * 0,4)))

        self._actvBuff[1] = True

        return Mss

class LckDmnManifest(Manifest):
    def __init__(self, lv):
        self._name = "Fauste de Fe"
        self._sprite =r"Assets\BttlSprit\Fause.gif"
        self._lvBp = LCKDMN_LV

        super().__init__(lv)  

    def callAbility(self):
        Mss = self.get_name()  + " usa su habilidad especial."

        self._evdBn += int(self._evdBs * 0.2)
        self._spdBn += int(self._spdBs * 0.2)
        self._luckBn += int(self._luckBs * 0.1)

        Mss += "\n" + self.get_name()  + " incrementa su ESQ, VLC y SRT."

        self._actvBuff[1] = True

        return Mss

#Clases de Jefes

class SpnBossManifest(Manifest):
    def __init__(self, lv):
        self. _name = "Kamathra"
        self._sprite =r"Assets\BttlSprit\Fause.gif"
        self._lvBp = SPNBOSS_LV

        super().__init__(lv)
        
    def act(self):
        return self.attack()

    def takeDamage(self, dmg):
        rdDmg = dmg - self.get_defn()
        if(self.get_defn() > dmg ):
            rdDmg = 0
        Mss = self.get_name() + " recibe " + str(rdDmg) + " de daño."
        
        if rdDmg >= self.get_hp():
            self.set_hp(0)
            Mss+= "\n" + self.death()
        else:
            self.set_hp(self.get_hp() - rdDmg) 
            if (random.randrange(1,BASETOLUCK) + self._luck )>= BASETOLUCK:
                Mss += "\n" + self.callAbility()
        return Mss

    def callAbility (self):
        counterDmg = random.randrange(RANDDMGLOW,RANDDMGUP) * 2 + self.get_atkDmg()
        Mss = self.get_name()  + " usa su habilidad especial." + "\n"
        Mss += self.get_name() + " contrataca!"
        Mss += "\n" + self.get_opp().takeDamage(counterDmg)
        return Mss

class FnBossManifest(Manifest):
    def __init__(self, lv):
        self._name = "Vahruksha"
        self._sprite =r"Assets\BttlSprit\Fause.gif"
        self._lvBp = FNBOSS_LV

        super().__init__(lv)       

    def callAbility(self):
        Mss = self.get_name()  + " usa su habilidad especial."

        self._spdBn += int(self._spdBs * 0.25)
        self._luckBn += int(self._luckBs * 0.25)

        Mss += "\n" + self.get_name()  + " incrementa su VLC y SRT."

        self._actvBuff[1] = True

        return Mss

class PssBossDmnManifest(Manifest):
    def __init__(self, lv):
        self._name = "Nzolukaya"
        self._sprite =r"Assets\BttlSprit\Fause.gif"
        self._lvBp = PSSBOSS_LV

        super().__init__(lv)       

    def act(self):
        Mss = None
        if (random.randrange(1,BASETOLUCK) + self._luck )>= BASETOLUCK:  
            Mss = self.callAbility()
        else:
            Mss = self.attack()
        return Mss

    def callAbility(self):
        Mss = self.get_name()  + " usa su habilidad especial." + "\n"
        Mss += "\n" + self.takeDamage(int(self._maxHp * 0.01))

        hurtDmg = int(random.randrange(RANDDMGLOW,RANDDMGUP) * (2 + (self._hp/self._maxHp))) + self.get_atkDmg()

        Mss += self.get_name() + " ataca a " + self.get_opp().get_name() + "."
        Mss += "\n" + self.get_opp().takeDamage(hurtDmg)
        return Mss

class FnlBossDmnManifest(Manifest):
    def __init__(self, lv):
        self._name = "Eliadran"
        self._sprite =r"Assets\BttlSprit\Fause.gif"
        self._lvBp = FNLBOSS_LV
        
        super().__init__(lv)
        
        self._abilityUse = 5

    def act(self):
        Mss = ""
        if random.randrange(1,BASETOLUCK) + self._luck >= BASETOLUCK:
            if self._abilityUse > 0:
                Mss += self.attack()
            else:
                Mss = self.callAbility()
    
        Mss += self.attack()
        return Mss

    def callAbility(self):
        Mss = self.get_name()  + " usa su habilidad especial."

        Mss += "\n" + self.takeDamage(int(self._maxHp * 0.05))

        self._atkBn = int(self._atkBs * 0.2)
        self._atkDmgBn = int(self._atkDmgBs * 0.2)
        self._spdBn = int(self._spdBn * 0.2)
        self._luckBn = int(self._luckBs * 0.1)

        Mss += "\n" + self.get_name()  + "incrementa su ATK, DAN, VLC y SRT."

        self._abilityUse -=1

        return Mss


'''
M1 = AtkDmnManifest(5)
M2 = DefDmnManifest(1)

M1.set_opp(M2)
M2.set_opp(M1)

print(M1.xpUp(100))
print(M1.xpUp(100))
print(M1.get_xp())
print(M1.checkXp())
'''