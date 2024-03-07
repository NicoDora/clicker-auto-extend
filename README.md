# clicker-auto-extend

클리커를 사용하는 도서관에서 무한으로 시간연장 해주는 프로그램

<img width="230" alt="스크린샷 2024-03-04 오후 10 14 44" src="https://github.com/NicoDora/clicker-auto-extend/assets/76510679/12172f43-114c-49f8-9545-b6db2d6c4336">

---

### 들어가기 전에...

본 프로그램은 클리커를 사용하는 도서관에서 무한으로 시간연장 해주는 프로그램입니다.

인덕대학교 도서관 좌석관리시스템 페이지를 기반으로 작성되어 타 학교나 기관 페이지에서는 작동하지 않을 수 있습니다.

작동 원리는 다음과 같습니다.

- http request를 통해 빠르게 남은 자리로 이동하고 다시 본인의 자리로 돌아옵니다.
- 자리 이동을 하면 시간은 초기화되고, 자리 이동에는 횟수 제한이 없어 무한으로 시간연장이 가능합니다.

### 인덕대학교 도서관 1층 좌석 배치도

<img width="1428" alt="스크린샷 2024-03-07 오후 10 12 39" src="https://github.com/NicoDora/clicker-auto-extend/assets/76510679/2c34d22b-e51f-404b-979d-6d773a1eba11">

## 사용방법

1. 먼저 `main.py` 파일을 복사하거나 git pull 명령어를 통해 본인의 로컬에 저장합니다.

2. 파이썬은 알아서 다운받으세요.

3. 필수 라이브러리를 설치합니다.

   ```bash
   pip install selenium
   pip install requests
   ```

4. 코드 내에 인덕대학교 포털시스템 로그인 정보를 입력합니다.

   ![code](https://github.com/NicoDora/clicker-auto-extend/assets/76510679/977527bc-dde2-48e5-af64-e9dbc8087a26)

5. 자리를 예약하고 싶으면 0, 자리를 연장하고 싶으면 1을 입력합니다.
   (action_code 값이 없으면 동작하지 않으니 주의하세요.)

   ![code3](https://github.com/NicoDora/clicker-auto-extend/assets/76510679/a2e803d2-b537-49a2-b6c6-d3195d9fd8c7)

6. 원하는 자리 번호나 현재 자신의 자리 번호를 입력합니다.

   ![code2](https://github.com/NicoDora/clicker-auto-extend/assets/76510679/a5d6aaa6-f245-48ce-8bc9-b13b61a253bb)

7. 코드를 실행하고 약 10초 내에 자리가 예약되거나 연장됩니다.
