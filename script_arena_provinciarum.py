from selenium.common.exceptions import NoSuchElementException
from functions import puts,check_bonus,log_in,check_notifications,check_hp,eat_food,delay
import selectors as SELECTORS
import time

def loop(client, user, enemy_selection, max_hp, exit_on_no_food, max_arenas):  
  done_arenas = 0
  
  # If cannot determine cooldown time, must be working or somethings wrong. Exit script
  if not (SELECTORS.get_arena_cooldown_time(client, True)):
    puts("Exiting arena provinciarum")
    return
    
  puts("Entering arena provinciarum")
  
  while True:
    wait_time = 60
    log_in(client, user,"Checking if we can log in")     
    check_notifications(client)
    
    # Check if we need to eat
    if check_hp(client, max_hp):
    
      # Go to expeditions
      check_notifications(client)
      arena_bar = SELECTORS.get_arena_bar(client)
      if (arena_bar):
        arena_bar.click()
      
      # Get go to tab
      check_notifications(client)
      tab = SELECTORS.get_arena_provinciarum_tab(client)
      if (tab):
        tab.click()
        
      check_notifications(client)	 	
      if SELECTORS.is_arena_provinciarum_on_cooldown(client):
        puts("Arena on cooldown")
        wait_time = SELECTORS.get_arena_cooldown_time(client, False)
      else:
        puts("Starting arena")
        check_notifications(client)
        
        enemy = SELECTORS.get_arena_provinciarum_enemy(client, enemy_selection)
        if (enemy):
          enemy.click()
          done_arenas += 1
          wait_time = 5 * 60
          
    else: # Eat food
      wait_time = 0
      if not (eat_food(client)): # no food
        if(exit_on_no_food):
          return
        else:
          wait_time = 30 * 60

    if (done_arenas == max_arenas):
      puts("Exiting script after {0} arenas".format(max_arenas))
      return
      
    check_notifications(client)
    delay(wait_time)