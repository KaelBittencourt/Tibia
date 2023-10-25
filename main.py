import pyautogui as pg
import keyboard

REGION_BATTLE = (1746, 486, 171, 44)
REGION_LOOT = (779, 335, 188, 197)

POSITION_MANA_FULL = (914, 40)
COLOR_MANA = (0, 56, 116)

POSITION_LIFE = (15, 47)
COLOR_GREEN_LIFE = (0, 174, 0)

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
    loot = pg.locateAllOnScreen('imgs/monster_dead.png', confidence=0.9, region=REGION_LOOT)
    for box in loot:
        x, y = pg.center(box)
        pg.moveTo(x, y)
        pg.click(button="right")
    


def check_status(name, delay, x, y, rgb, button_name):
    print(f'checando {name}...')
    pg.sleep(delay)
    if pg.pixelMatchesColor(x, y, rgb):
        pg.press(button_name)



def eat_food():
    pg.press('f12')
    print('Comendo...')



#pg.displayMousePosition()

# check_status('mana', 5, *POSITION_MANA_FULL, COLOR_MANA, 'F3')

keyboard.wait('h')
check_status('life', 1, *POSITION_LIFE, COLOR_GREEN_LIFE, 'F3')

