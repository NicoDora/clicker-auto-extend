# clicker-auto-extend

클리커를 사용하는 도서관에서 무한으로 시간연장 해주는 프로그램

<img width="230" alt="스크린샷 2024-03-04 오후 10 14 44" src="https://github.com/NicoDora/clicker-auto-extend/assets/76510679/12172f43-114c-49f8-9545-b6db2d6c4336">

---

### 들어가기 전에...

본 프로그램은 클리커를 사용하는 도서관에서 무한으로 시간연장 해주는 프로그램입니다.

인덕대학교 도서관 좌석관리시스템 페이지를 기반으로 작성되어 타 학교나 기관 페이지에서는 작동하지 않을 수 있습니다.

작동 원리는 다음과 같습니다.

- 예약 페이지에 로그인을 하지 않은 상태로 접속하면, 자리이동이 가능합니다.
- 자리이동을 하면 시간은 초기화되므로 무한으로 시간연장이 가능합니다.

## 사용방법

1. 먼저 `main.py` 파일을 복사하여 본인의 로컬에 저장합니다.

2. 파이썬은 알아서 다운받으세요.

3. 필수 라이브러리를 설치합니다.

   ```bash
   pip install selenium
   ```

4. 코드 내에 인덕대학교 포털시스템 로그인 정보를 입력합니다.
   ![code1](https://github.com/NicoDora/clicker-auto-extend/assets/76510679/b81070e2-a889-458e-b61e-ea5539812903)

5. 현재 내가 이용중인 좌석의 번호를 입력합니다.
   ![code2](https://github.com/NicoDora/clicker-auto-extend/assets/76510679/eb74c705-3f49-4ded-b51c-c95d0841df50)

6. 코드를 실행합니다.
