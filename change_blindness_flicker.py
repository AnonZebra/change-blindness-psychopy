#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.2),
    on Tue Jun  7 11:28:37 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

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

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.2'
expName = 'change_blindness_flicker'  # from the Builder filename that created this script
expInfo = {'participant': ''}
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
    originPath='/Users/workingman/Documents/ASD_and_Synesthesia/Python/psychopy_shared_github/change_blindness_project/change_blindness_flicker.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_welcome = visual.TextStim(win=win, name='text_welcome',
    text='Du kommer att visas bildspel.\n\nVarje bildspel växlar mellan två bilder. I den ena bilden har ett föremål tagits bort så att det saknas. \n\nDu ska leta efter objektet som hela tiden försvinner och dyker upp igen i bildspelet. Så snart du hittar det, klicka med vänster musknapp på den plats objektet befinner sig.\n\nTestet tar cirka 10-15 minuter. Du kommer att se ett meddelande när du är klar.\n\nKlicka på texten nedanför för att pröva ett exempel.',
    font='Arial',
    units='deg', pos=(0, 0), height=0.7, wrapWidth=26, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_welcome_continue = visual.TextStim(win=win, name='text_welcome_continue',
    text='Klicka här när du läst klart för att pröva ett exempel',
    font='Arial',
    units='deg', pos=(0, -7), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_welcome = event.Mouse(win=win)
x, y = [None, None]
mouse_welcome.mouseClock = core.Clock()

# Initialize components for Routine "practice"
practiceClock = core.Clock()
# form circle representing target area of practice image
practice_target_radius = 22.140398025397776
practice_target_xcoord = -222.0
practice_target_ycoord = 171.0
practice_target_coords = (
    practice_target_xcoord,
    practice_target_ycoord
)
circle_practice = visual.Polygon(
    win=win, name='circle_practice',
    edges=120, size=(practice_target_radius*2, practice_target_radius*2),
    ori=0, pos=practice_target_coords,
    lineWidth=1, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# feedback text stimulus for practice
text_feedback = visual.TextStim(win=win, name='text_feedback',
    text='',
    font='Arial',
    units='deg', pos=(0, 12), height=0.8, wrapWidth=20, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# 'continue' text stimulus for practice
text_continue = visual.TextStim(win=win, name='text_continue',
    text='Klicka här för att fortsätta.',
    font='Arial',
    units='deg', pos=(0, -12), height=0.5, wrapWidth=20, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_practice = event.Mouse(win=win)
x, y = [None, None]
mouse_practice.mouseClock = core.Clock()

# Initialize components for Routine "start"
startClock = core.Clock()
text_start_inst = visual.TextStim(win=win, name='text_start_inst',
    text='Testet fortsätter till nästa bildspel om du inte svarar inom 30 sekunder.\n\nTestet tar cirka 10-15 minuter. Du kommer att se ett meddelande när du är klar.\n\nKlicka på texten nedanför för att börja.',
    font='Arial',
    units='deg', pos=(0, 0), height=0.7, wrapWidth=26, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_start_continue = visual.TextStim(win=win, name='text_start_continue',
    text='Klicka här när du läst klart för att starta experimentet',
    font='Arial',
    units='deg', pos=(0, -7), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_start = event.Mouse(win=win)
x, y = [None, None]
mouse_start.mouseClock = core.Clock()

# Initialize components for Routine "fixation_3000ms"
fixation_3000msClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',units='deg', 
    size=(5, 5),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "blank_1000ms"
blank_1000msClock = core.Clock()
text_blank_placeholder = visual.TextStim(win=win, name='text_blank_placeholder',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
# form image components for drawing stimuli
img_absent = visual.ImageStim(
    win=win,
    name='img_absent', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1024, 768),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
img_present = visual.ImageStim(
    win=win,
    name='img_present', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1024, 768),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
mouse_trial = event.Mouse(win=win)
x, y = [None, None]
mouse_trial.mouseClock = core.Clock()

# Initialize components for Routine "end_screen"
end_screenClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='Tack!\n\nTa cirka två minuters paus innan du matar in ditt deltagar-ID för nästa test.',
    font='Arial',
    units='deg', pos=(0, 0), height=1.5, wrapWidth=26, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_welcome
mouse_welcome.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionsComponents = [text_welcome, text_welcome_continue, mouse_welcome]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome* updates
    if text_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome.frameNStart = frameN  # exact frame index
        text_welcome.tStart = t  # local t and not account for scr refresh
        text_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome, 'tStartRefresh')  # time at next scr refresh
        text_welcome.setAutoDraw(True)
    
    # *text_welcome_continue* updates
    if text_welcome_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome_continue.frameNStart = frameN  # exact frame index
        text_welcome_continue.tStart = t  # local t and not account for scr refresh
        text_welcome_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome_continue, 'tStartRefresh')  # time at next scr refresh
        text_welcome_continue.setAutoDraw(True)
    # *mouse_welcome* updates
    if mouse_welcome.status == NOT_STARTED and t >= 2.5-frameTolerance:
        # keep track of start time/frame for later
        mouse_welcome.frameNStart = frameN  # exact frame index
        mouse_welcome.tStart = t  # local t and not account for scr refresh
        mouse_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_welcome, 'tStartRefresh')  # time at next scr refresh
        mouse_welcome.status = STARTED
        mouse_welcome.mouseClock.reset()
        prevButtonState = mouse_welcome.getPressed()  # if button is down already this ISN'T a new click
    if mouse_welcome.status == STARTED:  # only update if started and not finished!
        buttons = mouse_welcome.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(text_welcome_continue)
                    clickableList = text_welcome_continue
                except:
                    clickableList = [text_welcome_continue]
                for obj in clickableList:
                    if obj.contains(mouse_welcome):
                        gotValidClick = True
                        mouse_welcome.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice"-------
continueRoutine = True
# update component parameters for each repeat
img_present.setImage(os.path.join('img_stimuli', '019_L_filler_present_lamp_sized.jpg'))
img_absent.setImage(os.path.join('img_stimuli', '019_L_filler_absent_lamp_sized.jpg'))

# initialize list of previous frame's clicked buttons
prevButtonState = []

# initialize indicator of whether participant has tried
# to click target or not
has_clicked = False
# setup some python lists for storing info about the mouse_practice
mouse_practice.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
practiceComponents = [mouse_practice]
for thisComponent in practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice"-------
while continueRoutine:
    # get current time
    t = practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    buttons = mouse_practice.getPressed()
    if buttons != prevButtonState and t>0.2:  # button state changed and more than 0.2s have passed since onset?
        prevButtonState = buttons
        if buttons[0] == 1:  # state changed to a new left button click
            if has_clicked:
                # check if mouse was 'inside' continue text
                if text_continue.contains(mouse_practice):
                    continueRoutine = False
            else:
                # check if mouse was inside target circle
                correct_click = False
                if circle_practice.contains(mouse_practice):
                        correct_click = True
                if correct_click:
                    text_feedback.text = 'Det var rätt! Föremålet är markerat nedan i rött.'
                else:
                    text_feedback.text = 'Du missade föremålet. Det är markerat nedan i rött.'
                x, y = mouse_practice.getPos()
                mouse_practice.x = x
                mouse_practice.y = y
                has_clicked = True
    
    if not has_clicked:
        # show image with target present for 240ms, 
        # nothing for 80ms, then the image with the
        # target absent for 240ms, then nothing for the 
        # remaining 80ms of the cycle
        # (so in total, each cycle is 640ms)
        if tThisFlip%0.64<0.24:
            img_present.draw()
        elif 0.32 <= (tThisFlip%0.64)<0.56:
            img_absent.draw()
    else:
        img_present.draw()
        circle_practice.draw()
        text_feedback.draw()
        text_continue.draw()
    # *mouse_practice* updates
    if mouse_practice.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_practice.frameNStart = frameN  # exact frame index
        mouse_practice.tStart = t  # local t and not account for scr refresh
        mouse_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_practice, 'tStartRefresh')  # time at next scr refresh
        mouse_practice.status = STARTED
        mouse_practice.mouseClock.reset()
        prevButtonState = mouse_practice.getPressed()  # if button is down already this ISN'T a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice"-------
for thisComponent in practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data about where participant clicked on target area
thisExp.addData('mouse_practice.x', mouse_practice.x)
thisExp.addData('mouse_practice.y', mouse_practice.y)
thisExp.addData('mouse_practice.correct', correct_click)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_start
mouse_start.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
startComponents = [text_start_inst, text_start_continue, mouse_start]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_start_inst* updates
    if text_start_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_start_inst.frameNStart = frameN  # exact frame index
        text_start_inst.tStart = t  # local t and not account for scr refresh
        text_start_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_start_inst, 'tStartRefresh')  # time at next scr refresh
        text_start_inst.setAutoDraw(True)
    
    # *text_start_continue* updates
    if text_start_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_start_continue.frameNStart = frameN  # exact frame index
        text_start_continue.tStart = t  # local t and not account for scr refresh
        text_start_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_start_continue, 'tStartRefresh')  # time at next scr refresh
        text_start_continue.setAutoDraw(True)
    # *mouse_start* updates
    if mouse_start.status == NOT_STARTED and t >= 2.5-frameTolerance:
        # keep track of start time/frame for later
        mouse_start.frameNStart = frameN  # exact frame index
        mouse_start.tStart = t  # local t and not account for scr refresh
        mouse_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_start, 'tStartRefresh')  # time at next scr refresh
        mouse_start.status = STARTED
        mouse_start.mouseClock.reset()
        prevButtonState = mouse_start.getPressed()  # if button is down already this ISN'T a new click
    if mouse_start.status == STARTED:  # only update if started and not finished!
        buttons = mouse_start.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(text_start_continue)
                    clickableList = text_start_continue
                except:
                    clickableList = [text_start_continue]
                for obj in clickableList:
                    if obj.contains(mouse_start):
                        gotValidClick = True
                        mouse_start.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
