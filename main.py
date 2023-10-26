import pyautogui as pg
import actions
import constants
import json
from pynput.keyboard import Listener
from pynput import keyboard
import threading

def kill_monster():
    while actions.check_battle() == None:
        print('Matando os Monstros')
        if event_th.is_set():
            return
        pg.press('space')
        while pg.locateOnScreen('imgs/red_target.png', confidence=0.7, region=constants.REGION_BATTLE) != None:
            if event_th.is_set():
                return
            print('esperando o mostro morrer')
        print('procurando outro monstro')


def get_loot():
    loot = pg.locateAllOnScreen('imgs/monster_dead.png', confidence=0.9, region=constants.REGION_LOOT)
    for box in loot:
        x, y = pg.center(box)
        pg.moveTo(x, y)
        pg.click(button="right")

def go_to_flag(path, wait):
    flag = pg.locateOnScreen(path, confidence=0.8, region=constants.REGION_MAP)
    if flag:
        x, y = pg.center(flag)
        if event_th.is_set():
            return
        pg.moveTo(x, y)
        pg.click()
        pg.sleep(wait)

def check_player_position():
    return pg.locateOnScreen('imgs/point_player.png', confidence=0.8, region=constants.REGION_MAP)
    
def run():
    with open(f'{constants.FOLDER_NAME}/infos.json', 'r') as file:
        data = json.loads(file.read())
    for item in data:
        if event_th.is_set():
            return
        kill_monster()
        if event_th.is_set():
            return
        pg.sleep(1)
        get_loot()
        if event_th.is_set():
            return
        go_to_flag(item['path'], item['wait'])
        if event_th.is_set():
            return
        if check_player_position():
            kill_monster()
            if event_th.is_set():
                return
            pg.sleep(1)
            get_loot()
            if event_th.is_set():
                return
            go_to_flag(item['path'], item['wait'])
        actions.eat_food()
        actions.hole_down(item['down_hole'])
        if event_th.is_set():
            return        
        actions.hole_up(item['up_hole'], f'{constants.FOLDER_NAME}/anchor_floor_2.png', 430, 0)
        actions.hole_up(item['up_hole'], f'{constants.FOLDER_NAME}/anchor_floor_3.png', 130, 130)

def key_code(key):
    print('key ->', key)
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.delete:
        th_run.start()
        
global event_th
event_th = threading.Event()
th_run = threading.Thread(target=run)

with Listener(on_press=key_code) as listener:
    listener.join()

keyboard.wait('h')
run()