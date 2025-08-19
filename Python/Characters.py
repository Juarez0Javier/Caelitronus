import random
import asyncio


#Dados
DANDIE = 8
ATKDIE = 20

#Liimites minimos


BASETOHIT = 10
BASETOLUCK = 100

#Multiplicadores
CRITMULT = 1.5

#Blueprints de Niveles de Manifestacion
ATKDMN_LV = [
{"StartLv": 1, "EndLv":8},
{"PV": 150, "DEF": 0, "ESQ": 10, "ATK": 20, "DAN": 10, "VLC": 10, "SRT": 5},
{"PV": 25, "DEF": 0, "ESQ": 0, "ATK": 10, "DAN": 0, "VLC": 5, "SRT": 0},
{"PV": 0, "DEF": 0, "ESQ": 0, "ATK": 5, "DAN": 10, "VLC": 5, "SRT": 0},
{"PV": 25, "DEF": 5, "ESQ": 5, "ATK": 0, "DAN": 0, "VLC": 0, "SRT": 5},
{"PV": 0, "DEF": 0, "ESQ": 0, "ATK": 5, "DAN": 5, "VLC": 5, "SRT": 5},
{"PV": 0, "DEF": 0, "ESQ": 0, "ATK": 10, "DAN": 10, "VLC": 0, "SRT": 0},
{"PV": 0, "DEF": 0, "ESQ": 0, "ATK": 5, "DAN": 5, "VLC": 5, "SRT": 5},
{"PV": 25, "DEF": 5, "ESQ": 10, "ATK": 0, "DAN": 0, "VLC": 0, "SRT": 0}
]
DEFDMN_LV = [
{"StartLv": 1, "EndLv":8},
{"PV": 200, "DEF": 10, "ESQ": 15, "ATK": 10, "DAN": 0, "VLC": 5, "SRT": 5},
{"PV": 50, "DEF": 5, "ESQ": 0, "ATK": 0, "DAN": 5, "VLC": 0, "SRT": 0},
{"PV": 25, "DEF": 5, "ESQ": 5, "ATK": 0, "DAN": 0, "VLC": 0, "SRT": 5},
{"PV": 0, "DEF": 5, "ESQ": 5, "ATK": 0, "DAN": 0, "VLC": 5, "SRT": 5},
{"PV": 25, "DEF": 5, "ESQ": 5, "ATK": 0, "DAN": 0, "VLC": 5, "SRT": 0},
{"PV": 50, "DEF": 10, "ESQ": 0, "ATK": 0, "DAN": 0, "VLC": 0, "SRT": 0},
{"PV": 0, "DEF": 0, "ESQ": 0, "ATK": 5, "DAN": 10, "VLC": 5, "SRT": 0}
]
LCKDMN_LV = [
{"StartLv": 1, "EndLv":8},
{"PV": 150, "DEF": 0, "ESQ":15, "ATK": 10, "DAN": 0, "VLC": 15, "SRT": 15},
{"PV": 0, "DEF": 0, "ESQ": 5, "ATK": 5, "DAN": 0, "VLC": 5, "SRT": 10},
{"PV": 25, "DEF": 0, "ESQ": 5, "ATK": 0, "DAN": 5, "VLC": 5, "SRT": 0},
{"PV": 0, "DEF": 0, "ESQ": 0, "ATK": 5, "DAN": 5, "VLC": 5, "SRT": 5},
{"PV": 25, "DEF": 5, "ESQ": 5, "ATK": 0, "DAN": 0, "VLC": 5, "SRT": 5},
{"PV": 0, "DEF": 0, "ESQ": 0, "ATK": 0, "DAN": 0, "VLC": 10, "SRT": 10},
{"PV": 25, "DEF": 0, "ESQ": 0, "ATK": 0, "DAN": 0, "VLC": 5, "SRT": 10},
{"PV": 25, "DEF": 10, "ESQ": 0, "ATK": 0, "DAN": 5, "VLC": 5, "SRT": 10}
]

