# Gladiatus Automation #

Gladiatus Automation is a pile of python code which uses Selenium framework to automate a very old browser game, published by GameForge.

## How to get it running? ##

As we are using python, additional setup is required such as python itself, selenium framework and browser drivers.

First of all you should install latest version of python from https://www.python.org/downloads/. Make sure to install pip and include installation directory to PATH environment variable so you could use py/python and pip commands from terminal.

Next step would be to download browser drivers, currently only **Google Chrome** is tested to work. Select the latest version from https://sites.google.com/a/chromium.org/chromedriver/downloads and put downloaded executable to any folder which is mentioned in PATH environment variable. For Windows users I would suggest to place it into Python installation directory. As for linux, good old /bin or /usr/bin directories are fine.

Lastly you should create a directory, run 'pip install selenium' and clone repo. That's it.

## How to use it? ##

Okay, so now we've got everything set up, we need a profile to specify a user. Create a file named username.py in the same directory with the following contents.

DEFAULT_GLADIATUS_URI = "http://www.gladiatus.lt"  
ACCOUNT_USERNAME = "name"  
ACCOUNT_PASSWORD = "password64"  
ACCOUNT_SERVER   = "Provincija 14"   

No details will be sent over the network (only when logging in), if you don't believe it, see for yourself. Password should be encoded in base64 and account server should be full text matching the selection box option.

To start automation, run 'py main.py username' command in the console.  Afterwards you should see log message that web driver is starting and new browser window popups. Automation script will login automatically.

## How to change scripts? ##

At this moment, there are no interface to manage automation, thus we have to do it manual way. You will find script execution at the bottom of main.py file. Feel free to create your own execution order. Note, that currently only 3 scripts are available.

## * Job Stables * ##

When started, bot will work in stables for parameter hours or until buffer overflow if -1 specified.  

``` SCRIPT_STABLES.loop(client, USER, 2, True) ```

Script takes couple of number type parameters (ignore first two).
1. Exit script after working for n hours
2. Exit script if we still have expedition or dungeon points, but don't exit if we were working previously


## * Expedition Script * ##

Does expeditions and eats food from inventory if needed.  

``` SCRIPT_EXPEDITIONS.loop(client, USER, 5, 4, 40, True, True, 1) ```

Script takes couple of number type parameters (ignore first two).
1. Selects which menu option should be used in locations
2. Selects which enemy should be attacked
3. Minimum health percentage when it should start to eat food
4. Exit script on 0 expedition points
5. Exit script when out of food
6. Exit script after n expedition fights

## * Dungeoning Script * ##

Does dungeons by clearing every available enemy.  

``` SCRIPT_DUNGEONS.loop(client, USER, 5, True, 1) ```

Script takes couple of number type parameters (ignore first two).
1. Selects which menu option should be used in locations
2. Exit script on 0 dungeon points
3. Exit script after n dungeon fights
