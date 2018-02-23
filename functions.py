from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotVisibleException,WebDriverException
import selectors as SELECTORS
import base64
import time

def puts (text):
  # Print message to console
  message = '['+str(datetime.now())+']$ '+ text
  # file = open("automation.log","a") 
  # file.write(message+'\n')
  # file.close()
  print(message)

def delay(wait_time):
  # Delay automation
  for second in range (1,wait_time+1):
    puts("Currently at {0}/{1}".format(str(second),str(wait_time)))
    time.sleep(1)
  
def check_hp(client, max_percentage):
  # Check if HP is in proper range
  puts("Checking if there is sufficient amount of HP, at least ({0}%)".format(str(max_percentage)))
  
  hp_percentage = SELECTORS.get_current_hp_percentage(client)
  if (hp_percentage) and (hp_percentage >= max_percentage):
    return True
    
  return False

def eat_food(client):
  # Eat food from inventory if possible
  puts("Most likely not enough health, will check if can eat something")
  
  character_view_link = SELECTORS.get_character_view(client)
  if (character_view_link):  
    character_view_link.click()
    
  time.sleep(2)
  puts("Enumerating items")
  
  min_price = 9999999
  min_tab = False
  min_item_id = -1
  
  for tab_index in range(1,9):
    puts("Checking tab {0}".format(str(tab_index)))
    
    tab = SELECTORS.get_tab(client, tab_index)
    if(tab):
      tab.click()
    
    inv = SELECTORS.get_inventory(client)
    
    if(inv): 
      for element in (inv.find_elements_by_css_selector("*")):
        try:
          element_type = int(element.get_attribute("data-content-type"))
        except TypeError:
          element_type = -1
        if (element_type == 64): # If food
          price = int(element.get_attribute("data-price-gold"))
          print(price)
          if (price < min_price):
            min_price = price
            min_item_id = int(element.get_attribute("data-item-id"))
            min_tab = tab
  
  if (min_item_id == -1):
    return False

  min_tab.click()
  
  # Get avatar and inventory objects
  avatar = SELECTORS.get_avatar(client)
  inv = SELECTORS.get_inventory(client)
  if not (avatar or inv):
    return False
    
  selected_element = False
  
  # Need to look again for the element :/
  for element in (inv.find_elements_by_css_selector("*")):
    element_type = int(element.get_attribute("data-content-type"))
    if (element_type == 64): # If food
      id = int(element.get_attribute("data-item-id"))
      if (id == min_item_id):
        selected_element = element
		
  print(selected_element)
  print(avatar)
  print(min_item_id)
  
  puts("Dragging food")
  actionChains = ActionChains(client)
  actionChains.drag_and_drop(selected_element, avatar).perform()
  return True
  
def check_bonus(client):
  # Check for bonus link
  bonus_link = SELECTORS.get_bonus(client)
  
  if(bonus_link):
    bonus_link.click()
    puts("Clicking bonus link")
    return True
    
  puts("No bonus link")
  return False
  
def check_notifications(client):
  # Possible event such as level up could break automation, thus we have to check and click
  found = True
  if check_bonus(client):
    time.sleep(1)
  
  while found:
    link_notification = SELECTORS.get_notification(client)
    if not (link_notification):
      return False
      
    try:
      link_notification.click()
      puts("Notification closed")
    except (NoSuchElementException, ElementNotVisibleException):
      found = False
      puts("No notifications found")
      
  return True

def log_in(client,user,notice):
  puts(notice)
  box_username = SELECTORS.get_username_box(client)
  box_password = SELECTORS.get_password_box(client)
  box_server = SELECTORS.get_server_box(client)
  
  if not (box_username or box_password or box_server):
    puts("Already logged in, or redirected to unknown page")
    return False
    
  puts("Logging in")
  box_username.send_keys(user.ACCOUNT_USERNAME)
  box_password.send_keys(base64.b64decode(user.ACCOUNT_PASSWORD).decode("utf-8"))
  box_server.select_by_visible_text(user.ACCOUNT_SERVER)
  box_username.send_keys(Keys.RETURN)
  return True

