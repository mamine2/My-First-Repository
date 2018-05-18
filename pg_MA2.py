import pyautogui as pg
import time

pg.hotkey('winleft','ctrl','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.2)
pg.hotkey('winleft','up')
pg.typewrite('jay ajayi is the most average running back in the nfl\n',0.1)

time.sleep(2)

pg.hotkey('ctrl','t')
pg.typewrite('Why have the Packers sucked this entire year?\n',0.1)

time.sleep(2)

pg.hotkey('ctrl','t')
pg.typewrite('netflix.com\n',0.1)
time.sleep(1)
pg.hotkey('tab')
time.sleep(1)
pg.hotkey('tab')
time.sleep(1)
pg.hotkey('enter')
