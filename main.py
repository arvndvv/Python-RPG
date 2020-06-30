import time
import sys
import os
import random
from classes.game import person,bcolors
usrname=input(bcolors.lightgreen+"Your Name:"+bcolors.endc)
os.system('cls' if os.name == 'nt' else 'clear')
def enemystat():
    
    print(bcolors.fail+bcolors.bold+enemy_name+bcolors.endc)
    print(bcolors.purple)
    sys.stdout.write("HP:"+str(enemy.get_hp())+"/"+str(enemy.get_maxhp())+"\tMP:"+str(enemy.get_mp())+"/"+str(enemy.get_maxmp()))
    print("")
    sys.stdout.write("ATK:"+str(enemy.get_attack())+"\t\tDF:"+str(enemy.get_defence()))
    print(bcolors.endc+"\n")

def playerstat():
    playerhp=player.get_hp()
    playermaxhp=player.get_maxhp()
    playermp=player.get_mp()
    playermaxmp=player.get_maxmp()
    atk=player.get_attack()
    df=player.get_defence()
    print(bcolors.lightgreen+bcolors.bold+player.get_name().upper()+bcolors.endc)

    print(bcolors.lightgrey+"Witcher"+bcolors.endc)
    for j in range(0,ul):
        sys.stdout.write('-')
    print(""+bcolors.purple)
    sys.stdout.write("HP:"+str(playerhp)+"/"+str(playermaxhp)+"\tMP:"+str(playermp)+"/"+str(playermaxmp))
    print("")
    sys.stdout.write("ATK:"+str(atk)+"\t\tDF:"+str(df))
    print("\n"+bcolors.endc)

intro=['You are a Witcher, wandering in the dense forest\n',
        'of Dandakaranya, Known for worst kind of monsters.\n',
        'shh! There is some movement in the bushes to the far left!\n']
magic=[{"name":"fire","cost":10,"dmg":60},
        {"name":"Thunder","cost":15,"dmg":70},
        {"name":"water","cost":5,"dmg":30},
        {"name":"drone","cost":10,"dmg":55}]
enemies=["Evil","ShadowLeg","Deadeye","Zombie","Decay","Crypt","Locado","DarkWitch","Snape","NullMouth"]

e=random.randrange(0,len(enemies))
hps=[460,730,550,670,700,860,900,930,1100,1200]
mps=[10,15,20,25,30,35,40,45,50,55]
atks=[20,25,30,35,40,45,50,55,60,65]
dfs=[5,7,10,12,15,20,22,25,27,30]
ehp=hps[e]
emp=mps[e]
eatk=atks[e]
edf=dfs[e]
ul=len(usrname)
if ul<7:
    ul=7
player=person(560,70,40,36,magic,usrname)
enemy_name=enemies[e]
enemy = person(ehp,emp,eatk,edf,magic,enemy_name)
playerhp=player.get_hp()
playermaxhp=player.get_maxhp()
playermp=player.get_mp()
playermaxmp=player.get_maxmp()
atk=player.get_attack()
df=player.get_defence()
running=True
i=0
print(bcolors.lightgreen+bcolors.bold+player.get_name().upper()+bcolors.endc)

print(bcolors.lightgrey+"Witcher"+bcolors.endc)
for j in range(0,ul):
    sys.stdout.write('-')
print(""+bcolors.purple)
sys.stdout.write("HP:"+str(playerhp)+"/"+str(playermaxhp)+"\tMP:"+str(playermp)+"/"+str(playermaxmp))
print("")
sys.stdout.write("ATK:"+str(atk)+"\t\tDF:"+str(df))
print("\n"+bcolors.endc)
for introline in intro:
    for l in introline:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0)
time.sleep(0.6)
player.take_damage(50)
playerstat()
print(bcolors.fail+bcolors.bold+"\nAN ENEMY ATTACKS!"+bcolors.endc)
time.sleep(1)
print("=================")
print(bcolors.fail+bcolors.bold+enemy_name+bcolors.endc)
print(""+bcolors.purple)
sys.stdout.write("HP:"+str(enemy.get_hp())+"/"+str(enemy.get_maxhp())+"\tMP:"+str(enemy.get_mp())+"/"+str(enemy.get_maxmp()))
print("")
sys.stdout.write("ATK:"+str(enemy.get_attack())+"\t\tDF:"+str(enemy.get_defence()))
print(bcolors.endc+"\n")

while running:
    
    player.choose_action()
    choice = input(bcolors.okblue+"Choose action:"+bcolors.endc)
    index=int(choice)-1
    if index==0:
        dmg=player.generate_damage()
        enemy.take_damage(dmg)
        print("")
        print(bcolors.okgreen+"You have attacked enemy causing "+str(dmg)+" damage!\n"+bcolors.endc)
        print("=================")
        if enemy.get_hp()==0:
            print(bcolors.cyan+enemy_name+" was killed! You won!")
            break
            running=False
        else:
            enemystat()
    elif index==1:
        player.choose_magic()
        magic_choice=int(input("Choose:"))-1
        magic_dmg=player.generate_spell_damage(magic_choice)
        spell=player.get_spellname(magic_choice)
        cost=player.get_spell_mpcost(magic_choice)
        current_mp=player.get_mp()
        if cost>current_mp:
            print(bcolors.fail+"\n Not enough magic points!")
            continue
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.okgreen+"\nYou used "+spell+" spell to cause "+str(magic_dmg)+" damage!"+bcolors.endc)
        enemystat()
    else:
        print("wrong Choice!")
    time.sleep(2)

    enemy_choice=0
    if enemy_choice==0:
        enemy_dmg=enemy.generate_damage()
        player.take_damage(enemy_dmg)
        print(bcolors.warning+enemy_name+" Attacked causing "+str(enemy_dmg)+" damage\n"+bcolors.endc)
        print("=================")
        if player.get_hp()==0:
            print(bcolors.fail+"You were killed! You Loss!")
            break
            running=False
        else:
            playerstat()
    elif enemy_choice==1:
        print("Not Available!")
    else:
        print("wrong Choice!")