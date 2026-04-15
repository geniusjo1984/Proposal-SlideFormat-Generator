# Proposal-SlideFormat-Generator

사용자가 제공한 RfP/RFP 문서를 바탕으로 제안서 장표용 작업 폴더, 제어 문서, 과업별 장표 계획을 만드는 Codex skill 저장소입니다.

영문 문서: [README.md](README.md)
변경 이력: [CHANGELOG.md](CHANGELOG.md)
최신 릴리스: [v0.1.0](https://github.com/geniusjo1984/Proposal-SlideFormat-Generator/releases/tag/v0.1.0)

## 구성

- `proposal-slideformat-generator/`
  - `SKILL.md`: skill 트리거 조건과 작업 지침
  - `references/`: `DESIGN.md`, `TASK.md`, `AGENT.md`, 워크플로우 템플릿
  - `scripts/init_project.ps1`: 프로젝트 폴더 초기화 스크립트

## 이 Skill이 하는 일

- 표준 제안서 프로젝트 폴더 구조 생성
- 초기 스캐폴드 후 `RfP`가 없으면 거기서 멈추고 입력을 요청
- 사용자가 기본설계를 요청했을 때 `DESIGN.md`, `TASK.md` 생성
- `02.Reference_Templete`에 레퍼런스가 있으면 그 기준으로 `DESIGN.md` 재구성
- `02.Reference_Templete`가 비어 있거나 사용할 수 없으면 `references/design-template.md`를 즉시 기본 디자인 기준으로 사용
- `DESIGN.md`, `TASK.md` 확정 후에는 사용자 제공 `AGENT.md`를 우선 재사용하고, 없거나 명시적으로 요청한 경우에만 생성
- 슬라이드 생성은 Stitch MCP 또는 Stitch skill을 우선 사용
- Stitch가 없으면 먼저 설치를 권장
- Stitch를 쓰지 않는 fallback 경로에서는 `html` 장표 산출물을 생성
- `TASK.md`를 고정 파일이 아니라 RfP 기반 프로젝트별 산출물로 취급
- 공공 제안서형, 컨설팅형 장표 기획 워크플로우 지원
- 슬라이드 비율을 기본적으로 A4 가로로 고정

## 설치

이 저장소를 clone한 뒤 `proposal-slideformat-generator/` 폴더를 Codex skills 경로에 복사하면 됩니다.

```powershell
git clone https://github.com/geniusjo1984/Proposal-SlideFormat-Generator.git
Copy-Item -Recurse -Force .\Proposal-SlideFormat-Generator\proposal-slideformat-generator $HOME\.codex\skills\
```

GitHub 저장소 설치를 지원하는 Codex skill installer를 사용 중이면, 이 저장소에서 `proposal-slideformat-generator` 폴더를 선택해 설치할 수도 있습니다.

## 사용

프로젝트 상위 폴더를 새로 만들고 그 아래 표준 하위 폴더를 생성:

```powershell
.\proposal-slideformat-generator\scripts\init_project.ps1 -ProjectName client-a-rfp -BasePath .\projects
```

이 단계에서는 폴더만 만들고 `01.Input_RfP`에 `RfP`를 넣으라는 안내 파일만 생성합니다.
그 다음 `02.Reference_Templete`, `03.Reference_Contents_Main`, `04.Reference_Contents_Assistance`에 참고자료를 넣습니다.

그 후 Codex에게 기본설계 요청을 하면 `DESIGN.md`와 `TASK.md`를 생성하도록 쓰면 됩니다.

`DESIGN.md`를 구성할 때 Codex는 시각 레퍼런스를 `02.Reference_Templete`에서만 확인해야 합니다. 이 폴더가 비어 있거나 사용할 수 없으면 다른 폴더를 뒤지지 말고 즉시 `references/design-template.md`를 사용해야 합니다.

`AGENT.md`는 이미 사용자가 제공한 기준 파일이 있으면 기본적으로 그것을 재사용하고, 없거나 사용자가 명시적으로 재생성을 요청한 경우에만 새로 만듭니다.

슬라이드 생성 단계에서는 Codex가 Stitch를 우선 사용하고, Stitch가 없으면 먼저 설치를 권장한 뒤 필요하면 일반 workflow로 진행합니다. 일반 workflow에서는 `DESIGN.md`의 고정 A4 레이아웃 규칙을 따르는 `html` 장표를 생성합니다.

기본 샘플 슬라이드 생성 예시는 아래와 같습니다.

```powershell
python .\proposal-slideformat-generator\scripts\generate_calibration_slide.py --output-dir .\05.Output_Slide --format html
```

## 주의사항

- 고객사 RfP, 내부 템플릿, 저작권 있는 참고자료는 공개 저장소에 올리지 않는 편이 안전합니다.
- 이 저장소에는 재사용 가능한 skill 로직과 템플릿만 유지하는 것이 좋습니다.
- 스크린샷과 고객사별 샘플 자료는 의도적으로 포함하지 않았습니다.
