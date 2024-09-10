import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        self.max_health_viking = health

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        
    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

        

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
        
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        if not self.saxonArmy:
            return "No Saxons left to attack!"
        
        chosen_saxon = random.choice(self.saxonArmy)
        chosen_viking = random.choice(self.vikingArmy)
        
        # health check of the chosen Viking, and then decide whether to increase the damage
        if chosen_viking.health <= (chosen_viking.max_health_viking * 0.3):
            damage = chosen_viking.attack() * 2
            print(f"Viking {chosen_viking.name} has less than 30 percent of life, this attack deals double the damage")
        else:
            damage = chosen_viking.attack()
        output_message = chosen_saxon.receiveDamage(damage)

        if chosen_saxon.health <= 0:
            self.saxonArmy.remove(chosen_saxon)
            print(f"a Saxon has been slain by Viking {chosen_viking.name} with {damage} damage.")

        return output_message

    def saxonAttack(self):
        if not self.vikingArmy:
            return "No Vikings left to attack!"
        
        chosen_saxon = random.choice(self.saxonArmy)
        chosen_viking = random.choice(self.vikingArmy)
        damage = chosen_saxon.attack()
        output_message = chosen_viking.receiveDamage(damage)

        if chosen_viking.health <= 0:
            self.vikingArmy.remove(chosen_viking)
            print(f"Viking {chosen_viking.name} has been slain by Saxon with {damage} damage.")

        return output_message


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    

# #yop
# class War2:

#     def __init__(self):
#         # your code here

#     def addViking(self, Viking):
#         # your code here
    
#     def addSaxon(self, Saxon):
#         # your code here
    
#     def vikingAttack(self):
#         # your code here

#     def saxonAttack(self):
#         # your code here

#     def showStatus(self):
#         # your code here

#     pass 