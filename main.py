import requests
import json

user_id = "" # 아이디 입력
user_pass = "" # 비밀번호 입력

action_code = "0" # 자리 선택: 0, 자리 이동: 1
seat_number = "" # 현재 내 좌석 번호 or 원하는 좌석 번호 입력

seat_reservation_url = "https://seat.induk.ac.kr/Clicker/ReadingRoomAction" # 좌석 예약 페이지 주소
lib_first_floor_id = "20240130112852987" # 도서관 1층 아이디
lib_url = f"https://seat.induk.ac.kr/Clicker/UserSeat/{ lib_first_floor_id }?DeviceName=normal"
get_available_seat_url = "https://seat.induk.ac.kr/Clicker/GetSeatObjects"
release_seat_url = "https://seat.induk.ac.kr/Clicker/ReleaseReadingSeat"
seat_number_json_path = "seat_number.json"

def request_seat(seat_id):
  try:
    response = requests.get(
      seat_reservation_url, params = {
        f"ActionCode": { '0' },
          "SeatId": { seat_id },
          "UserId": { user_id },
          "UserPass": { user_pass },
          "DeviceName": "desktop",
          "Kiosk": "false",
          "Guid": "qscjmubo4mmk1wslxq0gdx3q"
        })
    data = response.json()

    return data['g_flag_update_excute_success']
  
  except Exception as error:
    return { "error": error }
  
def release_seat(seat_id):
  try:
    response = requests.get(
      release_seat_url, params = {
        "SeatId": seat_id,
        "UserId": user_id,
        "UserPass": user_pass,
        "DeviceName": "desktop",
        "Kiosk": "false",
      })
    data = response.json()
    return data['l_communication_status']
  except Exception as error:
    return { "error": error }

if __name__ == "__main__":
  # 좌석 번호를 좌석 고유 아이디로 변환
  with open(seat_number_json_path, "r") as file:
    data = json.load(file)
    seat_id = data[seat_number]

  if action_code == '1':
    release = release_seat(seat_id)
    if release == '0':
      print("좌석 취소 성공")
    else:
      print("좌석 취소 실패")

  result = request_seat(seat_id)
  if result:
    print("예약 성공")
  else:
    print("예약 실패")
