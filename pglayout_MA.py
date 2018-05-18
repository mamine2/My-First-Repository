import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.4)

pg.hotkey('winleft','up')
time.sleep(3)

pg.moveTo(135, 44, 1.5)
pg.click()
pg.typewrite('Aaron Rodgers Injury\n','.4')
pg.moveTo(370, 185, 1.5)
pg.click()
