from selenium.common.exceptions import NoSuchElementException
from functions import puts,check_bonus,log_in,check_notifications
import time

def loop(client, user, job_link_text,job_link_do_text):
  puts("Working in stables")
  while True:
    wait_time = 3610
    log_in(client, user,"Checking if we can log in")
    check_bonus(client)
    check_notifications(client)

    try:
      job_link = client.find_element_by_link_text(job_link_text)
      job_link.click();
    except NoSuchElementException:
      puts("Can't access Job menu, maybe disconnected?")

    try:
      job_link_do = client.find_element_by_id(job_link_do_text)
      job_link_do.click()
      puts("Starting Work")
    except NoSuchElementException:
      puts("Unable to start working, will try again in 60 seconds") 
      wait_time = 60
    for second in range (1,wait_time+1):
      puts("Currently at {0}/{1}".format(str(second),str(wait_time)))
      time.sleep(1)
