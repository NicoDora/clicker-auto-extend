from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import re
import json

user_id = "" # 아이디 입력
user_pass = "" # 비밀번호 입력

action_code = "0" # 자리 선택: 0, 자리 이동: 1
seat_number = "" # 현재 내 좌석 번호 or 원하는 좌석 번호 입력

seat_reservation_url = "https://seat.induk.ac.kr/Clicker/ReadingRoomAction" # 좌석 예약 페이지 주소

lib_first_floor_id = "20240130112852987" # 도서관 1층 아이디
lib_url = f"https://seat.induk.ac.kr/Clicker/UserSeat/{ lib_first_floor_id }?DeviceName=normal"

seat_number_json_path = "seat_number.json"

def find_available_seat():
  try:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    chrome_options.add_argument("lang=ko_KR")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(lib_url)

    wait = WebDriverWait(driver, 10)

    element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="clicker_div_guide_map"]//div[@title="배정가능"]'))).get_attribute('id')

    my_seat_number_locate = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[@class="clicker_s_s_no" and text()="{ seat_number }"]')))

    # 상위 div 찾기
    parent_div = my_seat_number_locate.find_element(By.XPATH, "./parent::div")

    # 상위 div의 id 값 가져오기
    my_seat_full_id = parent_div.get_attribute('id')

    my_seat_id = re.search(r'\d+$', my_seat_full_id).group()
    next_seat_id = re.search(r'\d+$', element).group()

    driver.quit()

    return my_seat_id, next_seat_id

  except Exception as error:
    return False, { "error": error }

def request_seat(seat_id):
  try:
    response = requests.get(
      seat_reservation_url, params = {
        f"ActionCode": { action_code },
          "SeatId": { seat_id },
          "UserId": { user_id },
          "UserPass": { user_pass },
          "DeviceName": "desktop",
          "Kiosk": "false",
          "Guid": "rtoaqegxcqaih1bldkdmnmum"
        })
    data = response.json()

    return data['g_flag_update_excute_success']
  
  except:
    return { "error": "request error" }

if __name__ == "__main__":

  if action_code == '0':
    with open(seat_number_json_path, "r") as file:
      # JSON 파일 읽기
      data = json.load(file)
      seat_id = data[seat_number]

    result = request_seat(seat_id)

    if result:
      print("예약 성공")
    else:
      print("예약 실패")

  elif action_code == '1':
    # 선택가능한 좌석 아이디 찾기
    my_seat_id, next_seat_id = find_available_seat()
    if not my_seat_id and "error" in next_seat_id:
      print(next_seat_id)
      exit()

    # 좌석 예약 요청
    request_seat(next_seat_id)
    
    # 원래 좌석으로 이동
    result = request_seat(my_seat_id)
    if result:
      print("이동 성공")
    else:
      print("이동 실패")
