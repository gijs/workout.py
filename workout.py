#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice, randint
import os
import time

WAIT_INTERVAL = 3

def notify(title, text):
    os.system("""
              /usr/local/bin/terminal-notifier -title "{}" -message "{}" -sound "Glass" 
              """.format(title, text))
    time.sleep(10)
    os.system("""
              /usr/local/bin/terminal-notifier -title "{}" -message "{}" -sound "Frog" 
              """.format("3", "3"))    
    time.sleep(WAIT_INTERVAL)
    os.system("""
              /usr/local/bin/terminal-notifier -title "{}" -message "{}" -sound "Frog" 
              """.format("2", "2"))        
    time.sleep(WAIT_INTERVAL)
    os.system("""
              /usr/local/bin/terminal-notifier -title "{}" -message "{}" -sound "Frog" 
              """.format("1", "1"))        
    time.sleep(WAIT_INTERVAL)
    os.system("""
              /usr/local/bin/terminal-notifier -title "{}" -message "{}" -sound "Frog" 
              """.format("Go! Perform the mini workout", text))        
    time.sleep(WAIT_INTERVAL)
    os.system("pmset displaysleepnow")


workouts = [
    "{} pushups".format(randint(5,20)),
    "{} airsquats".format(randint(5,20)),
    
    "{} second hollow hold".format(randint(10,30)),
    "{} second plank hold".format(randint(10,30)),
    "{} second side plank hold".format(randint(10,15)),
    
    "{} pike walks".format(randint(2,10)),
    "{} lunges".format(randint(2,10)),
    "{} sit-ups".format(randint(5,20)),

    "{} burpees".format(randint(5,20)),
    "{} second L-sit (in chair or on the ground)".format(randint(5,10)),
]

selected_workout = choice(workouts)

notify("💪🏻  Time to work out!", selected_workout)
