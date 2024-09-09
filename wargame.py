
from vikingsClasses import Soldier, Viking, Saxon, War
import random


soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]

war = War()


#Create 5 Vikings
for i in range(0,5):
    if i:
        war.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))

#Create 5 Saxons
for i in range(0,5):
    if i:
        war.addSaxon(Saxon(100,random.randint(0,100)))
    
round = 0
while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    war.vikingAttack()
    war.saxonAttack()
    print(f"round: {round} // Viking army: {len(war.vikingArmy)} warriors",f"and Saxon army: {len(war.saxonArmy)} warriors")
    print(war.showStatus())
    round += 1