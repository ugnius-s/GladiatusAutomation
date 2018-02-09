from functions import puts
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
import time

###########    JOB     ###########

def get_job_menu(client):
  client.execute_script("switchMenu(1)")
  time.sleep(1)
  try:
    return client.find_element_by_css_selector("#submenu1 > a:nth-child(1)")
  except (NoSuchElementException, ElementNotVisibleException):
    return False

def get_job_do(client):
  time.sleep(1)
  try:
    return client.find_element_by_css_selector("#doWork")
  except (NoSuchElementException, ElementNotVisibleException):
    return False
    
def get_job_cooldown_time(client):
  time.sleep(1)
  try:
    cooldown = client.find_element_by_css_selector(
      "#content > article > section > table > tbody > tr:nth-child(3) > td:nth-child(2) > span")
    nums = [int(n) for n in cooldown.text.split(':')]
    return nums[0] * 3600 + nums[1] * 60 + nums[2]
  except (NoSuchElementException, ElementNotVisibleException):
    return False

########### EXPEDITION ###########

def get_points(client):
  time.sleep(1)
  try:
    return int(client.find_element_by_css_selector("#expeditionpoints_value_point").text)
  except (NoSuchElementException, ElementNotVisibleException):
    return False

def get_expedition_bar(client):
  time.sleep(1)
  try:
    return client.find_element_by_css_selector("#cooldown_bar_expedition > a:nth-child(3)")
  except (NoSuchElementException, ElementNotVisibleException):
    return False
    
def get_location(client, location_selection):
  client.execute_script("switchMenu(2)")
  time.sleep(1)
  puts("Selected {0} location".format(location_selection))
  try:
    return client.find_element_by_css_selector("#submenu2 > a:nth-child({0})".format(str(location_selection)))
  except (NoSuchElementException, ElementNotVisibleException):
    puts("Cannot select place {0}".format(str(location_selection)))
  return False
  
def get_enemy(client, enemy_selection):
  time.sleep(1)
  puts("Selected {0} enemy".format(enemy_selection))
  try:
    return client.find_element_by_css_selector(
          "div.expedition_box:nth-child({0}) > div:nth-child(2) > button:nth-child(1)".format(str(enemy_selection)))
  except (NoSuchElementException, ElementNotVisibleException):
    puts("Cannot select enemy {0}".format(str(location_selection)))
  return False
  
def get_expedition_cooldown_time(client, check_for_work):
  time.sleep(1)
  try:
    cooldown_bar_text = client.find_element_by_css_selector("#cooldown_bar_text_expedition").text
    if (cooldown_bar_text == "-"):
      return False
    if (check_for_work):
      return  True
    nums = [int(n) for n in cooldown_bar_text.split(':')]
    return nums[0] * 3600 + nums[1] * 60 + nums[2]
  except (NoSuchElementException, ElementNotVisibleException):
    return False
    
def is_expedition_on_cooldown(client):
  time.sleep(1)
  try:
    cooldown_indicator = client.find_elements_by_class_name("expedition_cooldown_reduce")
    if(len(cooldown_indicator) > 0):
      return True
  except (NoSuchElementException, ElementNotVisibleException):
    return False