HEALANG_LV = [
{"StartLv": 1, "EndLv": 4},
{"PV": 150, "DEF": 0, "ESQ": 5, "ATK": 10, "DAN": 0, "VLC": 5, "SRT": 10},
{"PV": 25, "DEF": 0, "ESQ": 5, "ATK": 0, "DAN": 0, "VLC": 5, "SRT": 5},
{"PV": 0, "DEF": 0, "ESQ": 5, "ATK": 5, "DAN": 0, "VLC": 5, "SRT": 5},
{"PV": 0, "DEF": 5, "ESQ": 5, "ATK": 0, "DAN": 5, "VLC": 5, "SRT": 0}
]
DRAINANG_LV = [
{"StartLv": 1, "EndLv": 4},
{"PV": 150, "DEF": 0, "ESQ": 5, "ATK": 5, "DAN": 5, "VLC": 0, "SRT": 10},
{"PV": 25, "DEF": 0, "ESQ": 5, "ATK": 5, "DAN": 5, "VLC": 0, "SRT": 0},
{"PV": 25, "DEF": 0, "ESQ": 0, "ATK": 0, "DAN": 0, "VLC": 5, "SRT": 10},
{"PV": 0, "DEF": 0, "ESQ": 0, "ATK": 0, "DAN": 10, "VLC": 5, "SRT": 5}
]
LAZANG_LV = [
{"StartLv": 1, "EndLv": 4},
{"PV": 125, "DEF": 5, "ESQ": 15, "ATK": 5, "DAN": 0, "VLC": 0, "SRT": 10},
{"PV": 0, "DEF": 0, "ESQ": 5, "ATK": 5, "DAN": 5, "VLC": 0, "SRT": 5},
{"PV": 50, "DEF": 0, "ESQ": 5, "ATK": 0, "DAN": 0, "VLC": 0, "SRT": 5},
{"PV": 0, "DEF": 5, "ESQ": 0, "ATK": 0, "DAN": 0, "VLC": 5, "SRT": 10}
]

SPNBOSS_LV = [
{"StartLv": 2, "EndLv": 5},
{"PV": 200, "DEF": 5, "ESQ": 10, "ATK": 15, "DAN": 25, "VLC": 5, "SRT": 15},
{"PV": 0, "DEF": 5, "ESQ": 5, "ATK": 0, "DAN": 0, "VLC": 5, "SRT": 5},
{"PV": 25, "DEF": 0, "ESQ": 5, "ATK": 0, "DAN": 5, "VLC": 0, "SRT": 5},
{"PV": 25, "DEF": 0, "ESQ": 5, "ATK": 5, "DAN": 0, "VLC": 5, "SRT": 0}
]
FNBOSS_LV = [
{"StartLv": 2, "EndLv": 5},
{"PV": 175, "DEF": 0, "ESQ": 10, "ATK": 25, "DAN": 10, "VLC": 25, "SRT": 10},
{"PV": 200, "DEF": 0, "ESQ": 5, "ATK": 5, "DAN": 5, "VLC": 0, "SRT": 0},
{"PV": 25, "DEF": 0, "ESQ": 0, "ATK": 5, "DAN": 0, "VLC": 5, "SRT": 5},
{"PV": 0, "DEF": 0, "ESQ": 0, "ATK": 5, "DAN": 5, "VLC": 5, "SRT": 5}
]
PSSBOSS_LV = [
{"StartLv": 2, "EndLv": 5},
{"PV": 275, "DEF": 5, "ESQ": 10, "ATK": 15, "DAN": 10, "VLC": 10, "SRT": 10},
{"PV": 25, "DEF": 0, "ESQ": 5, "ATK": 10, "DAN": 0, "VLC": 5, "SRT": 5},
{"PV": 0, "DEF": 0, "ESQ": 5, "ATK": 0, "DAN": 5, "VLC": 5, "SRT": 5},
{"PV": 25, "DEF": 0, "ESQ": 0, "ATK": 5, "DAN": 5, "VLC": 5, "SRT": 0}
]
FNLBOSS_LV = [
{"StartLv": 5, "EndLv": 6},
{"PV": 500, "DEF": 15, "ESQ": 25, "ATK": 35, "DAN": 20, "VLC": 20, "SRT": 20},
{"PV": 0, "DEF": 0, "ESQ": 5, "ATK": 5, "DAN": 5, "VLC": 5, "SRT": 0}
]

