from selenium.common.exceptions import NoSuchElementException
from functions import puts,check_bonus,log_in,check_notifications,delay
import time

def loop(client, user, hours):
  puts("Working in stables for {0} hours".format(hours))
  worked_hours = 0
  
  while True:
    wait_time = 3610
    log_in(client, user,"Checking if we can log in")
    check_notifications(client)
    time.sleep(1)

    if (worked_hours == hours):
      puts("Exiting script after working for {0} hours".format(worked_hours))
      return

    client.execute_script("switchMenu(1)")
	
    try:
      job_link = client.find_element_by_css_selector("#submenu1 > a:nth-child(1)")
      job_link.click();
    except NoSuchElementException:
      puts("Can't access Job menu, maybe disconnected?")

    try:
      job_link_do = client.find_element_by_css_selector("#doWork")
      job_link_do.click()
      worked_hours += 1
      puts("Starting Work")
    except NoSuchElementException:
      puts("Unable to start working, will try again in 60 seconds") 
      wait_time = 60

    delay(wait_time)
