import random

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

class Manifest:
    def __init__(self, name, sprite, lv, xp, maxHp, defn, evd, atk, atkDmg, spd, luck, opp):

        #Nombre y Sprite

        self._name = name
        self._sprite = sprite

        #Nivel y Experiencia

        self._lv = lv
        self._xp = xp
        
        # Stats siendo Vida (hp), Vida Maxima (maxHp), Defensa (defn), Evasion (evd), Ataque (atk),
        # Daño (atkDmg), Velocidad (spd), y Suerte (luck)

        self._hp = maxHp
        self._maxHp = maxHp
        self._defn = defn
        self._evd = evd
        self._atk = atk
        self._atkDmg = atkDmg
        self._spd = spd
        self._luck = luck

        #Opponente

        self._opp = opp

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
    
    def xpUp(self):
        #Evento en caso de ganar experiencia.
        pass

    def lvUp(self):
        #Evento en caso de subir de nivel. Deberia ser llamado por ganar experiencia
        pass

#Clases de Angeles

class HealManifest (Manifest):

    def act(self):
        btlMssg = self.attack()
        if random.randrange(self.get_luck(),(BASETOLUCK + 1)) == BASETOLUCK:
            btlMssg += "\n" + self.callAbility()
        return btlMssg 

    def callAbility(self):
        heal = int(self.get_maxHp() * 0.25)
        return self.get_name()  + " usa su habilidad especial." + "\n" +  self.heal(heal)
    
class DrainManifest (Manifest):

    def callAbility(self):
        drainDmg = int (random.randrange(RANDDMGLOW,RANDDMGUP) * 2 + self.get_atkDmg())
        btlMssg = self.get_name()  + " usa su habilidad especial." + "\n"
        btlMssg += self.get_name() + " le absorbe vida a " + self.get_opp().get_name() + "."
        btlMssg += "\n" + self.get_opp().takeDamage(drainDmg)
        btlMssg += "\n" + self.heal(int(drainDmg * 0.5))
        return btlMssg

class LazManifest (Manifest):

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
        rvHeal = int(random.randrange(self.get_luck(),(BASETOLUCK + 1)) * 0.1 * self.get_maxHp())
        btlMssg = self.get_name()  + " usa su habilidad especial." + "\n"
        btlMssg += self.get_name()  + " revive!" + "\n"
        btlMssg += self.heal(rvHeal)
        return btlMssg

#Clases de Demonio Principal

class AtkDmnManifest(Manifest):

    def callAbility(self, opp):
        return super().callAbility(opp)

class DefDmnManifest(Manifest):
    pass  

class LckDmnManifest(Manifest):
    pass

#Clases de Jefes

class SpnBossManifest(Manifest):
    pass
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
    pass

class PssBossDmnManifest(Manifest):
    pass

class FnBossDmnManifest(Manifest):
    pass


M1Dicc = {
    "Name": "Angel Bueno",
    "Sprite": None,
    "Level": 1,
    "Exp": 0,
    "Health": 20,
    "Defense": 0,
    "Evade": 0,
    "Attack": 4,
    "Damage": 2,
    "Speed": 5,
    "Luck": 5,
    "Opponent": None
}

M2Dicc = {
    "Name": "Espina",
    "Sprite": None,
    "Level": 1,
    "Exp": 0,
    "Health": 30,
    "Defense": 0,
    "Evade": 0,
    "Attack": 1,
    "Damage": 3,
    "Speed": 6,
    "Luck": 2,
    "Opponent": None
}

M1 = HealManifest(*list(M1Dicc.values()))
M2 = SpnBossManifest(*list(M2Dicc.values()))

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

