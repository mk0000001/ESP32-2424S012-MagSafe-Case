# ESP32 원형 디스플레이 케이스 V18 프로젝트 보고서

# ESP32 Round Display Case V18 Project Report

2026년 10월 31일 · 한국어 다음 영어 · 설계와 조립 기록

31 October 2026 · Korean followed by English · Design and assembly record

이 보고서는 ESP32-2424S012 계열 디스플레이, 실측 50×30×5 mm 배터리와 내부 자석 링을 사용하는 PLA 케이스의 V18 설계와 출력·조립 방법을 정리한다. V18은 배터리 흔들림을 줄이고 USB-C 구멍 뒤로 보이던 기판을 가리는 변경이다.

This report documents the V18 PLA enclosure for an ESP32-2424S012 family display, a measured 50×30×5 mm battery and an internal magnetic ring. V18 reduces nominal battery play and shields the PCB previously visible behind the USB-C opening.

케이스 부품 5개와 재사용 조임 툴 1개를 출력한다. V17 사용자는 본체와 안쪽 배터리 받침판만 다시 출력하면 된다. CAD·메시 검사는 통과했지만 V18의 실제 출력 체결력과 내구성은 아직 시험하지 않았다.

Print five enclosure parts and one reusable tightening tool. V17 users only need to reprint the body and inner battery tray. CAD and mesh checks passed; physical V18 fit, fastening force and durability remain untested.


---

## 1 하드웨어와 식별 근거

### 1 Hardware and identification evidence

| 부품 / Item | 수량 / Qty | 확인 정보 / Evidence |
|---|---|---|
| 디스플레이 보드 / Display module | 1 | ESP32-2424S012 계열 / family; PCB HW-791, V0.0.1; ESP32-C3-MINI-1U |
| 리튬폴리머 배터리 / Li-polymer battery | 1 | 사진 라벨 / label: YCJ603048, 3.7 V, 880 mAh; 사용자 실측 / measured: 50×30×5 mm |
| 자석 스티커 / Magnetic ring sticker | 1 | 임시값 / provisional: OD 56, ID 46, t 0.55 mm |
| USB-C 케이블 / USB-C cable | 1 | 외부 부속품, 모델 미제공 / external accessory; model unspecified |
| 자석 접착층 / Magnet adhesive | 1식 / set | 스티커 자체 접착층 / sticker adhesive; 두꺼운 추가 테이프 미포함 / no extra thick tape allowance |

공급 모듈 자료의 주요 사양은 1.28인치 IPS 240×240, GC9A01, ESP32-C3 160 MHz, 4 MB Flash다. USB-C, 배터리 충방전 회로, BAT 커넥터, BOOT·RST·KEY1과 확장 커넥터는 보드에 포함된다. 사진에 IP5306 전원 IC와 외장 안테나 커넥터가 보이지만 별도 안테나 포함 여부는 미확인이다.

The supplied module documentation specifies a 1.28-inch 240×240 IPS display, GC9A01 controller, ESP32-C3 at 160 MHz and 4 MB Flash. USB-C, battery power circuitry, BAT socket, BOOT/RST/KEY1 and expansion connectors are integrated. The photos show an IP5306 power IC and an external antenna connector; inclusion of a separate antenna is unconfirmed.

사용자 상품은 정전식 터치형으로 제시됐지만 실물 PCB의 정확한 N/C 접미 SKU는 확인되지 않았다. 배터리의 Coms UB917은 모델 코드·전압·용량이 같은 유통 후보이며 구매 SKU로 확정한 것은 아니다. 공식 판매 자료는 30×50×6 mm로 적혀 있어, 5 mm 기준 케이스에 6 mm 제품이 맞는다고 보장하지 않는다.

The user supplied a capacitive-touch product reference, but the exact N/C SKU suffix is not confirmed on the PCB. Coms UB917 is a matching battery distribution candidate, not a confirmed purchase SKU. Its official listing states 30×50×6 mm; this enclosure is based on the user’s 5 mm measurement and does not establish compatibility with a 6 mm replacement.

흰색 배터리 2핀 커넥터의 정확한 시리즈·피치·극성은 사진만으로 확정하지 않았다. 자석 치수도 실측 전 임시값이다. 모듈 원본 자료와 사용자 사진을 hardware 폴더에 함께 보관했다.