#Bluprint de Experiencia para Subir de Nivel
XPPROG = [10,30,60,100,150,210,280]

#Lista de Stats
STATLIST = ['PV','DEF','ESQ','ATK','DAN','VLC','SRT']

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
        self._hp = self._lvBp[1]['PV']
        self._maxHp = self._lvBp[1]['PV']
        self._defnBs = self._lvBp[1]['DEF']
        self._evdBs = self._lvBp[1]['ESQ']
        self._atkBs = self._lvBp[1]['ATK']
        self._atkDmgBs = self._lvBp[1]['DAN']
        self._spdBs = self._lvBp[1]['VLC']
        self._luckBs = self._lvBp[1]['SRT']

        #Definiendo Stats Base
        self._statBuffer = {'PV':0,'DEF':0,'ESQ':0,'ATK':0,'DAN':0,'VLC':0,'SRT':0}

        self.setUpBuff()

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
        return self._defnBs
    def set_defn(self, defn):
        self._defnBs = defn   

    def get_evd(self):
        return self._evdBs
    def set_evd(self, evd):
        self._evdBs = evd 

    def get_atk(self):
        return self._atkBs
    def set_atk(self, atk):
        self._atkBs = atk

    def get_atkDmg(self):
        return self._atkDmgBs
    def set_atkDmg(self, atkDmg):
        self._atkDmgBs = atkDmg

    def get_spd(self):
        return self._spdBs
    def set_spd(self, spd):
        print(spd)
        self._spdBs = spd

    def get_luck(self):
        return self._luckBs
    def set_luck(self, luck):
        self._luckBs = luck

    def get_opp(self):
        return self._opp
    def set_opp(self, opp):
        self._opp = opp

    def get_actvBuff(self):
        return self._actvBuff
    def get_lvBp(self):
        return self._lvBp

    def get_bsStatByKey(self,key):
        if key == "PV":
            return self.get_maxHp()
        if key == "DEF":
            return self._defnBs
        if key == "ESQ":
            return self._evdBs
        if key == "ATK":
            return self._atkBs
        if key == "DAN":
            return self._atkDmgBs
        if key == "VLC":
            return self._spdBs
        if key == "SRT":
            return self._luckBs   
    def set_bsStatByKey(self,key,value):
        if key == "PV":
            self.set_maxHp(value)
        if key == "DEF":
            self._defnBs = value
        if key == "ESQ":
            self._evdBs = value
        if key == "ATK":
            self._atkBs = value
        if key == "DAN":
            self._atkDmgBs = value
        if key == "VLC":
            self._spdBs = value
        if key == "SRT":
            self._luckBs = value
    
    ##Funciones de Atacar y Ser Atacado
    ##Las funciones siempre retornan los mensajes de acciones

    def act(self):

        Mss = ""
        if (random.randrange(1,BASETOLUCK) + self.get_luck() >= BASETOLUCK) and (self._actvBuff[1] == False):  
            Mss += self.callAbility()
        Mss += self.attack()
        return Mss

    def attack (self):
        Mss = self.get_name()
        mult = 1

        if (random.randrange(1,ATKDIE) + self.get_atk()/10) >= (BASETOHIT + self.get_opp().get_evd()/10):
            Mss+= " golpea a " + self.get_opp().get_name() + "." + "\n"
            if random.randrange(1,BASETOLUCK) + self._luckBs >= BASETOLUCK:
                 mult = CRITMULT
                 Mss+= "Ataque Critico!" + "\n"
            Mss+= self.get_opp().takeDamage(int(random.randrange(1,DANDIE) * 5 * mult + self.get_atkDmg() ))
        else:
            Mss+=" le erra a " + self.get_opp().get_name() + "." + "\n"
        return Mss

    def takeDamage(self, dmg):
        rdDmg = dmg - self.get_defn()
        if(self.get_defn() > dmg ):
            rdDmg = 0
        Mss = self.get_name() + " recibe " + str(rdDmg) + " de daño." + "\n"

        if rdDmg >= self.get_hp():
            self.set_hp(0)
            Mss+= '\n' + self.death()
        else:
            self.set_hp(self.get_hp() - rdDmg) 
        return Mss
    
    def death(self):
        return self.get_name() + " muere." + "\n"
        
    def heal(self,heal):
        Mss = self.get_name() + " se cura " 
        effHeal = self.get_maxHp() - self.get_hp()
        if heal >= effHeal:
            self.set_hp(self.get_hp() + effHeal)
            Mss += str(effHeal)
        else:
            self.set_hp(self.get_hp() + heal)
            Mss += str(heal)
        Mss += " de vida." + "\n"
        return Mss
    
    #Metodos de Abilidades
    
    def callAbility(self):
        return self.get_name()  + " usa su habilidad especial." + "\n"
    
    def setUpBuff(self):
        for key in STATLIST:
            self._statBuffer[key] = self.get_bsStatByKey(key)

    def endBuff(self):

        for key in STATLIST:
            self.set_bsStatByKey(key, self._statBuffer[key])

        self._actvBuff[1] = False

        return self.get_name()  + " pierde el incremento a sus estadísticas." + "\n"
    
    #Metodos 'Ganar Experiencia' y 'Subir de Nivel'

    def xpUp(self,xp):
        Mss = self.get_name() 
        if self._xp == self._xpBp[-1]:
            Mss += " no puede ganar mas experiencia." + "\n"   
        else:
            Mss += " gana " + str(xp) + " puntos de experiencia." + "\n"
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

        for stat in STATLIST:
            #print (stat + ": " + str(self.get_bsStatByKey(stat)) + " - " +  stat + " Incr: +" + str(self._lvBp[Offset][stat]))
            self.set_bsStatByKey(stat,self.get_bsStatByKey(stat) + self._lvBp[Offset][stat])
            #print (stat + " Rslt: " + str(self.get_bsStatByKey(stat)))

        self.heal(self.get_maxHp())

