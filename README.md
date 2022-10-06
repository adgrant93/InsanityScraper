# InsanityScraper
Scraper to download all the MsInsanity Wallpapers. 

-----
MsInsanity:

https://twitter.com/msinsanity_bot

-----
Why?
  Because MsInsanity Artists are great! Also they are only available on this site vk.com a russian site. All the ones from the last 5 years are there at this time based on my in depth research. Vk only lets you search through if you have an account (what a bother). I didn't want to do that (not giving them my phone number). So I found if you click on an image and exit out of the sign in box you can see the picture, open the link in a new tab and download :D. So I just made a script that starts at that first link or 'Initialization Vector (IV)' if you will (idk if I used that right lol), and just wgets and clicks and wgets and clicks and wgets and clicks........ around 900+ times and gets all the wallpapers no account needed and a lot of time saved. Pretty cool huh! :D This is my first web scraper and it was a lot of fun to make. And I learned some transferable skills so win-win!

-----
Prerequisites:

You need pip installed, Selenium installed, Chrome (bleh) and chrome web driver for your version of chrome. Will probably work with chromium too.

Installing pip (if you don't have it. if on linux you probably do.):

https://www.geeksforgeeks.org/how-to-install-pip-in-macos/

Selenium: (From terminal/cmd) pip install selenium
Chrome Web Driver: https://chromedriver.chromium.org/downloads
Note: Download the right one for your version of Chrome. To check chrome version do the following:
  Open Chrome > 3 dots/hamburger icon > Help > About
Chrome: https://www.google.com/chrome/
Chromium (untested): https://www.chromium.org/getting-involved/download-chromium/

-----
Use:

Web driver path is hard coded it doesn't take input yet. You can modify line 22 'executable_path' variable with your absolute path, this is just me on my mac. You would use "C:\\Folder\\webdriver.exe" for windows for example. This person gives a great example (where I got a lot of info on selenium from).
 
https://medium.com/jaanvi/headless-browser-in-python-9a1dcc2b608b

Run the py file from the directory you want the downloads to be. (I downloaded it to my MsInsanity Folder for example.)
python3 insanityScraper.py

Please read below for updates on bugs and whatnot.

-----
Update 10/6: 
  It's basically done. It missed like 2 wallpapers at the very end and accidentally downloaded 2 twice. Just a race condition thing. Will probably add a sleep or whatever to the code later to fix that. For now I just downloaded the last 2 manually ;D
  Directory choosing needs to be added I think I'm being limited by wget here but we'll see.
  Also there is a lot of hard coding going on here. Who did that? >=^( If the number of wallpapers goes above 1000 it'll definitely have issues. I think if they add more wallpapers it might not get them all? idk until they add a new one lol.
  I removed the headless option just so you can see what its doing. I'll probably add it back in the final version. 
