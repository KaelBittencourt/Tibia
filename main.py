import pyautogui as pg
import keyboard

REGION_BATTLE = (1746, 486, 171, 44)
REGION_LOOT = (779, 335, 188, 197)

def check_battle():
    return pg.locateOnScreen('imgs/region_battle.PNG', region=REGION_BATTLE)

def kill_monster():
    while True:
        keyboard.wait('h')
        
        is_battle = check_battle()
        if is_battle == None:
            print('entrei aqui')
            pg.press('space')
            
            # Verifica se ainda estiver com o monstro vivo ele não passa para o proximo target
            while pg.locateOnScreen('imgs/red_target.png', confidence=0.7, region=REGION_BATTLE) != None: 
                print('esperando o mostro morrer')
            print('procurando outro monstro')
            # ---------------------------------------
        print(is_battle)
#kill_monster()


def get_loot():
    loot = pg.locateAllOnScreen('imgs/monster_dead.png', confidence=0.7, region=REGION_LOOT)
    print('loot >>>>>>', loot)
    
keyboard.wait('h')
get_loot