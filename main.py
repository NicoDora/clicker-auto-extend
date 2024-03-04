from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

user_id = "nicodora" # 아이디 입력
user_password = "password" # 비밀번호 입력

my_seat = "150" # 현재 내 좌석 번호 입력

url = "https://seat.induk.ac.kr/clicker/UserSeat/" # 좌석 예약 페이지 주소

def initialize_driver():
  chrome_options = Options()

  chrome_options.add_experimental_option("detach", True)
  chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36")

  driver = webdriver.Chrome(options=chrome_options)
  driver.maximize_window()

  return driver

def navigate_to_page(driver, url):
  driver.get(url)

def clickable_seat(wait):
  try:
    clickable_seat = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@title="배정가능"]')))
    clickable_seat.click()
  except:
    print("No available seat")

def login(wait, id, password):
  try:
    id_element = wait.until(EC.element_to_be_clickable((By.ID, 'textUserId')))
    id_element.send_keys(id)

    password_element = wait.until(EC.element_to_be_clickable((By.ID, 'textUserPass')))
    password_element.send_keys(password)
  except:
    print("login failed")

def change_seat(wait):
  try:
    login_button = wait.until(EC.element_to_be_clickable((By.ID, 'buttonChangeSeat')))
    login_button.click()
  except:
    print("change seat failed")

def click_cancel(wait):
  try:
    cancel_button = wait.until(EC.element_to_be_clickable((By.ID, 'buttonCloseSeat')))
    cancel_button.click()
  except:
    print("cancel failed")

def select_my_seat(wait, seat_id):
  try:
    my_seat = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[@class="clicker_s_s_no" and text()="{ seat_id }"]')))
    my_seat.click()
  except:
    print("select seat failed")

def find_change_button(wait):
  try:
    return wait.until(EC.element_to_be_clickable((By.ID, 'buttonChangeSeat'))) 
  except:
    return False

def main():
  try:
    driver = initialize_driver()

    wait = WebDriverWait(driver, 10)
    wait_short = WebDriverWait(driver, 1)

    navigate_to_page(driver, url)

    clickable_seat(wait)
    login(wait, user_id, user_password)
    change_seat(wait)
    click_cancel(wait)

    select_my_seat(wait, my_seat)

    if not find_change_button(wait_short):
      click_cancel(wait)
    
    select_my_seat(wait, my_seat)
    login(wait, user_id, user_password)
    change_seat(wait)

    click_cancel(wait)

  except Exception as error:
    print(error)

  finally:
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
  main()