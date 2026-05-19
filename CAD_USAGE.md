# ACTF 3D 설계 실행 가이드 (무료)

이 프로젝트는 **CadQuery (무료/오픈소스)** 기반으로 ACTF 개념 3D 모델을 생성합니다.

## 1) 설치
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2) 생성 실행
```bash
python actf_3d_design.py
```

## 3) 결과물
`output/` 폴더에 아래 파일이 생성됩니다.
- `actf_exoskeleton.step`
- `actf_exoskeleton.stl`
- `actf_endoskeleton.step`
- `actf_endoskeleton.stl`
- `actf_full_body.step`

## 4) 권장 무료 뷰어
- FreeCAD (무료)
- CAD Assistant (무료)

STEP 파일을 열어 구조를 확인하고 후처리(치수 정밀화, 세분화 설계)하면 됩니다.
