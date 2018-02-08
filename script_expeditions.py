from selenium.common.exceptions import NoSuchElementException
from functions import puts,check_bonus,log_in,check_notifications,check_hp,eat_food
import time

def loop(client, user, place_selection, enemy_selection, max_hp):
  puts("Doing expedition")
  
  while True:
    wait_time = 60
    log_in(client, user,"Checking if we can log in")
    check_bonus(client)
    check_notifications(client)
    time.sleep(1)
	
    if check_hp(client, max_hp):
      try:
        menu_link = client.find_element_by_css_selector("#cooldown_bar_expedition > a:nth-child(3)")
        menu_link.click();
      except NoSuchElementException:
        puts("Can't access expeditions menu, maybe disconnected?")
    
      try:
        puts("Selected {0} place and {1} enemy".format(str(place_selection), str(enemy_selection)))
        place_link = client.find_element_by_css_selector("#submenu2 > a:nth-child({0})".format(str(place_selection)))
        place_link.click();
      except (NoSuchElementException, ElementNotVisibleException):
        puts("Cannot select place {0}".format(str(place_selection)))
      time.sleep(2)

      cooldown_bar_text = client.find_element_by_css_selector("#cooldown_bar_text_expedition")	
      cooldown_indicator = client.find_elements_by_class_name("expedition_cooldown_reduce")
	
      if len(cooldown_indicator) > 0:
        puts("Expedition on cooldown")
        nums = [int(n) for n in cooldown_bar_text.text.split(':')]
        wait_time = nums[0] * 3600 + nums[1] * 60 + nums[2]
      else:
        puts("Starting expedition")
        enemy_link = client.find_element_by_css_selector(
          "div.expedition_box:nth-child({0}) > div:nth-child(2) > button:nth-child(1)".format(str(enemy_selection)))
        enemy_link.click()
        wait_time = 5 * 60
    else:
      eaten = eat_food(client)
      wait_time = 0
      if (eaten == False): # no food
        wait_time = 30 * 60
    for second in range (1,wait_time+1):
      puts("Currently at {0}/{1}".format(str(second),str(wait_time)))
      time.sleep(1)