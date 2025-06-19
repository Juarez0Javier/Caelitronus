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
    def __init__(self, name, sprite, lv, xp, maxHp, defn, evd, atk, atkDmg, spd, luck):

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

    def get_hp(self):
        return self._hp
    def set_hp(self, hp):
        self._hp = hp

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

    def get_atk(self):
        return self._atkDmg
    def set_atk(self, atkDmg):
        self._atkDmg = atkDmg

    def get_spd(self):
        return self._spd
    def set_spd(self, spd):
        self._spd = spd

    def get_luck(self):
        return self._luck
    def set_luck(self, luck):
        self._luck = luck

    ##Funciones de Atacar y Ser Atacado
    ##Las funciones siempre retornan los mensajes de acciones

    def act(self,opp):
        if random.randrange(self._luck,(BASETOLUCK + 1)) == BASETOLUCK:
            return self.callAbility(opp)
        else:
            return self.attack(opp)

    def attack (self, opp):
        btlMssg = self._name
        mult = 1
        if (random.randrange(RANDATKLOW,RANDATKUP) + self._atk) >= (BASETOHIT + opp.get_evd()):
            #Animacion de Ataque - Golpea
            btlMssg+= " golpea a " + opp.get_name() + "."
            if random.randrange(self._luck,(BASETOLUCK + 1)) >= BASETOLUCK:
                 mult = CRITMULT
                 btlMssg+= " Ataque Critico!"
            btlMssg+= "\n" + opp.takeDamage((random.randrange(RANDDMGLOW,RANDDMGUP) + self._atkDmg) * mult)
        else:
            #Animacion de Ataque - Erra
            btlMssg+= " le erra a " + opp.get_name() + "."
        return btlMssg

    def takeDamage(self, dmg):
        rdDmg = dmg - self._defn
        if(self._defn > dmg ):
            rdDmg = 0
        btlMssg = self._name + " recibe " + str(rdDmg) + " de daño."
        #Animacion de recibir daño
        if rdDmg >= self._hp:
            self._hp = 0
            btlMssg+= "\n" + self.death()
        else:
            self._hp -= rdDmg
        return btlMssg
        
    def callAbility(self,opp):
        return self._name  + " usa su habilidad especial."
    
    def heal(self,heal):
        btlMssg = self._name + " se cura "
        effHeal = self._maxHp - self._hp
        if heal >= effHeal:
            self._hp += effHeal
            btlMssg += str(effHeal)
        else:
            self._hp += heal
            btlMssg += str(heal)
        btlMssg += " de vida."
        return btlMssg

    def death(self):
        #Animacion Muerte
        return self._name + " muere."
    
    def xpUp(self):
        #Evento en caso de ganar experiencia.
        pass

    def lvUp(self):
        #Evento en caso de subir de nivel. Deberia ser llamado por ganar experiencia
        pass

#Clases de Angeles

class HealManifest (Manifest):

    def act(self, opp):
        btlMssg = self.attack(opp)
        if random.randrange(self._luck,(BASETOLUCK + 1)) == BASETOLUCK:
            btlMssg += "\n" + self.callAbility()
        return btlMssg 

    def callAbility(self):
        heal = int(self._maxHp * 0.25)
        return self._name  + " usa su habilidad especial." + "\n" +  self.heal(heal)
    
class DrainManifest (Manifest):

    def callAbility(self,opp):
        drainDmg = int (random.randrange(RANDDMGLOW,RANDDMGUP) * 2 + self._atkDmg)
        btlMssg = self._name  + " usa su habilidad especial." + "\n"
        btlMssg += self._name + " le absorbe vida a " + opp.get_name() + "."
        btlMssg += "\n" + opp.takeDamage(drainDmg)
        btlMssg += "\n" + self.heal(int(drainDmg * 0.5))
        return btlMssg

class LazManifest (Manifest):

    _abilityUse = 1

    def act(self, opp):
        return self.attack(opp)
    
    def death(self):
        btlMssg = self._name + " muere."
        if self._abilityUse > 0:
            self._abilityUse -= 1
            btlMssg += "\n" + self.callAbility()
        return btlMssg
    
    def callAbility(self):
        btlMssg = ""
        rvHeal = int(random.randrange(self._luck,(BASETOLUCK + 1)) * 0.1 *self._maxHp)
        btlMssg = self._name  + " usa su habilidad especial." + "\n"
        btlMssg += self._name  + " revive!" + "\n"
        btlMssg += self.heal(rvHeal)
        return btlMssg

#Clases de Demonio Principal

class AtkDmnManifest(Manifest):

    def callAbility(self, opp):
        return super().callAbility(opp)


#Clases de Jefes

class SpnManifest(Manifest):
    pass

M1 = HealManifest("Angel Bueno","",1,0,20,0,0,2,4,9,1)
M2 = LazManifest("Angel Malo","",1,0,40,0,0,1,1,2,2)

i = 0
while M1.get_hp() > 0 and M2.get_hp() > 0:
    print("##################################")
    print(M1.act(M2))
    print("----------------------------------")
    print(M2.act(M1))
    print("----------------------------------")
    print(M1.get_name() + " le queda " + str(M1.get_hp()) + " de vida.")
    print(M2.get_name() + " le queda " + str(M2.get_hp()) + " de vida.")
    i+=1
print("Turnos Totales: " + str(i))