The exact series, pitch and polarity of the white two-pin battery connector were not established from photographs. Magnet dimensions are provisional pending measurement. Original module documents and user photographs are archived in hardware/.


---

## 2 구조와 설계 기준

### 2 Structure and design basis

초기 일체형 PLA 걸쇠의 파손과 얕은 결합 문제를 반영해, 보드 받침틀과 나사 링이 보드를 고정하도록 구성했다. 받침틀은 넓은 지지면과 깊어진 키 결합으로 본체에 앉고, 링은 툴로 조인 뒤 그대로 남는다. 금속 나사·너트·인서트는 추가하지 않는다.

After failures of the early integral PLA clips and shallow engagement, the design uses a separate support frame and threaded ring to retain the board. Broad frame seats and deeper keyed engagement locate it in the body. The ring stays installed after the tool is removed. No metal screws, nuts or inserts are added.

| 항목 / Parameter | 현재 설계값 / Current design |
|---|---|
| 전체 플라스틱 외형 / Plastic envelope | 외경 / OD 65.30 mm; 높이 / height 26.85 mm |
| 화면과 PCB 스택 / Screen-to-PCB stack | 사용자 4 mm 자연 상태, 3 mm 눌림 / user: 4 mm relaxed, 3 mm pressed; 설계 포획 높이 / capture 3.7 mm |
| 받침틀 결합 / Frame engagement | 지지 어깨 / seat width 8 mm; 본체 키 / key height 2.2 mm; 홈 깊이 / slot depth 2.4 mm |
| 나사 링과 툴 / Threaded ring and tool | 피치 / pitch 3.2 mm; 손잡이 3개와 툴 접점 3개 / three grips and three tool contacts |
| 뚜껑 잠금 / Lid locks | 안쪽 판 / inner tray 10°; 뚜껑 전체 / complete lid 20°; 각 지정 시점 기준 / from specified viewing sides |

안쪽 받침판은 머리 있는 기둥 2개와 큰 진입 구멍을 쓰는 회전 잠금이다. 바깥 뚜껑은 3개 돌기로 본체와 맞물리며, 한 돌기를 넓게 해 조립 방향을 구분한다. 재료 탄성에 의존하는 얇은 스냅 다리 대신 회전해서 걸어 잠근다.

The inner tray uses two headed posts and large entry holes for rotational capture. Three lugs lock the outer lid to the body, with one wider lug defining its orientation. These locks engage by rotation rather than relying on thin flexible snap legs.


---

## 3 V18 변경과 배터리 자석 공간

### 3 V18 changes and battery and magnet space

| 항목 / Item | V17 | V18 |
|---|---|---|
| 배터리 받침 높이 / Pad height above floor | 0.5 mm | 1.0 mm |
| 가이드 내측 / Guide interior | 51×31 mm | 50.6×30.6 mm |
| 가이드 전체 높이 / Total guide height | 1.9 mm | 3.2 mm |
| 배터리 수직 이동 여유 / Vertical free travel | 0.8 mm | 0.3 mm |
| USB-C 가림벽 / PCB sight shield | 없음 / none | 두께 / thickness 1.2 mm |
| USB-C 통과 창 / Socket window | 큰 내부 개구 / large internal opening | 10.6×5.2 mm |

배터리 받침 4곳과 중앙의 넓은 접촉부를 높여 들썩임을 줄였다. 50×30 mm 배터리의 좌우 여유는 각 0.3 mm이고, 5 mm 두께 기준 위아래 이동 여유도 0.3 mm다. 설계상 배터리를 압축해 고정하지 않는다.

Four battery supports and a broad centre contact are raised to reduce rocking. A nominal 50×30 mm battery has 0.3 mm lateral clearance per side, with 0.3 mm vertical travel for a 5 mm thickness. Retention does not rely on nominal battery compression.

자석은 바깥 뚜껑 안쪽의 얇은 원형 홈에 들어가며, 외부 플라스틱 표면은 0.6 mm 두께로 이어진다. 홈은 외경 57.2 mm, 내경 44 mm, 깊이 약 0.667 mm다. 자석 스티커는 안쪽 받침판 아래에 붙여 흡착 면이 바깥 뚜껑을 향하게 한다. 실제 자석 치수와 접착·흡착력 확인은 남아 있다.

