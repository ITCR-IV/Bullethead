'''
****************************************************************************************************************
    Instituto Tecnológico de Costa Rica
    Ingeniería en Computadores
                
    Lenguaje y Versión: Python 3.8.3

    Autor: Ignacio Vargas Campos

    Versión: 1.0

    Fecha de última modificación: 17 de julio 2020
****************************************************************************************************************
'''

from tkinter import *
from random import *
from unidecode import unidecode
import pygame
import os

#mi_auto_doc()
def mi_auto_doc():
    print("switch_screen(newScreen, level=1):",switch_screen.__doc__)
    print("display_positions(scoreboard,position=1):",display_positions.__doc__)
    print("display_names(scoreboard,position=1):",display_names.__doc__)
    print("display_scores(scoreboard,position=1):",display_scores.__doc__)
    print("score_position(score,scoreboard):",score_position.__doc__)
    print("check_enemy_collisions(enemyType, enemy, bulletsList=bullets):",check_enemy_collisions.__doc__)
    print("check_player_collisions(bulletsList=bullets):",check_player_collisions.__doc__)
    print("enemy_spawning(enemyType,amount,delay):",enemy_spawning.__doc__)
    print("level_instructions(level)",level_instructions.__doc__)
    print("animate_player(which):",animate_player.__doc__)
    print("animate_missiles(which):",animate_missiles.__doc__)
    print("animate_commons(which):",animate_commons.__doc__)
    print("animate_crushers():",animate_crushers.__doc__)
    print("animate_bullets():",animate_bullets.__doc__)
    print("move_player():",move_player.__doc__)
    print("move_missile(missile):",move_missile.__doc__)
    print("move_common(common):",move_common.__doc__)
    print("move_crusher(crusher):",move_crusher.__doc__)
    print("move_bullet(bullet):",move_bullet.__doc__)

#misc functions
seed()

def quit_application():
    root.destroy()
    pygame.mixer.quit()
    