#Clases de Angeles

class HealManifest (Manifest):
    def __init__(self, lv):
        self._name = "Angel Sagrado"
        self._sprite =r"Assets\\BttlSprit\\AnSag.png"
        self. _lvBp = HEALANG_LV

        super().__init__(lv)
           
    def callAbility(self):
        heal = int(self.get_maxHp() * 0.25)
        return self.get_name()  + " usa su habilidad especial." + "\n" +  self.heal(heal)
    
class DrainManifest (Manifest):
    def __init__(self, lv):
        self._name = "Angel Oscuro"
        self._sprite =r"Assets\\BttlSprit\\AnOsc.png"
        self._lvBp = DRAINANG_LV

        super().__init__(lv)        

    def act(self):
        Mss = None
        if random.randrange(1,BASETOLUCK) + self._luckBs >= BASETOLUCK:  
            Mss = self.callAbility() + "\n"
        else:
            Mss = self.attack() + "\n"
        return Mss

    def callAbility(self):
        drainDmg = int(random.randrange(1,DANDIE) * 5 * CRITMULT + self.get_atkDmg())
        Mss = self.get_name()  + " usa su habilidad especial." + "\n"
        Mss += self.get_name() + " le absorbe vida a " + self.get_opp().get_name() + "." + "\n"
        Mss += self.get_opp().takeDamage(drainDmg)
        Mss += self.heal(int(drainDmg * 0.5))
        return Mss

