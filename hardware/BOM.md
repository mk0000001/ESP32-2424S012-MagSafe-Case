# 사용 하드웨어 전체 목록

실물 라벨, 사용자 실측, 제조사 원문, 미확인 항목을 구분했다. 수량은 케이스1대 기준이다.

## 전자부품과 자석

| ID | 부품 | 수량 | 확인 내용 | 근거/상태 |
|---|---|---:|---|---|
| HW-01 | ESP32-2424S012 원형 LCD 보드 | 1 | 1.28인치,240×240 IPS,GC9A01,ESP32-C3-MINI-1U,USB-C,배터리 충전 인터페이스 | 사용자 보드 사진·공급 자료. PCB표기`HW-791`,`V0.0.1` |
| HW-02 | YCJ 603048 리튬폴리머 배터리 | 1 | 라벨3.7V/880mAh. 케이스 설계 실측50×30×5mm | 사용자 사진·실측. [모델 조사](battery/YCJ-603048.md) |
| HW-03 | 맥세이프 자석 링 스티커 | 1 | 임시 외경56/내경46/두께0.55mm | 사용자가 일반 제품 구매, 실측 미완료. 홈은외경57.2/내경44/높이약0.667mm |
| HW-04 | USB-C 충전 케이블 | 1 | 외부 연결용. CAD 시험 머리15×8mm,금속부 길이6.11mm | 케이블 모델 미제공. 실제 삽입은 사용자 확인 대상 |
| HW-05 | 자석용 접착층 | 1식 | 스티커 자체 접착층 사용 | 별도 접착제/두꺼운 양면테이프 치수는 설계에 포함하지 않음 |

배터리 전선과 흰색2핀 커넥터는 HW-02에 부착된 것을 사용한다. 커넥터 피치·정확한 시리즈·극성은 사진만으로 확정하지 않았다. 'JST 호환'이라는 이유만으로 다른 배터리의 결선을 같다고 보지 않는다.

## 보드에 이미 포함된 하드웨어

다음은 HW-01 내부 구성으로, 별도 수량을 더해 구매하는 부품이 아니다.

- ESP32-C3-MINI-1U 모듈. 제조사 사양서 기준160MHz/4MB Flash/400KB SRAM.
- GC9A01 구동1.28인치240×240 IPS LCD와 백라이트.
- 사용자 제공 상품명은 정전식 터치형. 원문 자료에는N(비터치)/C(정전식) 변형이 함께 있으며, 실물 PCB에는 계열명이 표시되어 있다.
- USB-C 소켓, 리튬 배터리 충방전 회로, BAT2핀 커넥터, 디버그/확장 커넥터,BOOT·RST·KEY1 버튼.
- 사진에서IP5306 표기가 보이는 전원 IC. 정확한 보드 실장 변경은 [공급 회로도](ESP32-2424S012/vendor/5-Schematic/)와 실물을 함께 기준으로 본다.
- ESP32-C3-MINI-1U 외장 안테나 커넥터가 보인다. 별도 안테나의 실제 장착/포함 여부는 사진으로 확인되지 않았다.

## 출력 부품

| ID | 파일 | 수량 | 분류 |
|---|---|---:|---|
| P-01 | `BODY_V18_PRINT.stl` | 1 | 케이스 |
| P-02 | `BOARD_SUPPORT_FRAME_V18_PRINT.stl` | 1 | 케이스 |
| P-03 | `SCREW_RETAINING_RING_3POINT_V18_PRINT.stl` | 1 | 케이스 |
| P-04 | `MAGSAFE_OUTER_LID_V18_PRINT.stl` | 1 | 케이스 |
| P-05 | `BATTERY_TRAY_INNER_V18_PRINT.stl` | 1 | 케이스 |
| T-01 | `RING_TOOL_3POINT_V18_PRINT.stl` | 1 | 재사용 조립 도구 |

현재 케이스 조립에는 금속 나사·너트·인서트·별도 일체형 스냅 걸쇠를 추가하지 않는다.

## 원문 자료

- [사용자가 제공한 모듈 자료와 사진](ESP32-2424S012/README.md)
- [GUITION 모듈 공식 제품](https://www.guition.com/esp32-display-module/1-28-inch-esp32-display-module)
- [GUITION 공식 사양서](https://www.guition.com/ku/icms/upload/fb081940d6fc11f09850077a33e1404f/FTPData/UEditor/file/2026121/1768961091229/ESP32-2424S012%20Specifications-EN.pdf)
- [Coms 공식 배터리 목록: UB917](https://www.comsmart.co.kr/cmart/shop/list.php?ca_id=f04070)
- [Coms UB917 공식 상세 이미지](https://comsmart.co.kr/productnew/sub21/UB917.jpg)
- [임시 자석 치수의 판매자 예시](https://blueboltchargers.de/products/magsafe-magnetring-fur-iphone-und-android)

조회/정리일:2026-10-30. 가격과 재고는 부품표에 고정하지 않았다.
