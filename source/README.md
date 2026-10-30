# 형상 재생성

V18 생성 입력은`cad/V17/brep/`의 기준 형상이다. V17 전체 모델을 다시 설계하는 대신 검증한 기준형상에서V18 본체 가림벽과 배터리 받침판을 생성한다.

FreeCAD Python 환경에서`source/freecad/build_v18.py`를 실행하면`build/V18/`에FreeCAD/BREP/출력STL/검사JSON을 생성한다. 배포된`cad/V18/`와`print/V18/`는 덮어쓰지 않는다.

`source/verify_meshes.py`는Python과trimesh를 사용해배포STL6개를 검사한다. CAD검사는빌드스크립트에서수행하며수밀성·면방향등의메쉬검사와구분한다.

`cad/`의BREP는조립좌표,`print/`의STL은출력방향과바닥Z=0이적용된좌표다. 단위는mm이다. 모듈 제조사 원본CAD를 재생성하는 스크립트는 아니다.
