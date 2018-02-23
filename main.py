# Imports;
from selenium import webdriver

import importlib
import sys
from functions import *

USER = __import__(sys.argv[1])
SCRIPT_STABLES = __import__('script_stables')
SCRIPT_EXPEDITIONS = __import__('script_expeditions')
SCRIPT_DUNGEONS = __import__('script_dungeons')
SCRIPT_ARENA_PROVINCIARUM = __import__('script_arena_provinciarum')

# Create client driver;
puts("Creating web driver")
client = webdriver.Chrome()
client.get(USER.DEFAULT_GLADIATUS_URI)

# Login;
log_in(client,USER,"First time log in")

while True:
  #SCRIPT_ARENA_PROVINCIARUM.loop(client, USER, 5, 50, True, 5)
  SCRIPT_EXPEDITIONS.loop(client, USER, 6, 2, 40, True, True, 1)
  SCRIPT_DUNGEONS.loop(client, USER, 5, True, 1)
  SCRIPT_STABLES.loop(client, USER, 1, True) 
