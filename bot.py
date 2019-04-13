#import pyscreenshot as ImageGrab
from PIL import ImageGrab
import pyautogui
import time

#guide: https://www.youtube.com/watch?v=bf_UOFFaHiY
#part2: https://www.youtube.com/watch?v=5Jwd69MRYwg

#spillet køres på http://www.trex-game.skipser.com/

#cordinaterne på tingene på skærmen
class Cordinates():

    #cordi til replay button, når man dør
    replayBtn = (340,390)
    dinosaur = (171,395)


#Bruger pyautogui til at klikke et på replaybtn coordinater på skærmen
def restartGame():
    pyautogui.click(Cordinates.replayBtn);


#func til at simulere space
def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('space');


restartGame()
time.sleep(1)
pressSpace()