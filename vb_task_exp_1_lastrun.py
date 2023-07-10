#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Wed Jul  5 18:10:20 2023
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

# Run 'Before Experiment' code from code_4
short_blocks = [4, 5, 6]
long_blocks = [38, 40, 42]

firstRun = [ np.random.randint(2) for i in range(10) ]
secondRun = [ np.random.randint(2) for i in range(10) ]
thirdRun = [ np.random.randint(2) for i in range(10) ]

firstRunBlockDuration = [ (np.random.choice(short_blocks) if firstRun[i] == 0 \
    else np.random.choice(long_blocks)) for i in range(10) ]
    
secondRunBlockDuration = [ (np.random.choice(short_blocks) if secondRun[i] == 0 \
    else np.random.choice(long_blocks)) for i in range(10) ]

thirdRunBlockDuration = [ (np.random.choice(short_blocks) if thirdRun[i] == 0 \
    else np.random.choice(long_blocks)) for i in range(10) ]
    
   
   
   
firstCounter = 0
secondCounter = 0
thridCounter = 0


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'vb_task_exp_1'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'group': ['A', 'B'],
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
    originPath='/Users/eliasaoundurand/Projets/CausaL/psychopy_exps/vb_task_exp_1_lastrun.py',
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
    size=[1512, 982], fullscr=True, screen=0, 
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

