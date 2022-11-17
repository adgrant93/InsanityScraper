# InsanityScraper
Scraper to download photos from vk.com.

(Originally designed for all the MsInsanity Wallpapers) 

-----
MsInsanity Links:

Twitter: https://twitter.com/madskillz_arts

Facebook: https://www.facebook.com/animeirl/

Instagram: https://www.instagram.com/madskillz_arts/

Patreon: https://www.patreon.com/ms_arts

-----
Why?
  Because MsInsanity Artists are great! Also they are only available on this site vk.com a russian site. All the ones from the last 5 years are there at this time based on my in depth research. Vk only lets you search through if you have an account (what a bother). I didn't want to do that (not giving them my phone number). So I found if you click on an image and exit out of the sign in box you can see the picture, open the link in a new tab and download :D. So I just made a script that starts at that first link or 'Initialization Vector (IV)' if you will (idk if I used that right lol), and just wgets and clicks and wgets and clicks and wgets and clicks........ around 1900+ times and gets all the wallpapers no account needed and a lot of time saved. Pretty cool huh! :D This is my first web scraper and it was a lot of fun to make. And I learned some transferable skills so win-win!

-----
Prerequisites:

You need pip, wget, and Selenium modules installed. You need Chrome (bleh) and chrome web driver for your version of chrome. Will probably work with chromium too.

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
Web driver path is hard coded it doesn't take input yet. You can modify line 21 'executable_path' variable with your absolute path, this is just me on my mac. You would use "C:\\Folder\\chromedriver.exe" for windows for example. This person gives a great example (where I got a lot of info on selenium from).
 
https://medium.com/jaanvi/headless-browser-in-python-9a1dcc2b608b

How to Run:
Run the py file from the directory you want the downloads to be. (I downloaded it to my MsInsanity Folder for example.)
python3 insanityScraper.py

Download Link:
When you find an artist you like, you need to click on the first picture of their collection (On their main page). Click the 'x' when it asks you to sign in, the post and picture will load. Then supply that link. An example of this is below:

https://vk.com/msinsanity?z=photo-72806334_457241185%2Falbum-72806334_00%2Frev

Removing Duplicates:
Unfortunately, duplicate removal is not implemented yet. If you can use the following commands in the directory to remove dupes For MacOS, Linux, and Windows.

MacOS/Linux:
ls | grep '(' | xargs rm

Windows:
powershell -c "Remove-Item * -Include '*(*'"

-----
Please read below for updates on bugs and whatnot.

Update 11/12:
  I overhauled the code and added a few features. It will now grab every single wallpaper even if there are duplicates :D (no one likes dupes...)! Also you can put in your own link so anything on VK can be pulled. I provided an example of which page to supply for any particular page. In the future, I will add the ability to start downloading at another point. If you for example lost your connection at page 301, you will be able to start again from there. Maybe I should work on recovery for this..... Also need to add the ability to add webdriver directory.

Update 10/6: 
  It's basically done. It missed like 2 wallpapers at the very end and accidentally downloaded 2 twice. Just a race condition thing. Will probably add a sleep or whatever to the code later to fix that. For now I just downloaded the last 2 manually ;D
  Directory choosing needs to be added I think I'm being limited by wget here but we'll see.
  Also there is a lot of hard coding going on here. Who did that? >=^( If the number of wallpapers goes above 1000 it'll definitely have issues. I think if they add more wallpapers it might not get them all? idk until they add a new one lol.
  I removed the headless option just so you can see what its doing. I'll probably add it back in the final version. 