class LazManifest (Manifest):
    def __init__(self, lv):
        self._name = "Angel Lázaro"
        self._sprite =r"Assets\\BttlSprit\\AnLaz.png"
        self._lvBp = LAZANG_LV

        super().__init__(lv)
        
    def act(self):
        return self.attack()
    
    def death(self):
        Mss = self.get_name() + " muere." + "\n"
        if self._abilityUse > 0:
            self._abilityUse -= 1
            Mss += self.callAbility()
        return Mss
    
    def callAbility(self):
        Mss = ""
        rvHeal = int(random.randrange(self._luckBs,(BASETOLUCK)) * 0.0075 * self.get_maxHp())
        Mss = self.get_name()  + " usa su habilidad especial." + "\n"
        Mss += self.get_name()  + " revive!" + "\n"
        Mss += self.heal(rvHeal)
        return Mss

#Clases de Demonio Principal

class AtkDmnManifest(Manifest):
    def __init__(self, lv):
        self._name = "Fauste de Fe"
        self._sprite =r"Assets\\BttlSprit\\Fause.png"
        self._lvBp = ATKDMN_LV

        super().__init__(lv)

    def callAbility(self):
        Mss = self.get_name()  + " usa su habilidad especial." + "\n"

        self.setUpBuff()

        self._statBuffer['ATK'] = self._atkBs
        self._statBuffer['DAN'] = self._atkDmgBs

        self._atkBs += int(self._statBuffer['ATK'] * 0.4)
        self._atkDmgBs += int(self._statBuffer['DAN'] * 0.3)

        Mss += self.get_name()  + " incrementa su ATK y DAN." + "\n"

        self._actvBuff[1] = True

        return Mss

class DefDmnManifest(Manifest):
    def __init__(self, lv):
        self._name = "Fauste de Fe"
        self._sprite =r"Assets\\BttlSprit\\Fause.png"
        self._lvBp = DEFDMN_LV

        super().__init__(lv)     

    def callAbility(self):

        Mss = self.get_name()  + " usa su habilidad especial." + "\n"

        self.setUpBuff()

        self._statBuffer['DEF'] = self.get_defn()

        self._defnBs += int(self._statBuffer['DEF'] * 0.4)

        Mss += self.get_name()  + " incrementa su DEF." + "\n"
        Mss += str(self.heal(int(self.get_maxHp() * 0.25))) + "\n"

        self._actvBuff[1] = True

        return Mss

class LckDmnManifest(Manifest):
    def __init__(self, lv):
        self._name = "Fauste de Fe"
        self._sprite =r"Assets\\BttlSprit\\Fause.png"
        self._lvBp = LCKDMN_LV

        super().__init__(lv)  

    def callAbility(self):
        Mss = self.get_name()  + " usa su habilidad especial." + "\n"

        self.setUpBuff()

        self._statBuffer['ESQ'] = self._evdBs
        self._statBuffer['VLC'] = self._spdBs
        self._statBuffer['SRT'] = self._luckBs

        self._evdBs += int(self._statBuffer['ESQ'] * 0.25)
        self._spdBs += int(self._statBuffer['VLC'] * 0.3)
        self._luckBs += int(self._statBuffer['SRT'] * 0.15)
        

        Mss += self.get_name()  + " incrementa su ESQ, VLC y SRT." + "\n"

        self._actvBuff[1] = True

        return Mss

#Clases de Jefes

class SpnBossManifest(Manifest):
    def __init__(self, lv):
        self. _name = "Kamathra"
        self._sprite =r"Assets\\BttlSprit\\Kamathra.png"
        self._lvBp = SPNBOSS_LV

        super().__init__(lv)
        
    def act(self):
        return self.attack()

    def takeDamage(self, dmg):
        rdDmg = dmg - self.get_defn()
        if(self.get_defn() > dmg ):
            rdDmg = 0
        Mss = self.get_name() + " recibe " + str(rdDmg) + " de daño." + "\n"
        
        if rdDmg >= self.get_hp():
            self.set_hp(0)
            Mss+= self.death()
        else:
            self.set_hp(self.get_hp() - rdDmg) 
            if (random.randrange(1,BASETOLUCK) + self._luckBs )>= BASETOLUCK:
                Mss += self.callAbility() + "\n"
        return Mss

    def callAbility (self):
        counterDmg = int(random.randrange(1,DANDIE) * 5 * CRITMULT + self.get_atkDmg())
        Mss = self.get_name()  + " usa su habilidad especial." + "\n"
        Mss += self.get_name() + " contrataca!" + "\n"
        Mss += self.get_opp().takeDamage(counterDmg) + "\n"
        return Mss

