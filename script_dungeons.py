from selenium.common.exceptions import NoSuchElementException
from functions import puts,check_bonus,log_in,check_notifications,delay
import selectors as SELECTORS
import time

def loop(client, user, location_selection, exit_on_zero_points):    
  # If cannot determine cooldown time, must be working or somethings wrong. Exit script
  if not (SELECTORS.get_expedition_cooldown_time(client, True)):
    puts("Exiting dungeons")
    return
  puts("Doing dungeons")
  
  while True:
    wait_time = 60
    log_in(client, user,"Checking if we can log in")
    check_notifications(client)
    
    # Check if we need to exit before delay
    if (SELECTORS.get_dungeon_points(client) == 0 and exit_on_zero_points):
      puts("Exiting dungeon script")
      return
        
    # Go to dungeons
    check_notifications(client)
    puts("Entering dungeons")

    dungeon_bar = SELECTORS.get_dungeon_bar(client)
    if (dungeon_bar):
      dungeon_bar.click()
      
    # Get go to location
    check_notifications(client)
    puts("Entering {0} location".format(location_selection))

    location = SELECTORS.get_location(client, location_selection)
    if (location):
      location.click()
      
    # Get go to dungeon tab
    check_notifications(client)
    puts("Clicking on dungeon tab")

    tab = SELECTORS.get_dungeon_tab(client)
    if (tab):
      tab.click()
      
    # Dificulty 1
    check_notifications(client)
    puts("Selecting first difficulty")

    dif1 = SELECTORS.get_dungeon_dif1(client)
    if(dif1):
      dif1.click()
    else:
      puts("Couldn't select first difficulty, maybe already in a dungeon?")
      
    if SELECTORS.is_dungeon_on_cooldown(client):
      puts("Dungeon on cooldown")
      wait_time = SELECTORS.get_dungeon_cooldown_time(client, False)
    else:
      # Select first found label and click attack
      puts("Fighting in dungeon")
      areas = SELECTORS.get_dungeon_areas(client)
      if(areas):
        areas[0].click()
        wait_time = 5 * 60
    
    check_notifications(client)
    delay(wait_time)