from selenium.common.exceptions import NoSuchElementException
from functions import puts,check_bonus,log_in,check_notifications,check_hp,eat_food,delay
import selectors as SELECTORS
import time

def loop(client, user, enemy_selection, 
    max_hp, exit_on_zero_points, exit_on_no_food, max_events):  
  done_events = 0
  log_in(client, user,"Checking if we can log in")     
    
  puts("Entering fight event")
  while True:
    wait_time = 60
    log_in(client, user,"Checking if we can log in")     
    check_notifications(client)
    
    # Check if we need to eat
    if check_hp(client, max_hp):
    
      # Go to expeditions
      expedition_bar = SELECTORS.get_expedition_bar(client)
      if (expedition_bar):
        expedition_bar.click()
      
      time.sleep(1)
      puts("Entering fight events")
      
      # Get go to location
      location = SELECTORS.get_event_fight_location(client)
      if (location):
        location.click()

      puts("Getting cooldowns")	 	    
      if SELECTORS.get_event_fight_cooldown_time(client, False):
        puts("Fight event on cooldown")
        wait_time = SELECTORS.get_event_fight_cooldown_time(client, False)
      else:
        puts("Starting fight event")
        enemy = SELECTORS.get_event_fight_enemy(client, enemy_selection)
        if (enemy):
          enemy.click()
          done_events += 1
          wait_time = 5 * 60
          
    else: # Eat food
      wait_time = 0
      if not (eat_food(client)): # no food
        if(exit_on_no_food):
          return
        else:
          wait_time = 30 * 60

    if (done_events == max_events):
      puts("Exiting script after {0} events".format(max_events))
      return
      
    delay(wait_time)