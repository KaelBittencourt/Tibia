import pyautogui as pg
import constants

def eat_food():
    pg.press('f12')
    print('Comendo...')


def hole_down(should_down):
    if should_down:
        box = pg.locateOnScreen('imgs/hole_down.png', confidence = 0.8)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x, y)
            pg.click()
            pg.sleep(5)


def hole_up(should_up, img_anchor, plus_x, plus_y):
    if should_up:
        box = pg.locateOnScreen(img_anchor, confidence=0.8)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x + plus_x, y + plus_y, 3)
            pg.press('f4')
            pg.click()
            

def check_status(name, delay, x, y, rgb, button_name):
    print(f'checando {name}...')
    pg.sleep(delay)
    if pg.pixelMatchesColor(x, y, rgb):
        pg.press(button_name)
        
        
def check_battle():
    return pg.locateOnScreen('imgs/region_battle.PNG', region=constants.REGION_BATTLE)