class FnBossManifest(Manifest):
    def __init__(self, lv):
        self._name = "Vahruksha"
        self._sprite =r"Assets\\BttlSprit\\Vahruksha.png"
        self._lvBp = FNBOSS_LV

        super().__init__(lv)       

    def callAbility(self):
        Mss = self.get_name()  + " usa su habilidad especial." + "\n"

        self.setUpBuff()

        self._statBuffer['VLC'] = self._spdBs
        self._statBuffer['SRT'] = self._luckBs

        self._spdBs += int(self._statBuffer['VLC'] * 0.3)
        self._luckBs += int(self._statBuffer['SRT'] * 0.3)

        Mss += self.get_name()  + " incrementa su VLC y SRT." + "\n"

        self._actvBuff[1] = True

        return Mss

class PssBossManifest(Manifest):
    def __init__(self, lv):
        self._name = "Nzolukaya"
        self._sprite =r"Assets\\BttlSprit\\Nzolukaya.png"
        self._lvBp = PSSBOSS_LV

        super().__init__(lv)       

    def act(self):
        Mss = None
        if (random.randrange(1,BASETOLUCK) + self._luckBs)>= BASETOLUCK:  
            Mss = self.callAbility()
        else:
            Mss = self.attack()
        return Mss

    def callAbility(self):
        Mss = self.get_name()  + " usa su habilidad especial." + "\n"
        
        rawDmg = int(self.get_maxHp() * 0.10)

        Mss += self.get_name()  + " reduce su vida por " + str(rawDmg) + "\n"

        hurtDmg = int(random.randrange(1,DANDIE) * 5 * (CRITMULT + (self._hp/self._maxHp))) + self.get_atkDmg()

        Mss += self.get_name() + " ataca a " + self.get_opp().get_name() + "." + "\n"
        Mss += str(self.get_opp().takeDamage(hurtDmg)) + "\n"
        return Mss 

class FnlBossManifest(Manifest):
    def __init__(self, lv):
        self._name = "Eliadran"
        self._sprite =r"Assets\\BttlSprit\\Eliadran.png"
        self._lvBp = FNLBOSS_LV
        
        super().__init__(lv)
        
        self._abilityUse = 5

    def act(self):
        Mss = ""
        if random.randrange(1,BASETOLUCK) + self._luckBs >= BASETOLUCK:
            Mss += self.callAbility()

        Mss += self.attack()
        return Mss

    def callAbility(self):
        Mss = self.get_name()  + " usa su habilidad especial." + "\n"

        rawDmg = int(self.get_maxHp() * 0.10)

        Mss += self.get_name()  + " reduce su vida por " + str(rawDmg) + "\n"

        self.set_hp(int(self.get_hp() - rawDmg))

        if self._abilityUse > 0:

            if self._abilityUse == 5:

                self.setUpBuff()

                self._statBuffer['ATK'] = self._atkBs
                self._statBuffer['DAN'] = self._atkDmgBs
                self._statBuffer['VLC'] = self._spdBs
                self._statBuffer['SRT'] = self._luckBs

            self._atkBs += int(self._statBuffer['ATK'] * 0.2)
            self._atkDmgBs += int(self._statBuffer['DAN'] * 0.2)
            self._spdBs += int(self._statBuffer['VLC'] * 0.2)
            self._luckBs += int(self._statBuffer['SRT'] * 0.1)

            Mss += self.get_name()  + " incrementa su ATK, DAN, VLC y SRT." + "\n"

            self._abilityUse -=1
        else:
            self.attack()
        return Mss

'''
M1 = AtkDmnManifest(1)

M1.lvUp()

statList = ['PV','DEF','ESQ','ATK','DAN','VLC','SRT']
for stat in statList:
    print (stat + ": " + str(M1.get_bsStatByKey(stat)))
'''