The magnet fits into a shallow annular recess inside the outer lid, behind a continuous 0.6 mm outer plastic skin. The recess is 57.2 mm OD, 44 mm ID and approximately 0.667 mm deep. Bond the sticker under the inner tray with its active face toward the outer lid. Actual magnet fit, adhesion and holding force remain to be checked.


---

## 4 USB 포트와 출력 목록

### 4 USB port and print list

이전에 맞춘 17×10.7 mm 케이블 머리 공간과 삽입 깊이는 유지했다. 뒤쪽 통과 창만 좁혀 기판이 보이는 영역을 줄였으며, 아래쪽은 링과 0.4 mm CAD 간격을 남겼다. 방수·방진 구조로 검증한 것은 아니다.

The previously fitted 17×10.7 mm cable-head recess and insertion depth are retained. A smaller rear window reduces PCB visibility, while the lower edge keeps 0.4 mm CAD clearance to the ring. This is not a validated water or dust seal.

| 출력 파일 / Print filename | 수량 / Qty | V17 재사용 / V17 reuse |
|---|---|---|
| BODY_V18_PRINT.stl | 1 | 재출력 / reprint |
| BOARD_SUPPORT_FRAME_V18_PRINT.stl | 1 | 가능 / yes |
| SCREW_RETAINING_RING_3POINT_V18_PRINT.stl | 1 | 가능 / yes |
| MAGSAFE_OUTER_LID_V18_PRINT.stl | 1 | 가능 / yes |
| BATTERY_TRAY_INNER_V18_PRINT.stl | 1 | 재출력 / reprint |
| RING_TOOL_3POINT_V18_PRINT.stl | 1 | 가능 / yes |

6개 파일을 각각 1개씩, 100% 배율과 저장된 방향으로 출력한다. 시작 설정은 PLA, 노즐 0.4 mm, 레이어 0.2 mm, 벽 4줄 이상이다. 툴은 넓은 T 손잡이를 바닥에 두고 인필 약 40%를 시작값으로 쓴다.

Print one of each of the six files at 100% scale in the stored orientation. Suggested starting settings are PLA, 0.4 mm nozzle, 0.2 mm layers and at least four walls. Place the broad T handle of the tool on the bed; start at about 40% infill for the tool.

툴은 서포트 없이 출력하도록 설계했으나 실제 브리징은 슬라이서에서 확인한다. 나사산과 홈의 실밥·버를 정리한 뒤 손으로 조립한다. 전동 공구로 툴을 돌리지 않는다.

The tool is designed for support-free printing; inspect the actual bridging in the slicer. Remove stringing and burrs from threads and slots before hand assembly. Do not drive the tool with a power tool.


---

## 5 보드 조립

### 5 Board assembly

### 1 본체에 보드 넣기

1 Seat the display module

화면을 아래, 노란 PCB를 위로 놓고 USB-C를 본체 충전 구멍에 맞춰 앉힌다.

Place the screen face down with the yellow PCB facing up. Align the USB-C socket with the opening in the body.

### 2 보드 받침틀 넣기

2 Fit the board support frame

BOARD_SUPPORT_FRAME의 깊은 홈 3개를 본체 돌기 3개에 맞춰 끝까지 내려 앉힌다.

Align the three deep slots in BOARD_SUPPORT_FRAME with the three body keys and lower the frame onto its seats.

### 3 나사 링으로 보드 고정

3 Secure the board with the threaded ring

링을 손으로 먼저 나사산에 맞춘다. 툴 돌기 3개를 링 홈에 끼우고 기기 뒤에서 보아 시계 방향으로 손으로 조인다. 닿아 멈추면 그만 조이고 툴을 빼낸다.

Start the ring on the thread by hand. Engage the three tool pegs and turn clockwise when viewed from the rear of the device. Stop when seated and remove the tool.

툴은 배터리를 넣기 전에 사용하고 바로 빼낸다. 기판 위 부품을 눌러 링을 억지로 조이지 않는다. 링 조임의 실제 토크나 체결력은 아직 측정하지 않았다.

Use and remove the tool before fitting the battery. Do not force the ring by pressing components on the PCB. Actual tightening torque and retention force have not been measured.


---

## 6 자석과 배터리 조립

### 6 Magnet and battery assembly

### 4 자석 스티커 붙이기

4 Attach the magnet sticker

