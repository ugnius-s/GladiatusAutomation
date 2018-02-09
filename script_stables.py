from selenium.common.exceptions import NoSuchElementException
from functions import puts,check_bonus,log_in,check_notifications,delay
import selectors as SELECTORS
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
	
    job_menu = SELECTORS.get_job_menu(client)
    if (job_menu): 
      job_menu.click();

    job_do = SELECTORS.get_job_do(client)
    if (job_do):
      job_do.click()
      worked_hours += 1
      puts("Starting Work")
    else:
     wait_time = SELECTORS.get_job_cooldown_time(client)

    delay(wait_time)
