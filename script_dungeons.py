from selenium.common.exceptions import NoSuchElementException
from functions import puts,check_bonus,log_in,check_notifications,delay
import selectors as SELECTORS
import time

def loop(client, user, location_selection, exit_on_zero_points, max_dungeon_fights):    
  done_dungeon_fights = 0
  
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
    puts("Entering dungeons")

    dungeon_bar = SELECTORS.get_dungeon_bar(client)
    if (dungeon_bar):
      dungeon_bar.click()
      
    # Go to location
    location = SELECTORS.get_location(client, location_selection)
    if (location):
      location.click()
      
    # Go to dungeon tab
    puts("Clicking on dungeon tab")

    tab = SELECTORS.get_dungeon_tab(client)
    if (tab):
      tab.click()
      
    # Dificulty 1
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
        done_dungeon_fights += 1
        wait_time = 5 * 60
 
    if (done_dungeon_fights == max_dungeon_fights):
      puts("Exiting script after {0} dungeons".format(done_dungeon_fights))
      return 

    delay(wait_time)