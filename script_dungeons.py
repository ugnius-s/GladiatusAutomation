from selenium.common.exceptions import NoSuchElementException
from functions import puts,check_bonus,log_in,check_notifications,delay
import selectors as SELECTORS
import time

def loop(client, user, location_selection, exit_on_zero_points):  
  puts("Entering dungeons")
  
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
    dungeon_bar = SELECTORS.get_dungeon_bar(client)
    
    if (dungeon_bar):
      dungeon_bar.click()

    check_notifications(client)
    delay(wait_time)