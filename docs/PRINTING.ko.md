# V18 출력 안내

각각 1개, 배율100%, 저장된 방향 그대로 출력한다.

| 파일 | 용도 | V17에서 재출력 |
|---|---|---|
| `BODY_V18_PRINT.stl` | 본체 / USB-C 기판 가림벽 | 필요 |
| `BOARD_SUPPORT_FRAME_V18_PRINT.stl` | 보드 받침틀 | 기존 부품 재사용 가능 |
| `SCREW_RETAINING_RING_3POINT_V18_PRINT.stl` | 보드 고정 나사 링 | 기존 부품 재사용 가능 |
| `MAGSAFE_OUTER_LID_V18_PRINT.stl` | 바깥 자석 뚜껑 | 기존 부품 재사용 가능 |
| `BATTERY_TRAY_INNER_V18_PRINT.stl` | 높인 배터리 돌기 / 좁힌 가이드 | 필요 |
| `RING_TOOL_3POINT_V18_PRINT.stl` | 조립용 툴 | 기존 부품 재사용 가능 |

재질 PLA, 노즐0.4mm, 레이어0.2mm, 벽4줄 이상을 시작값으로 사용한다. 툴은 넓은 T손잡이 면이 바닥으로 오며 인필40% 정도를 시작값으로 삼는다. 서포트 없이 출력하도록 형상을 잡았으나 실제 브리징 품질은 프린터와 재료에 따라 확인해야 한다.

슬라이서에서 나사산·홈·USB-C 안쪽 창에 의도하지 않은 서포트가 들어가는지 미리 확인한다. 조립 전 나사산과 기둥 머리의 실밥·버를 정리한다. 조임 툴은 손으로 쓰며 전동 공구에 물리지 않는다.

FreeCAD의 반투명 표시와 참고 배터리/자석은 설명용이다. 출력 파일은 `print/V18/`의 6개 STL이다.

## English

Print one of each of the six listed files at 100% scale in the stored orientation. V17 users only need to reprint BODY and BATTERY_TRAY_INNER; the other four shapes are unchanged. Five parts remain in the case; RING_TOOL is a reusable assembly tool.

Start with PLA, 0.4 mm nozzle, 0.2 mm layers and at least four walls. Print the tool with its broad T handle on the bed and start around 40% infill. The tool is designed without supports, but check bridging and unwanted supports in the threads, slots and USB window in your slicer. Remove burrs and stringing before assembly. Tighten by hand; do not use a power tool. Reference batteries, magnets and transparent display settings in FreeCAD are explanatory. Print the six files in print/V18/.
