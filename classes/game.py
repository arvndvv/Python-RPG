import random
class bcolors:
    header= '\033[95m'
    okblue= '\033[94m'
    okgreen= '\033[92m'
    warning= '\033[93m'
    fail= '\033[91m'
    endc = '\033[0m'
    bold='\033[1m'
    underline='\033[4n'
    lightgrey='\033[37m'
    lightgreen='\033[92m'
    purple='\033[96m'
    orange='\033[43m'
    cyan='\033[36m'
class person:
    
    def __init__(self,hp,mp,atk,df,magic,name):
        
        self.name=name
        self.maxhp=hp
        self.hp=hp
        self.maxmp=mp
        self.mp=mp
        self.atkl=atk-20
        self.atkh=atk
        self.df=df
        self.magic=magic
        self.actions=['Attack','Magic']
    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)
    
    def get_attack(self):
        return self.atkh
        
    def get_defence(self):
        return self.df

  
    
    def generate_spell_damage(self,i):
        mgl=self.magic[i]["dmg"]-10
        mgh=self.magic[i]["dmg"]
        return random.randrange(mgl,mgh)
    
    def take_damage(self,dmg):
        self.hp-=dmg
        if self.hp<0:
            self.hp=0
        return self.hp
    
    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp
    
    def get_maxhp(self):
        return self.maxhp
    
    def get_mp(self):
        return self.mp
    
    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self,cost):
        self.mp-=cost

    def get_spellname(self,i):
        return self.magic[i]["name"]

    def get_spell_mpcost(self,i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i=1
        print("Actions")
        for item in self.actions:
            print(str(i)+":",item)
            i+=1

    def choose_magic(self):
        i=1
        print("Magics")
        for spell in self.magic:
            print(str(i)+":",spell["name"],"(cost:",str(spell["cost"])+")")
            i+=1