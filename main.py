# Imports;
from selenium import webdriver

import importlib
import sys
from functions import *

USER = __import__(sys.argv[1])
SCRIPT_STABLES = __import__('script_stables')
SCRIPT_EXPEDITIONS = __import__('script_expeditions')
SCRIPT_DUNGEONS = __import__('script_dungeons')

# Create client driver;
puts("Creating web driver")
client = webdriver.Chrome()
client.get(USER.DEFAULT_GLADIATUS_URI)

# Login;
log_in(client,USER,"First time log in")

while True:
  #SCRIPT_EXPEDITIONS.loop(client, USER, 5, 4, 40, True, True)
  SCRIPT_DUNGEONS.loop(client, USER, 5, True)
  #SCRIPT_STABLES.loop(client, USER, 1) 
