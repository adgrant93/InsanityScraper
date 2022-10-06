# InsanityScraper
Scraper to download all the MsInsanity Wallpapers

You need Selenium installed as well as Chrome (bleh) and chrome web driver for your version of chrome. Will probably work with chromium too.

Installing pip (if you don't have it):

https://www.geeksforgeeks.org/how-to-install-pip-in-macos/

Selenium: pip install selenium
Chrome Web Driver: https://chromedriver.chromium.org/downloads
Note: Download the right one for your version of Chrome. To check chrome version do the following:
  Open Chrome > 3 dots/hamburger icon > Help > About
Chrome: https://www.google.com/chrome/
Chromium (untested): https://www.chromium.org/getting-involved/download-chromium/

Use:

Web driver path is hard coded it doesn't take input yet. You can modify line 22 'executable_path' variable with your absolute path, this is just me on my mac. You would use "C:\\Folder\\webdriver.exe" for windows for example. This person gives a great example (where I got a lot of info on selenium from).
 
https://medium.com/jaanvi/headless-browser-in-python-9a1dcc2b608b

Run the py file from the directory you want the downloads to be. (I downloaded it to my MsInsanity Folder for example.)

Update 10/6: 
  It's basically done. It missed like 2 wallpapers at the very end and accidentally downloaded 2 twice. Just a race condition thing. Will probably add a sleep or whatever to the code later to fix that. For now I just downloaded the last 2 manually ;D
  Directory choosing needs to be added I think I'm being limited by wget here but we'll see.
  Also there is a lot of hard coding going on here. If the number of wallpapers goes above 1000 it'll definitely have issues. I think if they add more wallpapers it might not get them all? idk until they add a new one lol.
  I removed the headless option just so you can see what its doing. I'll probably add it back in the final version. 
