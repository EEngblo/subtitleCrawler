# Subtitle Crawler for RedKiwi
## Install
### 1. Install Python 3: [download](https://www.python.org/downloads/)
### 2. Install [youtube-dl](https://github.com/rg3/youtube-dl/)
```bash
brew install youtube-dl
```
### 3. Install pip3: [follow this](https://itsevans.com/install-pip-osx/)
### 4. Install [webvtt-py](https://github.com/glut23/webvtt-py)
```bash
pip3 install webvtt-py
```

## Usage
```
$ python3 subtitleCrawler.py
Would you like to manually merge some splitted sentences? (y/n)
> y
Enter the full URL of an YouTube channel or video
> https://www.youtube.com/watch?v=yM-_rAceMU8
==============================================================
 🧐  Download subtitles from https://www.youtube.com/watch?v=yM-_rAceMU8 🧐
==============================================================
[youtube] yM-_rAceMU8: Downloading webpage
[youtube] yM-_rAceMU8: Downloading video info webpage
WARNING: en-US subtitles not available for yM-_rAceMU8
WARNING: en-UK subtitles not available for yM-_rAceMU8
[info] Writing video subtitles to: How to Say No at Work__|__yM-_rAceMU8__|__69.en.vtt
==============================================================
 😎  Download completed!  😎

 🤯  Parse subtitles into .json  🤯
==============================================================
  Parse How to Say No at Work.. done!
==============================================================
 😎  Parsing completed!  😎 
```
If you want to manually merge splitted sentences such as,
``` json
    "00:00:03,080": {
      "endTime": "00:00:07,120",
      "text": "My name is Marion and I had spent 25 years",
      "translations": []
    },
    "00:00:07,120": {
      "endTime": "00:00:09,920",
      "text": "in an organization and had worked my way in",
      "translations": []
    },
```
please answer `y` or `Y` for the first question. By this, you will face this for every sentences
```
 🤯  Parse subtitles into .json  🤯
==============================================================
  Parse How to Say No at Work
----------------------------------------------
 - Current: So, you're cutting the timeline in half?
    - Next: Well I guess the team can't possibly
# Enter (1) to commit current sentence; (3) to merge; (5) to remove current sentence:
> 
```
if you enter `1` here, it will commit 'So, you're cutting the timeline in half?' as a sentence.

if you enter `3` here, it will merge 'So, you're cutting the timeline in half?' and ' Well I guess the team can't possibly' and ask again.

if you enter `5` here, it will discard 'So, you're cutting the timeline in half?'