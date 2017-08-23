#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os

def notify(title, text):
    os.system("""
              /usr/local/bin/terminal-notifier -title "{}" -message "{}" -sound "Purr" 
              """.format(title, text))

workouts = [
    "10 pushups",
    "30 second hollow hold",
    "30 second plank hold",
    "10 airsquats",
    "2 pike walks",
    "10 lunge steps",
    "10 sit ups",
    "30 second side plank (pick a side)",
    "10 burpees",
    "10 second L-sit in chair",
]

selected_workout = random.choice(workouts)

notify("💪🏻  Time to work out!", selected_workout)
