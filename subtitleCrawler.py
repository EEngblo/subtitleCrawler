#################################################
#
# YouTube subtitle crawler for RedKiwi
#   by Jinyoung Oh 2018/11/16
#
#################################################


# pip3 install webvtt-py
# brew install youtube-dl

import os
import sys
import glob
import webvtt
import json
from datetime import datetime

manualMode = input("Would you like to manually merge some splitted sentences? (y/n) \n")
URL = input("Enter the full URL of an YouTube channel or video\n")

print("===============================================================================================")
print(" 🧐  Download subtitles from " + URL + " 🧐")
print("===============================================================================================")

os.system('mkdir result') # to init the result folder
os.system('youtube-dl --write-sub --sub-lang en,en-US,en-UK --skip-download -ciw -o "%(title)s__|__%(id)s__|__%(duration)s.%(ext)s" ' + URL)

print("===============================================================================================")
print(" 😎  Download completed!  😎 ")
print()
print(" 🤯  Parse subtitles into .json  🤯")
print("===============================================================================================")

foldername = URL.split("youtube.com/")[1]

for rawFilename in glob.glob('*.vtt'):

    filename = rawFilename.split('__|__')
    title = filename[0]
    youTubeVideoId = filename[1]
    fullDurationInMs = int(filename[2].split('.en')[0]) * 1000
    
    fragments = dict()

    if manualMode != 'y' and manualMode != 'Y':
        # Auto mode
        print("  Parse %s" % title, end=".. ")
        for caption in webvtt.read(rawFilename):
            start = caption.start.replace('.',',')
            fragments[start] = {
                'endTime': caption.end.replace('.',','),
                'text': caption.text.replace('\n',' '),
                'translations': [],
            }

    else:
        # Manually merge some splitted senteces
        print("  Parse %s" % title)
        prevCaption = None

        for caption in webvtt.read(rawFilename):
            # per each sentence

            if prevCaption == None: # init
                prevCaption = caption
                continue

            print("----------------------------------------------")
            print(" - Current: " + prevCaption.text)
            print("    - Next: " + caption.text)

            action = input("# Enter (1) to commit current sentence; (3) to merge; (5) to remove current sentence:\n")
            while (action != '1') and (action != '3') and (action != '5'):
                action = input("# Enter (1) to commit current sentence; (3) to merge; (5) to remove current sentence:\n")

            if(action == '1'):
                start = prevCaption.start.replace('.',',')
                fragments[start] = {
                    'endTime': prevCaption.end.replace('.',','),
                    'text': prevCaption.text.replace('\n',' '),
                    'translations': [],
                }
                prevCaption = caption
            elif(action == '3'):
                prevCaption.text += " " + caption.text
                prevCaption.end = caption.end
            elif(action == '5'):
                prevCaption = caption

        print("----------------------------------------------")
        if(action == '3'):
            print('3')
            start = prevCaption.start.replace('.',',')
            fragments[start] = {
                'endTime': prevCaption.end.replace('.',','),
                'text': prevCaption.text.replace('\n',' '),
                'translations': [],
            }
        else:
            print(" - Current: " + prevCaption.text)
            print("    - Next: __(This is the last sentence)__")
            action = input("# Enter (1) to commit current sentence; (3) to merge; (5) to remove current sentence:\n")
            while (action != '1') and (action != '5'):
                action = input("# Enter (1) to commit current sentence; (3) to merge; (5) to remove current sentence:\n")

            if(action == '1'):
                start = prevCaption.start.replace('.',',')
                fragments[start] = {
                    'endTime': prevCaption.end.replace('.',','),
                    'text': prevCaption.text.replace('\n',' '),
                    'translations': [],
                }
                prevCaption = caption
            elif(action == '5'):
                prevCaption = caption
            print("----------------------------------------------")

    JSON = {
        "youTubeVideoId" : youTubeVideoId,
        "title" : title,
        "createdAt" : None,
        "durationInMs" : fullDurationInMs,
        "fullDurationInMs" : fullDurationInMs,
        "description" : "",
        "tags" : [],
        "fragments" : fragments,
    }

    # Fix this line to change the file names of JSONs
    with open("./result/" + title + ".json", 'w') as j:
        json.dump(JSON, j, indent=2)

    os.remove(rawFilename)
    print("done!")

print("===============================================================================================")
print(" 😎  Parsing completed!  😎 ")
    