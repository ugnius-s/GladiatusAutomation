# Gladiatus Automation #

Gladiatus Automation is a pile of python code using Selenium framework to automate a very old browser game, published by Gameforge, called Gladiatus.

*Automation code is ameturely written and needs lot of refactoring, but I'm too lazy.*

## How to get it running? ##

As we are using python, additional setup is required such as python programming language, selenium framework and browser drivers.

First of all you should install latest version of python from https://www.python.org/downloads/. Make sure to install pip and set proper environment variables so you could use py/python and pip commands from terminal.

Next step would be to download browser drivers, currently only **Google Chrome** was tested. Select the latest version from https://sites.google.com/a/chromium.org/chromedriver/downloads and put downloaded executable to any folder which is mentioned in PATH environment variable. For Windows users I would suggest to place it into Python installation directory.

Lastly you should create a directory, run 'pip install selenium' and clone repo. That's it.

## How to use it? ##

Okay, so now we've got everything set up, we need a profile to specify a user. Create a file named username.py in the same directory with the following contents.

DEFAULT_GLADIATUS_URI = "http://www.gladiatus.lt"  
ACCOUNT_USERNAME = "name"  
ACCOUNT_PASSWORD = "password"  
ACCOUNT_SERVER   = "Provincija 14"   

No details will be sent over the network, if you don't believe it, see for yourself.

To start automation, run 'py main.py username' command in the console.  Afterwards you should see log message in the console that web driver is starting and new browser window popups. Automation script will login automatically.

## How to change scripts? ##

At this moment, there are no interface to manage automation, thus we have to do it manual way. You will find script execution at the bottom of main.py file. Uncoment which script you want to execute. Note, that currently only 2 scripts are available.

## * Job Stables * ##

When started, bot will work in stables for every hour until end of universe.  

``` SCRIPT_STABLES.loop(client, USER) ```

## * Expedition Script * ##

Does expeditions and eats food from inventory if needed.  

``` SCRIPT_EXPEDITIONS.loop(client, USER, 5, 4, 40) ```

Script takes couple of number type parameters.
* First: Selects which menu option should be selected in locations
* Second: Selects which enemy should be attacked
* Third: Minimum health percentage when it should start to eat food