img_trial_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(os.path.join("specification_csvs", "change_blindness_flicker_stimuli_data.csv")),
    seed=None, name='img_trial_loop')
thisExp.addLoop(img_trial_loop)  # add the loop to the experiment
thisImg_trial_loop = img_trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisImg_trial_loop.rgb)
if thisImg_trial_loop != None:
    for paramName in thisImg_trial_loop:
        exec('{} = thisImg_trial_loop[paramName]'.format(paramName))

for thisImg_trial_loop in img_trial_loop:
    currentLoop = img_trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisImg_trial_loop.rgb)
    if thisImg_trial_loop != None:
        for paramName in thisImg_trial_loop:
            exec('{} = thisImg_trial_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation_3000ms"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_3000msComponents = [polygon]
    for thisComponent in fixation_3000msComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixation_3000msClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation_3000ms"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_3000msClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixation_3000msClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_3000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_3000ms"-------
    for thisComponent in fixation_3000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "blank_1000ms"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank_1000msComponents = [text_blank_placeholder]
    for thisComponent in blank_1000msComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank_1000msClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank_1000ms"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_1000msClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank_1000msClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_blank_placeholder* updates
        if text_blank_placeholder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_blank_placeholder.frameNStart = frameN  # exact frame index
            text_blank_placeholder.tStart = t  # local t and not account for scr refresh
            text_blank_placeholder.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_blank_placeholder, 'tStartRefresh')  # time at next scr refresh
            text_blank_placeholder.setAutoDraw(True)
        if text_blank_placeholder.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_blank_placeholder.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_blank_placeholder.tStop = t  # not accounting for scr refresh
                text_blank_placeholder.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_blank_placeholder, 'tStopRefresh')  # time at next scr refresh
                text_blank_placeholder.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_1000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank_1000ms"-------
    for thisComponent in blank_1000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    img_present.setImage(os.path.join('img_stimuli', target_present))
    img_absent.setImage(os.path.join('img_stimuli', target_absent))
    
    
    # store trial start time for saving during "End Routine"
    trial_start_time = globalClock.getTime()
    # setup some python lists for storing info about the mouse_trial
    mouse_trial.x = []
    mouse_trial.y = []
    mouse_trial.leftButton = []
    mouse_trial.midButton = []
    mouse_trial.rightButton = []
    mouse_trial.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trialComponents = [mouse_trial]
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
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # show image with target present for 240ms, 
        # nothing for 80ms, then the image with the
        # target absent for 240ms, then nothing for the 
        # remaining 80ms of the cycle
        # (so in total, each cycle is 640ms)
        
        if tThisFlip%0.64<0.24:
            img_present.draw()
        elif 0.32 <= (tThisFlip%0.64)<0.56:
            img_absent.draw()
        # *mouse_trial* updates
        if mouse_trial.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_trial.frameNStart = frameN  # exact frame index
            mouse_trial.tStart = t  # local t and not account for scr refresh
            mouse_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_trial, 'tStartRefresh')  # time at next scr refresh
            mouse_trial.status = STARTED
            mouse_trial.mouseClock.reset()
            prevButtonState = mouse_trial.getPressed()  # if button is down already this ISN'T a new click
        if mouse_trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_trial.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                mouse_trial.tStop = t  # not accounting for scr refresh
                mouse_trial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_trial, 'tStopRefresh')  # time at next scr refresh
                mouse_trial.status = FINISHED
        if mouse_trial.status == STARTED:  # only update if started and not finished!
            buttons = mouse_trial.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse_trial.getPos()
                    mouse_trial.x.append(x)
                    mouse_trial.y.append(y)
                    buttons = mouse_trial.getPressed()
                    mouse_trial.leftButton.append(buttons[0])
                    mouse_trial.midButton.append(buttons[1])
                    mouse_trial.rightButton.append(buttons[2])
                    mouse_trial.time.append(mouse_trial.mouseClock.getTime())
                    
                    continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # save trial end time
    trial_end_time = globalClock.getTime()
    
    # if the participant did make a mouse click during the trial's 30s
    if len(mouse_trial.x): 
        # if participant's click is within two times the target radius, 
        # determined using Pythagora's, register the click as being correct.
        # (the radius is based on the pixel area specified in the excel sheet from the change blindness database.
        # the reason that we multiply the radius by 2 here is that for
        # elongated objects, the radius ends up being way too short,
        # and the risk of false negatives is probably much greater than
        # false positives)
        if (((target_xcoord_px - mouse_trial.x)**2 + (target_ycoord_px - mouse_trial.y)**2)**(1/2)) < target_radius_px*2:
            img_trial_loop.addData('mouse_trial.correct', 1)
        # if participant's click is more than 2 target radii away from
        # the target center, register it as incorrect.
        else:
            img_trial_loop.addData('mouse_trial.correct', 0)
    else:
        img_trial_loop.addData('mouse_trial.correct', "no_response")
    
    # save trial start time, using saved value from "Begin Routine",
    # and trial end time
    img_trial_loop.addData('trial_start_time', trial_start_time)
    img_trial_loop.addData('trial_end_time', trial_end_time)
    
    # store data for img_trial_loop (TrialHandler)
    img_trial_loop.addData('mouse_trial.x', mouse_trial.x)
    img_trial_loop.addData('mouse_trial.y', mouse_trial.y)
    img_trial_loop.addData('mouse_trial.leftButton', mouse_trial.leftButton)
    img_trial_loop.addData('mouse_trial.midButton', mouse_trial.midButton)
    img_trial_loop.addData('mouse_trial.rightButton', mouse_trial.rightButton)
    img_trial_loop.addData('mouse_trial.time', mouse_trial.time)
    img_trial_loop.addData('mouse_trial.started', mouse_trial.tStart)
    img_trial_loop.addData('mouse_trial.stopped', mouse_trial.tStop)
    thisExp.nextEntry()
    
# completed 1 repeats of 'img_trial_loop'


# ------Prepare to start Routine "end_screen"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
end_screenComponents = [text_end]
for thisComponent in end_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if text_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_end.frameNStart = frameN  # exact frame index
        text_end.tStart = t  # local t and not account for scr refresh
        text_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
        text_end.setAutoDraw(True)
    if text_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_end.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text_end.tStop = t  # not accounting for scr refresh
            text_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_end, 'tStopRefresh')  # time at next scr refresh
            text_end.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_screen"-------
for thisComponent in end_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

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
