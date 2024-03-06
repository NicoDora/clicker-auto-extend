from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import re

user_id = "" # 아이디 입력
user_pass = "" # 비밀번호 입력

action_code = "1" # 자리 선택: 0, 자리 이동: 1

seat_id = "" # 현재 내 좌석 아이디 or 원하는 좌석 아이디 입력

seat_reservation_url = "https://seat.induk.ac.kr/Clicker/ReadingRoomAction" # 좌석 예약 페이지 주소

lib_first_floor_id = "20240130112852987" # 도서관 1층 아이디

lib_url = f"https://seat.induk.ac.kr/Clicker/UserSeat/{ lib_first_floor_id }?DeviceName=normal"

def find_available_seat():
  try:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    chrome_options.add_argument("lang=ko_KR")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://seat.induk.ac.kr/Clicker/UserSeat/20240130112852987?DeviceName=normal")

    wait = WebDriverWait(driver, 10)

    element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="clicker_div_guide_map"]//div[@title="배정가능"]'))).get_attribute('id')

    id = re.search(r'\d+$', element).group()

    driver.quit()

    return id

  except:
    return { "error": "find_available_seat error" }

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
          "Guid": "yvjk25bqcbfzhpplohn0zkn0"
        })
    data = response.json()

    return data['g_flag_update_excute_success']
  
  except:
    return { "error": "request error" }

if __name__ == "__main__":
  # 선택가능한 좌석 아이디 찾기
  available_seat_id = find_available_seat()
  # 좌석 예약 요청
  request_seat(available_seat_id)
  
  # 원래 좌석으로 이동
  result = request_seat(seat_id)
  if result:
    print("이동 성공")
  else:
    print("이동 실패")