실제 자석이 홈에 들어가는지 먼저 확인한다. 안쪽 배터리 받침판 아래쪽에 붙이고, 흡착 면이 바깥 뚜껑을 향하도록 한다.

Check that the actual magnet fits the recess before bonding it to the underside of the inner battery tray, with its active face toward the outer lid.

### 5 안쪽 배터리 받침판 잠그기

5 Lock the inner battery tray

분리한 바깥 뚜껑의 안쪽을 위로 놓는다. 큰 구멍 2개로 기둥 머리를 통과시킨 다음, 뚜껑 안쪽에서 보아 시계 방향 10도로 돌려 좁은 곡선 홈에 건다. 눌러 끼우는 스냅 구조가 아니다.

Place the detached outer lid with its inside facing up. Pass the two post heads through the large holes, then rotate the tray clockwise by 10 degrees when looking into the lid. The heads capture the narrow curved slots; this is a bayonet, not a press-fit snap.

### 6 배터리 넣고 연결

6 Fit and connect the battery

50×30×5 mm 배터리를 가이드 안에 놓고 보드 배터리 커넥터에 연결한다. 전선을 안쪽으로 정리해 테두리와 잠금 홈에 끼이지 않게 한다. 배터리를 눌러 찌그러뜨리며 닫지 않는다.

Place the 50×30×5 mm battery inside the guide and connect it to the board. Route the leads inward, clear of the rim and locking tracks. Do not close the case by compressing the battery.


---

## 7 뚜껑 잠금과 분해

### 7 Lid locking and disassembly

### 7 뚜껑 전체 잠그기

7 Lock the complete lid

넓은 돌기 1개를 본체의 넓은 진입 홈에 맞춰 넣는다. 기기 뒤에서 보아 시계 방향 20도로 멈추는 곳까지 돌린다.

Align the one wider lid lug with the wider entry in the body. Turn the complete lid clockwise by 20 degrees when viewed from the rear of the device, up to the stop.

분해할 때 뚜껑 전체는 기기 뒤에서 보아 반시계 방향 20도로 연다. 안쪽 받침판은 분리한 뚜껑 안쪽에서 보아 반시계 방향 10도로 푼다. 두 동작은 서로 반대 면을 보는 설명이므로 같은 시점으로 섞어 읽지 않는다.

For disassembly, turn the complete lid counterclockwise by 20 degrees as viewed from the device rear. Turn the inner tray counterclockwise by 10 degrees as viewed into the detached lid. These instructions use opposite viewing sides; do not interpret both from one viewpoint.

보드 링을 풀기 전에는 뚜껑과 배터리를 분리하고 배터리 커넥터를 뽑는다. 영상은 실제 케이스 CAD의 이동과 회전을 사용하지만, 전자부품·배터리·자석은 설명용 외형이다. 커넥터 결합 동작 자체는 자막으로 안내한다.

Before loosening the board ring, remove the lid and battery and disconnect the battery plug. The animation moves and rotates native case CAD, while electronics, battery and magnet are explanatory envelopes. Connector mating itself is described in captions.


---

## 8 검증 결과와 남은 확인

### 8 Verification results and remaining checks

| 검사 / Check | 결과 / Result |
|---|---|
| STL 6개 / Six print meshes | 수밀, 면 방향 일관, 양의 체적, 단일 연결체 / watertight, consistent winding, positive volume, one connected solid; print Z minimum 0 |
| 설치 부품 5개 / Five installed parts | 쌍별 CAD 겹침 체적 0 / zero pairwise CAD overlap volume |
| USB-C 케이블 / USB-C cable | 머리 15×8 mm 등 가정 외형의 27개 삽입 자세: 겹침 0 / 27 insertion poses of the assumed cable envelope: no overlap |
| 조립 운동 / Assembly motion | 링·툴, 받침판, 뚜껑 회전과 삽입 경로 확인 / checked ring/tool, inner tray and lid insertion and rotation |
| 재생성 / Rebuild | 6개 CAD의 대칭 차 체적 0 / zero CAD symmetric-difference volume for all six parts |
| 애니메이션 / Animation | 한국어→영어 자막, MP4 전체 디코딩 성공 / Korean then English captions; full MP4 decode passed |

