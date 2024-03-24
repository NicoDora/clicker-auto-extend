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

seat_number_json_path = "seat_number.json"


def find_available_seat():
  try:
    response = requests.post(get_available_seat_url).json()
    
    target_object = None
    for item in response["_Model_lg_clicker_for_compact_object_list"]:
      if item["l_tooltip"] == "배정가능":
        target_object = item
        break

    if target_object is not None:
      return target_object["l_id"]
    else:
      return { "error": "배정 가능한 좌석이 없습니다." }

  except Exception as error:
    return { "error": error }

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
  
  except Exception as error:
    return { "error": error }

if __name__ == "__main__":
  # 좌석 번호를 좌석 고유 아이디로 변환
  with open(seat_number_json_path, "r") as file:
    data = json.load(file)
    seat_id = data[seat_number]

  if action_code == '0':
    result = request_seat(seat_id)

    if result:
      print("예약 성공")
    else:
      print("예약 실패")

  elif action_code == '1':
    # 선택가능한 좌석 아이디 찾기
    next_seat_id = find_available_seat()
    if not seat_id and "error" in next_seat_id:
      print(next_seat_id)
      exit()

    # 좌석 예약 요청
    request_seat(next_seat_id)
    
    # 원래 좌석으로 이동
    result = request_seat(seat_id)
    if result:
      print("이동 성공")
    else:
      print("이동 실패")
