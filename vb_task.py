#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Mon Feb  6 14:58:35 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
corrAns = "left"


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'vb_task'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/eliasaoundurand/Projets/CausaL/psychopy_exps/vb_task.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "instructions_1" ---
text_instr = visual.TextStim(win=win, name='text_instr',
    text="Règles du jeu"+'\n' + " \n Tu es un dénicheur de talent de joueurs de volleyball et, en vue de la prochaine saison, tu es contacté par les équipes  de la ligue pour évaluer l'impact des nouveaux joueurs. " + "\n Chacune des 45 équipes de la ligue aimerait avoir ton avis pour décider de signer ou non un nouveau joueur." + " \n Pour mieux évaluer chaque nouveau joueur proposé par chaque équipe, vous aurez la possibilité de simuler une série de matchs tests. Cela vous permettra de comprendre comment l'équipe en question se comporte (c'est-à-dire si elle gagne ou perd) selon que le nouveau joueur entre sur le terrain ou non.",
    font='Arial',
    pos=(0.0, 0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_next = visual.ImageStim(
    win=win,
    name='image_next', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "instructions_2" ---
text_instr_2 = visual.TextStim(win=win, name='text_instr_2',
    text="Règles du jeu" + "\n"+" \n A chaque partie, vous décidez vous-même si vous laissez le joueur participer ou si laissez-le sur le banc." + "\n Rappelez-vous que votre objectif n'est pas de faire gagner le plus de matchs à l'équipe, mais d'évaluer l'impact du joueur, c'est-à-dire de comprendre s'il est utile à l'équipe en question." 

,
    font='Arial',
    pos=(0.0,0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_next_2 = visual.ImageStim(
    win=win,
    name='image_next_2', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# --- Initialize components for Routine "instructions_3" ---
text_instr_3 = visual.TextStim(win=win, name='text_instr_3',
    text="Règles du jeu"+ "\n"+"\n Pour chaque joueur, vous pourrez simuler un certain nombre de parties à l'aide des touches «flèche droite» et «flèche gauche» sur le clavier."+"\n En choisissant « Avec », vous simulerez un match de l'équipe en question avec la participation du joueur." +"\n En choisissant « Sans », vous simulerez une partie sans sa participation."
,
    font='Arial',
    pos=(0.0,0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_next_3 = visual.ImageStim(
    win=win,
    name='image_next_3', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
image_with = visual.ImageStim(
    win=win,
    name='image_with', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_without = visual.ImageStim(
    win=win,
    name='image_without', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "instructions_4" ---
text_instr_4 = visual.TextStim(win=win, name='text_instr_4',
    text="Règles du jeu" + "\n"+"\n Par la suite, un smiley indiquera si l'équipe avec ou sans le joueur a gagné (smiley face) ou si elle a perdu (sad face)",
    font='Arial',
    pos=(0.0,0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_next_4 = visual.ImageStim(
    win=win,
    name='image_next_4', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()
images_win = visual.ImageStim(
    win=win,
    name='images_win', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_loose = visual.ImageStim(
    win=win,
    name='image_loose', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "instructions_5" ---
text_instr_5 = visual.TextStim(win=win, name='text_instr_5',
    text="Règles du jeu" + "\n"+ " \n Le délai pour prendre vos décisions sera de 2 secondes après la disparition du smiley. Si vous retardez trop longtemps votre décision, un point d'interrogation apparaîtra indiquant que vous devrez choisir plus rapidement.",
    font='Arial',
    pos=(0.0,0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_next_5 = visual.ImageStim(
    win=win,
    name='image_next_5', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()

# --- Initialize components for Routine "instructions_6" ---
text_instr_6 = visual.TextStim(win=win, name='text_instr_6',
    text="Règles du jeu" + "\n"+ " \n Pour chaque joueur, vous aurez la possibilité de simuler un nombre variable de matchs avant de passer au joueur et à l'équipe suivants." + "\n Le nombre de jeux que vous pouvez simuler variera aléatoirement d'un minimum de 5 à un maximum de 40.",
    font='Arial',
    pos=(0.0,0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_next_6 = visual.ImageStim(
    win=win,
    name='image_next_6', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()

# --- Initialize components for Routine "instructions_7" ---
text_instr_7 = visual.TextStim(win=win, name='text_instr_7',
    text="Règles du jeu" + "\n"+ " \n Ensuite, il vous sera demandé d'évaluer la valeur du joueur avec un score compris entre 0 (valeur minimale) et 10 (valeur maximale)." + "\n Par exemple:" + " \n 10 : Le joueur fait toujours gagner l'équipe qu'il joue" + "\n 0 : Le joueur n'a pas d'impact dans l'équipe" + "\n Il vous sera alors demandé si vous recommanderiez l'achat du lecteur."
,
    font='Arial',
    pos=(0.0,0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_next_7 = visual.ImageStim(
    win=win,
    name='image_next_7', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_7 = event.Mouse(win=win)
x, y = [None, None]
mouse_7.mouseClock = core.Clock()

# --- Initialize components for Routine "instructions_8" ---
text_instr_8 = visual.TextStim(win=win, name='text_instr_8',
    text="Règles du jeu" + "\n"+ " \n Paiement: Une fois les 45 joueurs et équipes évalués, nous calculerons votre rémunération en fonction de la précision de la valeur que vous avez donnée aux différents joueurs (0 à 10) par rapport à leur impact réel." + "\n Le jugement concernant un seul joueur sera tiré au sort pour le calcul du paiement. Si la valeur que vous avez estimée est identique à la valeur réelle du joueur, vous gagnerez 10€." + " \n Plus vous vous éloignez de la valeur réelle, moins vous serez payé (selon le schéma ci-contre)" + "\n Cette somme s'ajoutera aux 5 € de jetons de présence.",
    font='Arial',
    pos=(0.0,0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_next_8 = visual.ImageStim(
    win=win,
    name='image_next_8', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_8 = event.Mouse(win=win)
x, y = [None, None]
mouse_8.mouseClock = core.Clock()

# --- Initialize components for Routine "instructions_9" ---
text_instr_9 = visual.TextStim(win=win, name='text_instr_9',
    text="Fin des instructions",
    font='Arial',
    pos=(0.0,0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_next_9 = visual.ImageStim(
    win=win,
    name='image_next_9', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
mouse_9.mouseClock = core.Clock()

# --- Initialize components for Routine "trial" ---
game = visual.TextStim(win=win, name='game',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
question_mark = visual.TextStim(win=win, name='question_mark',
    text='?',
    font='Open Sans',
    units='cm', pos=(0, 0), height=2.5, wrapWidth=None, ori=0.0, 
    color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "outcome" ---
fb = visual.TextStim(win=win, name='fb',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instructions_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_1Components = [text_instr, image_next, mouse]
for thisComponent in instructions_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr* updates
    if text_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr.frameNStart = frameN  # exact frame index
        text_instr.tStart = t  # local t and not account for scr refresh
        text_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instr.started')
        text_instr.setAutoDraw(True)
    
    # *image_next* updates
    if image_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_next.frameNStart = frameN  # exact frame index
        image_next.tStart = t  # local t and not account for scr refresh
        image_next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_next, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_next.started')
        image_next.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(image_next)
                    clickableList = image_next
                except:
                    clickableList = [image_next]
                for obj in clickableList:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_1" ---
for thisComponent in instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.addData('mouse.clicked_name', mouse.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
mouse_2.x = []
mouse_2.y = []
mouse_2.leftButton = []
mouse_2.midButton = []
mouse_2.rightButton = []
mouse_2.time = []
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_2Components = [text_instr_2, image_next_2, mouse_2]
for thisComponent in instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr_2* updates
    if text_instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr_2.frameNStart = frameN  # exact frame index
        text_instr_2.tStart = t  # local t and not account for scr refresh
        text_instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instr_2.started')
        text_instr_2.setAutoDraw(True)
    
    # *image_next_2* updates
    if image_next_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_next_2.frameNStart = frameN  # exact frame index
        image_next_2.tStart = t  # local t and not account for scr refresh
        image_next_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_next_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_next_2.started')
        image_next_2.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_2.started', t)
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(image_next)
                    clickableList = image_next
                except:
                    clickableList = [image_next]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                x, y = mouse_2.getPos()
                mouse_2.x.append(x)
                mouse_2.y.append(y)
                buttons = mouse_2.getPressed()
                mouse_2.leftButton.append(buttons[0])
                mouse_2.midButton.append(buttons[1])
                mouse_2.rightButton.append(buttons[2])
                mouse_2.time.append(mouse_2.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_2" ---
for thisComponent in instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_2.x', mouse_2.x)
thisExp.addData('mouse_2.y', mouse_2.y)
thisExp.addData('mouse_2.leftButton', mouse_2.leftButton)
thisExp.addData('mouse_2.midButton', mouse_2.midButton)
thisExp.addData('mouse_2.rightButton', mouse_2.rightButton)
thisExp.addData('mouse_2.time', mouse_2.time)
thisExp.addData('mouse_2.clicked_name', mouse_2.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
mouse_3.x = []
mouse_3.y = []
mouse_3.leftButton = []
mouse_3.midButton = []
mouse_3.rightButton = []
mouse_3.time = []
mouse_3.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_3Components = [text_instr_3, image_next_3, mouse_3, image_with, image_without]
for thisComponent in instructions_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr_3* updates
    if text_instr_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr_3.frameNStart = frameN  # exact frame index
        text_instr_3.tStart = t  # local t and not account for scr refresh
        text_instr_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instr_3.started')
        text_instr_3.setAutoDraw(True)
    
    # *image_next_3* updates
    if image_next_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_next_3.frameNStart = frameN  # exact frame index
        image_next_3.tStart = t  # local t and not account for scr refresh
        image_next_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_next_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_next_3.started')
        image_next_3.setAutoDraw(True)
    # *mouse_3* updates
    if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_3.frameNStart = frameN  # exact frame index
        mouse_3.tStart = t  # local t and not account for scr refresh
        mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_3.started', t)
        mouse_3.status = STARTED
        mouse_3.mouseClock.reset()
        prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(image_next)
                    clickableList = image_next
                except:
                    clickableList = [image_next]
                for obj in clickableList:
                    if obj.contains(mouse_3):
                        gotValidClick = True
                        mouse_3.clicked_name.append(obj.name)
                x, y = mouse_3.getPos()
                mouse_3.x.append(x)
                mouse_3.y.append(y)
                buttons = mouse_3.getPressed()
                mouse_3.leftButton.append(buttons[0])
                mouse_3.midButton.append(buttons[1])
                mouse_3.rightButton.append(buttons[2])
                mouse_3.time.append(mouse_3.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # *image_with* updates
    if image_with.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_with.frameNStart = frameN  # exact frame index
        image_with.tStart = t  # local t and not account for scr refresh
        image_with.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_with, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_with.started')
        image_with.setAutoDraw(True)
    
    # *image_without* updates
    if image_without.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_without.frameNStart = frameN  # exact frame index
        image_without.tStart = t  # local t and not account for scr refresh
        image_without.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_without, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_without.started')
        image_without.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_3" ---
for thisComponent in instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_3.x', mouse_3.x)
thisExp.addData('mouse_3.y', mouse_3.y)
thisExp.addData('mouse_3.leftButton', mouse_3.leftButton)
thisExp.addData('mouse_3.midButton', mouse_3.midButton)
thisExp.addData('mouse_3.rightButton', mouse_3.rightButton)
thisExp.addData('mouse_3.time', mouse_3.time)
thisExp.addData('mouse_3.clicked_name', mouse_3.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_4
mouse_4.x = []
mouse_4.y = []
mouse_4.leftButton = []
mouse_4.midButton = []
mouse_4.rightButton = []
mouse_4.time = []
mouse_4.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_4Components = [text_instr_4, image_next_4, mouse_4, images_win, image_loose]
for thisComponent in instructions_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr_4* updates
    if text_instr_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr_4.frameNStart = frameN  # exact frame index
        text_instr_4.tStart = t  # local t and not account for scr refresh
        text_instr_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instr_4.started')
        text_instr_4.setAutoDraw(True)
    
    # *image_next_4* updates
    if image_next_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_next_4.frameNStart = frameN  # exact frame index
        image_next_4.tStart = t  # local t and not account for scr refresh
        image_next_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_next_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_next_4.started')
        image_next_4.setAutoDraw(True)
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_4.started', t)
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(image_next)
                    clickableList = image_next
                except:
                    clickableList = [image_next]
                for obj in clickableList:
                    if obj.contains(mouse_4):
                        gotValidClick = True
                        mouse_4.clicked_name.append(obj.name)
                x, y = mouse_4.getPos()
                mouse_4.x.append(x)
                mouse_4.y.append(y)
                buttons = mouse_4.getPressed()
                mouse_4.leftButton.append(buttons[0])
                mouse_4.midButton.append(buttons[1])
                mouse_4.rightButton.append(buttons[2])
                mouse_4.time.append(mouse_4.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # *images_win* updates
    if images_win.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        images_win.frameNStart = frameN  # exact frame index
        images_win.tStart = t  # local t and not account for scr refresh
        images_win.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(images_win, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'images_win.started')
        images_win.setAutoDraw(True)
    
    # *image_loose* updates
    if image_loose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_loose.frameNStart = frameN  # exact frame index
        image_loose.tStart = t  # local t and not account for scr refresh
        image_loose.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_loose, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_loose.started')
        image_loose.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_4" ---
for thisComponent in instructions_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_4.x', mouse_4.x)
thisExp.addData('mouse_4.y', mouse_4.y)
thisExp.addData('mouse_4.leftButton', mouse_4.leftButton)
thisExp.addData('mouse_4.midButton', mouse_4.midButton)
thisExp.addData('mouse_4.rightButton', mouse_4.rightButton)
thisExp.addData('mouse_4.time', mouse_4.time)
thisExp.addData('mouse_4.clicked_name', mouse_4.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_5
mouse_5.x = []
mouse_5.y = []
mouse_5.leftButton = []
mouse_5.midButton = []
mouse_5.rightButton = []
mouse_5.time = []
mouse_5.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_5Components = [text_instr_5, image_next_5, mouse_5]
for thisComponent in instructions_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr_5* updates
    if text_instr_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr_5.frameNStart = frameN  # exact frame index
        text_instr_5.tStart = t  # local t and not account for scr refresh
        text_instr_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instr_5.started')
        text_instr_5.setAutoDraw(True)
    
    # *image_next_5* updates
    if image_next_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_next_5.frameNStart = frameN  # exact frame index
        image_next_5.tStart = t  # local t and not account for scr refresh
        image_next_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_next_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_next_5.started')
        image_next_5.setAutoDraw(True)
    # *mouse_5* updates
    if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_5.frameNStart = frameN  # exact frame index
        mouse_5.tStart = t  # local t and not account for scr refresh
        mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_5.started', t)
        mouse_5.status = STARTED
        mouse_5.mouseClock.reset()
        prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
    if mouse_5.status == STARTED:  # only update if started and not finished!
        buttons = mouse_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(image_next)
                    clickableList = image_next
                except:
                    clickableList = [image_next]
                for obj in clickableList:
                    if obj.contains(mouse_5):
                        gotValidClick = True
                        mouse_5.clicked_name.append(obj.name)
                x, y = mouse_5.getPos()
                mouse_5.x.append(x)
                mouse_5.y.append(y)
                buttons = mouse_5.getPressed()
                mouse_5.leftButton.append(buttons[0])
                mouse_5.midButton.append(buttons[1])
                mouse_5.rightButton.append(buttons[2])
                mouse_5.time.append(mouse_5.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_5" ---
for thisComponent in instructions_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_5.x', mouse_5.x)
thisExp.addData('mouse_5.y', mouse_5.y)
thisExp.addData('mouse_5.leftButton', mouse_5.leftButton)
thisExp.addData('mouse_5.midButton', mouse_5.midButton)
thisExp.addData('mouse_5.rightButton', mouse_5.rightButton)
thisExp.addData('mouse_5.time', mouse_5.time)
thisExp.addData('mouse_5.clicked_name', mouse_5.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_6" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_6
mouse_6.x = []
mouse_6.y = []
mouse_6.leftButton = []
mouse_6.midButton = []
mouse_6.rightButton = []
mouse_6.time = []
mouse_6.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_6Components = [text_instr_6, image_next_6, mouse_6]
for thisComponent in instructions_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_6" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr_6* updates
    if text_instr_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr_6.frameNStart = frameN  # exact frame index
        text_instr_6.tStart = t  # local t and not account for scr refresh
        text_instr_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instr_6.started')
        text_instr_6.setAutoDraw(True)
    
    # *image_next_6* updates
    if image_next_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_next_6.frameNStart = frameN  # exact frame index
        image_next_6.tStart = t  # local t and not account for scr refresh
        image_next_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_next_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_next_6.started')
        image_next_6.setAutoDraw(True)
    # *mouse_6* updates
    if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_6.frameNStart = frameN  # exact frame index
        mouse_6.tStart = t  # local t and not account for scr refresh
        mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_6.started', t)
        mouse_6.status = STARTED
        mouse_6.mouseClock.reset()
        prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
    if mouse_6.status == STARTED:  # only update if started and not finished!
        buttons = mouse_6.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(image_next)
                    clickableList = image_next
                except:
                    clickableList = [image_next]
                for obj in clickableList:
                    if obj.contains(mouse_6):
                        gotValidClick = True
                        mouse_6.clicked_name.append(obj.name)
                x, y = mouse_6.getPos()
                mouse_6.x.append(x)
                mouse_6.y.append(y)
                buttons = mouse_6.getPressed()
                mouse_6.leftButton.append(buttons[0])
                mouse_6.midButton.append(buttons[1])
                mouse_6.rightButton.append(buttons[2])
                mouse_6.time.append(mouse_6.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_6" ---
for thisComponent in instructions_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_6.x', mouse_6.x)
thisExp.addData('mouse_6.y', mouse_6.y)
thisExp.addData('mouse_6.leftButton', mouse_6.leftButton)
thisExp.addData('mouse_6.midButton', mouse_6.midButton)
thisExp.addData('mouse_6.rightButton', mouse_6.rightButton)
thisExp.addData('mouse_6.time', mouse_6.time)
thisExp.addData('mouse_6.clicked_name', mouse_6.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_7" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_7
mouse_7.x = []
mouse_7.y = []
mouse_7.leftButton = []
mouse_7.midButton = []
mouse_7.rightButton = []
mouse_7.time = []
mouse_7.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_7Components = [text_instr_7, image_next_7, mouse_7]
for thisComponent in instructions_7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_7" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr_7* updates
    if text_instr_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr_7.frameNStart = frameN  # exact frame index
        text_instr_7.tStart = t  # local t and not account for scr refresh
        text_instr_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instr_7.started')
        text_instr_7.setAutoDraw(True)
    
    # *image_next_7* updates
    if image_next_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_next_7.frameNStart = frameN  # exact frame index
        image_next_7.tStart = t  # local t and not account for scr refresh
        image_next_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_next_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_next_7.started')
        image_next_7.setAutoDraw(True)
    # *mouse_7* updates
    if mouse_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_7.frameNStart = frameN  # exact frame index
        mouse_7.tStart = t  # local t and not account for scr refresh
        mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_7.started', t)
        mouse_7.status = STARTED
        mouse_7.mouseClock.reset()
        prevButtonState = mouse_7.getPressed()  # if button is down already this ISN'T a new click
    if mouse_7.status == STARTED:  # only update if started and not finished!
        buttons = mouse_7.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(image_next)
                    clickableList = image_next
                except:
                    clickableList = [image_next]
                for obj in clickableList:
                    if obj.contains(mouse_7):
                        gotValidClick = True
                        mouse_7.clicked_name.append(obj.name)
                x, y = mouse_7.getPos()
                mouse_7.x.append(x)
                mouse_7.y.append(y)
                buttons = mouse_7.getPressed()
                mouse_7.leftButton.append(buttons[0])
                mouse_7.midButton.append(buttons[1])
                mouse_7.rightButton.append(buttons[2])
                mouse_7.time.append(mouse_7.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_7" ---
for thisComponent in instructions_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_7.x', mouse_7.x)
thisExp.addData('mouse_7.y', mouse_7.y)
thisExp.addData('mouse_7.leftButton', mouse_7.leftButton)
thisExp.addData('mouse_7.midButton', mouse_7.midButton)
thisExp.addData('mouse_7.rightButton', mouse_7.rightButton)
thisExp.addData('mouse_7.time', mouse_7.time)
thisExp.addData('mouse_7.clicked_name', mouse_7.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_8" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_8
mouse_8.x = []
mouse_8.y = []
mouse_8.leftButton = []
mouse_8.midButton = []
mouse_8.rightButton = []
mouse_8.time = []
mouse_8.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_8Components = [text_instr_8, image_next_8, mouse_8]
for thisComponent in instructions_8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_8" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr_8* updates
    if text_instr_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr_8.frameNStart = frameN  # exact frame index
        text_instr_8.tStart = t  # local t and not account for scr refresh
        text_instr_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instr_8.started')
        text_instr_8.setAutoDraw(True)
    
    # *image_next_8* updates
    if image_next_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_next_8.frameNStart = frameN  # exact frame index
        image_next_8.tStart = t  # local t and not account for scr refresh
        image_next_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_next_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_next_8.started')
        image_next_8.setAutoDraw(True)
    # *mouse_8* updates
    if mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_8.frameNStart = frameN  # exact frame index
        mouse_8.tStart = t  # local t and not account for scr refresh
        mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_8.started', t)
        mouse_8.status = STARTED
        mouse_8.mouseClock.reset()
        prevButtonState = mouse_8.getPressed()  # if button is down already this ISN'T a new click
    if mouse_8.status == STARTED:  # only update if started and not finished!
        buttons = mouse_8.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(image_next)
                    clickableList = image_next
                except:
                    clickableList = [image_next]
                for obj in clickableList:
                    if obj.contains(mouse_8):
                        gotValidClick = True
                        mouse_8.clicked_name.append(obj.name)
                x, y = mouse_8.getPos()
                mouse_8.x.append(x)
                mouse_8.y.append(y)
                buttons = mouse_8.getPressed()
                mouse_8.leftButton.append(buttons[0])
                mouse_8.midButton.append(buttons[1])
                mouse_8.rightButton.append(buttons[2])
                mouse_8.time.append(mouse_8.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_8" ---
for thisComponent in instructions_8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_8.x', mouse_8.x)
thisExp.addData('mouse_8.y', mouse_8.y)
thisExp.addData('mouse_8.leftButton', mouse_8.leftButton)
thisExp.addData('mouse_8.midButton', mouse_8.midButton)
thisExp.addData('mouse_8.rightButton', mouse_8.rightButton)
thisExp.addData('mouse_8.time', mouse_8.time)
thisExp.addData('mouse_8.clicked_name', mouse_8.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_9" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_9
mouse_9.x = []
mouse_9.y = []
mouse_9.leftButton = []
mouse_9.midButton = []
mouse_9.rightButton = []
mouse_9.time = []
mouse_9.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_9Components = [text_instr_9, image_next_9, mouse_9]
for thisComponent in instructions_9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_9" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr_9* updates
    if text_instr_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr_9.frameNStart = frameN  # exact frame index
        text_instr_9.tStart = t  # local t and not account for scr refresh
        text_instr_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instr_9.started')
        text_instr_9.setAutoDraw(True)
    
    # *image_next_9* updates
    if image_next_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_next_9.frameNStart = frameN  # exact frame index
        image_next_9.tStart = t  # local t and not account for scr refresh
        image_next_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_next_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_next_9.started')
        image_next_9.setAutoDraw(True)
    # *mouse_9* updates
    if mouse_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_9.frameNStart = frameN  # exact frame index
        mouse_9.tStart = t  # local t and not account for scr refresh
        mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_9.started', t)
        mouse_9.status = STARTED
        mouse_9.mouseClock.reset()
        prevButtonState = mouse_9.getPressed()  # if button is down already this ISN'T a new click
    if mouse_9.status == STARTED:  # only update if started and not finished!
        buttons = mouse_9.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(image_next)
                    clickableList = image_next
                except:
                    clickableList = [image_next]
                for obj in clickableList:
                    if obj.contains(mouse_9):
                        gotValidClick = True
                        mouse_9.clicked_name.append(obj.name)
                x, y = mouse_9.getPos()
                mouse_9.x.append(x)
                mouse_9.y.append(y)
                buttons = mouse_9.getPressed()
                mouse_9.leftButton.append(buttons[0])
                mouse_9.midButton.append(buttons[1])
                mouse_9.rightButton.append(buttons[2])
                mouse_9.time.append(mouse_9.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_9" ---
for thisComponent in instructions_9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_9.x', mouse_9.x)
thisExp.addData('mouse_9.y', mouse_9.y)
thisExp.addData('mouse_9.leftButton', mouse_9.leftButton)
thisExp.addData('mouse_9.midButton', mouse_9.midButton)
thisExp.addData('mouse_9.rightButton', mouse_9.rightButton)
thisExp.addData('mouse_9.time', mouse_9.time)
thisExp.addData('mouse_9.clicked_name', mouse_9.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [game, question_mark, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *game* updates
        if game.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            game.frameNStart = frameN  # exact frame index
            game.tStart = t  # local t and not account for scr refresh
            game.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(game, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'game.started')
            game.setAutoDraw(True)
        
        # *question_mark* updates
        if question_mark.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            question_mark.frameNStart = frameN  # exact frame index
            question_mark.tStart = t  # local t and not account for scr refresh
            question_mark.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_mark, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'question_mark.started')
            question_mark.setAutoDraw(True)
        if question_mark.status == STARTED:  # only update if drawing
            question_mark.setOpacity(1.0, log=False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "outcome" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from fb_code
    # Check if the key press was correct or not.
    # This routine will need to follow another routine with a 
    # key response component in it called "key_resp" 
    # and the "store correct" option enabled. 
    # If your experiment is missing that you will 
    # not receive feedback and an error message will be displayed.
    
    # If a key response component has been added and feedback is functioning.
    # 1. remove lines 12, 13, 15, 22 and 23.
    # 2. dedent lines 16 to 21
    
    fb_text = 'no key_resp component found - look at the Std out window for info'
    fb_col = 'black'
    
    try:
        if key_resp.corr:
            fb_text = 'Correct!'
            fb_col = 'green'
        else:
            fb_text = 'Incorrect'
            fb_col = 'red'
    except:
        print('Make sure that you have:\n1. a routine with a keyboard component in it called "key_resp"\n 2. In the key_Resp component in the "data" tab select "Store Correct".\n in the "Correct answer" field use "$corrAns" (where corrAns is a column header in your conditions file indicating the correct key press')
    
    fb.setColor(fb_col, colorSpace='rgb')
    fb.setText(fb_text)
    # keep track of which components have finished
    outcomeComponents = [fb]
    for thisComponent in outcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "outcome" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fb* updates
        if fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fb.frameNStart = frameN  # exact frame index
            fb.tStart = t  # local t and not account for scr refresh
            fb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fb, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fb.started')
            fb.setAutoDraw(True)
        if fb.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fb.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fb.tStop = t  # not accounting for scr refresh
                fb.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fb.stopped')
                fb.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in outcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "outcome" ---
    for thisComponent in outcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
