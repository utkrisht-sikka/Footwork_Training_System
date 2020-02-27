import pygame as pg
import time,serial,cv2
'''
source of background image:https://www.wikihow.com/Coach-Badminton
source pf video function:https://www.geeksforgeeks.org/python-play-a-video-using-opencv/
'''
emergency=False#to quit during the training
d=2
try:
    arduino=serial.Serial('COM5',timeout=1)
except:
    print('Arduino not correctly communicated')


#time.sleep(2)


pg.init()
win=pg.display.set_mode((728,546))
pg.display.set_caption('FOOTWORK TRAINING SYSTEM')
run=True
font=pg.font.SysFont('Monotypecorsiva',25)
MyClock=pg.time.Clock()
bg=pg.image.load('backg.jpg')
white=(255,255,255)
skin=(255,225,172)
paleyellow=(255,165,0)
red=(255,0,255)
blue=(0,0,255)
black=(0,0,0)
a=0

#sel.rect.


l,la=[],[]
class button:
    def __init__(self,x,y,w,h):
        self.click=False
        self.rect=pg.Rect((x,y),(w,h))
        self.image=pg.Surface(self.rect.size).convert()
la.append(button(20,400,220,100))
la.append(button(260,400,220,100))
la.append(button(540,400,220,100))
l.append('nothing')
l.append(button(60,93,200,200))#1
l.append(button(270,93,200,200))#2
l.append(button(480,93,200,200))#3
l.append(button(480,303,200,200))#4
l.append(button(270,303,200,200))#5
l.append(button(60,303,200,200))#6
for i in range(1,7):
    l[i].image.fill((blue))

la[0].image.fill((skin))
la[1].image.fill((skin))
la[2].image.fill((skin))
def wait():
    '''
    waits for arduino to send string 'correct'
    '''
    global arduino,emergency
    if emergency==True:
        return
    v=arduino.readline()
    v1=v.decode()
    while True:
        press=pg.key.get_pressed()
        if press[pg.K_q]:
            emergency=True
            break
        v=arduino.readline()
        v1=v.decode()
        for i in pg.event.get():
            if i.type == pg.QUIT:
                run=False
        if v1[:-2]== 'correct' :
            break
def redi(i):
    '''
    fills the ith square with red
    '''
    if emergency==True:
        return

    l[i].image.fill((red))
    win.blit(l[i].image,l[i].rect)
    pg.display.update()
    time.sleep(0.5)
def blui(i):
    '''
    fills the ith square with blue
    '''
    if emergency==True:
        return
    l[i].image.fill((blue))
    win.blit(l[i].image,l[i].rect)
    pg.display.update()
    time.sleep(0.5)

def Reversed():

    win.fill((black))
    global arduino,emergency
    var='3'
    vid('vidReversed.3gpp')
    arduino.write(var.encode()) #send '3'
    for i in range(1,7):
        l[i].image.fill((blue))
        win.blit(l[i].image,l[i].rect)
    pg.display.update()
    right()
    redi(3)
    wait()
    blui(3)
    left()
    redi(5)
    wait()
    blui(5)
    left()
    redi(4)
    wait()
    blui(4)
    right()
    redi(6)
    wait()
    blui(6)
    emergency=False
    time.sleep(d)
def right():
    '''
    instructes that now right leg has to be placed
    '''
    global emergency
    if emergency==True:
        return
    win.fill(pg.Color("black"), (300, 46,200,40))
    t='RIGHT LEG'
    t2='press Q to exit'
    win.blit(font.render(t,True,(paleyellow)),(300,46))
    win.blit(font.render(t2,True,(red)),(540,46))
    pg.display.update()
    time.sleep(0.25)
def left():
    '''
    instructes that now left leg has to be placed
    '''
    global emergency
    if emergency==True:
        return
    win.fill(pg.Color("black"), (300, 46,200,40))
    t='LEFT LEG'#21 spaces
    t2='press Q to exit'
    win.blit(font.render(t,True,(paleyellow)),(300,46))
    win.blit(font.render(t2,True,(red)),(540,46))
    pg.display.update()
    time.sleep(0.25)
def Springbackandforth():
    win.fill((black))
    global arduino,emergency
    #vid('vidSpringbackandforth.3gpp')
    var='2'

    arduino.write(var.encode()) #send '2'
    time.sleep(d)

    for i in range(1,7):
        l[i].image.fill((blue))
        win.blit(l[i].image,l[i].rect)
    pg.display.update()
        
    right()
    redi(2)

    wait()
    blui(2)
    left()
    redi(1)

    wait()
    blui(1)
    left()
    redi(5)

    wait()
    blui(5)
    right()
    redi(4)

    wait()
    blui(4)
    right()
    redi(3)

    wait()
    blui(3)
    left()
    redi(2)

    wait()
    blui(2)
    right()
    redi(5)

    wait()
    blui(5)
    left()
    redi(6)

    wait()
    emergency=False
    time.sleep(d)
    
def Behindtheback():
    win.fill((black))
    global arduino,emergency
    vid('vidBehindtheback.3gpp')
    var='1'

    arduino.write(var.encode()) #send '1'

    for i in range(1,7):
        l[i].image.fill((blue))
        win.blit(l[i].image,l[i].rect)
    pg.display.update()

    right()
    redi(5)
    wait()
    blui(5)
    left()
    redi(6)
    wait()
    blui(6)
    right()
    redi(3)
    wait()
    blui(3)
    right()
    redi(5)
    blui(5)
    emergency=False
    time.sleep(d)


def vid(a):
    '''
    plays the video of the respective practice set
    a is name of the video file
    '''
    mat = cv2.VideoCapture(a)
    if mat.isOpened()== False:
        print("Cannot start the video")
    while mat.isOpened():
        check, pic = cap.read()
        if check == True:
            cv2.imshow('Frame', pic)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    mat.release()
    cv2.destroyAllWindows()


sel=la[0]
sel.image.fill(paleyellow)
def g_e_l():
    '''
    this function processes the action of pressing left,right keys and space bar
    '''
    global sel,a,arduino

    pg.key.set_repeat(1)
    press=pg.key.get_pressed()
    if press[pg.K_LEFT]:
        sel.image.fill((skin))
        if a==0:
            a=2

        else:
            a=a-1
        sel=la[a]
        sel.image.fill(paleyellow)
        time.sleep(0.5)
    elif press[pg.K_RIGHT]:
        sel.image.fill(skin)
        if a==2:
            a=0
        else:
            a=a+1
        sel=la[a]
        sel.image.fill(paleyellow)
        time.sleep(0.5)
    if press[pg.K_SPACE]:
        if a==0:
            Behindtheback()
            var='1'
            time.sleep(1)
        elif a==1:
            Springbackandforth()
            var='2'

            arduino.write(var.encode()) #send '2'
        elif a==2:
            Reversed()
            var='3'
            time.sleep(1)

while run:
    win.blit(bg,(0,0))
    win.blit(la[0].image,la[0].rect)
    win.blit(la[1].image,la[1].rect)
    win.blit(la[2].image,la[2].rect)
    g_e_l()
    t1,t2,t3='Behind the back','Sprint back and forth','Reversed'
    win.blit(font.render(t1,True,(0,0,0)),(40,410))
    win.blit(font.render(t2,True,(0,0,0)),(270,410))
    win.blit(font.render(t3,True,(0,0,0)),(580,410))
    pg.display.update()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run=False
    MyClock.tick(60)
pg.quit()