위 결과는 형상과 가정 치수의 CAD 검사다. 본체 STL의 재생성 시 삼각형 순서가 달라질 수 있어 바이트 일치와 CAD 형상 일치를 구분했다. 원본 검증 JSON은 validation/V18에 보관한다.

These are geometric checks using assumed nominal envelopes. Regenerated body STL triangles may be ordered differently, so byte identity is distinguished from CAD geometry equivalence. Detailed verification JSON files are retained in validation/V18/.

다음 실물 확인은 V18 출력 후 수행해야 한다. 배터리 흔들림과 무압축 폐쇄, 케이블 완전 삽입, 나사 링의 손 조임과 반복 탈착, 뚜껑 잠금과 전선 끼임, 실제 자석 치수·접착력·흡착력을 확인한다. 프린터 수축·브리징·PLA 층간 강도에 따른 조정 가능성이 남아 있다.

After printing V18, check battery play and closure without compression, full cable insertion, hand tightening and repeated removal of the ring, lid locking and wire clearance, and actual magnet dimensions, adhesion and holding force. Printer shrinkage, bridging and PLA layer strength may require further adjustment.

이전 출력물 사진은 부품 식별과 문제 피드백 자료다. V18 실물 통과 증거로 제시하지 않는다. 자석의 임시 치수와 배터리 판매자 6 mm 표기는 향후 치수 확정 시 다시 반영할 항목이다.

Photographs of earlier prints serve as hardware identification and issue feedback, not evidence of successful physical V18 testing. Provisional magnet dimensions and the supplier’s 6 mm battery specification need review when actual dimensions are confirmed.


---

## 9 파일 안내와 참고 자료

### 9 File guide and references

| 경로 / Path | 내용 / Contents |
|---|---|
| print/V18/ | 출력 STL 6개 / six print STL files |
| cad/V18/ | FreeCAD 원본과 BREP / native FreeCAD and BREP |
| media/V18/ | 한영 자막 MP4·GIF·SRT와 그림 / Korean-English MP4, GIF, SRT and figures |
| reports/V18/ | 이 보고서 PDF와 수정용 Markdown / this PDF report and editable Markdown |
| hardware/ | 부품표·모듈 원문·하드웨어 사진 / BOM, original module documentation and hardware photos |
| source/ 및 validation/ | 재생성 스크립트와 검사 기록 / rebuild scripts and verification records |

GitHub V18 릴리스에는 기존 출력·CAD 묶음과 모듈 원본 ZIP을 보존하고, 보고서와 한영 애니메이션을 포함하는 최신 묶음을 추가한다. NAS에도 같은 파일을 복사하고 SHA-256으로 일치를 확인한다. 원문 자료와 제품 사진의 권리는 각 권리자에게 있다.

The GitHub V18 release retains the earlier print/CAD package and original module ZIP and adds an updated bundle containing this report and the bilingual animation. Identical files are copied to NAS and compared using SHA-256. Original documents and product photographs remain the property of their respective rights holders.

- 프로젝트와 V18 릴리스 / Project and V18 release: https://github.com/mk0000001/ESP32-2424S012-MagSafe-Case/releases/tag/v18

- GUITION 공식 모듈 제품 / Official GUITION module page: https://www.guition.com/esp32-display-module/1-28-inch-esp32-display-module

- Coms 공식 배터리 목록 / Official Coms battery listing: https://www.comsmart.co.kr/cmart/shop/list.php?ca_id=f04070

- Coms UB917 공식 상세 이미지 / Official UB917 detail image: https://comsmart.co.kr/productnew/sub21/UB917.jpg

- 공급 사양서 / Supplied specification: hardware/ESP32-2424S012/vendor/2-Specification/ESP32-2424S012 Specifications-EN.pdf

- 사용자 보드와 배터리 사진 / User board and battery photos: hardware/ESP32-2424S012/photos/ and hardware/battery/photos/

- 자석 임시 치수의 판매 예시 / Seller example for provisional magnet dimensions: https://blueboltchargers.de/products/magsafe-magnetring-fur-iphone-und-android

자료 정리일은 2026년 10월 30일, 보고서 작성일은 10월 31일이다. 공급 자료에 전체 모듈 STEP/STP는 없으며, 전자부품 CAD는 설명용이다.

Sources compiled 30 October 2026; report prepared 31 October. The archive contains no full-module STEP/STP. Electronics CAD is explanatory.
