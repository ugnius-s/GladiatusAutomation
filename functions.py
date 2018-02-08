from datetime import datetime
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from objects import BOX_USERNAME,BOX_PASSWORD,BOX_SERVER
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

def puts (text):
  print('['+str(datetime.now())+']$ '+text)

  
def check_hp(client, max_percentage):
  puts("Checking if there is sufficient amount of HP, at least ({0}%)".format(str(max_percentage)))
  hp_percentage = client.find_element_by_id("header_values_hp_percent").text[:-1]
  if int(hp_percentage) >= max_percentage:
    return True
  return False

def eat_food(client):
  puts("Most likely not enough health, will check if can eat something")
  character_view_link = client.find_element_by_css_selector("#mainmenu > a:nth-child(1)")
  character_view_link.click()
  time.sleep(2)

  puts("Enumerating items")
  min_price = 9999999
  min_tab = False
  min_item_id = -1
  
  for tab_index in range(1,9):
    puts("Checking tab {0}".format(str(tab_index)))
    tab = client.find_element_by_css_selector("#inventory_nav > a:nth-child({0})".format(tab_index))
    tab.click()
    inv = client.find_element_by_id("inv")
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
  avatar = client.find_element_by_css_selector("#avatar > div:nth-child(4)")
  inv = client.find_element_by_id("inv")
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
  
def check_notifications(client):
  # Possible event such as level up could break automation, thus we have to check and click
  puts("Checking for notifications")
  found = True
  while found:
    try:
      link_notification = client.find_element_by_id("linknotification")
      link_notification.click()
    except (NoSuchElementException, ElementNotVisibleException):
      found = False
      puts("No notifications found")
	  
def check_bonus(client):
  try:
    bonus_link = client.find_element_by_id("linkLoginBonus")
    bonus_link.click()
    puts("Clicking bonus link")
  except NoSuchElementException:
    puts("No bonus link")

def log_in(client,user,notice):
  try:
    puts(notice)
    # Grab login fields;
    box_username = client.find_element_by_id(BOX_USERNAME)  # Find the search box
    box_password = client.find_element_by_id(BOX_PASSWORD)  # Find the search box
    box_server = Select(client.find_element_by_id(BOX_SERVER))

    puts("Logging in")
    # Login;
    box_username.send_keys(user.ACCOUNT_USERNAME)
    box_password.send_keys(user.ACCOUNT_PASSWORD)
    box_server.select_by_visible_text(user.ACCOUNT_SERVER)
    box_username.send_keys(Keys.RETURN)
  except NoSuchElementException:
    puts("Already logged in, or redirected to unknown page")