# --- Initialize components for Routine "demographics" ---
age = visual.TextStim(win=win, name='age',
    text="À quel groupe d'âge appartenez-vous?",
    font='Arial',
    pos=(0.0, 0.4), height=0.026, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
respAge = visual.Slider(win=win, name='respAge',
    startValue=None, size=(0.9, 0.015), pos=(0, 0.3), units=None,
    labels=("Moins de 16", "16-20", "21-25", "26-30", "31-35", "36-40", "Plus de 40"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.026,
    flip=False, ori=0.0, depth=-1, readOnly=False)
gender = visual.TextStim(win=win, name='gender',
    text='Quel est votre genre?',
    font='Arial',
    pos=(0, 0.2), height=0.026, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
genderResp1 = visual.Slider(win=win, name='genderResp1',
    startValue=None, size=(0.9, 0.015), pos=(0, 0.15), units=None,
    labels=("Autre", "Non-binaire", "Homme", "Femme"), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.026,
    flip=False, ori=0.0, depth=-3, readOnly=False)
student = visual.TextStim(win=win, name='student',
    text='Êtes-vous étudiant?',
    font='Arial',
    pos=(0, 0), height=0.026, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
studentResp = visual.Slider(win=win, name='studentResp',
    startValue=None, size=(1.1, 0.02), pos=(0, -0.05), units=None,
    labels=("Licence", "Master", "Doctorat", "Non"), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.026,
    flip=False, ori=0.0, depth=-5, readOnly=False)
mood = visual.TextStim(win=win, name='mood',
    text='Quel est votre humeur actuelle? ',
    font='Arial',
    pos=(0, -0.15), height=0.026, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
moodResp = visual.Slider(win=win, name='moodResp',
    startValue=None, size=(1.1, 0.02), pos=(0, -0.2), units=None,
    labels=("Low", "Okay", "Great!"), ticks=(1, 2, 3), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.03,
    flip=False, ori=0.0, depth=-7, readOnly=False)
nextButton = visual.ImageStim(
    win=win,
    name='nextButton', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.4), size=(0.15, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "instr_gen_1" ---
text_instr = visual.TextStim(win=win, name='text_instr',
    text="Insctructions générales:"+"\n Vous êtes un dénicheur de talents pour des équipes de volleyball. Les équipes de la ligue souhaitent connaître votre avis sur la signature de nouveaux joueurs. Vous allez participer à des matchs tests pour évaluer l'impact des nouveaux joueurs sur leur équipe."+"\n Appuyez sur la touche espace pour continuer.",
    font='Arial',
    pos=(0.0, 0.0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "instr_gen_2" ---
text_instr_2 = visual.TextStim(win=win, name='text_instr_2',
    text="Instructions générales:"+ "\n Le jeu se déroule en trois saisons en plus d'une phase d'entraînement pour vous familiariser avec le jeu. Lors de la a première saison, vous prendrez toutes les décisions. Les règles changeront pour la deuxième et troisième saison, vous serez alors assisté par un coach adjoint."+"\n Appuyez sur la touche espace pour continuer.",
    font='Arial',
    pos=(0.0,0.0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "instr_gen_3" ---
text_instr_3 = visual.TextStim(win=win, name='text_instr_3',
    text="Rémunération"+"\n À la fin de chaque série de jeux, vous évaluerez l'impact du joueur sur les matchs entre -10 (minimal) et 10 (maximal) en passant par 0 (neutre) et recommenderez ou non l'achat du joueur. Votre rémunération sera calculée en fonction de la précision de l'impact que vous avez attribué aux différents joueurs par rapport à leur impact réel. Un seul joueur sera sélectionné au hasard pour le calcul du paiement. Si l'impact estimé est identique à l'impact réel, vous gagnerez 10 €. Plus vous vous éloignez de l'impact réel moins vous serez payé. Cette somme s'ajoutera aux 5 € de jetons de présence." +"\n Appuyez sur la touche espace pour continuer.",
    font='Arial',
    pos=(0.0,0.0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# --- Initialize components for Routine "instruction_trial_1" ---
text_instr_13 = visual.TextStim(win=win, name='text_instr_13',
    text="Règles du jeu:" + "\n Votre objectif est de décider si un nouveau joueur doit participer au match ou rester sur le banc, puis d'évaluer son impact sur l'équipe en termes de victoire ou de défaite. Pour chaque joueur, vous disposerez d'un certain nombre de matchs pour prendre votre décision. Utilisez la touche flèche droite pour inclure le joueur dans le match (Avec) et la touche flèche gauche pour le laisser sur le banc (Sans), figures gauche."+"\n Un smiley souriant représente une victoire, tandis qu'un smiley triste indique une défaite, figures droite. Vous devez prendre votre décision dans les 2 secondes suivant la disparition du smiley." + "\n À la fin de la série de matchs pour chaque joueur, évaluez l'impact du joueur sur les résultats en attribuant un score compris entre -10 (impact négatif) et 10 (impact positif), en passant par 0 (impact neutre). Enfin, recommandez ou non l'achat du joueur en fonction de votre évaluation."+"\n Appuyez sur la touche espace pour commencer.",
    font='Arial',
    pos=(0.0,0.05), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()
image_avec = visual.ImageStim(
    win=win,
    name='image_avec', 
    image='images/Avec.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.6, 0.1), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_sans = visual.ImageStim(
    win=win,
    name='image_sans', 
    image='images/Sans.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.1), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_victoire = visual.ImageStim(
    win=win,
    name='image_victoire', 
    image='images/Win.png', mask=None, anchor='center',
    ori=0.0, pos=(0.63, 0.1), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_defaite = visual.ImageStim(
    win=win,
    name='image_defaite', 
    image='images/Lose.png', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0.1), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
text_avec = visual.TextStim(win=win, name='text_avec',
    text="avec",
    font='Open Sans',
    pos=(-0.6, 0.05), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
text_sans = visual.TextStim(win=win, name='text_sans',
    text="sans",
    font='Open Sans',
    pos=(-0.4, 0.05), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
text_victoire = visual.TextStim(win=win, name='text_victoire',
    text="C'est une victoire!",
    font='Open Sans',
    pos=(0.63, 0.0), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
text_defaite = visual.TextStim(win=win, name='text_defaite',
    text="C'est une défaite!",
    font='Open Sans',
    pos=(0.4, 0.0), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# --- Initialize components for Routine "info_training" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text="Début de l'entraînement",
    font='Open Sans',
    pos=(0, 0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "joueur_number_instr" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "fixation" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.015, 0.015),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "cues" ---
# Set experiment start values for variable component nombre_matchs
nombre_matchs = 1
nombre_matchsContainer = []
question_mark_training = visual.TextStim(win=win, name='question_mark_training',
    text='Trop lent',
    font='Open Sans',
    pos=(0, -0.1), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_training = keyboard.Keyboard()
avec_training = visual.TextStim(win=win, name='avec_training',
    text="avec",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-4.0);
sans_training = visual.TextStim(win=win, name='sans_training',
    text="sans",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-5.0);
nombre_match_training = visual.TextStim(win=win, name='nombre_match_training',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
text_question = visual.TextStim(win=win, name='text_question',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-7.0);
cross_training = visual.ShapeStim(
    win=win, name='cross_training', vertices='cross',
    size=(0.015, 0.015),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-8.0, interpolate=True)
avec_cues = visual.ImageStim(
    win=win,
    name='avec_cues', 
    image='images/Avec.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
sans_cues = visual.ImageStim(
    win=win,
    name='sans_cues', 
    image='images/Sans.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
joueur = visual.TextStim(win=win, name='joueur',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.35), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

# --- Initialize components for Routine "feedback" ---
text_question_outcome = visual.TextStim(win=win, name='text_question_outcome',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
nombre_match_training_outcome = visual.TextStim(win=win, name='nombre_match_training_outcome',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
text_avec_fb = visual.TextStim(win=win, name='text_avec_fb',
    text="avec",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-3.0);
text_sans_fb = visual.TextStim(win=win, name='text_sans_fb',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-4.0);
avec_feedback = visual.ImageStim(
    win=win,
    name='avec_feedback', 
    image='images/Avec.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
sans_feedback = visual.ImageStim(
    win=win,
    name='sans_feedback', 
    image='images/Sans.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color='white', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
outcome_feedback = visual.ImageStim(
    win=win,
    name='outcome_feedback', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
text_resultat = visual.TextStim(win=win, name='text_resultat',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
cross_outcome_training = visual.ShapeStim(
    win=win, name='cross_outcome_training', vertices='cross',
    size=(0.015, 0.015),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-9.0, interpolate=True)
joueur_feedback = visual.TextStim(win=win, name='joueur_feedback',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.35), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "question" ---
attractiveness = visual.Slider(win=win, name='attractiveness',
    startValue=None, size=(0.9, 0.05), pos=(0, 0), units=None,
    labels=(-10, -9, -8, -7, -6, -5, -4, -3, -2, -1,  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), ticks=(-10, -9, -8, -7, -6, -5, -4, -3, -2, -1,  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.026,
    flip=False, ori=0.0, depth=-1, readOnly=False)
text_question_1 = visual.TextStim(win=win, name='text_question_1',
    text='',
    font='Open Sans',
    pos=(0, 0.2), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
validate = visual.TextStim(win=win, name='validate',
    text='VALIDER',
    font='Open Sans',
    pos=(0.4, -0.3), height=0.026, wrapWidth=None, ori=0.0, 
    color=[-1.0000, 0.0039, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-3.0);
mouse_15 = event.Mouse(win=win)
x, y = [None, None]
mouse_15.mouseClock = core.Clock()
slider_recommandation = visual.Slider(win=win, name='slider_recommandation',
    startValue=None, size=(0.1, 0.05), pos=(0, -0.3), units=None,
    labels=('non', 'oui'), ticks=(0,1), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.026,
    flip=False, ori=0.0, depth=-5, readOnly=False)
text_recommandation = visual.TextStim(win=win, name='text_recommandation',
    text="Recommandez-vous l'achat du joueur?",
    font='Open Sans',
    pos=(0.0, -0.2), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ending" ---
text = visual.TextStim(win=win, name='text',
    text="Fin."+"\n Appuyez sur la touche espace pour passer à la saison suivante.",
    font='Open Sans',
    pos=(0, 0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# --- Initialize components for Routine "info_trial_1" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text="Première saison",
    font='Open Sans',
    pos=(0, 0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "instruction_trial_1" ---
text_instr_13 = visual.TextStim(win=win, name='text_instr_13',
    text="Règles du jeu:" + "\n Votre objectif est de décider si un nouveau joueur doit participer au match ou rester sur le banc, puis d'évaluer son impact sur l'équipe en termes de victoire ou de défaite. Pour chaque joueur, vous disposerez d'un certain nombre de matchs pour prendre votre décision. Utilisez la touche flèche droite pour inclure le joueur dans le match (Avec) et la touche flèche gauche pour le laisser sur le banc (Sans), figures gauche."+"\n Un smiley souriant représente une victoire, tandis qu'un smiley triste indique une défaite, figures droite. Vous devez prendre votre décision dans les 2 secondes suivant la disparition du smiley." + "\n À la fin de la série de matchs pour chaque joueur, évaluez l'impact du joueur sur les résultats en attribuant un score compris entre -10 (impact négatif) et 10 (impact positif), en passant par 0 (impact neutre). Enfin, recommandez ou non l'achat du joueur en fonction de votre évaluation."+"\n Appuyez sur la touche espace pour commencer.",
    font='Arial',
    pos=(0.0,0.05), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()
image_avec = visual.ImageStim(
    win=win,
    name='image_avec', 
    image='images/Avec.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.6, 0.1), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_sans = visual.ImageStim(
    win=win,
    name='image_sans', 
    image='images/Sans.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.1), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_victoire = visual.ImageStim(
    win=win,
    name='image_victoire', 
    image='images/Win.png', mask=None, anchor='center',
    ori=0.0, pos=(0.63, 0.1), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_defaite = visual.ImageStim(
    win=win,
    name='image_defaite', 
    image='images/Lose.png', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0.1), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
text_avec = visual.TextStim(win=win, name='text_avec',
    text="avec",
    font='Open Sans',
    pos=(-0.6, 0.05), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
text_sans = visual.TextStim(win=win, name='text_sans',
    text="sans",
    font='Open Sans',
    pos=(-0.4, 0.05), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
text_victoire = visual.TextStim(win=win, name='text_victoire',
    text="C'est une victoire!",
    font='Open Sans',
    pos=(0.63, 0.0), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
text_defaite = visual.TextStim(win=win, name='text_defaite',
    text="C'est une défaite!",
    font='Open Sans',
    pos=(0.4, 0.0), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# --- Initialize components for Routine "joueur_number_instr" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "fixation" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.015, 0.015),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "cues" ---
# Set experiment start values for variable component nombre_matchs
nombre_matchs = 1
nombre_matchsContainer = []
question_mark_training = visual.TextStim(win=win, name='question_mark_training',
    text='Trop lent',
    font='Open Sans',
    pos=(0, -0.1), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_training = keyboard.Keyboard()
avec_training = visual.TextStim(win=win, name='avec_training',
    text="avec",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-4.0);
sans_training = visual.TextStim(win=win, name='sans_training',
    text="sans",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-5.0);
nombre_match_training = visual.TextStim(win=win, name='nombre_match_training',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
text_question = visual.TextStim(win=win, name='text_question',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-7.0);
cross_training = visual.ShapeStim(
    win=win, name='cross_training', vertices='cross',
    size=(0.015, 0.015),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-8.0, interpolate=True)
avec_cues = visual.ImageStim(
    win=win,
    name='avec_cues', 
    image='images/Avec.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
sans_cues = visual.ImageStim(
    win=win,
    name='sans_cues', 
    image='images/Sans.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
joueur = visual.TextStim(win=win, name='joueur',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.35), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

# --- Initialize components for Routine "feedback" ---
text_question_outcome = visual.TextStim(win=win, name='text_question_outcome',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
nombre_match_training_outcome = visual.TextStim(win=win, name='nombre_match_training_outcome',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
text_avec_fb = visual.TextStim(win=win, name='text_avec_fb',
    text="avec",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-3.0);
text_sans_fb = visual.TextStim(win=win, name='text_sans_fb',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-4.0);
avec_feedback = visual.ImageStim(
    win=win,
    name='avec_feedback', 
    image='images/Avec.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
sans_feedback = visual.ImageStim(
    win=win,
    name='sans_feedback', 
    image='images/Sans.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color='white', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
outcome_feedback = visual.ImageStim(
    win=win,
    name='outcome_feedback', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
text_resultat = visual.TextStim(win=win, name='text_resultat',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
cross_outcome_training = visual.ShapeStim(
    win=win, name='cross_outcome_training', vertices='cross',
    size=(0.015, 0.015),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1.0, depth=-9.0, interpolate=True)
joueur_feedback = visual.TextStim(win=win, name='joueur_feedback',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.35), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "question" ---
attractiveness = visual.Slider(win=win, name='attractiveness',
    startValue=None, size=(0.9, 0.05), pos=(0, 0), units=None,
    labels=(-10, -9, -8, -7, -6, -5, -4, -3, -2, -1,  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), ticks=(-10, -9, -8, -7, -6, -5, -4, -3, -2, -1,  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.026,
    flip=False, ori=0.0, depth=-1, readOnly=False)
text_question_1 = visual.TextStim(win=win, name='text_question_1',
    text='',
    font='Open Sans',
    pos=(0, 0.2), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
validate = visual.TextStim(win=win, name='validate',
    text='VALIDER',
    font='Open Sans',
    pos=(0.4, -0.3), height=0.026, wrapWidth=None, ori=0.0, 
    color=[-1.0000, 0.0039, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-3.0);
mouse_15 = event.Mouse(win=win)
x, y = [None, None]
mouse_15.mouseClock = core.Clock()
slider_recommandation = visual.Slider(win=win, name='slider_recommandation',
    startValue=None, size=(0.1, 0.05), pos=(0, -0.3), units=None,
    labels=('non', 'oui'), ticks=(0,1), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.026,
    flip=False, ori=0.0, depth=-5, readOnly=False)
text_recommandation = visual.TextStim(win=win, name='text_recommandation',
    text="Recommandez-vous l'achat du joueur?",
    font='Open Sans',
    pos=(0.0, -0.2), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ending" ---
text = visual.TextStim(win=win, name='text',
    text="Fin."+"\n Appuyez sur la touche espace pour passer à la saison suivante.",
    font='Open Sans',
    pos=(0, 0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# --- Initialize components for Routine "instruction_trial_23" ---
text_instr_11 = visual.TextStim(win=win, name='text_instr_11',
    text='',
    font='Arial',
    pos=(0.0,0.0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()
avec_inst_23 = visual.ImageStim(
    win=win,
    name='avec_inst_23', 
    image='images/Avec.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sans_instr_23 = visual.ImageStim(
    win=win,
    name='sans_instr_23', 
    image='images/Sans.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.1, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
domicile_instr_23 = visual.ImageStim(
    win=win,
    name='domicile_instr_23', 
    image='images/Home.png', mask=None, anchor='center',
    ori=0.0, pos=(0.1, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
exterieur_instr_23 = visual.ImageStim(
    win=win,
    name='exterieur_instr_23', 
    image='images/Outside.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
avec_instr_23 = visual.TextStim(win=win, name='avec_instr_23',
    text="avec",
    font='Open Sans',
    pos=(-0.3, -0.4), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
sans_inst_23 = visual.TextStim(win=win, name='sans_inst_23',
    text="sans",
    font='Open Sans',
    pos=(-0.1, -0.4), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
domicile_inst_23 = visual.TextStim(win=win, name='domicile_inst_23',
    text="domicile",
    font='Open Sans',
    pos=(0.1, -0.4), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-8.0);
exterieur_inst_23 = visual.TextStim(win=win, name='exterieur_inst_23',
    text="extérieur",
    font='Open Sans',
    pos=(0.3, -0.4), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# --- Initialize components for Routine "joueur_number_instr" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "fixation" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.015, 0.015),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "cues_23" ---
# Set experiment start values for variable component nombre_matchs_third
nombre_matchs_third = 1
nombre_matchs_thirdContainer = []
key_resp_3 = keyboard.Keyboard()
question_mark3 = visual.TextStim(win=win, name='question_mark3',
    text='Trop lent',
    font='Open Sans',
    pos=(0, -0.1), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
avec3 = visual.TextStim(win=win, name='avec3',
    text="avec",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-4.0);
sans3 = visual.TextStim(win=win, name='sans3',
    text="sans",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-5.0);
domicile3 = visual.TextStim(win=win, name='domicile3',
    text="domicile",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
exterieur3 = visual.TextStim(win=win, name='exterieur3',
    text="extérieur",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-7.0);
observation = visual.TextStim(win=win, name='observation',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-8.0);
# Set experiment start values for variable component observation_var
observation_var = ''
observation_varContainer = []
text_nombre_matchs_third = visual.TextStim(win=win, name='text_nombre_matchs_third',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.4), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-10.0);
question_trial23 = visual.TextStim(win=win, name='question_trial23',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-11.0);
numero_joueur_cues_23 = visual.TextStim(win=win, name='numero_joueur_cues_23',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.35), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
cross_fixation = visual.ShapeStim(
    win=win, name='cross_fixation', vertices='cross',
    size=(0.015, 0.015),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-13.0, interpolate=True)
avec_cues_23 = visual.ImageStim(
    win=win,
    name='avec_cues_23', 
    image='images/Avec.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color='white', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
sans_cues_23 = visual.ImageStim(
    win=win,
    name='sans_cues_23', 
    image='images/Sans.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
domicile_cues_23 = visual.ImageStim(
    win=win,
    name='domicile_cues_23', 
    image='images/Home.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
exterieur_cues_23 = visual.ImageStim(
    win=win,
    name='exterieur_cues_23', 
    image='images/Outside.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)

# --- Initialize components for Routine "feedback_23" ---
fb_text_choice_component = visual.TextStim(win=win, name='fb_text_choice_component',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
image_outcome3 = visual.ImageStim(
    win=win,
    name='image_outcome3', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(3.5, 3.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
# Set experiment start values for variable component outcome3_var
outcome3_var = ''
outcome3_varContainer = []
nombre_matchs_third_outcome = visual.TextStim(win=win, name='nombre_matchs_third_outcome',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-4.0);
avec3_outcome = visual.TextStim(win=win, name='avec3_outcome',
    text="avec",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
sans3_outcome = visual.TextStim(win=win, name='sans3_outcome',
    text="sans",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
domicile3_outcome = visual.TextStim(win=win, name='domicile3_outcome',
    text="domicile",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-7.0);
exterieur3_outcome = visual.TextStim(win=win, name='exterieur3_outcome',
    text="extérieur",
    font='Open Sans',
    pos=[0,0], height=0.026, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-8.0);
resultat3_outcome = visual.TextStim(win=win, name='resultat3_outcome',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-9.0);
domicile_image23 = visual.ImageStim(
    win=win,
    name='domicile_image23', 
    image='images/Home.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color='white', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
exterieur_image23 = visual.ImageStim(
    win=win,
    name='exterieur_image23', 
    image='images/Outside.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color='white', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
question_outcome23 = visual.TextStim(win=win, name='question_outcome23',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
text_joueur_numero = visual.TextStim(win=win, name='text_joueur_numero',
    text='',
    font='Open Sans',
    pos=(-0.5, 0.35), height=0.026, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
cross_feedback23 = visual.ShapeStim(
    win=win, name='cross_feedback23', vertices='cross',
    size=(0.015, 0.015),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-14.0, interpolate=True)
avec_image23 = visual.ImageStim(
    win=win,
    name='avec_image23', 
    image='images/Avec.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
sans_image23 = visual.ImageStim(
    win=win,
    name='sans_image23', 
    image='images/Sans.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)

# --- Initialize components for Routine "question" ---
attractiveness = visual.Slider(win=win, name='attractiveness',
    startValue=None, size=(0.9, 0.05), pos=(0, 0), units=None,
    labels=(-10, -9, -8, -7, -6, -5, -4, -3, -2, -1,  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), ticks=(-10, -9, -8, -7, -6, -5, -4, -3, -2, -1,  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.026,
    flip=False, ori=0.0, depth=-1, readOnly=False)
text_question_1 = visual.TextStim(win=win, name='text_question_1',
    text='',
    font='Open Sans',
    pos=(0, 0.2), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
validate = visual.TextStim(win=win, name='validate',
    text='VALIDER',
    font='Open Sans',
    pos=(0.4, -0.3), height=0.026, wrapWidth=None, ori=0.0, 
    color=[-1.0000, 0.0039, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-3.0);
mouse_15 = event.Mouse(win=win)
x, y = [None, None]
mouse_15.mouseClock = core.Clock()
slider_recommandation = visual.Slider(win=win, name='slider_recommandation',
    startValue=None, size=(0.1, 0.05), pos=(0, -0.3), units=None,
    labels=('non', 'oui'), ticks=(0,1), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.026,
    flip=False, ori=0.0, depth=-5, readOnly=False)
text_recommandation = visual.TextStim(win=win, name='text_recommandation',
    text="Recommandez-vous l'achat du joueur?",
    font='Open Sans',
    pos=(0.0, -0.2), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ending" ---
text = visual.TextStim(win=win, name='text',
    text="Fin."+"\n Appuyez sur la touche espace pour passer à la saison suivante.",
    font='Open Sans',
    pos=(0, 0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# --- Initialize components for Routine "instruction_end" ---
text_instr_12 = visual.TextStim(win=win, name='text_instr_12',
    text="Fin du jeu" + "\n Merci d'avoir participé!"+"\n Appuyez sur la touche espace pour terminer la session.",
    font='Arial',
    pos=(0.0,0.0), height=0.026, wrapWidth=0.56, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_12 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "demographics" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
respAge.reset()
genderResp1.reset()
studentResp.reset()
moodResp.reset()
# setup some python lists for storing info about the mouse
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
demographicsComponents = [age, respAge, gender, genderResp1, student, studentResp, mood, moodResp, nextButton, mouse]
for thisComponent in demographicsComponents:
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

# --- Run Routine "demographics" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *age* updates
    if age.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        age.frameNStart = frameN  # exact frame index
        age.tStart = t  # local t and not account for scr refresh
        age.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(age, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'age.started')
        age.setAutoDraw(True)
    
    # *respAge* updates
    if respAge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respAge.frameNStart = frameN  # exact frame index
        respAge.tStart = t  # local t and not account for scr refresh
        respAge.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respAge, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'respAge.started')
        respAge.setAutoDraw(True)
    
    # *gender* updates
    if gender.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gender.frameNStart = frameN  # exact frame index
        gender.tStart = t  # local t and not account for scr refresh
        gender.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gender, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'gender.started')
        gender.setAutoDraw(True)
    
    # *genderResp1* updates
    if genderResp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        genderResp1.frameNStart = frameN  # exact frame index
        genderResp1.tStart = t  # local t and not account for scr refresh
        genderResp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(genderResp1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'genderResp1.started')
        genderResp1.setAutoDraw(True)
    
    # *student* updates
    if student.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        student.frameNStart = frameN  # exact frame index
        student.tStart = t  # local t and not account for scr refresh
        student.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(student, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'student.started')
        student.setAutoDraw(True)
    
    # *studentResp* updates
    if studentResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        studentResp.frameNStart = frameN  # exact frame index
        studentResp.tStart = t  # local t and not account for scr refresh
        studentResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(studentResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'studentResp.started')
        studentResp.setAutoDraw(True)
    
    # *mood* updates
    if mood.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mood.frameNStart = frameN  # exact frame index
        mood.tStart = t  # local t and not account for scr refresh
        mood.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mood, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'mood.started')
        mood.setAutoDraw(True)
    
    # *moodResp* updates
    if moodResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        moodResp.frameNStart = frameN  # exact frame index
        moodResp.tStart = t  # local t and not account for scr refresh
        moodResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(moodResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'moodResp.started')
        moodResp.setAutoDraw(True)
    
    # *nextButton* updates
    if nextButton.status == NOT_STARTED and respAge.rating and genderResp1.rating and studentResp.rating and moodResp.rating:
        # keep track of start time/frame for later
        nextButton.frameNStart = frameN  # exact frame index
        nextButton.tStart = t  # local t and not account for scr refresh
        nextButton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nextButton, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'nextButton.started')
        nextButton.setAutoDraw(True)
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
                    iter(nextButton)
                    clickableList = nextButton
                except:
                    clickableList = [nextButton]
                for obj in clickableList:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
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
    for thisComponent in demographicsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "demographics" ---
for thisComponent in demographicsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('respAge.response', respAge.getRating())
thisExp.addData('respAge.rt', respAge.getRT())
thisExp.addData('genderResp1.response', genderResp1.getRating())
thisExp.addData('genderResp1.rt', genderResp1.getRT())
thisExp.addData('studentResp.response', studentResp.getRating())
thisExp.addData('studentResp.rt', studentResp.getRT())
thisExp.addData('moodResp.response', moodResp.getRating())
thisExp.addData('moodResp.rt', moodResp.getRT())
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(nextButton)
        clickableList = nextButton
    except:
        clickableList = [nextButton]
    for obj in clickableList:
        if obj.contains(mouse):
            gotValidClick = True
            mouse.clicked_name.append(obj.name)
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
if len(mouse.clicked_name):
    thisExp.addData('mouse.clicked_name', mouse.clicked_name[0])
thisExp.nextEntry()
# the Routine "demographics" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instr_gen_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
instr_gen_1Components = [text_instr, key_resp_4]
for thisComponent in instr_gen_1Components:
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

# --- Run Routine "instr_gen_1" ---
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
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_4.started')
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
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
    for thisComponent in instr_gen_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instr_gen_1" ---
for thisComponent in instr_gen_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "instr_gen_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instr_gen_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
instr_gen_2Components = [text_instr_2, key_resp_5]
for thisComponent in instr_gen_2Components:
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

# --- Run Routine "instr_gen_2" ---
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
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_5.started')
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
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
    for thisComponent in instr_gen_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instr_gen_2" ---
for thisComponent in instr_gen_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "instr_gen_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instr_gen_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
instr_gen_3Components = [text_instr_3, key_resp_7]
for thisComponent in instr_gen_3Components:
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

# --- Run Routine "instr_gen_3" ---
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
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_7.started')
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
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
    for thisComponent in instr_gen_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instr_gen_3" ---
for thisComponent in instr_gen_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "instr_gen_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction_trial_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
instruction_trial_1Components = [text_instr_13, key_resp_8, image_avec, image_sans, image_victoire, image_defaite, text_avec, text_sans, text_victoire, text_defaite]
for thisComponent in instruction_trial_1Components:
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

# --- Run Routine "instruction_trial_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr_13* updates
    if text_instr_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr_13.frameNStart = frameN  # exact frame index
        text_instr_13.tStart = t  # local t and not account for scr refresh
        text_instr_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instr_13.started')
        text_instr_13.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_8.started')
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_avec* updates
    if image_avec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_avec.frameNStart = frameN  # exact frame index
        image_avec.tStart = t  # local t and not account for scr refresh
        image_avec.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_avec, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_avec.started')
        image_avec.setAutoDraw(True)
    
    # *image_sans* updates
    if image_sans.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_sans.frameNStart = frameN  # exact frame index
        image_sans.tStart = t  # local t and not account for scr refresh
        image_sans.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_sans, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_sans.started')
        image_sans.setAutoDraw(True)
    
    # *image_victoire* updates
    if image_victoire.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_victoire.frameNStart = frameN  # exact frame index
        image_victoire.tStart = t  # local t and not account for scr refresh
        image_victoire.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_victoire, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_victoire.started')
        image_victoire.setAutoDraw(True)
    
    # *image_defaite* updates
    if image_defaite.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_defaite.frameNStart = frameN  # exact frame index
        image_defaite.tStart = t  # local t and not account for scr refresh
        image_defaite.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_defaite, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_defaite.started')
        image_defaite.setAutoDraw(True)
    
    # *text_avec* updates
    if text_avec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_avec.frameNStart = frameN  # exact frame index
        text_avec.tStart = t  # local t and not account for scr refresh
        text_avec.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_avec, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_avec.started')
        text_avec.setAutoDraw(True)
    
    # *text_sans* updates
    if text_sans.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_sans.frameNStart = frameN  # exact frame index
        text_sans.tStart = t  # local t and not account for scr refresh
        text_sans.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_sans, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_sans.started')
        text_sans.setAutoDraw(True)
    
    # *text_victoire* updates
    if text_victoire.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_victoire.frameNStart = frameN  # exact frame index
        text_victoire.tStart = t  # local t and not account for scr refresh
        text_victoire.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_victoire, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_victoire.started')
        text_victoire.setAutoDraw(True)
    
    # *text_defaite* updates
    if text_defaite.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_defaite.frameNStart = frameN  # exact frame index
        text_defaite.tStart = t  # local t and not account for scr refresh
        text_defaite.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_defaite, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_defaite.started')
        text_defaite.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_trial_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_trial_1" ---
for thisComponent in instruction_trial_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "instruction_trial_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "info_training" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
info_trainingComponents = [text_3]
for thisComponent in info_trainingComponents:
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

# --- Run Routine "info_training" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.stopped')
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in info_trainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "info_training" ---
for thisComponent in info_trainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# set up handler to look after randomisation of conditions etc
trainingRun = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/loopConditions.csv'),
    seed=None, name='trainingRun')
thisExp.addLoop(trainingRun)  # add the loop to the experiment
thisTrainingRun = trainingRun.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrainingRun.rgb)
if thisTrainingRun != None:
    for paramName in thisTrainingRun:
        exec('{} = thisTrainingRun[paramName]'.format(paramName))

for thisTrainingRun in trainingRun:
    currentLoop = trainingRun
    # abbreviate parameter names if possible (e.g. rgb = thisTrainingRun.rgb)
    if thisTrainingRun != None:
        for paramName in thisTrainingRun:
            exec('{} = thisTrainingRun[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "joueur_number_instr" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_5
    try: 
        joueur_number = Condition
    except: 
        joueur_number = "25"
    text_4.setText("Joueur {}".format(chr(joueur_number+64)))
    # keep track of which components have finished
    joueur_number_instrComponents = [text_4]
    for thisComponent in joueur_number_instrComponents:
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
    
    # --- Run Routine "joueur_number_instr" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.stopped')
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in joueur_number_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "joueur_number_instr" ---
    for thisComponent in joueur_number_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    trainingBlocks = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions/CounterBalancedKeys.csv', selection=[np.random.randint(1, 4)]),
        seed=None, name='trainingBlocks')
    thisExp.addLoop(trainingBlocks)  # add the loop to the experiment
    thisTrainingBlock = trainingBlocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrainingBlock.rgb)
    if thisTrainingBlock != None:
        for paramName in thisTrainingBlock:
            exec('{} = thisTrainingBlock[paramName]'.format(paramName))
    
    for thisTrainingBlock in trainingBlocks:
        currentLoop = trainingBlocks
        # abbreviate parameter names if possible (e.g. rgb = thisTrainingBlock.rgb)
        if thisTrainingBlock != None:
            for paramName in thisTrainingBlock:
                exec('{} = thisTrainingBlock[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [cross]
        for thisComponent in fixationComponents:
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
        
        # --- Run Routine "fixation" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.started')
                cross.setAutoDraw(True)
            if cross.status == STARTED:
                if frameN >= 40:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross.stopped')
                    cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "cues" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        try: 
            joueur_number = Condition
        except: 
            joueur_number = "25"
        key_resp_training.keys = []
        key_resp_training.rt = []
        _key_resp_training_allKeys = []
        avec_training.setPos([tuple(float(x) for x in avec_pos_text.strip("()").split(","))])
        sans_training.setPos([tuple(float(x) for x in sans_pos_text.strip("()").split(","))])
        nombre_match_training.setText("match n° {}".format(nombre_matchs))
        text_question.setText("Question: Voulez vous faire jouer l'équipe avec ou sans le joueur {} ?".format(chr(joueur_number+64)))
        avec_cues.setPos([tuple(float(x) for x in avec_pos_image.strip("()").split(","))])
        sans_cues.setPos([tuple(float(x) for x in sans_pos_image.strip("()").split(","))])
        joueur.setText("joueur {}".format(chr(joueur_number+64)))
        # keep track of which components have finished
        cuesComponents = [question_mark_training, key_resp_training, avec_training, sans_training, nombre_match_training, text_question, cross_training, avec_cues, sans_cues, joueur]
        for thisComponent in cuesComponents:
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
        
        # --- Run Routine "cues" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question_mark_training* updates
            if question_mark_training.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                question_mark_training.frameNStart = frameN  # exact frame index
                question_mark_training.tStart = t  # local t and not account for scr refresh
                question_mark_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_mark_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'question_mark_training.started')
                question_mark_training.setAutoDraw(True)
            
            # *key_resp_training* updates
            waitOnFlip = False
            if key_resp_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_training.frameNStart = frameN  # exact frame index
                key_resp_training.tStart = t  # local t and not account for scr refresh
                key_resp_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_training.started')
                key_resp_training.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_training.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_training.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_training.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_training.getKeys(keyList=['left','right'], waitRelease=False)
                _key_resp_training_allKeys.extend(theseKeys)
                if len(_key_resp_training_allKeys):
                    key_resp_training.keys = _key_resp_training_allKeys[-1].name  # just the last key pressed
                    key_resp_training.rt = _key_resp_training_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_training.keys == str("'left'")) or (key_resp_training.keys == "'left'"):
                        key_resp_training.corr = 1
                    else:
                        key_resp_training.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *avec_training* updates
            if avec_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                avec_training.frameNStart = frameN  # exact frame index
                avec_training.tStart = t  # local t and not account for scr refresh
                avec_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(avec_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'avec_training.started')
                avec_training.setAutoDraw(True)
            
            # *sans_training* updates
            if sans_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sans_training.frameNStart = frameN  # exact frame index
                sans_training.tStart = t  # local t and not account for scr refresh
                sans_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sans_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sans_training.started')
                sans_training.setAutoDraw(True)
            
            # *nombre_match_training* updates
            if nombre_match_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                nombre_match_training.frameNStart = frameN  # exact frame index
                nombre_match_training.tStart = t  # local t and not account for scr refresh
                nombre_match_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nombre_match_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nombre_match_training.started')
                nombre_match_training.setAutoDraw(True)
            
            # *text_question* updates
            if text_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_question.frameNStart = frameN  # exact frame index
                text_question.tStart = t  # local t and not account for scr refresh
                text_question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_question, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_question.started')
                text_question.setAutoDraw(True)
            
            # *cross_training* updates
            if cross_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_training.frameNStart = frameN  # exact frame index
                cross_training.tStart = t  # local t and not account for scr refresh
                cross_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_training.started')
                cross_training.setAutoDraw(True)
            
            # *avec_cues* updates
            if avec_cues.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                avec_cues.frameNStart = frameN  # exact frame index
                avec_cues.tStart = t  # local t and not account for scr refresh
                avec_cues.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(avec_cues, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'avec_cues.started')
                avec_cues.setAutoDraw(True)
            
            # *sans_cues* updates
            if sans_cues.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sans_cues.frameNStart = frameN  # exact frame index
                sans_cues.tStart = t  # local t and not account for scr refresh
                sans_cues.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sans_cues, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sans_cues.started')
                sans_cues.setAutoDraw(True)
            
            # *joueur* updates
            if joueur.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                joueur.frameNStart = frameN  # exact frame index
                joueur.tStart = t  # local t and not account for scr refresh
                joueur.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(joueur, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'joueur.started')
                joueur.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cuesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "cues" ---
        for thisComponent in cuesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_training.keys in ['', [], None]:  # No response was made
            key_resp_training.keys = None
            # was no response the correct answer?!
            if str("'left'").lower() == 'none':
               key_resp_training.corr = 1;  # correct non-response
            else:
               key_resp_training.corr = 0;  # failed to respond (incorrectly)
        # store data for trainingBlocks (TrialHandler)
        trainingBlocks.addData('key_resp_training.keys',key_resp_training.keys)
        trainingBlocks.addData('key_resp_training.corr', key_resp_training.corr)
        if key_resp_training.keys != None:  # we had a response
            trainingBlocks.addData('key_resp_training.rt', key_resp_training.rt)
        # the Routine "cues" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from fb_code_4
        # Check if the key press was correct or not.
        # This routine will need to follow another routine with a 
        # key response component in it called "key_resp" 
        # and the "store correct" option enabled. 
        # If your experiment is missing that you will 
        # not receive feedback and an error message will be displayed.
        
        #bern_param_play = 0.5
        #bern_param_not_play = 0.5
        
        if key_resp_training.keys == avec_key:
            # c'est à dire si avec est actionné en l'occurence play
            # on a Bern(p)
            text_avec_fb_color = "white"
            text_sans_fb_color = "black"
            outcome = np.random.binomial(1, bern_param_play, size=1)
            if outcome == 1 :
                fb_text_training = 'images/Win.png'
                fb_text_training_show = "C'est une victoire!"
            else: 
                fb_text_training = 'images/Lose.png'
                fb_text_training_show = "C'est une défaite!"
                
        if key_resp_training.keys == sans_key:
            # ie si sans est actionné
            text_avec_fb_color = "black"
            text_sans_fb_color = "white"
            outcome = np.random.binomial(1, bern_param_not_play, size=1)
            if outcome == 1:
                fb_text_training = 'images/Win.png'
                fb_text_training_show = "C'est une victoire!"
            else:
                fb_text_training = 'images/Lose.png'
                fb_text_training_show = "C'est une défaite!"
        
        try: 
            joueur_number = Condition
        except: 
            joueur_number = "25"
        
        
        print('key_resp_training.keys', key_resp_training.keys)
        print('avec color', text_avec_fb_color)
        print('sans color', text_sans_fb_color)
        print('key avec', avec_key)
        text_question_outcome.setText("Question: Voulez vous faire jouer l'équipe avec ou sans le joueur {} ?".format(chr(joueur_number+64)))
        nombre_match_training_outcome.setText("match n° {}".format(nombre_matchs))
        text_avec_fb.setPos([tuple(float(x) for x in avec_pos_text.strip("()").split(","))])
        text_sans_fb.setPos([tuple(float(x) for x in sans_pos_text.strip("()").split(","))])
        text_sans_fb.setText("sans")
        avec_feedback.setColor(text_sans_fb_color, colorSpace='rgb')
        avec_feedback.setPos([tuple(float(x) for x in avec_pos_image.strip("()").split(","))])
        sans_feedback.setColor(text_avec_fb_color, colorSpace='rgb')
        sans_feedback.setPos([tuple(float(x) for x in sans_pos_image.strip("()").split(","))])
        text_resultat.setText(fb_text_training_show)
        joueur_feedback.setText("joueur {}".format(chr(joueur_number+64)))
        # keep track of which components have finished
        feedbackComponents = [text_question_outcome, nombre_match_training_outcome, text_avec_fb, text_sans_fb, avec_feedback, sans_feedback, outcome_feedback, text_resultat, cross_outcome_training, joueur_feedback]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_question_outcome* updates
            if text_question_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_question_outcome.frameNStart = frameN  # exact frame index
                text_question_outcome.tStart = t  # local t and not account for scr refresh
                text_question_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_question_outcome, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_question_outcome.started')
                text_question_outcome.setAutoDraw(True)
            if text_question_outcome.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_question_outcome.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_question_outcome.tStop = t  # not accounting for scr refresh
                    text_question_outcome.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_question_outcome.stopped')
                    text_question_outcome.setAutoDraw(False)
            
            # *nombre_match_training_outcome* updates
            if nombre_match_training_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                nombre_match_training_outcome.frameNStart = frameN  # exact frame index
                nombre_match_training_outcome.tStart = t  # local t and not account for scr refresh
                nombre_match_training_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nombre_match_training_outcome, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nombre_match_training_outcome.started')
                nombre_match_training_outcome.setAutoDraw(True)
            if nombre_match_training_outcome.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > nombre_match_training_outcome.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    nombre_match_training_outcome.tStop = t  # not accounting for scr refresh
                    nombre_match_training_outcome.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'nombre_match_training_outcome.stopped')
                    nombre_match_training_outcome.setAutoDraw(False)
            
            # *text_avec_fb* updates
            if text_avec_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_avec_fb.frameNStart = frameN  # exact frame index
                text_avec_fb.tStart = t  # local t and not account for scr refresh
                text_avec_fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_avec_fb, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_avec_fb.started')
                text_avec_fb.setAutoDraw(True)
            if text_avec_fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_avec_fb.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_avec_fb.tStop = t  # not accounting for scr refresh
                    text_avec_fb.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_avec_fb.stopped')
                    text_avec_fb.setAutoDraw(False)
            if text_avec_fb.status == STARTED:  # only update if drawing
                text_avec_fb.setColor(text_avec_fb_color, colorSpace='rgb', log=False)
            
            # *text_sans_fb* updates
            if text_sans_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_sans_fb.frameNStart = frameN  # exact frame index
                text_sans_fb.tStart = t  # local t and not account for scr refresh
                text_sans_fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_sans_fb, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_sans_fb.started')
                text_sans_fb.setAutoDraw(True)
            if text_sans_fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_sans_fb.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_sans_fb.tStop = t  # not accounting for scr refresh
                    text_sans_fb.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_sans_fb.stopped')
                    text_sans_fb.setAutoDraw(False)
            if text_sans_fb.status == STARTED:  # only update if drawing
                text_sans_fb.setColor(text_sans_fb_color, colorSpace='rgb', log=False)
            
            # *avec_feedback* updates
            if avec_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                avec_feedback.frameNStart = frameN  # exact frame index
                avec_feedback.tStart = t  # local t and not account for scr refresh
                avec_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(avec_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'avec_feedback.started')
                avec_feedback.setAutoDraw(True)
            if avec_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > avec_feedback.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    avec_feedback.tStop = t  # not accounting for scr refresh
                    avec_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'avec_feedback.stopped')
                    avec_feedback.setAutoDraw(False)
            
            # *sans_feedback* updates
            if sans_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sans_feedback.frameNStart = frameN  # exact frame index
                sans_feedback.tStart = t  # local t and not account for scr refresh
                sans_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sans_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sans_feedback.started')
                sans_feedback.setAutoDraw(True)
            if sans_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sans_feedback.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sans_feedback.tStop = t  # not accounting for scr refresh
                    sans_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sans_feedback.stopped')
                    sans_feedback.setAutoDraw(False)
            
            # *outcome_feedback* updates
            if outcome_feedback.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                outcome_feedback.frameNStart = frameN  # exact frame index
                outcome_feedback.tStart = t  # local t and not account for scr refresh
                outcome_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(outcome_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'outcome_feedback.started')
                outcome_feedback.setAutoDraw(True)
            if outcome_feedback.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 2-frameTolerance:
                    # keep track of stop time/frame for later
                    outcome_feedback.tStop = t  # not accounting for scr refresh
                    outcome_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'outcome_feedback.stopped')
                    outcome_feedback.setAutoDraw(False)
            if outcome_feedback.status == STARTED:  # only update if drawing
                outcome_feedback.setImage(fb_text_training, log=False)
            
            # *text_resultat* updates
            if text_resultat.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_resultat.frameNStart = frameN  # exact frame index
                text_resultat.tStart = t  # local t and not account for scr refresh
                text_resultat.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_resultat, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_resultat.started')
                text_resultat.setAutoDraw(True)
            if text_resultat.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_resultat.tStop = t  # not accounting for scr refresh
                    text_resultat.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_resultat.stopped')
                    text_resultat.setAutoDraw(False)
            
            # *cross_outcome_training* updates
            if cross_outcome_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_outcome_training.frameNStart = frameN  # exact frame index
                cross_outcome_training.tStart = t  # local t and not account for scr refresh
                cross_outcome_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_outcome_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_outcome_training.started')
                cross_outcome_training.setAutoDraw(True)
            if cross_outcome_training.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_outcome_training.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_outcome_training.tStop = t  # not accounting for scr refresh
                    cross_outcome_training.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross_outcome_training.stopped')
                    cross_outcome_training.setAutoDraw(False)
            
            # *joueur_feedback* updates
            if joueur_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                joueur_feedback.frameNStart = frameN  # exact frame index
                joueur_feedback.tStart = t  # local t and not account for scr refresh
                joueur_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(joueur_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'joueur_feedback.started')
                joueur_feedback.setAutoDraw(True)
            if joueur_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > joueur_feedback.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    joueur_feedback.tStop = t  # not accounting for scr refresh
                    joueur_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'joueur_feedback.stopped')
                    joueur_feedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from fb_code_4
        nombre_matchs += 1
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
    # completed 5.0 repeats of 'trainingBlocks'
    
    
    # --- Prepare to start Routine "question" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_6
    try: 
        joueur_number = Condition
    except: 
        joueur_number = "25"
    attractiveness.reset()
    text_question_1.setText("Évaluation de l'impact du joueur {}".format(chr(joueur_number+64)) + "\n" "\n Attribuez une note à l'impact du joueur {} sur le match en utilisant une échelle de -10 (le joueur contribue à la défaite de l'équipe), 0 (aucun impact sur le match) à 10 (le joueur contribue à la victoire de l'équipe).".format(chr(joueur_number+64)) + "\n Cliquez sur valider pour confirmer.")
    # setup some python lists for storing info about the mouse_15
    mouse_15.x = []
    mouse_15.y = []
    mouse_15.leftButton = []
    mouse_15.midButton = []
    mouse_15.rightButton = []
    mouse_15.time = []
    mouse_15.clicked_name = []
    gotValidClick = False  # until a click is received
    slider_recommandation.reset()
    # keep track of which components have finished
    questionComponents = [attractiveness, text_question_1, validate, mouse_15, slider_recommandation, text_recommandation]
    for thisComponent in questionComponents:
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
    
    # --- Run Routine "question" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *attractiveness* updates
        if attractiveness.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            attractiveness.frameNStart = frameN  # exact frame index
            attractiveness.tStart = t  # local t and not account for scr refresh
            attractiveness.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attractiveness, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'attractiveness.started')
            attractiveness.setAutoDraw(True)
        
        # *text_question_1* updates
        if text_question_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_question_1.frameNStart = frameN  # exact frame index
            text_question_1.tStart = t  # local t and not account for scr refresh
            text_question_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_question_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_question_1.started')
            text_question_1.setAutoDraw(True)
        
        # *validate* updates
        if validate.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            validate.frameNStart = frameN  # exact frame index
            validate.tStart = t  # local t and not account for scr refresh
            validate.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(validate, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'validate.started')
            validate.setAutoDraw(True)
        # *mouse_15* updates
        if mouse_15.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_15.frameNStart = frameN  # exact frame index
            mouse_15.tStart = t  # local t and not account for scr refresh
            mouse_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_15.started', t)
            mouse_15.status = STARTED
            mouse_15.mouseClock.reset()
            prevButtonState = mouse_15.getPressed()  # if button is down already this ISN'T a new click
        if mouse_15.status == STARTED:  # only update if started and not finished!
            buttons = mouse_15.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(validate)
                        clickableList = validate
                    except:
                        clickableList = [validate]
                    for obj in clickableList:
                        if obj.contains(mouse_15):
                            gotValidClick = True
                            mouse_15.clicked_name.append(obj.name)
                    x, y = mouse_15.getPos()
                    mouse_15.x.append(x)
                    mouse_15.y.append(y)
                    buttons = mouse_15.getPressed()
                    mouse_15.leftButton.append(buttons[0])
                    mouse_15.midButton.append(buttons[1])
                    mouse_15.rightButton.append(buttons[2])
                    mouse_15.time.append(mouse_15.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *slider_recommandation* updates
        if slider_recommandation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_recommandation.frameNStart = frameN  # exact frame index
            slider_recommandation.tStart = t  # local t and not account for scr refresh
            slider_recommandation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_recommandation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_recommandation.started')
            slider_recommandation.setAutoDraw(True)
        
        # *text_recommandation* updates
        if text_recommandation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_recommandation.frameNStart = frameN  # exact frame index
            text_recommandation.tStart = t  # local t and not account for scr refresh
            text_recommandation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_recommandation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_recommandation.started')
            text_recommandation.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "question" ---
    for thisComponent in questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trainingRun.addData('attractiveness.response', attractiveness.getRating())
    trainingRun.addData('attractiveness.rt', attractiveness.getRT())
    # store data for trainingRun (TrialHandler)
    trainingRun.addData('mouse_15.x', mouse_15.x)
    trainingRun.addData('mouse_15.y', mouse_15.y)
    trainingRun.addData('mouse_15.leftButton', mouse_15.leftButton)
    trainingRun.addData('mouse_15.midButton', mouse_15.midButton)
    trainingRun.addData('mouse_15.rightButton', mouse_15.rightButton)
    trainingRun.addData('mouse_15.time', mouse_15.time)
    trainingRun.addData('mouse_15.clicked_name', mouse_15.clicked_name)
    trainingRun.addData('slider_recommandation.response', slider_recommandation.getRating())
    trainingRun.addData('slider_recommandation.rt', slider_recommandation.getRT())
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ending" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # keep track of which components have finished
    endingComponents = [text, key_resp_9]
    for thisComponent in endingComponents:
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
    
    # --- Run Routine "ending" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_9.started')
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
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
        for thisComponent in endingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ending" ---
    for thisComponent in endingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    trainingRun.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        trainingRun.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "ending" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'trainingRun'


# --- Prepare to start Routine "info_trial_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
info_trial_1Components = [text_2]
for thisComponent in info_trial_1Components:
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

# --- Run Routine "info_trial_1" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.stopped')
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in info_trial_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "info_trial_1" ---
for thisComponent in info_trial_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "instruction_trial_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
instruction_trial_1Components = [text_instr_13, key_resp_8, image_avec, image_sans, image_victoire, image_defaite, text_avec, text_sans, text_victoire, text_defaite]
for thisComponent in instruction_trial_1Components:
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

# --- Run Routine "instruction_trial_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr_13* updates
    if text_instr_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr_13.frameNStart = frameN  # exact frame index
        text_instr_13.tStart = t  # local t and not account for scr refresh
        text_instr_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instr_13.started')
        text_instr_13.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_8.started')
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_avec* updates
    if image_avec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_avec.frameNStart = frameN  # exact frame index
        image_avec.tStart = t  # local t and not account for scr refresh
        image_avec.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_avec, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_avec.started')
        image_avec.setAutoDraw(True)
    
    # *image_sans* updates
    if image_sans.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_sans.frameNStart = frameN  # exact frame index
        image_sans.tStart = t  # local t and not account for scr refresh
        image_sans.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_sans, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_sans.started')
        image_sans.setAutoDraw(True)
    
    # *image_victoire* updates
    if image_victoire.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_victoire.frameNStart = frameN  # exact frame index
        image_victoire.tStart = t  # local t and not account for scr refresh
        image_victoire.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_victoire, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_victoire.started')
        image_victoire.setAutoDraw(True)
    
    # *image_defaite* updates
    if image_defaite.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_defaite.frameNStart = frameN  # exact frame index
        image_defaite.tStart = t  # local t and not account for scr refresh
        image_defaite.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_defaite, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_defaite.started')
        image_defaite.setAutoDraw(True)
    
    # *text_avec* updates
    if text_avec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_avec.frameNStart = frameN  # exact frame index
        text_avec.tStart = t  # local t and not account for scr refresh
        text_avec.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_avec, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_avec.started')
        text_avec.setAutoDraw(True)
    
    # *text_sans* updates
    if text_sans.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_sans.frameNStart = frameN  # exact frame index
        text_sans.tStart = t  # local t and not account for scr refresh
        text_sans.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_sans, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_sans.started')
        text_sans.setAutoDraw(True)
    
    # *text_victoire* updates
    if text_victoire.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_victoire.frameNStart = frameN  # exact frame index
        text_victoire.tStart = t  # local t and not account for scr refresh
        text_victoire.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_victoire, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_victoire.started')
        text_victoire.setAutoDraw(True)
    
    # *text_defaite* updates
    if text_defaite.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_defaite.frameNStart = frameN  # exact frame index
        text_defaite.tStart = t  # local t and not account for scr refresh
        text_defaite.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_defaite, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_defaite.started')
        text_defaite.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_trial_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_trial_1" ---
for thisComponent in instruction_trial_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "instruction_trial_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
firstRun = data.TrialHandler(nReps=1.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/loopConditionsExp1.csv', selection='0'),
    seed=None, name='firstRun')
thisExp.addLoop(firstRun)  # add the loop to the experiment
thisFirstRun = firstRun.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFirstRun.rgb)
if thisFirstRun != None:
    for paramName in thisFirstRun:
        exec('{} = thisFirstRun[paramName]'.format(paramName))

for thisFirstRun in firstRun:
    currentLoop = firstRun
    # abbreviate parameter names if possible (e.g. rgb = thisFirstRun.rgb)
    if thisFirstRun != None:
        for paramName in thisFirstRun:
            exec('{} = thisFirstRun[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "joueur_number_instr" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_5
    try: 
        joueur_number = Condition
    except: 
        joueur_number = "25"
    text_4.setText("Joueur {}".format(chr(joueur_number+64)))
    # keep track of which components have finished
    joueur_number_instrComponents = [text_4]
    for thisComponent in joueur_number_instrComponents:
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
    
    # --- Run Routine "joueur_number_instr" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.stopped')
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in joueur_number_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "joueur_number_instr" ---
    for thisComponent in joueur_number_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    firstBlocks = data.TrialHandler(nReps=3.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions/CounterBalancedKeys.csv', selection=[np.random.randint(1, 4)]),
        seed=None, name='firstBlocks')
    thisExp.addLoop(firstBlocks)  # add the loop to the experiment
    thisFirstBlock = firstBlocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFirstBlock.rgb)
    if thisFirstBlock != None:
        for paramName in thisFirstBlock:
            exec('{} = thisFirstBlock[paramName]'.format(paramName))
    
    for thisFirstBlock in firstBlocks:
        currentLoop = firstBlocks
        # abbreviate parameter names if possible (e.g. rgb = thisFirstBlock.rgb)
        if thisFirstBlock != None:
            for paramName in thisFirstBlock:
                exec('{} = thisFirstBlock[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [cross]
        for thisComponent in fixationComponents:
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
        
        # --- Run Routine "fixation" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.started')
                cross.setAutoDraw(True)
            if cross.status == STARTED:
                if frameN >= 40:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross.stopped')
                    cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "cues" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        try: 
            joueur_number = Condition
        except: 
            joueur_number = "25"
        key_resp_training.keys = []
        key_resp_training.rt = []
        _key_resp_training_allKeys = []
        avec_training.setPos([tuple(float(x) for x in avec_pos_text.strip("()").split(","))])
        sans_training.setPos([tuple(float(x) for x in sans_pos_text.strip("()").split(","))])
        nombre_match_training.setText("match n° {}".format(nombre_matchs))
        text_question.setText("Question: Voulez vous faire jouer l'équipe avec ou sans le joueur {} ?".format(chr(joueur_number+64)))
        avec_cues.setPos([tuple(float(x) for x in avec_pos_image.strip("()").split(","))])
        sans_cues.setPos([tuple(float(x) for x in sans_pos_image.strip("()").split(","))])
        joueur.setText("joueur {}".format(chr(joueur_number+64)))
        # keep track of which components have finished
        cuesComponents = [question_mark_training, key_resp_training, avec_training, sans_training, nombre_match_training, text_question, cross_training, avec_cues, sans_cues, joueur]
        for thisComponent in cuesComponents:
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
        
        # --- Run Routine "cues" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question_mark_training* updates
            if question_mark_training.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                question_mark_training.frameNStart = frameN  # exact frame index
                question_mark_training.tStart = t  # local t and not account for scr refresh
                question_mark_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question_mark_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'question_mark_training.started')
                question_mark_training.setAutoDraw(True)
            
            # *key_resp_training* updates
            waitOnFlip = False
            if key_resp_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_training.frameNStart = frameN  # exact frame index
                key_resp_training.tStart = t  # local t and not account for scr refresh
                key_resp_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_training.started')
                key_resp_training.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_training.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_training.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_training.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_training.getKeys(keyList=['left','right'], waitRelease=False)
                _key_resp_training_allKeys.extend(theseKeys)
                if len(_key_resp_training_allKeys):
                    key_resp_training.keys = _key_resp_training_allKeys[-1].name  # just the last key pressed
                    key_resp_training.rt = _key_resp_training_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_training.keys == str("'left'")) or (key_resp_training.keys == "'left'"):
                        key_resp_training.corr = 1
                    else:
                        key_resp_training.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *avec_training* updates
            if avec_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                avec_training.frameNStart = frameN  # exact frame index
                avec_training.tStart = t  # local t and not account for scr refresh
                avec_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(avec_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'avec_training.started')
                avec_training.setAutoDraw(True)
            
            # *sans_training* updates
            if sans_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sans_training.frameNStart = frameN  # exact frame index
                sans_training.tStart = t  # local t and not account for scr refresh
                sans_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sans_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sans_training.started')
                sans_training.setAutoDraw(True)
            
            # *nombre_match_training* updates
            if nombre_match_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                nombre_match_training.frameNStart = frameN  # exact frame index
                nombre_match_training.tStart = t  # local t and not account for scr refresh
                nombre_match_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nombre_match_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nombre_match_training.started')
                nombre_match_training.setAutoDraw(True)
            
            # *text_question* updates
            if text_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_question.frameNStart = frameN  # exact frame index
                text_question.tStart = t  # local t and not account for scr refresh
                text_question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_question, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_question.started')
                text_question.setAutoDraw(True)
            
            # *cross_training* updates
            if cross_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_training.frameNStart = frameN  # exact frame index
                cross_training.tStart = t  # local t and not account for scr refresh
                cross_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_training.started')
                cross_training.setAutoDraw(True)
            
            # *avec_cues* updates
            if avec_cues.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                avec_cues.frameNStart = frameN  # exact frame index
                avec_cues.tStart = t  # local t and not account for scr refresh
                avec_cues.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(avec_cues, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'avec_cues.started')
                avec_cues.setAutoDraw(True)
            
            # *sans_cues* updates
            if sans_cues.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sans_cues.frameNStart = frameN  # exact frame index
                sans_cues.tStart = t  # local t and not account for scr refresh
                sans_cues.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sans_cues, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sans_cues.started')
                sans_cues.setAutoDraw(True)
            
            # *joueur* updates
            if joueur.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                joueur.frameNStart = frameN  # exact frame index
                joueur.tStart = t  # local t and not account for scr refresh
                joueur.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(joueur, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'joueur.started')
                joueur.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cuesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "cues" ---
        for thisComponent in cuesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_training.keys in ['', [], None]:  # No response was made
            key_resp_training.keys = None
            # was no response the correct answer?!
            if str("'left'").lower() == 'none':
               key_resp_training.corr = 1;  # correct non-response
            else:
               key_resp_training.corr = 0;  # failed to respond (incorrectly)
        # store data for firstBlocks (TrialHandler)
        firstBlocks.addData('key_resp_training.keys',key_resp_training.keys)
        firstBlocks.addData('key_resp_training.corr', key_resp_training.corr)
        if key_resp_training.keys != None:  # we had a response
            firstBlocks.addData('key_resp_training.rt', key_resp_training.rt)
        # the Routine "cues" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from fb_code_4
        # Check if the key press was correct or not.
        # This routine will need to follow another routine with a 
        # key response component in it called "key_resp" 
        # and the "store correct" option enabled. 
        # If your experiment is missing that you will 
        # not receive feedback and an error message will be displayed.
        
        #bern_param_play = 0.5
        #bern_param_not_play = 0.5
        
        if key_resp_training.keys == avec_key:
            # c'est à dire si avec est actionné en l'occurence play
            # on a Bern(p)
            text_avec_fb_color = "white"
            text_sans_fb_color = "black"
            outcome = np.random.binomial(1, bern_param_play, size=1)
            if outcome == 1 :
                fb_text_training = 'images/Win.png'
                fb_text_training_show = "C'est une victoire!"
            else: 
                fb_text_training = 'images/Lose.png'
                fb_text_training_show = "C'est une défaite!"
                
        if key_resp_training.keys == sans_key:
            # ie si sans est actionné
            text_avec_fb_color = "black"
            text_sans_fb_color = "white"
            outcome = np.random.binomial(1, bern_param_not_play, size=1)
            if outcome == 1:
                fb_text_training = 'images/Win.png'
                fb_text_training_show = "C'est une victoire!"
            else:
                fb_text_training = 'images/Lose.png'
                fb_text_training_show = "C'est une défaite!"
        
        try: 
            joueur_number = Condition
        except: 
            joueur_number = "25"
        
        
        print('key_resp_training.keys', key_resp_training.keys)
        print('avec color', text_avec_fb_color)
        print('sans color', text_sans_fb_color)
        print('key avec', avec_key)
        text_question_outcome.setText("Question: Voulez vous faire jouer l'équipe avec ou sans le joueur {} ?".format(chr(joueur_number+64)))
        nombre_match_training_outcome.setText("match n° {}".format(nombre_matchs))
        text_avec_fb.setPos([tuple(float(x) for x in avec_pos_text.strip("()").split(","))])
        text_sans_fb.setPos([tuple(float(x) for x in sans_pos_text.strip("()").split(","))])
        text_sans_fb.setText("sans")
        avec_feedback.setColor(text_sans_fb_color, colorSpace='rgb')
        avec_feedback.setPos([tuple(float(x) for x in avec_pos_image.strip("()").split(","))])
        sans_feedback.setColor(text_avec_fb_color, colorSpace='rgb')
        sans_feedback.setPos([tuple(float(x) for x in sans_pos_image.strip("()").split(","))])
        text_resultat.setText(fb_text_training_show)
        joueur_feedback.setText("joueur {}".format(chr(joueur_number+64)))
        # keep track of which components have finished
        feedbackComponents = [text_question_outcome, nombre_match_training_outcome, text_avec_fb, text_sans_fb, avec_feedback, sans_feedback, outcome_feedback, text_resultat, cross_outcome_training, joueur_feedback]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_question_outcome* updates
            if text_question_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_question_outcome.frameNStart = frameN  # exact frame index
                text_question_outcome.tStart = t  # local t and not account for scr refresh
                text_question_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_question_outcome, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_question_outcome.started')
                text_question_outcome.setAutoDraw(True)
            if text_question_outcome.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_question_outcome.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_question_outcome.tStop = t  # not accounting for scr refresh
                    text_question_outcome.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_question_outcome.stopped')
                    text_question_outcome.setAutoDraw(False)
            
            # *nombre_match_training_outcome* updates
            if nombre_match_training_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                nombre_match_training_outcome.frameNStart = frameN  # exact frame index
                nombre_match_training_outcome.tStart = t  # local t and not account for scr refresh
                nombre_match_training_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nombre_match_training_outcome, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nombre_match_training_outcome.started')
                nombre_match_training_outcome.setAutoDraw(True)
            if nombre_match_training_outcome.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > nombre_match_training_outcome.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    nombre_match_training_outcome.tStop = t  # not accounting for scr refresh
                    nombre_match_training_outcome.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'nombre_match_training_outcome.stopped')
                    nombre_match_training_outcome.setAutoDraw(False)
            
            # *text_avec_fb* updates
            if text_avec_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_avec_fb.frameNStart = frameN  # exact frame index
                text_avec_fb.tStart = t  # local t and not account for scr refresh
                text_avec_fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_avec_fb, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_avec_fb.started')
                text_avec_fb.setAutoDraw(True)
            if text_avec_fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_avec_fb.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_avec_fb.tStop = t  # not accounting for scr refresh
                    text_avec_fb.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_avec_fb.stopped')
                    text_avec_fb.setAutoDraw(False)
            if text_avec_fb.status == STARTED:  # only update if drawing
                text_avec_fb.setColor(text_avec_fb_color, colorSpace='rgb', log=False)
            
            # *text_sans_fb* updates
            if text_sans_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_sans_fb.frameNStart = frameN  # exact frame index
                text_sans_fb.tStart = t  # local t and not account for scr refresh
                text_sans_fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_sans_fb, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_sans_fb.started')
                text_sans_fb.setAutoDraw(True)
            if text_sans_fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_sans_fb.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_sans_fb.tStop = t  # not accounting for scr refresh
                    text_sans_fb.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_sans_fb.stopped')
                    text_sans_fb.setAutoDraw(False)
            if text_sans_fb.status == STARTED:  # only update if drawing
                text_sans_fb.setColor(text_sans_fb_color, colorSpace='rgb', log=False)
            
            # *avec_feedback* updates
            if avec_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                avec_feedback.frameNStart = frameN  # exact frame index
                avec_feedback.tStart = t  # local t and not account for scr refresh
                avec_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(avec_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'avec_feedback.started')
                avec_feedback.setAutoDraw(True)
            if avec_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > avec_feedback.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    avec_feedback.tStop = t  # not accounting for scr refresh
                    avec_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'avec_feedback.stopped')
                    avec_feedback.setAutoDraw(False)
            
            # *sans_feedback* updates
            if sans_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sans_feedback.frameNStart = frameN  # exact frame index
                sans_feedback.tStart = t  # local t and not account for scr refresh
                sans_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sans_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sans_feedback.started')
                sans_feedback.setAutoDraw(True)
            if sans_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sans_feedback.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    sans_feedback.tStop = t  # not accounting for scr refresh
                    sans_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sans_feedback.stopped')
                    sans_feedback.setAutoDraw(False)
            
            # *outcome_feedback* updates
            if outcome_feedback.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                outcome_feedback.frameNStart = frameN  # exact frame index
                outcome_feedback.tStart = t  # local t and not account for scr refresh
                outcome_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(outcome_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'outcome_feedback.started')
                outcome_feedback.setAutoDraw(True)
            if outcome_feedback.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 2-frameTolerance:
                    # keep track of stop time/frame for later
                    outcome_feedback.tStop = t  # not accounting for scr refresh
                    outcome_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'outcome_feedback.stopped')
                    outcome_feedback.setAutoDraw(False)
            if outcome_feedback.status == STARTED:  # only update if drawing
                outcome_feedback.setImage(fb_text_training, log=False)
            
            # *text_resultat* updates
            if text_resultat.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_resultat.frameNStart = frameN  # exact frame index
                text_resultat.tStart = t  # local t and not account for scr refresh
                text_resultat.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_resultat, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_resultat.started')
                text_resultat.setAutoDraw(True)
            if text_resultat.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_resultat.tStop = t  # not accounting for scr refresh
                    text_resultat.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_resultat.stopped')
                    text_resultat.setAutoDraw(False)
            
            # *cross_outcome_training* updates
            if cross_outcome_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_outcome_training.frameNStart = frameN  # exact frame index
                cross_outcome_training.tStart = t  # local t and not account for scr refresh
                cross_outcome_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_outcome_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_outcome_training.started')
                cross_outcome_training.setAutoDraw(True)
            if cross_outcome_training.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_outcome_training.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_outcome_training.tStop = t  # not accounting for scr refresh
                    cross_outcome_training.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross_outcome_training.stopped')
                    cross_outcome_training.setAutoDraw(False)
            
            # *joueur_feedback* updates
            if joueur_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                joueur_feedback.frameNStart = frameN  # exact frame index
                joueur_feedback.tStart = t  # local t and not account for scr refresh
                joueur_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(joueur_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'joueur_feedback.started')
                joueur_feedback.setAutoDraw(True)
            if joueur_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > joueur_feedback.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    joueur_feedback.tStop = t  # not accounting for scr refresh
                    joueur_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'joueur_feedback.stopped')
                    joueur_feedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from fb_code_4
        nombre_matchs += 1
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'firstBlocks'
    
    
    # --- Prepare to start Routine "question" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_6
    try: 
        joueur_number = Condition
    except: 
        joueur_number = "25"
    attractiveness.reset()
    text_question_1.setText("Évaluation de l'impact du joueur {}".format(chr(joueur_number+64)) + "\n" "\n Attribuez une note à l'impact du joueur {} sur le match en utilisant une échelle de -10 (le joueur contribue à la défaite de l'équipe), 0 (aucun impact sur le match) à 10 (le joueur contribue à la victoire de l'équipe).".format(chr(joueur_number+64)) + "\n Cliquez sur valider pour confirmer.")
    # setup some python lists for storing info about the mouse_15
    mouse_15.x = []
    mouse_15.y = []
    mouse_15.leftButton = []
    mouse_15.midButton = []
    mouse_15.rightButton = []
    mouse_15.time = []
    mouse_15.clicked_name = []
    gotValidClick = False  # until a click is received
    slider_recommandation.reset()
    # keep track of which components have finished
    questionComponents = [attractiveness, text_question_1, validate, mouse_15, slider_recommandation, text_recommandation]
    for thisComponent in questionComponents:
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
    
    # --- Run Routine "question" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *attractiveness* updates
        if attractiveness.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            attractiveness.frameNStart = frameN  # exact frame index
            attractiveness.tStart = t  # local t and not account for scr refresh
            attractiveness.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attractiveness, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'attractiveness.started')
            attractiveness.setAutoDraw(True)
        
        # *text_question_1* updates
        if text_question_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_question_1.frameNStart = frameN  # exact frame index
            text_question_1.tStart = t  # local t and not account for scr refresh
            text_question_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_question_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_question_1.started')
            text_question_1.setAutoDraw(True)
        
        # *validate* updates
        if validate.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            validate.frameNStart = frameN  # exact frame index
            validate.tStart = t  # local t and not account for scr refresh
            validate.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(validate, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'validate.started')
            validate.setAutoDraw(True)
        # *mouse_15* updates
        if mouse_15.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_15.frameNStart = frameN  # exact frame index
            mouse_15.tStart = t  # local t and not account for scr refresh
            mouse_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_15.started', t)
            mouse_15.status = STARTED
            mouse_15.mouseClock.reset()
            prevButtonState = mouse_15.getPressed()  # if button is down already this ISN'T a new click
        if mouse_15.status == STARTED:  # only update if started and not finished!
            buttons = mouse_15.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(validate)
                        clickableList = validate
                    except:
                        clickableList = [validate]
                    for obj in clickableList:
                        if obj.contains(mouse_15):
                            gotValidClick = True
                            mouse_15.clicked_name.append(obj.name)
                    x, y = mouse_15.getPos()
                    mouse_15.x.append(x)
                    mouse_15.y.append(y)
                    buttons = mouse_15.getPressed()
                    mouse_15.leftButton.append(buttons[0])
                    mouse_15.midButton.append(buttons[1])
                    mouse_15.rightButton.append(buttons[2])
                    mouse_15.time.append(mouse_15.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *slider_recommandation* updates
        if slider_recommandation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_recommandation.frameNStart = frameN  # exact frame index
            slider_recommandation.tStart = t  # local t and not account for scr refresh
            slider_recommandation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_recommandation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_recommandation.started')
            slider_recommandation.setAutoDraw(True)
        
        # *text_recommandation* updates
        if text_recommandation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_recommandation.frameNStart = frameN  # exact frame index
            text_recommandation.tStart = t  # local t and not account for scr refresh
            text_recommandation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_recommandation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_recommandation.started')
            text_recommandation.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "question" ---
    for thisComponent in questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    firstRun.addData('attractiveness.response', attractiveness.getRating())
    firstRun.addData('attractiveness.rt', attractiveness.getRT())
    # store data for firstRun (TrialHandler)
    firstRun.addData('mouse_15.x', mouse_15.x)
    firstRun.addData('mouse_15.y', mouse_15.y)
    firstRun.addData('mouse_15.leftButton', mouse_15.leftButton)
    firstRun.addData('mouse_15.midButton', mouse_15.midButton)
    firstRun.addData('mouse_15.rightButton', mouse_15.rightButton)
    firstRun.addData('mouse_15.time', mouse_15.time)
    firstRun.addData('mouse_15.clicked_name', mouse_15.clicked_name)
    firstRun.addData('slider_recommandation.response', slider_recommandation.getRating())
    firstRun.addData('slider_recommandation.rt', slider_recommandation.getRT())
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'firstRun'


# --- Prepare to start Routine "ending" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
endingComponents = [text, key_resp_9]
for thisComponent in endingComponents:
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

# --- Run Routine "ending" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_9.started')
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
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
    for thisComponent in endingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ending" ---
for thisComponent in endingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "ending" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_exps23 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/loopCounterBalanced'+expInfo['group']+'.csv'),
    seed=None, name='loop_exps23')
thisExp.addLoop(loop_exps23)  # add the loop to the experiment
thisLoop_exps23 = loop_exps23.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_exps23.rgb)
if thisLoop_exps23 != None:
    for paramName in thisLoop_exps23:
        exec('{} = thisLoop_exps23[paramName]'.format(paramName))

for thisLoop_exps23 in loop_exps23:
    currentLoop = loop_exps23
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_exps23.rgb)
    if thisLoop_exps23 != None:
        for paramName in thisLoop_exps23:
            exec('{} = thisLoop_exps23[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instruction_trial_23" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_instr_11.setText(text_instruction)
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # keep track of which components have finished
    instruction_trial_23Components = [text_instr_11, key_resp_11, avec_inst_23, sans_instr_23, domicile_instr_23, exterieur_instr_23, avec_instr_23, sans_inst_23, domicile_inst_23, exterieur_inst_23]
    for thisComponent in instruction_trial_23Components:
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
    
    # --- Run Routine "instruction_trial_23" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_instr_11* updates
        if text_instr_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_instr_11.frameNStart = frameN  # exact frame index
            text_instr_11.tStart = t  # local t and not account for scr refresh
            text_instr_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_instr_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_instr_11.started')
            text_instr_11.setAutoDraw(True)
        
        # *key_resp_11* updates
        waitOnFlip = False
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_11.started')
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *avec_inst_23* updates
        if avec_inst_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            avec_inst_23.frameNStart = frameN  # exact frame index
            avec_inst_23.tStart = t  # local t and not account for scr refresh
            avec_inst_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(avec_inst_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'avec_inst_23.started')
            avec_inst_23.setAutoDraw(True)
        
        # *sans_instr_23* updates
        if sans_instr_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sans_instr_23.frameNStart = frameN  # exact frame index
            sans_instr_23.tStart = t  # local t and not account for scr refresh
            sans_instr_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sans_instr_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sans_instr_23.started')
            sans_instr_23.setAutoDraw(True)
        
        # *domicile_instr_23* updates
        if domicile_instr_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            domicile_instr_23.frameNStart = frameN  # exact frame index
            domicile_instr_23.tStart = t  # local t and not account for scr refresh
            domicile_instr_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(domicile_instr_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'domicile_instr_23.started')
            domicile_instr_23.setAutoDraw(True)
        
        # *exterieur_instr_23* updates
        if exterieur_instr_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exterieur_instr_23.frameNStart = frameN  # exact frame index
            exterieur_instr_23.tStart = t  # local t and not account for scr refresh
            exterieur_instr_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exterieur_instr_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exterieur_instr_23.started')
            exterieur_instr_23.setAutoDraw(True)
        
        # *avec_instr_23* updates
        if avec_instr_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            avec_instr_23.frameNStart = frameN  # exact frame index
            avec_instr_23.tStart = t  # local t and not account for scr refresh
            avec_instr_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(avec_instr_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'avec_instr_23.started')
            avec_instr_23.setAutoDraw(True)
        
        # *sans_inst_23* updates
        if sans_inst_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sans_inst_23.frameNStart = frameN  # exact frame index
            sans_inst_23.tStart = t  # local t and not account for scr refresh
            sans_inst_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sans_inst_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sans_inst_23.started')
            sans_inst_23.setAutoDraw(True)
        
        # *domicile_inst_23* updates
        if domicile_inst_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            domicile_inst_23.frameNStart = frameN  # exact frame index
            domicile_inst_23.tStart = t  # local t and not account for scr refresh
            domicile_inst_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(domicile_inst_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'domicile_inst_23.started')
            domicile_inst_23.setAutoDraw(True)
        
        # *exterieur_inst_23* updates
        if exterieur_inst_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exterieur_inst_23.frameNStart = frameN  # exact frame index
            exterieur_inst_23.tStart = t  # local t and not account for scr refresh
            exterieur_inst_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exterieur_inst_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exterieur_inst_23.started')
            exterieur_inst_23.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_trial_23Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_trial_23" ---
    for thisComponent in instruction_trial_23Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    loop_exps23.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        loop_exps23.addData('key_resp_11.rt', key_resp_11.rt)
    # the Routine "instruction_trial_23" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    innerRun = data.TrialHandler(nReps=1.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions/loopConditionsExp2.csv'),
        seed=None, name='innerRun')
    thisExp.addLoop(innerRun)  # add the loop to the experiment
    thisInnerRun = innerRun.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInnerRun.rgb)
    if thisInnerRun != None:
        for paramName in thisInnerRun:
            exec('{} = thisInnerRun[paramName]'.format(paramName))
    
    for thisInnerRun in innerRun:
        currentLoop = innerRun
        # abbreviate parameter names if possible (e.g. rgb = thisInnerRun.rgb)
        if thisInnerRun != None:
            for paramName in thisInnerRun:
                exec('{} = thisInnerRun[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "joueur_number_instr" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_5
        try: 
            joueur_number = Condition
        except: 
            joueur_number = "25"
        text_4.setText("Joueur {}".format(chr(joueur_number+64)))
        # keep track of which components have finished
        joueur_number_instrComponents = [text_4]
        for thisComponent in joueur_number_instrComponents:
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
        
        # --- Run Routine "joueur_number_instr" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.started')
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_4.stopped')
                    text_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in joueur_number_instrComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "joueur_number_instr" ---
        for thisComponent in joueur_number_instrComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # set up handler to look after randomisation of conditions etc
        innerBlocks = data.TrialHandler(nReps=30.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('conditions/CounterBalancedKeys.csv', selection=[np.random.randint(1, 8)]),
            seed=None, name='innerBlocks')
        thisExp.addLoop(innerBlocks)  # add the loop to the experiment
        thisInnerBlock = innerBlocks.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisInnerBlock.rgb)
        if thisInnerBlock != None:
            for paramName in thisInnerBlock:
                exec('{} = thisInnerBlock[paramName]'.format(paramName))
        
        for thisInnerBlock in innerBlocks:
            currentLoop = innerBlocks
            # abbreviate parameter names if possible (e.g. rgb = thisInnerBlock.rgb)
            if thisInnerBlock != None:
                for paramName in thisInnerBlock:
                    exec('{} = thisInnerBlock[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "fixation" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # keep track of which components have finished
            fixationComponents = [cross]
            for thisComponent in fixationComponents:
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
            
            # --- Run Routine "fixation" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *cross* updates
                if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cross.frameNStart = frameN  # exact frame index
                    cross.tStart = t  # local t and not account for scr refresh
                    cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross.started')
                    cross.setAutoDraw(True)
                if cross.status == STARTED:
                    if frameN >= 40:
                        # keep track of stop time/frame for later
                        cross.tStop = t  # not accounting for scr refresh
                        cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'cross.stopped')
                        cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fixationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation" ---
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "cues_23" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_observation
            observation_trial = np.random.randint(2)
            
            if is_task_obs:
                
                if observation_trial:
                    observation_text = "Phase d'observation \n appuyez sur espace pour voir "+\
                                        "les choix du coach adjoint"
                    acceptable_keys = ['space']
                else:
                    acceptable_keys = ["left", "up", "down", "right"]
                    observation_text = "Phase d'intervention"
            else:
                
                acceptable_keys = ["left", "up", "down", "right"]
                observation_text = ""
            try: 
                joueur_number = Condition
            except: 
                joueur_number = "25"
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            avec3.setPos([tuple(float(x) for x in avec_pos_text.strip("()").split(","))])
            sans3.setPos([tuple(float(x) for x in sans_pos_text.strip("()").split(","))])
            domicile3.setPos([tuple(float(x) for x in dom_pos_text.strip("()").split(","))])
            exterieur3.setPos([tuple(float(x) for x in ext_pos_text.strip("()").split(","))])
            observation.setText(observation_text)
            observation_var = observation_trial  # Set routine start values for observation_var
            thisExp.addData('observation_var.routineStartVal', observation_var)  # Save exp start value
            text_nombre_matchs_third.setText("match n° {}".format(nombre_matchs_third))
            question_trial23.setText("Question: Voulez vous faire jouer l'équipe avec ou sans le joueur, à domicile ou à l'extérieur?".format(chr(joueur_number+64)))
            numero_joueur_cues_23.setText("joueur {}".format(chr(joueur_number+64)))
            avec_cues_23.setPos([tuple(float(x) for x in avec_pos_image.strip("()").split(","))])
            sans_cues_23.setPos([tuple(float(x) for x in sans_pos_image.strip("()").split(","))])
            domicile_cues_23.setPos([tuple(float(x) for x in dom_pos_image.strip("()").split(","))])
            exterieur_cues_23.setPos([tuple(float(x) for x in ext_pos_image.strip("()").split(","))])
            # keep track of which components have finished
            cues_23Components = [key_resp_3, question_mark3, avec3, sans3, domicile3, exterieur3, observation, text_nombre_matchs_third, question_trial23, numero_joueur_cues_23, cross_fixation, avec_cues_23, sans_cues_23, domicile_cues_23, exterieur_cues_23]
            for thisComponent in cues_23Components:
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
            
            # --- Run Routine "cues_23" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_3* updates
                waitOnFlip = False
                if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.tStart = t  # local t and not account for scr refresh
                    key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_3.started')
                    key_resp_3.status = STARTED
                    # AllowedKeys looks like a variable named `acceptable_keys`
                    if not type(acceptable_keys) in [list, tuple, np.ndarray]:
                        if not isinstance(acceptable_keys, str):
                            logging.error('AllowedKeys variable `acceptable_keys` is not string- or list-like.')
                            core.quit()
                        elif not ',' in acceptable_keys:
                            acceptable_keys = (acceptable_keys,)
                        else:
                            acceptable_keys = eval(acceptable_keys)
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_3.getKeys(keyList=list(acceptable_keys), waitRelease=False)
                    _key_resp_3_allKeys.extend(theseKeys)
                    if len(_key_resp_3_allKeys):
                        key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                        key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_3.keys == str('left')) or (key_resp_3.keys == 'left'):
                            key_resp_3.corr = 1
                        else:
                            key_resp_3.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *question_mark3* updates
                if question_mark3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                    # keep track of start time/frame for later
                    question_mark3.frameNStart = frameN  # exact frame index
                    question_mark3.tStart = t  # local t and not account for scr refresh
                    question_mark3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(question_mark3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'question_mark3.started')
                    question_mark3.setAutoDraw(True)
                
                # *avec3* updates
                if avec3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    avec3.frameNStart = frameN  # exact frame index
                    avec3.tStart = t  # local t and not account for scr refresh
                    avec3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(avec3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'avec3.started')
                    avec3.setAutoDraw(True)
                
                # *sans3* updates
                if sans3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sans3.frameNStart = frameN  # exact frame index
                    sans3.tStart = t  # local t and not account for scr refresh
                    sans3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sans3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sans3.started')
                    sans3.setAutoDraw(True)
                
                # *domicile3* updates
                if domicile3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    domicile3.frameNStart = frameN  # exact frame index
                    domicile3.tStart = t  # local t and not account for scr refresh
                    domicile3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(domicile3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'domicile3.started')
                    domicile3.setAutoDraw(True)
                
                # *exterieur3* updates
                if exterieur3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    exterieur3.frameNStart = frameN  # exact frame index
                    exterieur3.tStart = t  # local t and not account for scr refresh
                    exterieur3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(exterieur3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'exterieur3.started')
                    exterieur3.setAutoDraw(True)
                
                # *observation* updates
                if observation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    observation.frameNStart = frameN  # exact frame index
                    observation.tStart = t  # local t and not account for scr refresh
                    observation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(observation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'observation.started')
                    observation.setAutoDraw(True)
                observation_var = observation_trial  # Set frame start values for observation_var
                observation_varContainer.append(observation_var)  # Save frame values
                
                # *text_nombre_matchs_third* updates
                if text_nombre_matchs_third.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_nombre_matchs_third.frameNStart = frameN  # exact frame index
                    text_nombre_matchs_third.tStart = t  # local t and not account for scr refresh
                    text_nombre_matchs_third.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_nombre_matchs_third, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_nombre_matchs_third.started')
                    text_nombre_matchs_third.setAutoDraw(True)
                
                # *question_trial23* updates
                if question_trial23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    question_trial23.frameNStart = frameN  # exact frame index
                    question_trial23.tStart = t  # local t and not account for scr refresh
                    question_trial23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(question_trial23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'question_trial23.started')
                    question_trial23.setAutoDraw(True)
                
                # *numero_joueur_cues_23* updates
                if numero_joueur_cues_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    numero_joueur_cues_23.frameNStart = frameN  # exact frame index
                    numero_joueur_cues_23.tStart = t  # local t and not account for scr refresh
                    numero_joueur_cues_23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(numero_joueur_cues_23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'numero_joueur_cues_23.started')
                    numero_joueur_cues_23.setAutoDraw(True)
                
                # *cross_fixation* updates
                if cross_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cross_fixation.frameNStart = frameN  # exact frame index
                    cross_fixation.tStart = t  # local t and not account for scr refresh
                    cross_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cross_fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross_fixation.started')
                    cross_fixation.setAutoDraw(True)
                
                # *avec_cues_23* updates
                if avec_cues_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    avec_cues_23.frameNStart = frameN  # exact frame index
                    avec_cues_23.tStart = t  # local t and not account for scr refresh
                    avec_cues_23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(avec_cues_23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'avec_cues_23.started')
                    avec_cues_23.setAutoDraw(True)
                
                # *sans_cues_23* updates
                if sans_cues_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sans_cues_23.frameNStart = frameN  # exact frame index
                    sans_cues_23.tStart = t  # local t and not account for scr refresh
                    sans_cues_23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sans_cues_23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sans_cues_23.started')
                    sans_cues_23.setAutoDraw(True)
                
                # *domicile_cues_23* updates
                if domicile_cues_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    domicile_cues_23.frameNStart = frameN  # exact frame index
                    domicile_cues_23.tStart = t  # local t and not account for scr refresh
                    domicile_cues_23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(domicile_cues_23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'domicile_cues_23.started')
                    domicile_cues_23.setAutoDraw(True)
                
                # *exterieur_cues_23* updates
                if exterieur_cues_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    exterieur_cues_23.frameNStart = frameN  # exact frame index
                    exterieur_cues_23.tStart = t  # local t and not account for scr refresh
                    exterieur_cues_23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(exterieur_cues_23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'exterieur_cues_23.started')
                    exterieur_cues_23.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cues_23Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "cues_23" ---
            for thisComponent in cues_23Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_3.keys in ['', [], None]:  # No response was made
                key_resp_3.keys = None
                # was no response the correct answer?!
                if str('left').lower() == 'none':
                   key_resp_3.corr = 1;  # correct non-response
                else:
                   key_resp_3.corr = 0;  # failed to respond (incorrectly)
            # store data for innerBlocks (TrialHandler)
            innerBlocks.addData('key_resp_3.keys',key_resp_3.keys)
            innerBlocks.addData('key_resp_3.corr', key_resp_3.corr)
            if key_resp_3.keys != None:  # we had a response
                innerBlocks.addData('key_resp_3.rt', key_resp_3.rt)
            thisExp.addData('observation_var.routineEndVal', observation_var)  # Save end routine value
            # the Routine "cues_23" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback_23" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fb_code_3
            # Check if the key press was correct or not.
            # This routine will need to follow another routine with a 
            # key response component in it called "key_resp" 
            # and the "store correct" option enabled. 
            # If your experiment is missing that you will 
            # not receive feedback and an error message will be displayed.
            
            bern_params = { "bern_param_avec_exterieur": bern_param_left_down, 
                            "bern_param_avec_domicile": bern_param_left_up, 
                            "bern_param_sans_exterieur": bern_param_right_down, 
                            "bern_param_sans_domicile": bern_param_right_up,
                            "bern_param_z": bern_param_z,
                            "bern_param_exterieur": bern_param_down, 
                            "bern_param_domicile": bern_param_up}
                            
            dict_keys = {"avec" : avec_key, "sans"  : sans_key, "domicile" : dom_key, "exterieur" : ext_key}
            inv_dict = {v : k for k, v in dict_keys.items()}
            
            if is_task_obs :
                    
                if observation_trial: 
                    avec3_outcome_color = "black"
                    sans3_outcome_color = "black"
                    domicile3_outcome_color = "black"
                    exterieur3_outcome_color = "black"
                    
                    print('observation_trial')
                    terrain_choice = np.random.binomial(1, bern_param_z, size=1)
                    terrain = "domicile" if terrain_choice else "exterieur"
                    
                    # change color
                    formatted_var = "{}3_outcome_color = 'white'".format(terrain)
                    exec(formatted_var)
                    
                    joueur_choice = np.random.binomial(1, \
                        bern_params["bern_param_{}".format(terrain)], size=1)
                    joueur = "avec" if joueur_choice else "sans"
                    
                    #change color
                    formatted_var2 = "{}3_outcome_color = 'white'".format(joueur)
                    exec(formatted_var2)
                    
                    outcome3 = np.random.binomial(1, \
                        bern_params["bern_param_{}_{}".format(joueur, terrain)], size=1)
                    
                    #avec3_outcome_color = "black"
                    #sans3_outcome_color = "black"
                    #domicile3_outcome_color = "black"
                    #exterieur3_outcome_color = "black"
                    
                    image_domicile_opacity = 1 if terrain == "domicile" else 0
                    image_exterieur_opacity = 1 if terrain == "exterieur" else 0
                    
                    if outcome3[0] == 1:
                        fb_text3 = 'images/Win.png'
                        resultat3_outcome_text = "C'est une victoire!"
                    else:
                        fb_text3 = 'images/Lose.png'
                        resultat3_outcome_text = "C'est une défaite!"
                    
                    if terrain == "domicile":
                        fb_text_choice3 = "Choix du coach adjoint: \n {} le joueur, \n à {}"\
                            .format(joueur, terrain)
                    if terrain == "exterieur":
                        fb_text_choice3 = "Choix du coach adjoint: \n {} le joueur, \n à l' {}"\
                            .format(joueur, terrain)
                else: 
            
                        
                    print('intervention_trial')
                    if key_resp_3.keys == sans_key:
                        
                        avec3_outcome_color = "black"
                        sans3_outcome_color = "white"
                        domicile3_outcome_color = "black"
                        exterieur3_outcome_color = "black"
                       
                        
                        # right or left (ie play or not play)
                        other_choice = np.random.binomial(1, bern_param_z, size=1)
                        terrain = "domicile" if other_choice[0] else "exterieur"
                      
                        outcome3 = np.random.binomial(1, \
                            bern_params["bern_param_{}_{}".format("sans", terrain)], size=1)
                            
                        # change color for other choice
                        formatted_var_name = "{}3_outcome_color = 'white'".format(terrain)
                        exec(formatted_var_name)
                        
                        image_domicile_opacity = 1 if terrain == "domicile" else 0
                        image_exterieur_opacity = 1 if terrain == "exterieur" else 0
                        
                        # text for the trial
                        fb_text_choice3 = " Choix du coach adjoint : {}".format(terrain)
                        
                        # image outcome assignement
                        if outcome3[0] == 1:
                            fb_text3 = 'images/Win.png'
                            resultat3_outcome_text = "C'est une victoire!"
                        else:
                            fb_text3 = 'images/Lose.png'
                            resultat3_outcome_text = "C'est une défaite!"
            
                    if key_resp_3.keys == avec_key:
                        
                        avec3_outcome_color = "white"
                        sans3_outcome_color = "black"
                        domicile3_outcome_color = "black"
                        exterieur3_outcome_color = "black"
                        
                        image_domicile_opacity = 1
                        image_exterieur_opacity = 1
                        
                        # right or left (ie play or not play)
                        other_choice = np.random.binomial(1, bern_param_z, size=1)
                        terrain = "domicile" if other_choice[0] else "exterieur"
                        
                        outcome3 = np.random.binomial(1, \
                            bern_params["bern_param_{}_{}".format("avec", terrain)], size=1)
                        
                        # change color for other choice
                        print("change color")
                        formatted_var_name = "{}3_outcome_color = 'white'".format(terrain)
                        exec(formatted_var_name)
                        
                        # text for the trial
                        fb_text_choice3 = " Choix du coach adjoint : {}".format(terrain)
                        
                        # image outcome assignement
                        if outcome3[0] == 1:
                            fb_text3 = 'images/Win.png'
                            resultat3_outcome_text = "C'est une victoire!"
                        else:
                            fb_text3 = 'images/Lose.png'
                            resultat3_outcome_text = "C'est une défaite!"
                           
                    if key_resp_3.keys == dom_key:
                              
                        avec3_outcome_color = "black"
                        sans3_outcome_color = "black"
                        domicile3_outcome_color = "white"
                        exterieur3_outcome_color = "black"
                            
                        
                        # up or down (ie domicile ou exterieur)
                        other_choice = np.random.binomial(1, bern_params["bern_param_{}".format("domicile")], size=1)
                        joueur = "avec" if other_choice[0] else "sans"
            
                        outcome3 = np.random.binomial(1, \
                            bern_params["bern_param_{}_{}".format(joueur, "domicile")], size=1)
                            
                        # change color for other choice
                        print("change color")
                        formatted_var_name = "{}3_outcome_color = 'white'".format(joueur)
                        exec(formatted_var_name) 
                        
                        
                        image_domicile_opacity = 1 
                        image_exterieur_opacity = 0
                        
                        # text assignement for the other choice
                        fb_text_choice3 = " Choix du coach adjoint : {}".format(joueur)
                        
                        # image assignement for the outcome
                        if outcome3[0] == 1:
                            fb_text3 = 'images/Win.png'
                            resultat3_outcome_text = "C'est une victoire!"
                        else:
                            fb_text3 = 'images/Lose.png'
                            resultat3_outcome_text = "C'est une défaite!"
                            
                    if key_resp_3.keys == ext_key:
                        
                        avec3_outcome_color = "black"
                        sans3_outcome_color = "black"
                        domicile3_outcome_color = "black"
                        exterieur3_outcome_color = "white"
                        
                        
                        # up or down (ie domicile ou exterieur)
                        other_choice = np.random.binomial(1, \
                            bern_params["bern_param_{}".format("exterieur")], size=1)
                        joueur = "avec" if other_choice[0] else "sans"
                        
                        outcome3 = np.random.binomial(1, \
                            bern_params["bern_param_{}_{}".format(joueur, "exterieur")], size=1)
                            
                        # change color for other choice
                        formatted_var_name = "{}3_outcome_color = 'white'".format(joueur)
                        exec(formatted_var_name) 
                        
                        image_domicile_opacity = 0
                        image_exterieur_opacity = 1
                        
                        # text assignement for the other choice
                        fb_text_choice3 = " Choix du coach adjoint : {}".format(joueur)
                        
                        # image assignement for the outcome
                        if outcome3[0] == 1:
                            fb_text3 = 'images/Win.png'
                            resultat3_outcome_text = "C'est une victoire!"
                        else:
                            fb_text3 = 'images/Lose.png'
                            resultat3_outcome_text = "C'est une défaite!"
                            
            else:
                
                fb_text_choice3 = ""
                
                if key_resp_3.keys == sans_key:
                    
                    avec3_outcome_color = "black"
                    sans3_outcome_color = "white"
                    domicile3_outcome_color = "black"
                    exterieur3_outcome_color = "black"
                    
                    # right or left (ie play or not play)
                    other_choice = np.random.binomial(1, bern_param_z, size=1)
                    terrain = "domicile" if other_choice[0] else "exterieur"
                    
                    outcome3 = np.random.binomial(1, \
                        bern_params["bern_param_{}_{}".format("sans", terrain)], size=1)
                        
                    # change color
                    formatted_var = "{}3_outcome_color = 'white'".format(terrain)
                    exec(formatted_var)
                    
                    image_domicile_opacity = 1 if terrain == "domicile" else 0
                    image_exterieur_opacity = 1 if terrain == "exterieur" else 0
                    
                    # text for the trial
                    fb_text_choice3 = " Choix du coach adjoint : {}".format(terrain)
                    
                    # image outcome assignement
                    if outcome3[0] == 1:
                        fb_text3 = 'images/Win.png'
                        resultat3_outcome_text = "C'est une victoire!"
                    else:
                        fb_text3 = 'images/Lose.png'
                        resultat3_outcome_text = "C'est une défaite!"
            
                if key_resp_3.keys == avec_key:
                    
                    avec3_outcome_color = "white"
                    sans3_outcome_color = "black"
                    domicile3_outcome_color = "black"
                    exterieur3_outcome_color = "black"
                    
                    # right or left (ie play or not play)
                    other_choice = np.random.binomial(1, bern_param_z, size=1)
                    terrain = "domicile" if other_choice[0] else "exterieur"
                    
                    outcome3 = np.random.binomial(1, \
                        bern_params["bern_param_{}_{}".format("avec", terrain)], size=1)
                        
                    # change color
                    formatted_var = "{}3_outcome_color = 'white'".format(terrain)
                    exec(formatted_var)
                    
                    image_domicile_opacity = 1 if terrain_name == "domicile" else 0
                    image_exterieur_opacity = 1 if terrain_name == "exterieur" else 0
                    
                    # text for the trial
                    fb_text_choice3 = " Choix du coach adjoint : {}".format(terrain)
                    
                    # image outcome assignement
                    if outcome3[0] == 1:
                        fb_text3 = 'images/Win.png'
                        resultat3_outcome_text = "C'est une victoire!"
                    else:
                        fb_text3 = 'images/Lose.png'
                        resultat3_outcome_text = "C'est une défaite!"
                       
                if key_resp_3.keys == dom_key:
                          
                    avec3_outcome_color = "black"
                    sans3_outcome_color = "black"
                    domicile3_outcome_color = "white"
                    exterieur3_outcome_color = "black"
                    
                    # up or down (ie domicile ou exterieur)
                    other_choice = np.random.binomial(1, \
                        bern_params["bern_param_{}".format(domicile)], size=1)
                    joueur = "sans" if other_choice[0] else "avec"
                    
                    outcome3 = np.random.binomial(1, \
                        bern_params["bern_param_{}_{}".format(joueur, "domicile")], size=1)
                        
                    # change color
                    formatted_var = "{}3_outcome_color = 'white'".format(joueur)
                    exec(formatted_var)
                    
                    image_domicile_opacity = 1
                    image_exterieur_opacity = 0
                    
                    # text assignement for the other choice
                    fb_text_choice3 = " Choix du coach adjoint : {}".format(joueur)
                    
                    # image assignement for the outcome
                    if outcome3[0] == 1:
                        fb_text3 = 'images/Win.png'
                        resultat3_outcome_text = "C'est une victoire!"
                    else:
                        fb_text3 = 'images/Lose.png'
                        resultat3_outcome_text = "C'est une défaite!"
                        
                if key_resp_3.keys == ext_key:
                    
                    avec3_outcome_color = "black"
                    sans3_outcome_color = "black"
                    domicile3_outcome_color = "black"
                    exterieur3_outcome_color = "white"
                    
                    # up or down (ie domicile ou exterieur)
                    other_choice = np.random.binomial(1, \
                        bern_params["bern_param_{}".format("exterieur")], size=1)
                    joueur = "sans" if other_choice[0] else "avec"
                    
                    outcome3 = np.random.binomial(1, \
                        bern_params["bern_param_{}_{}".format(joueur, "exterieur")], size=1)
                        
                    # change color
                    formatted_var = "{}3_outcome_color = 'white'".format(joueur)
                    exec(formatted_var)
                    
                    image_domicile_opacity = 0
                    image_exterieur_opacity = 1
                    
                    # text assignement for the other choice
                    fb_text_choice3 = " Choix du coach adjoint : {}".format(joueur)
                    
                    # image assignement for the outcome
                    if outcome3[0] == 1:
                        fb_text3 = 'images/Win.png'
                        resultat3_outcome_text = "C'est une victoire!"
                    else:
                        fb_text3 = 'images/Lose.png'
                        resultat3_outcome_text = "C'est une défaite!"
                        
                        
            try: 
                joueur_number = Condition
            except: 
                joueur_number = "25"
            fb_text_choice_component.setText(fb_text_choice3)
            outcome3_var = outcome3  # Set routine start values for outcome3_var
            nombre_matchs_third_outcome.setText("match n° {}".format(nombre_matchs_third))
            avec3_outcome.setPos([tuple(float(x) for x in avec_pos_text.strip("()").split(","))])
            sans3_outcome.setPos([tuple(float(x) for x in sans_pos_text.strip("()").split(","))])
            domicile3_outcome.setPos([tuple(float(x) for x in dom_pos_text.strip("()").split(","))])
            exterieur3_outcome.setPos([tuple(float(x) for x in ext_pos_text.strip("()").split(","))])
            domicile_image23.setColor(exterieur3_outcome_color, colorSpace='rgb')
            domicile_image23.setOpacity(1.0)
            domicile_image23.setPos([tuple(float(x) for x in dom_pos_image.strip("()").split(","))])
            exterieur_image23.setColor(domicile3_outcome_color, colorSpace='rgb')
            exterieur_image23.setOpacity(1.0)
            exterieur_image23.setPos([tuple(float(x) for x in ext_pos_image.strip("()").split(","))])
            question_outcome23.setText("Question: Voulez vous faire jouer l'équipe avec ou sans le joueur, à domicile ou à l'extérieur?".format(chr(joueur_number+64)))
            text_joueur_numero.setText("joueur {}".format(chr(joueur_number+64)))
            avec_image23.setColor(sans3_outcome_color, colorSpace='rgb')
            avec_image23.setPos([tuple(float(x) for x in avec_pos_image.strip("()").split(","))])
            sans_image23.setColor(avec3_outcome_color, colorSpace='rgb')
            sans_image23.setPos([tuple(float(x) for x in sans_pos_image.strip("()").split(","))])
            # keep track of which components have finished
            feedback_23Components = [fb_text_choice_component, image_outcome3, nombre_matchs_third_outcome, avec3_outcome, sans3_outcome, domicile3_outcome, exterieur3_outcome, resultat3_outcome, domicile_image23, exterieur_image23, question_outcome23, text_joueur_numero, cross_feedback23, avec_image23, sans_image23]
            for thisComponent in feedback_23Components:
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
            
            # --- Run Routine "feedback_23" ---
            while continueRoutine and routineTimer.getTime() < 3.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fb_text_choice_component* updates
                if fb_text_choice_component.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fb_text_choice_component.frameNStart = frameN  # exact frame index
                    fb_text_choice_component.tStart = t  # local t and not account for scr refresh
                    fb_text_choice_component.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fb_text_choice_component, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fb_text_choice_component.started')
                    fb_text_choice_component.setAutoDraw(True)
                if fb_text_choice_component.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fb_text_choice_component.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fb_text_choice_component.tStop = t  # not accounting for scr refresh
                        fb_text_choice_component.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fb_text_choice_component.stopped')
                        fb_text_choice_component.setAutoDraw(False)
                
                # *image_outcome3* updates
                if image_outcome3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    image_outcome3.frameNStart = frameN  # exact frame index
                    image_outcome3.tStart = t  # local t and not account for scr refresh
                    image_outcome3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_outcome3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_outcome3.started')
                    image_outcome3.setAutoDraw(True)
                if image_outcome3.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_outcome3.tStop = t  # not accounting for scr refresh
                        image_outcome3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_outcome3.stopped')
                        image_outcome3.setAutoDraw(False)
                if image_outcome3.status == STARTED:  # only update if drawing
                    image_outcome3.setImage(fb_text3, log=False)
                
                # *nombre_matchs_third_outcome* updates
                if nombre_matchs_third_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    nombre_matchs_third_outcome.frameNStart = frameN  # exact frame index
                    nombre_matchs_third_outcome.tStart = t  # local t and not account for scr refresh
                    nombre_matchs_third_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(nombre_matchs_third_outcome, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'nombre_matchs_third_outcome.started')
                    nombre_matchs_third_outcome.setAutoDraw(True)
                if nombre_matchs_third_outcome.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > nombre_matchs_third_outcome.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        nombre_matchs_third_outcome.tStop = t  # not accounting for scr refresh
                        nombre_matchs_third_outcome.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'nombre_matchs_third_outcome.stopped')
                        nombre_matchs_third_outcome.setAutoDraw(False)
                
                # *avec3_outcome* updates
                if avec3_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    avec3_outcome.frameNStart = frameN  # exact frame index
                    avec3_outcome.tStart = t  # local t and not account for scr refresh
                    avec3_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(avec3_outcome, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'avec3_outcome.started')
                    avec3_outcome.setAutoDraw(True)
                if avec3_outcome.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > avec3_outcome.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        avec3_outcome.tStop = t  # not accounting for scr refresh
                        avec3_outcome.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'avec3_outcome.stopped')
                        avec3_outcome.setAutoDraw(False)
                if avec3_outcome.status == STARTED:  # only update if drawing
                    avec3_outcome.setColor(avec3_outcome_color, colorSpace='rgb', log=False)
                
                # *sans3_outcome* updates
                if sans3_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sans3_outcome.frameNStart = frameN  # exact frame index
                    sans3_outcome.tStart = t  # local t and not account for scr refresh
                    sans3_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sans3_outcome, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sans3_outcome.started')
                    sans3_outcome.setAutoDraw(True)
                if sans3_outcome.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sans3_outcome.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        sans3_outcome.tStop = t  # not accounting for scr refresh
                        sans3_outcome.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sans3_outcome.stopped')
                        sans3_outcome.setAutoDraw(False)
                if sans3_outcome.status == STARTED:  # only update if drawing
                    sans3_outcome.setColor(sans3_outcome_color, colorSpace='rgb', log=False)
                
                # *domicile3_outcome* updates
                if domicile3_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    domicile3_outcome.frameNStart = frameN  # exact frame index
                    domicile3_outcome.tStart = t  # local t and not account for scr refresh
                    domicile3_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(domicile3_outcome, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'domicile3_outcome.started')
                    domicile3_outcome.setAutoDraw(True)
                if domicile3_outcome.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > domicile3_outcome.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        domicile3_outcome.tStop = t  # not accounting for scr refresh
                        domicile3_outcome.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'domicile3_outcome.stopped')
                        domicile3_outcome.setAutoDraw(False)
                if domicile3_outcome.status == STARTED:  # only update if drawing
                    domicile3_outcome.setColor(domicile3_outcome_color, colorSpace='rgb', log=False)
                
                # *exterieur3_outcome* updates
                if exterieur3_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    exterieur3_outcome.frameNStart = frameN  # exact frame index
                    exterieur3_outcome.tStart = t  # local t and not account for scr refresh
                    exterieur3_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(exterieur3_outcome, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'exterieur3_outcome.started')
                    exterieur3_outcome.setAutoDraw(True)
                if exterieur3_outcome.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > exterieur3_outcome.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        exterieur3_outcome.tStop = t  # not accounting for scr refresh
                        exterieur3_outcome.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'exterieur3_outcome.stopped')
                        exterieur3_outcome.setAutoDraw(False)
                if exterieur3_outcome.status == STARTED:  # only update if drawing
                    exterieur3_outcome.setColor(exterieur3_outcome_color, colorSpace='rgb', log=False)
                
                # *resultat3_outcome* updates
                if resultat3_outcome.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    resultat3_outcome.frameNStart = frameN  # exact frame index
                    resultat3_outcome.tStart = t  # local t and not account for scr refresh
                    resultat3_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resultat3_outcome, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'resultat3_outcome.started')
                    resultat3_outcome.setAutoDraw(True)
                if resultat3_outcome.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        resultat3_outcome.tStop = t  # not accounting for scr refresh
                        resultat3_outcome.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resultat3_outcome.stopped')
                        resultat3_outcome.setAutoDraw(False)
                if resultat3_outcome.status == STARTED:  # only update if drawing
                    resultat3_outcome.setText(resultat3_outcome_text, log=False)
                
                # *domicile_image23* updates
                if domicile_image23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    domicile_image23.frameNStart = frameN  # exact frame index
                    domicile_image23.tStart = t  # local t and not account for scr refresh
                    domicile_image23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(domicile_image23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'domicile_image23.started')
                    domicile_image23.setAutoDraw(True)
                if domicile_image23.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > domicile_image23.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        domicile_image23.tStop = t  # not accounting for scr refresh
                        domicile_image23.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'domicile_image23.stopped')
                        domicile_image23.setAutoDraw(False)
                
                # *exterieur_image23* updates
                if exterieur_image23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    exterieur_image23.frameNStart = frameN  # exact frame index
                    exterieur_image23.tStart = t  # local t and not account for scr refresh
                    exterieur_image23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(exterieur_image23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'exterieur_image23.started')
                    exterieur_image23.setAutoDraw(True)
                if exterieur_image23.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > exterieur_image23.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        exterieur_image23.tStop = t  # not accounting for scr refresh
                        exterieur_image23.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'exterieur_image23.stopped')
                        exterieur_image23.setAutoDraw(False)
                
                # *question_outcome23* updates
                if question_outcome23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    question_outcome23.frameNStart = frameN  # exact frame index
                    question_outcome23.tStart = t  # local t and not account for scr refresh
                    question_outcome23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(question_outcome23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'question_outcome23.started')
                    question_outcome23.setAutoDraw(True)
                if question_outcome23.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > question_outcome23.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        question_outcome23.tStop = t  # not accounting for scr refresh
                        question_outcome23.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'question_outcome23.stopped')
                        question_outcome23.setAutoDraw(False)
                
                # *text_joueur_numero* updates
                if text_joueur_numero.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_joueur_numero.frameNStart = frameN  # exact frame index
                    text_joueur_numero.tStart = t  # local t and not account for scr refresh
                    text_joueur_numero.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_joueur_numero, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_joueur_numero.started')
                    text_joueur_numero.setAutoDraw(True)
                if text_joueur_numero.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_joueur_numero.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_joueur_numero.tStop = t  # not accounting for scr refresh
                        text_joueur_numero.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_joueur_numero.stopped')
                        text_joueur_numero.setAutoDraw(False)
                
                # *cross_feedback23* updates
                if cross_feedback23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cross_feedback23.frameNStart = frameN  # exact frame index
                    cross_feedback23.tStart = t  # local t and not account for scr refresh
                    cross_feedback23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cross_feedback23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross_feedback23.started')
                    cross_feedback23.setAutoDraw(True)
                if cross_feedback23.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cross_feedback23.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        cross_feedback23.tStop = t  # not accounting for scr refresh
                        cross_feedback23.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'cross_feedback23.stopped')
                        cross_feedback23.setAutoDraw(False)
                
                # *avec_image23* updates
                if avec_image23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    avec_image23.frameNStart = frameN  # exact frame index
                    avec_image23.tStart = t  # local t and not account for scr refresh
                    avec_image23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(avec_image23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'avec_image23.started')
                    avec_image23.setAutoDraw(True)
                if avec_image23.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > avec_image23.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        avec_image23.tStop = t  # not accounting for scr refresh
                        avec_image23.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'avec_image23.stopped')
                        avec_image23.setAutoDraw(False)
                
                # *sans_image23* updates
                if sans_image23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sans_image23.frameNStart = frameN  # exact frame index
                    sans_image23.tStart = t  # local t and not account for scr refresh
                    sans_image23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(sans_image23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sans_image23.started')
                    sans_image23.setAutoDraw(True)
                if sans_image23.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sans_image23.tStartRefresh + 3.5-frameTolerance:
                        # keep track of stop time/frame for later
                        sans_image23.tStop = t  # not accounting for scr refresh
                        sans_image23.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sans_image23.stopped')
                        sans_image23.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback_23Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback_23" ---
            for thisComponent in feedback_23Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from fb_code_3
            nombre_matchs_third += 1
            thisExp.addData('outcome3_var.routineEndVal', outcome3_var)  # Save end routine value
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-3.500000)
            thisExp.nextEntry()
            
        # completed 30.0 repeats of 'innerBlocks'
        
        
        # --- Prepare to start Routine "question" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_6
        try: 
            joueur_number = Condition
        except: 
            joueur_number = "25"
        attractiveness.reset()
        text_question_1.setText("Évaluation de l'impact du joueur {}".format(chr(joueur_number+64)) + "\n" "\n Attribuez une note à l'impact du joueur {} sur le match en utilisant une échelle de -10 (le joueur contribue à la défaite de l'équipe), 0 (aucun impact sur le match) à 10 (le joueur contribue à la victoire de l'équipe).".format(chr(joueur_number+64)) + "\n Cliquez sur valider pour confirmer.")
        # setup some python lists for storing info about the mouse_15
        mouse_15.x = []
        mouse_15.y = []
        mouse_15.leftButton = []
        mouse_15.midButton = []
        mouse_15.rightButton = []
        mouse_15.time = []
        mouse_15.clicked_name = []
        gotValidClick = False  # until a click is received
        slider_recommandation.reset()
        # keep track of which components have finished
        questionComponents = [attractiveness, text_question_1, validate, mouse_15, slider_recommandation, text_recommandation]
        for thisComponent in questionComponents:
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
        
        # --- Run Routine "question" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *attractiveness* updates
            if attractiveness.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                attractiveness.frameNStart = frameN  # exact frame index
                attractiveness.tStart = t  # local t and not account for scr refresh
                attractiveness.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(attractiveness, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'attractiveness.started')
                attractiveness.setAutoDraw(True)
            
            # *text_question_1* updates
            if text_question_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_question_1.frameNStart = frameN  # exact frame index
                text_question_1.tStart = t  # local t and not account for scr refresh
                text_question_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_question_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_question_1.started')
                text_question_1.setAutoDraw(True)
            
            # *validate* updates
            if validate.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                validate.frameNStart = frameN  # exact frame index
                validate.tStart = t  # local t and not account for scr refresh
                validate.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(validate, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'validate.started')
                validate.setAutoDraw(True)
            # *mouse_15* updates
            if mouse_15.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_15.frameNStart = frameN  # exact frame index
                mouse_15.tStart = t  # local t and not account for scr refresh
                mouse_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_15.started', t)
                mouse_15.status = STARTED
                mouse_15.mouseClock.reset()
                prevButtonState = mouse_15.getPressed()  # if button is down already this ISN'T a new click
            if mouse_15.status == STARTED:  # only update if started and not finished!
                buttons = mouse_15.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(validate)
                            clickableList = validate
                        except:
                            clickableList = [validate]
                        for obj in clickableList:
                            if obj.contains(mouse_15):
                                gotValidClick = True
                                mouse_15.clicked_name.append(obj.name)
                        x, y = mouse_15.getPos()
                        mouse_15.x.append(x)
                        mouse_15.y.append(y)
                        buttons = mouse_15.getPressed()
                        mouse_15.leftButton.append(buttons[0])
                        mouse_15.midButton.append(buttons[1])
                        mouse_15.rightButton.append(buttons[2])
                        mouse_15.time.append(mouse_15.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # abort routine on response
            
            # *slider_recommandation* updates
            if slider_recommandation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_recommandation.frameNStart = frameN  # exact frame index
                slider_recommandation.tStart = t  # local t and not account for scr refresh
                slider_recommandation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_recommandation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_recommandation.started')
                slider_recommandation.setAutoDraw(True)
            
            # *text_recommandation* updates
            if text_recommandation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_recommandation.frameNStart = frameN  # exact frame index
                text_recommandation.tStart = t  # local t and not account for scr refresh
                text_recommandation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_recommandation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_recommandation.started')
                text_recommandation.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in questionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "question" ---
        for thisComponent in questionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        innerRun.addData('attractiveness.response', attractiveness.getRating())
        innerRun.addData('attractiveness.rt', attractiveness.getRT())
        # store data for innerRun (TrialHandler)
        innerRun.addData('mouse_15.x', mouse_15.x)
        innerRun.addData('mouse_15.y', mouse_15.y)
        innerRun.addData('mouse_15.leftButton', mouse_15.leftButton)
        innerRun.addData('mouse_15.midButton', mouse_15.midButton)
        innerRun.addData('mouse_15.rightButton', mouse_15.rightButton)
        innerRun.addData('mouse_15.time', mouse_15.time)
        innerRun.addData('mouse_15.clicked_name', mouse_15.clicked_name)
        innerRun.addData('slider_recommandation.response', slider_recommandation.getRating())
        innerRun.addData('slider_recommandation.rt', slider_recommandation.getRT())
        # the Routine "question" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'innerRun'
    
    
    # --- Prepare to start Routine "ending" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # keep track of which components have finished
    endingComponents = [text, key_resp_9]
    for thisComponent in endingComponents:
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
    
    # --- Run Routine "ending" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_9.started')
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
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
        for thisComponent in endingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ending" ---
    for thisComponent in endingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    loop_exps23.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        loop_exps23.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "ending" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'loop_exps23'


# --- Prepare to start Routine "instruction_end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
instruction_endComponents = [text_instr_12, key_resp_12]
for thisComponent in instruction_endComponents:
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

# --- Run Routine "instruction_end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr_12* updates
    if text_instr_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr_12.frameNStart = frameN  # exact frame index
        text_instr_12.tStart = t  # local t and not account for scr refresh
        text_instr_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr_12, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instr_12.started')
        text_instr_12.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_12.started')
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
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
    for thisComponent in instruction_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_end" ---
for thisComponent in instruction_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.nextEntry()
# the Routine "instruction_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
