from selenium.common.exceptions import NoSuchElementException
from functions import puts,check_bonus,log_in,check_notifications,check_hp,eat_food,delay
import selectors as SELECTORS
import time

def loop(client, user, location_selection, 
  enemy_selection, max_hp, exit_on_zero_points, exit_on_no_food, max_expeditions):  
  done_expeditions = 0
  
  # If cannot determine cooldown time, must be working or somethings wrong. Exit script
  if not (SELECTORS.get_expedition_cooldown_time(client, True)):
    puts("Exiting expeditions")
    return
    
  puts("Entering expeditions")
  
  while True:
    wait_time = 60
    log_in(client, user,"Checking if we can log in")     
    check_notifications(client)

    # Check if we need to exit before delay
    if (SELECTORS.get_points(client) == 0 and exit_on_zero_points):
      puts("Exiting expedition script")
      return
    
    # Check if we need to eat
    if check_hp(client, max_hp):
    
      # Go to expeditions
      expedition_bar = SELECTORS.get_expedition_bar(client)
      if (expedition_bar):
        expedition_bar.click()
      
      # Get go to location
      check_notifications(client)
      location = SELECTORS.get_location(client, location_selection)
      if (location):
        location.click()
        
      puts("Getting cooldowns")
      check_notifications(client)
	 	
      if SELECTORS.is_expedition_on_cooldown(client):
        puts("Expedition on cooldown")
        wait_time = SELECTORS.get_expedition_cooldown_time(client, False)
      else:
        puts("Starting expedition")
        check_notifications(client)
        enemy = SELECTORS.get_enemy(client, enemy_selection)
        if (enemy):
          enemy.click()
          done_expeditions += 1
          wait_time = 5 * 60
          
    else: # Eat food
      wait_time = 0
      if not (eat_food(client)): # no food
        if(exit_on_no_food):
          return
        else:
          wait_time = 30 * 60

    if (done_expeditions == max_expeditions):
      puts("Exiting script after {0} expeditions".format(max_expeditions))
      return
      
    check_notifications(client)
    delay(wait_time)