def load_alphanums(alphanumDic,alphanums="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    if alphanums=="":
        path=os.path.join('imgs','characters','dot.png')
        alphanumDic['.']=PhotoImage(file=path)
        print("loaded alphanumerical characters")
        return
    else:
        path=os.path.join('imgs','characters',alphanums[0]+'.png')
        alphanumDic[alphanums[0]]=PhotoImage(file=path)
        load_alphanums(alphanumDic,alphanums[1:])

def load_img(file):
    '''
    Parameter: file name
    
    Return: PhotoImage object of specified image

    Restrictions: Image must be in 'imgs' folder, which must be in same folder as program, and it's name must be given as a string
    '''
    print("loaded "+file)
    path=os.path.join('imgs',file)
    image=PhotoImage(file=path)
    return image

def empty_list(emptiedList):
    if emptiedList==[]:
        return
    else:
        emptiedList.pop(0)
        empty_list(emptiedList)

def lenn(someList):
    '''
    Parameters: List or string
    
    Return: Length of that list or string

    Restrictions: Must only pass lists or strings
    '''
    if someList==[] or someList=="":
        return 0
    else:
        return 1+lenn(someList[1:])

def cancel_all(canvas,iterableList,afterList):
    if iterableList==[]:
        afterList=[]
    else:
        canvas.after_cancel(iterableList[0])
        cancel_all(canvas,iterableList[1:],afterList)

def limit_entry(stringVar,length):
    c = unidecode(stringVar.get()[0:length].upper().replace(' ','')) #limit to length, uppercase, and no spaces, and unidecode removes accents
    stringVar.set(c)

#file handling
def read_file(fileName):
    '''
    Parameters: fileName
    
    Return: List where each element is a line in the .txt and ends with \n character

    Restrictions: File must be in the same folder as main program and name given as string
    '''
    try:
        f=open(fileName, 'r')
        readList=f.readlines()
        f.close()
    except:
        f=open(fileName,'w')
        readList=[]
        f.close()
    return readList 
    
def save_file(fileName, glist):
    '''
    Parameters: fileName, list of data
    
    Return: None

    Restrictions: List elements must be strings, each representing a line and they must end on \n character
    '''
    #list must be [name,score,name,score]... for scores
    #all names and scores must end in " \n"
    try:
        f=open(fileName, 'w')
        f.writelines(glist)
        f.close()
        print(fileName[:-4]+" saved succesfully!") #[-4] para quitar el '.txt'
    except:
        print("Error while trying to save "+fileName[-4]+" data")
    return

#Main widget
root = Tk()

#global variables
height=600
width=600
screen='menu' # options: 'menu', 'game', 'help', 'credits', 'scores', 'pause'

pauseImg=None
resumeButton=None
quitButton=None
backMenuButton=None
#create main window
root.title('Bullethead')
root.minsize(width,height)
root.resizable(width=NO,height=NO)

#canvas creation
menuCanvas=     Canvas(root,width=width,height=height,bg='white')
gameCanvas=     Canvas(root,width=width,height=height,bg='white')
helpCanvas=     Canvas(root,width=width,height=height,bg='white')
scoresCanvas=   Canvas(root,width=width,height=height,bg='white')
creditsCanvas=  Canvas(root,width=width,height=height,bg='white')
levelsCanvas=   Canvas(root,width=width,height=height,bg='white')

#image loading
menuScreenImg=      load_img('screen menu.png')
gameScreenImg=      load_img('game bg.png')
scoresScreenImg=    load_img('screen scores.png')
helpScreenImg=      load_img('screen help.png')
creditsScreenImg=   load_img('screen credits.png')
pauseScreenImg=     load_img('screen pause.png')
levelsScreenImg=    load_img('screen level select.png')
gameOverScreenImg=  load_img('screen game over.png')
finishedScreenImg=  load_img('screen finished.png')

playButtonImg=      load_img('button PLAY.png')
scoresButtonImg=    load_img('button SCORES.png')
helpButtonImg=      load_img('button HELP.png')
creditsButtonImg=   load_img('button CREDITS.png')
backButtonImg=      load_img('button BACK.png')
pauseButtonImg=     load_img('button PAUSE.png')
resumeButtonImg=    load_img('button RESUME.png')
quitButtonImg=      load_img('button QUIT.png')
lvl1ButtonImg=      load_img('button LVL1.png')
lvl2ButtonImg=      load_img('button LVL2.png')
lvl3ButtonImg=      load_img('button LVL3.png')
keyButtonImg=       load_img('button KEY.png')
backMenuButtonImg=  load_img('button BACK TO MENU.png')
musicMenuButtonImg=     load_img('button MUSIC MENU.png')
musicGameButtonImg=     load_img('button MUSIC GAME.png')
musicOffMenuButtonImg=  load_img('button MUSIC OFF MENU.png')
musicOffGameButtonImg=  load_img('button MUSIC OFF GAME.png')
sfxMenuButtonImg=       load_img('button SFX MENU.png')
sfxGameButtonImg=       load_img('button SFX GAME.png')
sfxOffMenuButtonImg=    load_img('button SFX OFF MENU.png')
sfxOffGameButtonImg=    load_img('button SFX OFF GAME.png')

alphanums={} #dictionary goes [a,b,c,...,y,z,0,1,2,...,8,9,.]

#button creation
def play_button():
    return Button(menuCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=lambda: switch_screen('levels'),image=playButtonImg)

def lvl1_button():
    return Button(levelsCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=lambda: switch_screen('game', 1) if name.get().isalnum() else levelsCanvas.create_text(300,375,text="   please input a name using\nonly alphanumerical characters",fill='#ff3b3b',font=("Courier New",12)),image=lvl1ButtonImg)
def lvl2_button():
    return Button(levelsCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=lambda: switch_screen('game', 2) if name.get().isalnum() else levelsCanvas.create_text(300,375,text="   please input a name using\nonly alphanumerical characters",fill='#ff3b3b',font=("Courier New",12)),image=lvl2ButtonImg)
def lvl3_button():
    return Button(levelsCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=lambda: switch_screen('game', 3) if name.get().isalnum() else levelsCanvas.create_text(300,375,text="   please input a name using\nonly alphanumerical characters",fill='#ff3b3b',font=("Courier New",12)),image=lvl3ButtonImg)

def scores_button():
    return Button(menuCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=lambda: switch_screen('scores'),image=scoresButtonImg)

def help_button():
    return Button(menuCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=lambda: switch_screen('help'),image=helpButtonImg)

def jump_button():
    return Button(helpCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=push_jump_button,image=keyButtonImg,text=jumpKey,compound='center',font=("Courier New",18-(lenn(jumpKey)*2)))
def shoot_button():
    return Button(helpCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=push_shoot_button,image=keyButtonImg,text=shootKey,compound='center',font=("Courier New",18-(lenn(jumpKey)*2)))
def right_button():
    return Button(helpCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=push_right_button,image=keyButtonImg,text=rightKey,compound='center',font=("Courier New",18-(lenn(jumpKey)*2)))
def left_button():
    return Button(helpCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=push_left_button,image=keyButtonImg,text=leftKey,compound='center',font=("Courier New",18-(lenn(jumpKey)*2)))

def credits_button():
    return Button(menuCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=lambda: switch_screen('credits'),image=creditsButtonImg)

def back_button(specifyCanvas):
    return Button(specifyCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=lambda: switch_screen('menu'),image=backButtonImg)

def pause_button():
    return Button(gameCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=lambda: pause_game('pause'),image=pauseButtonImg)

def resume_button():
    return Button(gameCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=lambda: pause_game('resume'),image=resumeButtonImg)

def back_menu_button():
    return Button(gameCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=exit_game,image=backMenuButtonImg)

def quit_button():
    return Button(gameCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=exit_game,image=quitButtonImg)

musicButtons=[]
def music_button(specifyCanvas):
    if specifyCanvas==gameCanvas:
        return Button(specifyCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=toggle_music,image=musicGameButtonImg)
    else: 
        return Button(specifyCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=toggle_music,image=musicMenuButtonImg)

sfxButtons=[]
def sfx_button(specifyCanvas):
    if specifyCanvas==gameCanvas:
        return Button(specifyCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=toggle_sfx,image=sfxGameButtonImg)
    else:
        return Button(specifyCanvas,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,command=toggle_sfx,image=sfxMenuButtonImg)

#Screen loading/switching
def load_buttons():

    #music and sound buttons
    musicButtonMenu=    music_button(menuCanvas)
    musicButtonScores=  music_button(scoresCanvas)
    musicButtonHelp=    music_button(helpCanvas)
    musicButtonCredits= music_button(creditsCanvas)
    musicButtonLevels=  music_button(levelsCanvas)
    musicButtonGame=    music_button(gameCanvas)

    musicButtonMenu.place(anchor=NW,relx=557/width,rely=9/height)
    musicButtonHelp.place(anchor=NW,relx=557/width,rely=9/height)
    musicButtonCredits.place(anchor=NW,relx=557/width,rely=9/height)
    musicButtonLevels.place(anchor=NW,relx=557/width,rely=9/height)
    musicButtonScores.place(anchor=NW,relx=557/width,rely=9/height)
    musicButtonGame.place(anchor=NW,relx=557/width,rely=9/height) #557,9

    sfxButtonMenu=      sfx_button(menuCanvas)
    sfxButtonScores=    sfx_button(scoresCanvas)
    sfxButtonHelp=      sfx_button(helpCanvas)
    sfxButtonCredits=   sfx_button(creditsCanvas)
    sfxButtonLevels=    sfx_button(levelsCanvas)
    sfxButtonGame=      sfx_button(gameCanvas)
    
    sfxButtonMenu.place(anchor=NW,relx=573/width,rely=9/height)
    sfxButtonHelp.place(anchor=NW,relx=573/width,rely=9/height)
    sfxButtonCredits.place(anchor=NW,relx=573/width,rely=9/height)
    sfxButtonLevels.place(anchor=NW,relx=573/width,rely=9/height)
    sfxButtonScores.place(anchor=NW,relx=573/width,rely=9/height)
    sfxButtonGame.place(anchor=NW,relx=573/width,rely=9/height) #music x+=16

    musicButtons.extend([musicButtonMenu,musicButtonScores,musicButtonHelp,musicButtonCredits,musicButtonLevels,musicButtonGame])
    sfxButtons.extend([sfxButtonMenu,sfxButtonScores,sfxButtonHelp,sfxButtonCredits,sfxButtonLevels,sfxButtonGame])
    
    #game
    pauseButton=pause_button()
    pauseButton.place(anchor=NW,relx=543/width,rely=11/height)#545, 11 (-2 x)

    #levels
    lvl1Button=lvl1_button()
    lvl2Button=lvl2_button()
    lvl3Button=lvl3_button()

    lvl1Button.place(relx=161/width,rely=267/height,anchor=NW)
    lvl2Button.place(relx=282/width,rely=267/height,anchor=NW)
    lvl3Button.place(relx=404/width,rely=267/height,anchor=NW)

    backButton=back_button(levelsCanvas)
    backButton.place(anchor=NW,relx=227/width,rely=491/height)

    #menu
    playButton=play_button()
    scoresButton=scores_button()
    helpButton=help_button()
    creditsButton=credits_button()

    playButton.place(anchor=NW,relx=195/width,rely=243/height) #195,245 coords for button (y-2)
    scoresButton.place(anchor=NW,relx=223/width,rely=341/height) #x=223 y=343
    helpButton.place(anchor=NW,relx=223/width,rely=421/height) #y=423
    creditsButton.place(anchor=NW,relx=223/width,rely=503/height) #y=505

    #scores
    backButton=back_button(scoresCanvas)
    backButton.place(anchor=NW,relx=227/width,rely=491/height) #227,493 (y-2)
    
    #help
    global jumpButton,shootButton,rightButton,leftButton
    jumpButton=jump_button()
    shootButton=shoot_button()
    rightButton=right_button()
    leftButton=left_button()

    jumpButton.place(anchor=NW,relx=357/width,rely=322/height)
    shootButton.place(anchor=NW,relx=251/width,rely=322/height)
    rightButton.place(anchor=NW,relx=291/width,rely=366/height)
    leftButton.place(anchor=NW,relx=251/width,rely=366/height)

    backButton=back_button(helpCanvas)
    backButton.place(anchor=NW,relx=227/width,rely=491/height)

    #credits
    backButton=back_button(creditsCanvas)
    backButton.place(anchor=NW,relx=227/width,rely=491/height)

def load_game(level):
    gameCanvas.pack(expand=True)
    
    gameCanvas.create_image(2,0,anchor=NW,image=gameScreenImg)
    
    gameCanvas.focus_set()
    gameCanvas.bind("<KeyPress>", keydown)
    gameCanvas.bind("<KeyRelease>", keyup)

    create_player()
    create_healths()

    global second
    if level==1:
        second=0
        level_instructions(1)
    elif level==2:
        second=4
        level_instructions(2)
    elif level==3:
        second=4
        level_instructions(3)

    global scoreText,score
    score=0
    scoreText=gameCanvas.create_text(122,577,anchor=NW,text=score,fill='white',font=("Courier New",11))#122,582
    update_score()

    display_name_game(name.get(),lenn(name.get()))

    global timerText,timer
    timer=0.000
    gameCanvas.create_text(width-130,height-60,anchor=NW,text="Time played:",fill='white',font=("Courier New",11))
    timerText=gameCanvas.create_text(width-130,height-40,anchor=NW,text=timer,fill='white',font=("Courier New",11))
    update_timer()
    animate_player('movement')
    animate_player('frames')
    animate_missiles('movement')
    animate_missiles('frames')
    animate_commons('movement')
    animate_commons('frames')
    animate_crushers()
    animate_health_frames()
    animate_bullets()
    
def load_levels():
    levelsCanvas.pack(expand=True)
    levelsCanvas.create_image(2,0,anchor=NW,image=levelsScreenImg)

    length=18
    nameEntry=Entry(master=levelsCanvas,bg='white',font=("Courier New",13),fg='black',textvariable=name,width=length)
    nameEntry.place(relx=1/2,rely=1/3,anchor=CENTER)
    nameEntry.focus()
    name.trace("w",lambda name, index, mode, stringVar=name: limit_entry(stringVar,length))
    
def load_menu():
    menuCanvas.pack(expand=True)
    menuCanvas.create_image(2,0,anchor=NW,image=menuScreenImg)

def load_scores():
    scoresCanvas.pack(expand=True)
    scoresCanvas.create_image(2,0,anchor=NW,image=scoresScreenImg)

    display_positions(scoreboard)
    display_names(scoreboard)
    display_scores(scoreboard)

def load_help():
    helpCanvas.pack(expand=True)
    helpCanvas.create_image(2,0,anchor=NW,image=helpScreenImg)

    helpCanvas.focus_set()
    helpCanvas.bind("<Key>",change_keybinding)
    
def load_credits():
    creditsCanvas.pack(expand=True)
    creditsCanvas.create_image(2,0,anchor=NW,image=creditsScreenImg)

def stop_game():
    gameCanvas.after_cancel(playerMovementAnimation)
    gameCanvas.after_cancel(playerFrameAnimation)
    gameCanvas.after_cancel(healthFrameAnimation)
    gameCanvas.after_cancel(missilesMovementAnimation)
    gameCanvas.after_cancel(missilesFrameAnimation)
    gameCanvas.after_cancel(commonsMovementAnimation)
    gameCanvas.after_cancel(commonsFrameAnimation)
    gameCanvas.after_cancel(crushersAnimation)
    gameCanvas.after_cancel(bulletsAnimation)
    gameCanvas.after_cancel(levelInstructions)
    gameCanvas.after_cancel(scoreUpdating)
    gameCanvas.after_cancel(timerUpdating)
    
def switch_screen(newScreen, level=0):
    '''
    Parameters: newScreen, level=0 (only relevant for game screen)
    
    Return: None

    Restrictions: screen must be one of 'menu','levels','game','scores','help','credits'; level will default to 0 but must be specified between 1 and 3 if newScreen is 'game', must be int
    '''
    global screen
    if screen=='menu':
        menuCanvas.delete("all")
        menuCanvas.pack_forget()
    elif screen=='levels':
        levelsCanvas.delete("all")
        levelsCanvas.pack_forget()
    elif screen=='game' or screen=='pause' or screen=='game over':
        empty_list(commons)
        empty_list(missiles)
        empty_list(crushers)
        empty_list(bullets)
        empty_list(healths)
        stop_game()
        cancel_all(gameCanvas,enemySpawning,enemySpawning)
        gameCanvas.delete("all")
        gameCanvas.pack_forget()
        play_menu_music()
    elif screen=='scores':
        scoresCanvas.delete("all")
        scoresCanvas.pack_forget()
    elif screen=='help':
        helpCanvas.delete("all")
        helpCanvas.pack_forget()
    elif screen=='credits':
        creditsCanvas.delete("all")
        creditsCanvas.pack_forget()

    if newScreen=='menu':
        load_menu()
        screen='menu'
    elif newScreen=='levels':
        load_levels()
        screen='levels'
    elif newScreen=='game':
        screen='game'
        if level==1:
            load_game(1)
        elif level==2:
            load_game(2)
        elif level==3:
            load_game(3)
        play_game_music()
    elif newScreen=='scores':
        load_scores()
        screen='scores'
    elif newScreen=='help':
        load_help()
        screen='help'
    elif newScreen=='credits':
        load_credits()
        screen='credits'

def pause_game(state):
    '''
    Parameters: state
    
    Return: None

    Restrictions: state must be either 'pause' or 'resume'
    '''
    global pauseImg,resumeButton,quitButton,screen

    if screen!='game' and screen!='pause':
        return
    
    if state=='pause':
        if screen=='pause':
            pause_game("resume")
        else:
            screen='pause'
            stop_game()
            pauseImg=gameCanvas.create_image(76,208,anchor=NW,image=pauseScreenImg) #73,207 (+3x, +1y)

            resumeButton=resume_button()
            resumeButton.place(anchor=NW,relx=149/width,rely=276/height) #147,227 (+2, -1)
            quitButton=quit_button()
            quitButton.place(anchor=NW,relx=314/width,rely=276/height) #313 (+1, -1) ??
        
    elif state=='resume':
        screen='game'
        animate_player('movement')
        animate_player('frames')
        animate_missiles('movement')
        animate_missiles('frames')
        animate_commons('movement')
        animate_commons('frames')
        animate_crushers()
        animate_health_frames()
        animate_bullets()
        level_instructions(currentLvl)
        update_score()
        update_timer()
        
        gameCanvas.delete(pauseImg)
        resumeButton.destroy()
        quitButton.destroy()

def exit_game():
    if screen=='game over':
        backMenuButton.destroy()
    elif screen=='pause':
        resumeButton.destroy()
        quitButton.destroy()
    switch_screen("menu")

def game_over():
    global backMenuButton,screen
    if screen=='game over': #sometimes it gets called twice in a row
        return
    else:
        screen='game over'
        stop_game()
        gameCanvas.create_image(46,107,anchor=NW,image=gameOverScreenImg) #46,107
        gameCanvas.create_text(297,269,text=score,fill='white',font=("Courier New",20)) #297,269
        check_score(name.get(),score,scoreboard)
        save_file("scoreboard.txt",scoreboard)
    
        backMenuButton=back_menu_button()
        backMenuButton.place(anchor=NW,relx=192/width,rely=353/height) #192,353
    
def finished_game():
    global backMenuButton,screen
    if screen=='game over': 
        return
    else:
        screen='game over'
        stop_game()
        gameCanvas.create_image(46,107,anchor=NW,image=finishedScreenImg) #46,107
        gameCanvas.create_text(297,269,text=score,fill='white',font=("Courier New",20)) #297,269
        check_score(name.get(),score,scoreboard)
        save_file("scoreboard.txt",scoreboard)

        backMenuButton=back_menu_button()
        backMenuButton.place(anchor=NW,relx=192/width,rely=353/height) #192,353
    
##################################################################----HELP----###########################################################################################################################################
#Keys
jumpKey=''
leftKey=''
rightKey=''
shootKey=''

#Button variables
jumpButton=None
shootButton=None
rightButton=None
leftButton=None

jumpPushed=False
shootPushed=False
rightPushed=False
leftPushed=False

#Interchangeable keys

def push_jump_button():
    global jumpPushed,shootPushed,rightPushed,leftPushed
    jumpPushed,shootPushed,rightPushed,leftPushed=True,False,False,False
    jumpButton.config(text="")
    shootButton.config(text=shootKey)
    rightButton.config(text=rightKey)
    leftButton.config(text=leftKey)
def push_shoot_button():
    global jumpPushed,shootPushed,rightPushed,leftPushed
    jumpPushed,shootPushed,rightPushed,leftPushed=False,True,False,False
    jumpButton.config(text=jumpKey)
    shootButton.config(text="")
    rightButton.config(text=rightKey)
    leftButton.config(text=leftKey)
def push_right_button():
    global jumpPushed,shootPushed,rightPushed,leftPushed
    jumpPushed,shootPushed,rightPushed,leftPushed=False,False,True,False
    jumpButton.config(text=jumpKey)
    shootButton.config(text=shootKey)
    rightButton.config(text="")
    leftButton.config(text=leftKey)
def push_left_button():
    global jumpPushed,shootPushed,rightPushed,leftPushed
    jumpPushed,shootPushed,rightPushed,leftPushed=False,False,False,True
    jumpButton.config(text=jumpKey)
    shootButton.config(text=shootKey)
    rightButton.config(text=rightKey)
    leftButton.config(text="")
    
def change_keybinding(key):
    global jumpPushed,shootPushed,rightPushed,leftPushed,jumpKey,leftKey,rightKey,shootKey
    keyPressed=key.keysym.upper()
    print(keyPressed,type(keyPressed))
    if jumpPushed:
        if keyPressed!=shootKey and keyPressed!=rightKey and keyPressed!=leftKey:
            jumpKey=keyPressed
            jumpPushed=False
            jumpButton.config(text=jumpKey)
            jumpButton.config(font=("Courier New",18-(lenn(jumpKey)*2))) #ajustar el tamaño para palabras
            options[2]=keyPressed+'\n'
            save_file('options.txt',options)

    elif shootPushed:
        if keyPressed!=jumpKey and keyPressed!=rightKey and keyPressed!=leftKey:
            shootKey=keyPressed
            shootPushed=False
            shootButton.config(text=shootKey,font=("Courier New",18-(lenn(shootKey)*2)))
            options[3]=keyPressed+'\n'
            save_file('options.txt',options)
            
    elif rightPushed:
        if keyPressed!=jumpKey and keyPressed!=shootKey and keyPressed!=leftKey:
            rightKey=keyPressed
            rightPushed=False
            rightButton.config(text=rightKey,font=("Courier New",18-(lenn(rightKey)*2)))
            options[4]=keyPressed+'\n'
            save_file('options.txt',options)
        
    elif leftPushed:
        if keyPressed!=jumpKey and keyPressed!=shootKey and keyPressed!=rightKey:
            leftKey=keyPressed
            leftPushed=False
            leftButton.config(text=leftKey,font=("Courier New",18-(lenn(leftKey)*2)))
            options[5]=keyPressed+'\n'
            save_file('options.txt',options)

#music and sounds
pygame.mixer.pre_init(43500, -16, 1, 1024)
pygame.mixer.init()

hitHurtSound=pygame.mixer.Sound('audio\Hit Hurt.wav')
laserShootSound=pygame.mixer.Sound('audio\Laser Shoot.wav')
explosionSound=pygame.mixer.Sound('audio\Explosion.wav')

maxVolume=0.5
    
def play_menu_music():
    playing=pygame.mixer.music.get_busy() #true if music playing
    pygame.mixer.music.load('audio\Menu Theme.wav')
    if playing: pygame.mixer.music.play(-1)
    print('done')
    
def play_game_music():
    playing=pygame.mixer.music.get_busy()
    pygame.mixer.music.load('audio\Game Theme.wav')
    if playing: pygame.mixer.music.play(-1)

def toggle_music(buttonList=musicButtons):
    if buttonList==[]:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            options[0]='OFF\n'
        else:
            pygame.mixer.music.play(-1)
            options[0]='ON\n'
        save_file('options.txt',options)
    else:
        if buttonList[0].cget("image")==str(musicMenuButtonImg):
            buttonList[0].config(image=musicOffMenuButtonImg)
        elif buttonList[0].cget("image")==str(musicOffMenuButtonImg):
            buttonList[0].config(image=musicMenuButtonImg)
        elif buttonList[0].cget("image")==str(musicGameButtonImg):
            buttonList[0].config(image=musicOffGameButtonImg)
        elif buttonList[0].cget("image")==str(musicOffGameButtonImg):
            buttonList[0].config(image=musicGameButtonImg)
        toggle_music(buttonList[1:])
        
def sfx_on():
    hitHurtSound.set_volume(maxVolume)
    laserShootSound.set_volume(maxVolume)
    explosionSound.set_volume(maxVolume)

def sfx_off():
    hitHurtSound.set_volume(0)
    laserShootSound.set_volume(0)
    explosionSound.set_volume(0)
    
def toggle_sfx(buttonList=sfxButtons):
    if buttonList==[]:
        #print(explosionSound.get_volume())
        if explosionSound.get_volume()==maxVolume:
            sfx_off()
            options[1]='OFF\n'
        else:
            sfx_on()
            options[1]='ON\n'
        save_file('options.txt',options)
    else:
        if buttonList[0].cget("image")==str(sfxMenuButtonImg):
            buttonList[0].config(image=sfxOffMenuButtonImg)
        elif buttonList[0].cget("image")==str(sfxOffMenuButtonImg):
            buttonList[0].config(image=sfxMenuButtonImg)
        elif buttonList[0].cget("image")==str(sfxGameButtonImg):
            buttonList[0].config(image=sfxOffGameButtonImg)
        elif buttonList[0].cget("image")==str(sfxOffGameButtonImg):
            buttonList[0].config(image=sfxGameButtonImg)
        toggle_sfx(buttonList[1:])

##################################################################----SCOREBOARD----###########################################################################################################################################
scoreboard=[]

def display_positions(scoreboard,position=1):
    '''
    Parameters: scoreboard, position=1
    
    Return: None

    Restrictions: scoreboard must be a list that goes [name,score,name,score,...] and position shouldn't be specified
    '''
    #characters are 12x19
    if scoreboard==[]:
        return
    else:
        posY=118+(position-1)*33
        if position==10:
            scoresCanvas.create_image(113, posY, anchor=NW, image=alphanums["1"])
            scoresCanvas.create_image(126, posY, anchor=NW, image=alphanums["0"])
            scoresCanvas.create_image(139, posY, anchor=NW, image=alphanums["."])
        else:
            scoresCanvas.create_image(113, posY, anchor=NW, image=alphanums[str(position)]) #113,118
            scoresCanvas.create_image(126, posY, anchor=NW, image=alphanums["."])
            display_positions(scoreboard[2:],position+1)

def display_names_aux(name,length,position,character=0):
    '''
    Parameters: name, length, position, character=0
    
    Return: None

    Restrictions: name must be all caps, alphanumeric, and no accents; length must be the length of the name string, position must be int
    '''
    if name=='\n': #strings terminan en '\n'
        return
    else:
        #names centered on 266 (-7=259)
        posY=118+(position-1)*33
        if length%2==0:
            posX=266-(length/2-character)*13
        else:
            posX=259-((length-1)/2-character)*13
        scoresCanvas.create_image(posX, posY, anchor=NW, image=alphanums[name[0]])
        display_names_aux(name[1:],length,position,character+1)
            
def display_names(scoreboard,position=1):
    '''
    Parameters: scoreboard, position=1
    
    Return: None

    Restrictions: scoreboard must be a list that goes [name,score,name,score,...] and position shouldn't be specified
    '''
    if scoreboard==[]:
        return
    else:
        name=scoreboard[0]
        display_names_aux(name,lenn(name)-1,position) #-1 to account for \n
        display_names(scoreboard[2:],position+1)

def display_scores_aux(score,length,position,digit=0):
    '''
    Parameters: name, length, position, character=0
    
    Return: None

    Restrictions: name must be all caps, alphanumeric, and no accents; length must be the length of the name string, position must be int
    '''
    if score=='\n':
        return
    else:
        posY=118+(position-1)*33
        posX=485-((length-1)-digit)*13 #aligned right on 485
        scoresCanvas.create_image(posX, posY, anchor=NW, image=alphanums[score[0]])
        display_scores_aux(score[1:],length,position,digit+1)

def display_scores(scoreboard,position=1):
    '''
    Parameters: scoreboard, position=1
    
    Return: None

    Restrictions: scoreboard must be a list that goes [name,score,name,score,...] and position shouldn't be specified
    '''
    if scoreboard==[]:
        return
    else:
        score=scoreboard[1]
        display_scores_aux(score,lenn(score)-1,position)
        display_scores(scoreboard[2:],position+1)

def score_position(score,scoreboard):
    '''
    Parameters: score, scoreboard
    
    Return: Position of the new score in the scoreboard

    Restrictions: score must be int, scoreboard list that goes [name,score,name,score,...]
    '''
    if scoreboard==[] or score>int(scoreboard[1][:-1]): #[1] because [0] is name and [1] is score, int and [:-1] because scores get stored as 'score\n'
        return 1
    else:
        return 1+score_position(score,scoreboard[2:])
    
def check_score(name,score,scoreboard):
    position=score_position(score,scoreboard)
    if position<=10:
        scoreboard.insert((position-1)*2,name+"\n")
        scoreboard.insert(position*2-1,str(score)+"\n")
        if position==1:
            gameCanvas.create_text(width/2,292,text="------------------------------------",fill='#E82E53',font=("Courier New",15))
            gameCanvas.create_text(width/2,317,text="YOU ACHIEVED A NEW HIGHSCORE",fill='#E82E53',font=("Courier New",19))
            gameCanvas.create_text(width/2,342,text="------------------------------------",fill='#E82E53',font=("Courier New",15))
        elif position <=5:
            gameCanvas.create_text(width/2,320,text="Your score is the new #"+str(position)+"!",fill='#FF8000',font=("Courier New",20))
    if lenn(scoreboard)==22:
        scoreboard.pop()
        scoreboard.pop()
        
##################################################################----GAME----###########################################################################################################################################
#player
player=[] #[sprite,lives,speedX,speedY,currentFrame,shootTimer,playerFired,invulnerabilityTimer]
name=StringVar()

#misc
healths=[] #[sprite,currentFrame]
history=[]
floor=530
bullets=[]#[sprite,life,posX,posY,speedX,speedY,bulletType]
second=0
currentLvl=0

score=0
scoreText=None
timer=0
timerText=None

#after objects
playerMovementAnimation=None
playerFrameAnimation=None
healthFrameAnimation=None
missilesMovementAnimation=None
missilesFrameAnimation=None
commonsMovementAnimation=None
commonsFrameAnimation=None
crushersAnimation=None
bulletsAnimation=None

enemySpawning=[]
levelInstructions=None
scoreUpdating=None
timerUpdating=None

#enemies
missiles=[] #missile=[sprite,life,posX,posY,speedY,currentFrame,firedFlag]
commons=[]  #common= [sprite,life,posX,posY,speedX,speedY,currentFrame,flag, shootingTimer]
crushers=[] #crusher=[sprite,life,posX,posY,speedX,speedY,currentFrame,flag] flag determines whether falling or moving horizontally

#sprite loading
yellowSprite =  load_img('square sprite yellow.png') #player
blueSprite =    load_img('square sprite blue.png') #missiles
redSprite =     load_img('square sprite red.png') #crusher
greenSprite =   load_img('square sprite green.png') #commons
pinkSprite =    load_img('square sprite pink.png') #enemy bullets
blankSprite =   load_img('blank.png')
crusherSprite = load_img('sprite crusher.png') #crushers: vertical=38px horizontal=74px
crusherWhiteSprite =    load_img('sprite crusher white.png')
bulletSprite =  load_img('sprite bullet.png') #bullets: vertical=42px horizontal=19px
enemyBulletSprite =     load_img('sprite enemy bullet.png') #bullets: vertical=17px horizontal=17px

#Frames lists
#player: vertical=45px horizontal=36px
playerFrames=   [load_img('sprite player0.png'),load_img('sprite player1.png'),load_img('sprite player2.png'),load_img('sprite player3.png')] 
#misiles: vertical 49px horizontal 30px
missileFrames=  [load_img('sprite missile0.png'),load_img('sprite missile1.png'),load_img('sprite missile2.png'),load_img('sprite missile3.png'),load_img('sprite missile4.png'),load_img('sprite missile5.png'),load_img('sprite missile6.png'),load_img('sprite missile7.png'),load_img('sprite missile8.png'),load_img('sprite missile9.png'),load_img('sprite missile10.png'),load_img('sprite missile11.png'),load_img('sprite missile12.png')]
missileWhiteFrames= [load_img('sprite missile white0.png'),load_img('sprite missile white1.png'),load_img('sprite missile white2.png'),load_img('sprite missile white3.png'),load_img('sprite missile white4.png'),load_img('sprite missile white5.png'),load_img('sprite missile white6.png'),load_img('sprite missile white7.png'),load_img('sprite missile white8.png'),load_img('sprite missile white9.png'),load_img('sprite missile white10.png'),load_img('sprite missile white11.png'),load_img('sprite missile white12.png')]
#common: vertical=81px horizontal=68px
commonFrames=   [load_img('sprite common0.png'),load_img('sprite common1.png'),load_img('sprite common2.png'),load_img('sprite common3.png'),load_img('sprite common4.png')]
commonWhiteFrames= [load_img('sprite common white0.png'),load_img('sprite common white1.png'),load_img('sprite common white2.png'),load_img('sprite common white3.png'),load_img('sprite common white4.png')]
#health: vertical=30px horizontal=23px
healthFrames=   [load_img('sprite health0.png'),load_img('sprite health1.png'),load_img('sprite health2.png'),load_img('sprite health3.png'),load_img('sprite health4.png'),load_img('sprite health5.png'),load_img('sprite health6.png'),load_img('sprite health7.png'),load_img('sprite health8.png'),load_img('sprite health9.png'),load_img('sprite health10.png')]
#ground explosion:
groundFrames=   [load_img('sprite ground explosion0.png'),load_img('sprite ground explosion1.png'),load_img('sprite ground explosion2.png'),load_img('sprite ground explosion3.png'),load_img('sprite ground explosion4.png'),load_img('sprite ground explosion5.png'),load_img('sprite ground explosion6.png'),load_img('sprite ground explosion7.png'),load_img('sprite ground explosion8.png'),load_img('sprite ground explosion9.png'),load_img('sprite ground explosion10.png'),load_img('sprite ground explosion11.png'),load_img('sprite ground explosion12.png')]
#air explosion:
airFrames=      [load_img('sprite air explosion0.png'),load_img('sprite air explosion1.png'),load_img('sprite air explosion2.png'),load_img('sprite air explosion3.png'),load_img('sprite air explosion4.png'),load_img('sprite air explosion5.png'),load_img('sprite air explosion6.png'),load_img('sprite air explosion7.png'),load_img('sprite air explosion8.png')]

#entity creation
def create_player():
    global player
    lives=3
    speedX=0
    speedY=0
    currentFrame=0
    shootTimer=0
    playerFired=False
    invulnerabilityTimer=0
    sprite = gameCanvas.create_image(width/2, floor-45, anchor=NW, image=playerFrames[0])
    player=[sprite,lives,speedX,speedY,currentFrame,shootTimer,playerFired,invulnerabilityTimer]

def create_missile():
    lives=1
    posY=-70
    posX=randint(3,width-29)
    speedY=0
    currentFrame=0
    missile = gameCanvas.create_image(posX,posY,anchor=NW,image=missileFrames[0])
    
    newMissile=[missile,lives,posX,posY,speedY,currentFrame]
    
    missiles.append(newMissile)

def create_common():
    lives=3
    posY=10
    posX=-75
    speedX=0
    speedY=0
    currentFrame=0
    flag=-1
    shootingTimer=randint(15,115)
    common = gameCanvas.create_image(posX,posY,anchor=NW,image=commonFrames[0])
    
    newCommon=[common,lives,posX,posY,speedX,speedY,currentFrame, flag, shootingTimer]
    
    commons.append(newCommon)

def create_crusher():
    lives=5
    posX=randint(3,width-75)
    posY=-50
    speedX=0
    speedY=0
    flag=0
    crusher = gameCanvas.create_image(posX,posY,anchor=NW,image=crusherSprite)
    
    newCrusher=[crusher,lives,posX,posY,speedX,speedY, flag]
    
    crushers.append(newCrusher)

def create_bullet(entityType,entity):
    lives=1
    speedX=speedY=0
    
    if entityType=='player':
        posX=gameCanvas.coords(entity)[0]+8 #pwidth=36 bwidth=19
        posY=gameCanvas.coords(entity)[1]-42
        bulletType='player'
        bullet=gameCanvas.create_image(posX,posY,anchor=NW,image=bulletSprite)

    elif entityType=='common':
        posX=gameCanvas.coords(entity[0])[0]+25 #cwidth=68 bwidth=17
        posY=gameCanvas.coords(entity[0])[1]+81 #cheight=81
        bulletType='common'
        bullet=gameCanvas.create_image(posX,posY,anchor=NW,image=enemyBulletSprite)

    elif entityType=='crusher':
        if entity[6]==1: #move left, shoot right
            posX=gameCanvas.coords(entity[0])[0]+74 #cwidth=74 bwidth=17
            posY=gameCanvas.coords(entity[0])[1]+13 #cheight=38 bheight=17
            speedX=6
        elif entity[6]==2: #move right, shoot left
            posX=gameCanvas.coords(entity[0])[0]-17 
            posY=gameCanvas.coords(entity[0])[1]+13
            speedX=-6
        bulletType='crusher'
        bullet=gameCanvas.create_image(posX,posY,anchor=NW,image=enemyBulletSprite)


    newBullet=[bullet,lives,posX,posY,speedX,speedY,bulletType]
    bullets.append(newBullet)

def create_healths(i=0):
    if i<3:
        posX=41+24*i
        posY=559
        currentFrame=randint(0,10)
        health=gameCanvas.create_image(posX,posY,anchor=NW,image=healthFrames[currentFrame])
        newHealth=[health,currentFrame]
        healths.append(newHealth)
        create_healths(i+1)
    else:
        return

#Explosions
def ground_explosion(posX,posY,framesList=groundFrames,lastFrame=None):
    if framesList==[]:
        gameCanvas.delete(lastFrame)
        return
    else:
        if screen=='pause':
            gameCanvas.after(10,ground_explosion,posX,posY,framesList,lastFrame)
        else:  
            gameCanvas.delete(lastFrame) if lastFrame!=None else explosionSound.play()
            newFrame=gameCanvas.create_image(posX,posY,anchor=S,image=framesList[0])
            gameCanvas.after(33,ground_explosion,posX,posY,framesList[1:],newFrame)

def air_explosion(posX,posY,framesList=airFrames,lastFrame=None):
    if framesList==[]:
        gameCanvas.delete(lastFrame)
        return
    else:
        if screen=='pause':
            gameCanvas.after(10,ground_explosion,posX,posY,framesList,lastFrame)
        else:  
            gameCanvas.delete(lastFrame) if lastFrame!=None else explosionSound.play()
            newFrame=gameCanvas.create_image(posX,posY,anchor=CENTER,image=framesList[0])
            gameCanvas.after(72,air_explosion,posX,posY,framesList[1:],newFrame)
        
#Movement:
def fall_player():
    global player
    yposition= gameCanvas.coords(player[0])[1]
    if yposition<floor-45:
        player[3]+=1.5
    if yposition+player[3]>floor-45:
        player[3]=floor-45-yposition

def move_player():
    '''
    Return: None

    Restrictions: This function does not take any parameters
    '''
    #player=[sprite,speedX,speedY]
    global player
    horizontalVelocity=10
    xposition= gameCanvas.coords(player[0])[0]
    yposition= gameCanvas.coords(player[0])[1]

    if jumpKey in history and yposition==floor-45:
        player[3]=-20

    if rightKey in history and leftKey in history: player[2]=0
    elif rightKey in history:
        if xposition+horizontalVelocity<width-33: player[2]=horizontalVelocity
        else: player[2]=width-33-xposition
    elif leftKey in history:
        if xposition-horizontalVelocity>2: player[2]=-horizontalVelocity #ejes parecen realmente estar en pixel 2 y width+2 (???)
        else: player[2]=-xposition+2
    else:
        player[2]=0
    
    shoot_player()
    
def move_missile(missile):
    '''
    Parameters: missile
    
    Return: None

    Restrictions: missile must be a list with the format [image,life,posX,posY,speedY]
    '''
    #missile=[sprite,life,posX,posY,speedY]
    fallingSpeed=missile[4]=10
    if missile[3]>=floor-30: 
        missile[1]=0
    
    missile[3]+=missile[4]

def move_common(common):
    '''
    Parameters: common
    
    Return: None 

    Restrictions: common must be a list with the format [image,life,posX,posY,speedX,speedY,currentFrame, flag, shootTimer]
    '''
    #common= flag goes from 0 to maxFlag and counts steps down
    maxFlag=15
    horizontalSpeed=5
    verticalSpeed=4
    
    if common[2]<-100 or common[2]>width+68: 
        common[1]=0

    if common[3]>floor-(maxFlag*verticalSpeed)-81 and common[4]!=0:
        pass
    elif common[2] <= 13 or common[2]>=width-78:
        if common[7]==-1: #when it spawns and it's moving into the screen
            if common[2]<30:
                common[4]=horizontalSpeed
            else:
                common[7]=0 
                common[4]=0 
                common[5]=verticalSpeed
        elif common[7]==maxFlag: #starts or finishes descending
            if common[4]!=0: #starts descending
                common[7]=0 
                common[4]=0 
                common[5]=verticalSpeed
            elif common[2]<30: #finishes descent (left)
                common[4]=horizontalSpeed
                common[5]=0
            else: #finishes descent (right)
                common[4]=-horizontalSpeed
                common[5]=0
        else:
            common[7]+=1
    
    common[3]+=common[5]
    common[2]+=common[4]

    #shooting
    if common[7]==-1 or common[7]==maxFlag:
        shootTimer=common[8]
        if shootTimer==0:
            create_bullet("common",common)
            common[8]=randint(15,115)
        else:
            common[8]-=1

def move_crusher(crusher):
    '''
    Parameters: crusher
    
    Return: None 

    Restrictions: crusher must be a list with the format [image,life,posX,posY,speedX,speedY, flag]
    '''
    global score
    #crusher=[sprite,life,posX,posY,speedX,speedY, flag] flag: 0=falling (default), 1=left, 2=right
    #38x74
    horizontalSpeed=7
    verticalSpeed=7
    
    if crusher[2]<-74 or crusher[2]>width+74: #moves out of frame
        crusher[1]=0
        score+=2
    
    if crusher[6]==0 and crusher[3]>=floor-38: #reaches ground
        crusher[6]=randint(1,2) #1=left 2=right
        crusher[5]=0
        create_bullet("crusher",crusher)

    if crusher[6]==0:
        crusher[5]=verticalSpeed
    elif crusher[6]==1:
        crusher[4]=-horizontalSpeed
    elif crusher[6]==2:
        crusher[4]=horizontalSpeed

    crusher[3]+=crusher[5]
    crusher[2]+=crusher[4]

def move_bullet(bullet):
    '''
    Parameters: bullet
    
    Return: None 

    Restrictions: bullet must be a list with the format [image,life,posX,posY,speedX,speedY,bulletType]
    '''
    bulletType=bullet[6]
    if bulletType=='player':
        #[sprite,life,posX,posY,speedX,speedY,bulletType]
        #19x42
        speedY=bullet[5]=-20
        posY=bullet[3]
        bullet[3]+=speedY
        
        if posY<=-20:
            bullet[1]=0

    elif bulletType=='common':
        #17x17
        speedY=bullet[5]=10
        posY=bullet[3]
        bullet[3]+=speedY

        if posY>=floor:
            bullet[1]=0

    elif bulletType=='crusher':
        posX=bullet[2]
        speedX=bullet[4]
        bullet[2]+=speedX
        
        if posX<=-20 or posX>=620:
            bullet[1]=0
        
#Life:
def player_blinking():
    if player[7]==0:
        pass
    else:
        gameCanvas.itemconfig(player[0],image=blankSprite)
        gameCanvas.after(333,player_blinking)
        player[7]-=1
            
def check_life_player(player):
    if player[1]<lenn(healths) and lenn(healths)>0:
        gameCanvas.delete(healths[-1][0])
        healths.pop()
        check_life_player(player)
    
    if player[1]<=0:
        game_over()
        return "Dead"
    
def check_life_missile(missile):
    #30x40
    if missile[1]<=0:
        air_explosion(missile[2]+15,missile[3]+25) if missile[3]<floor-30 else ground_explosion(missile[2]+15,missile[3]+25)
        gameCanvas.delete(missile[0])   
        missiles.remove(missile)

def check_life_common(common):
    #68x81
    if common[1]<=0:
        air_explosion(common[2]+34,common[3]+40)
        gameCanvas.delete(common[0])
        commons.remove(common)

def check_life_crusher(crusher):
    #74x38
    if crusher[1]<=0:
        air_explosion(crusher[2]+37,crusher[3]+19)
        gameCanvas.delete(crusher[0])
        crushers.remove(crusher)

def check_life_bullet(bullet):
    bulletType=bullet[6]
    if bullet[1]==0:
        if bulletType!='player' and bullet[3]<floor and bullet[2]>-20 and bullet[2]<620: air_explosion(bullet[2]+8,bullet[3]+8)
        gameCanvas.delete(bullet[0])
        if bullet in bullets: #sometimes bugged and tried removing same bullet twice (?)
            bullets.remove(bullet)

#shooting/collisions
def shoot_player():
    shootingTimer=player[5]
    playerFired=player[6]

    shootingCooldown=5
    
    if shootKey in history and shootingTimer==0 and playerFired==False:
        shootingTimer=player[5]=shootingCooldown
        playerFired=player[6]=True
        create_bullet("player",player[0])
        laserShootSound.play()

    elif shootingTimer>0:
        shootingTimer=player[5]=shootingTimer-1

    if playerFired==True and shootKey not in history:
        playerFired=player[6]=False

def check_enemy_collisions(enemyType, enemy, bulletsList=bullets):
    '''
    Parameters: enemyType, enemy, bulletsList=bullets
    Return: None
    Restrictions: enemy Type must be one of 'common','missile','crusher'; enemy must be the list referencing a single enemy, bulletsList must not be specified
    '''
    global score
    invTimer=4
    #player: vertical=45px horizontal=36px
    #misiles: vertical 49px horizontal 30px
    #common: vertical=81px horizontal=68px
    #crushers: vertical=38px horizontal=74px
    #bullets: vertical=42px horizontal=19px
    playerPosX,playerPosY=gameCanvas.coords(player[0])
    enemyPosX,enemyPosY=(enemy[2],enemy[3])

    #body-body
    if enemyType=='common':
        if playerPosX<=enemyPosX+67 and playerPosX+35>=enemyPosX: 
            if playerPosY<=enemyPosY+80 and playerPosY+44>=enemyPosY:
                enemy[1]=0
                if player[7]==0:
                    player[1]-=1
                    player[7]=invTimer
                    player_blinking()
                return
    elif enemyType=='missile':
        if playerPosX<=enemyPosX+29 and playerPosX+35>=enemyPosX: 
            if playerPosY<=enemyPosY+48 and playerPosY+44>=enemyPosY:
                enemy[1]=0
                if player[7]==0:
                    player[1]-=2 #you lose 2 lives when getting hit by a missile
                    player[7]=invTimer
                    player_blinking()
                return
    elif enemyType=='crusher':
        if playerPosX<=enemyPosX+73 and playerPosX+35>=enemyPosX: 
            if playerPosY<=enemyPosY+37 and playerPosY+44>=enemyPosY:
                enemy[1]=0
                if player[7]==0:
                    player[1]-=1
                    player[7]=invTimer
                    player_blinking()
                return

    #body-bullet
    if bulletsList==[]:
        return
    else:
        bulletPosX=bulletsList[0][2]
        bulletPosY=bulletsList[0][3]
        bulletType=bulletsList[0][6]
        
        if enemyType=='common':
            if bulletType=='player':
                if enemyPosX<=bulletPosX+18 and enemyPosX+67>=bulletPosX: 
                    if enemyPosY<=bulletPosY+41 and enemyPosY+80>=bulletPosY: 
                        enemy[1]-=1
                        bulletsList[0][1]=0
                        gameCanvas.itemconfig(enemy[0],image=commonWhiteFrames[enemy[6]]) #common[6]=currentFrame
                        hitHurtSound.play()
                        if enemy[1]<=0:
                            score+=5
            check_enemy_collisions('common',enemy,bulletsList[1:])
            
        elif enemyType=='missile':
            if bulletType=='player':
                if enemyPosX<=bulletPosX+18 and enemyPosX+29>=bulletPosX:
                    if enemyPosY<=bulletPosY+41 and enemyPosY+40>=bulletPosY:
                        enemy[1]-=1
                        bulletsList[0][1]=0
                        hitHurtSound.play()
                        if enemy[1]<=0:
                            score+=1
            check_enemy_collisions('missile',enemy,bulletsList[1:])
        elif enemyType=='crusher':
            if bulletType=='player':
                if enemyPosX<=bulletPosX+18 and enemyPosX+73>=bulletPosX: #check width
                    if enemyPosY<=bulletPosY+41 and enemyPosY+37>=bulletPosY:
                        enemy[1]-=1
                        bulletsList[0][1]=0
                        gameCanvas.itemconfig(enemy[0],image=crusherWhiteSprite)
                        gameCanvas.after(91,lambda: gameCanvas.itemconfig(enemy[0],image=crusherSprite)) #crusher doesn't update frames on its own
                        hitHurtSound.play()
                        if enemy[1]<=0:
                            score+=20
            check_enemy_collisions('crusher',enemy,bulletsList[1:])

def check_player_collisions(bulletsList=bullets):
    '''
    Parameters: bulletsList=bullets
    
    Return: None

    Restrictions: must not specify parameter
    '''
    #player: vertical=45px horizontal=36px
    #misiles: vertical 49px horizontal 30px
    #common: vertical=81px horizontal=68px
    #crushers: vertical=38px horizontal=74px
    #bullets: vertical=42px horizontal=19px
    invTimer=3
    playerPosX,playerPosY=gameCanvas.coords(player[0])
    
    if bulletsList==[]:
        pass
    else:
        bulletType=bulletsList[0][6]
        if bulletType=='player':
            pass
        else:
            bulletPosX,bulletPosY=(bulletsList[0][2],bulletsList[0][3])
            if playerPosX<=bulletPosX+17 and playerPosX+35>=bulletPosX: 
                if playerPosY<=bulletPosY+17 and playerPosY+44>=bulletPosY:
                    bulletsList[0][1]=0
                    #check_life_bullet(bulletsList[0]) not sure why this was here
                    if player[7]==0:
                        player[1]-=1
                        player[7]=invTimer
                        player_blinking()
            check_player_collisions(bulletsList[1:])

#Levels
def enemy_spawning(enemyType,amount,delay):
    '''
    Parameters: enemyType,amount,delay
    
    Return: None

    Restrictions: enemyType must be one of 'common','missile','crusher'; amount must be an int detailing amount of enemies to spawn; delay must be miliseconds between spawns of type int
    '''
    #print("spawning shit: %d"%amount)
    if amount==0:
        return
    else:
        if screen=='pause':
            gameCanvas.after(100,enemy_spawning,enemyType,amount,delay)
        elif screen=='game':    
            if enemyType==None:
                return
            elif enemyType=='missile':
                create_missile()
            elif enemyType=='common':
                create_common()
            elif enemyType=='crusher':
                create_crusher()
            enemySpawning.append(gameCanvas.after(delay,enemy_spawning,enemyType,amount-1,delay))

def level_instructions(level):
    '''
    Parameters: level
    
    Return: None

    Restrictions: level must be int between 1 and 3
    '''
    global second, currentLvl, levelInstructions
    currentLvl=level
    if level==1:
        second+=1
        if second<=40:
            levelInstructions=gameCanvas.after(1000,level_instructions,1)
        else:
            currentLvl=2
            levelInstructions=gameCanvas.after(5000,level_instructions,2)
            second=0
        spawnDic={ #to setup level, add dictionary entry like second:('enemy type to spawn', amount to spawn, interval between spawns(in ms))
            1:('missile',4,1000),
            6:('common',4,1000),
            11:('missile',3,500),
            13:('missile',1,1),
            15:('crusher',4,2500),
            26:('missile',5,666),
            27:('common',6,2000),
            35:('missile',5,1000)
            }
        
    elif level==2:
        second+=1
        if second<=45:
            levelInstructions=gameCanvas.after(1000,level_instructions,2)
        else:
            currentLvl=3
            levelInstructions=gameCanvas.after(5000,level_instructions,3)
            second=0
        spawnDic={
            6:('common',12,1500),
            10:('missile',15,1000),
            23:('crusher',5,1000),
            29:('common',14,800),
            33:('crusher',3,1500),
            39:('missile',12,333)
            }
        
    elif level==3:
        second+=1
        if second<=45:
            levelInstructions=gameCanvas.after(1000,level_instructions,3)
        else:
            if commons==[] and missiles==[] and crushers==[]:
                finished_game()
            else:
                levelInstructions=gameCanvas.after(1000,level_instructions,3)
        spawnDic={
            5:('common',20,1000),
            6:('missile',39,1000),
            10:('crusher',7,2000),
            14:('missile',31,1000),
            21:('crusher',7,2000),
            22:('missile',23,1000),
            25:('common',7,1500),
            30:('missile',15,1000),
            37:('missile',37,200),
            38:('missile',21,333),
            39:('missile',18,333),
            40:('missile',15,333),
            41:('missile',12,333),
            42:('missile',9,333),
            43:('missile',6,333),
            44:('missile',3,333),
            }
    spawn=spawnDic.get(second,(None,0,0))
    enemy_spawning(spawn[0],spawn[1],spawn[2])
    
#animation loops
def animate_player(which):
    '''
    Parameter: movement or frames
    
    Return: None

    Restrictions: parameter must be string, either 'movement' or 'frames'
    '''
    global playerMovementAnimation,playerFrameAnimation
    if which=='movement':
        animate_player_movement()
        playerMovementAnimation=gameCanvas.after(33,animate_player,'movement')
        
    elif which=='frames':
        animate_player_frames()
        playerFrameAnimation=gameCanvas.after(125,animate_player,'frames')
        
def animate_player_movement():
    #print(player)
    if check_life_player(player)=='Dead':
        return
    else:
        fall_player()
        move_player()
        gameCanvas.move(player[0],player[2],player[3])
        check_player_collisions()

def animate_player_frames():
    global player
    player[4]+=1
    if player[4]==4: player[4]=0
    gameCanvas.itemconfig(player[0],image=playerFrames[player[4]])

def animate_health_frames(healthsList=healths):
    global healthFrameAnimation
    if healthsList==[]:
        healthFrameAnimation=gameCanvas.after(100,animate_health_frames)
        return
    else:
        healthsList[0][1]+=1
        if healthsList[0][1]==11: healthsList[0][1]=0
        gameCanvas.itemconfig(healthsList[0][0],image=healthFrames[healthsList[0][1]])
        animate_health_frames(healthsList[1:])

def animate_missiles(which):
    '''
    Parameter: movement or frames
    
    Return: None

    Restrictions: parameter must be string, either 'movement' or 'frames'
    '''
    global missilesMovementAnimation,missilesFrameAnimation
    if which=='movement':
        animate_missiles_movement()
        missilesMovementAnimation=gameCanvas.after(33,animate_missiles,'movement')
        
    elif which=='frames':
        animate_missiles_frames()
        missilesFrameAnimation=gameCanvas.after(42,animate_missiles,'frames')

def animate_missiles_movement(missilesList=missiles):
    if missilesList==[]:
        #print(missiles)
        return
    else:
        gameCanvas.move(missilesList[0][0],0,missilesList[0][4])
        move_missile(missilesList[0])
        check_enemy_collisions('missile',missilesList[0])
        check_life_missile(missilesList[0])
        animate_missiles_movement(missilesList[1:])

def animate_missiles_frames(missilesList=missiles):
    if missilesList==[]:
        return
    else:
        missilesList[0][5]+=1
        #print("FRAME:",missilesList[0][5])
        if missilesList[0][5]==13: missilesList[0][5]=0
        gameCanvas.itemconfig(missilesList[0][0],image=missileFrames[missilesList[0][5]])
        animate_missiles_frames(missilesList[1:])

def animate_commons(which):
    '''
    Parameter: movement or frames
    
    Return: None

    Restrictions: parameter must be string, either 'movement' or 'frames'
    '''
    global commonsMovementAnimation,commonsFrameAnimation
    if which=='movement':
        animate_commons_movement()
        commonsMovementAnimation=gameCanvas.after(33,animate_commons,'movement')
        
    elif which=='frames':
        animate_commons_frames()
        commonsFrameAnimation=gameCanvas.after(91,animate_commons,'frames')

def animate_commons_movement(commonsList=commons):
    if commonsList==[]:
        #print(commons)
        return
    else:
        gameCanvas.move(commonsList[0][0],commonsList[0][4],commonsList[0][5])
        move_common(commonsList[0])
        check_enemy_collisions('common',commonsList[0])
        check_life_common(commonsList[0])
        animate_commons_movement(commonsList[1:])
            

def animate_commons_frames(commonsList=commons):
    if commonsList==[]:
        return
    else:
        commonsList[0][6]+=1
        #print("FRAME:",commonsList[0][6])
        if commonsList[0][6]==5: commonsList[0][6]=0
        gameCanvas.itemconfig(commonsList[0][0],image=commonFrames[commonsList[0][6]])
        animate_commons_frames(commonsList[1:])

def animate_crushers():
    '''
    Return: None

    Restrictions: This function does not take parameters
    '''
    global crushersAnimation
    animate_crushers_movement()
    crushersAnimation=gameCanvas.after(33,animate_crushers)
    

def animate_crushers_movement(crushersList=crushers):
    #global crushersAnimation
    if crushersList==[]:
        #print(crushers)
        return
    else:
        gameCanvas.move(crushersList[0][0],crushersList[0][4],crushersList[0][5])
        move_crusher(crushersList[0])
        check_enemy_collisions('crusher',crushersList[0])
        check_life_crusher(crushersList[0])
        animate_crushers_movement(crushersList[1:])

def animate_bullets():
    '''
    Return: None

    Restrictions: This function does not take parameters
    '''
    global bulletsAnimation
    animate_bullets_movement()
    bulletsAnimation=gameCanvas.after(33,animate_bullets)
    
def animate_bullets_movement(bulletsList=bullets):
    #print(bulletsList)
    if bulletsList==[]:
        return
    else:
        gameCanvas.move(bulletsList[0][0],bulletsList[0][4],bulletsList[0][5])
        move_bullet(bulletsList[0])
        check_life_bullet(bulletsList[0])
        animate_bullets_movement(bulletsList[1:])
        
#Score, timer and name
def update_score():
    global scoreUpdating
    gameCanvas.itemconfig(scoreText,text=score)
    scoreUpdating=gameCanvas.after(100,update_score)

def update_timer():
    global timerUpdating,timer
    timer+=1
    gameCanvas.itemconfig(timerText,text=timer/100)
    timerUpdating=gameCanvas.after(10,update_timer)
    return

def display_name_game(name,length,character=0):
    '''
    Parameters: name,length,character=0
    
    Return: None

    Restrictions: name must be string, all caps, alphanumeric, no accents; length must be int, length of name; character must not be specified
    '''
    if name=='':
        return
    else:
        posY=580
        posX=570-((length-1)-character)*13 #aligned right on 485
        gameCanvas.create_image(posX, posY, anchor=NW, image=alphanums[name[0]])
        display_name_game(name[1:],length,character+1)
#Notar keypresses
def keyup(event):
    if  event.keysym.upper() in history :
        history.remove(event.keysym.upper())
        #print("released", repr(event.char))
        

def keydown(event):
    if not event.keysym.upper() in history :
        history.append(event.keysym.upper())
        #print("pressed", repr(event.char))

###################################################Main###################################################

load_menu()

options=read_file('options.txt')
options=(['ON\n','ON\n','W\n','J\n','D\n','A\n'] if options==[] else options) #[0] music, [1] sfx, [2] jump, [3] shoot, [4] right, [5] left

jumpKey,shootKey,rightKey,leftKey=options[2][:-1],options[3][:-1],options[4][:-1],options[5][:-1] #[-1] para quitar \n

load_buttons() #must go after keybind variables assignment and before toggle_music()

play_menu_music()
pygame.mixer.music.play(-1)
if options[0]=='OFF\n': toggle_music()

sfx_on()
if options[1]=='OFF\n': toggle_sfx()

scoreboard=read_file('scoreboard.txt')
load_alphanums(alphanums)

root.protocol("WM_DELETE_WINDOW", quit_application)
root.mainloop()
