<p align="center">
<img src="NEMESIS_TEAM_LOGO.jpg" alt="NEMESIS TEAM LOGO" style="border-radius:5px"/>
</p>

# Discord-Avatar-Autochange

## Introduction
A simple script that automatically keeps changing your discord avatar after a given amount of time based on the pictures you provide in a directory.


## DESCRIPTION
 - Since this scripts requires your Discord token DO NOT RUN THIS SCRIPT ON A PUBLIC SERVER like Replit etc.

---
## How to use

<br>

### To test

- ``` pip install -r requirements.txt ```
<br>
<br>
now to Set TOKEN and TIMEOUT in .env which Timeout is the time between each avatar change in <b style="color:green;">SECONDS</b>.
<br>
now to test the program run:

  -  ``` py main.py ```


<br>

---

### To Deploy
- Do all steps as mentioned before but do not run main file, After installing the requirements and setting TOKEN and TIMEOUT, Follow stebs below:
  - Edit `tools/win/DiscordAvatarStartUp.bat` and uncomment two lines which start with `cd` and `py` then replace the required paths. 
  <br> to uncomment remove `@rem`


  <br>
  - Now go to tools/win then run `addToStartup.bat` this will add `DiscordAvatarStartUp.bat` to the startup so the program will always launch on windows start up.
  <br>
  <br>
  - To Stop the program run `terminateDis.bat` in the projects root directory, or to make it simple you can make a shortcut or add it to taskbar.
  <br>
  <br>
  - Now that our launcher bat file is in startup you can either run 'DiscordAvatarStartUp.bat` once manually or restart your pc.

## NOTES
- Any Recommendation will be appreciated, don't forget `Pull requests` if you have any idea to improve this project . 👙🤺


### Do not HeZiTaTe to open issues if there was a problem!
<p align="center">
❤️❤️❤️
</p>
