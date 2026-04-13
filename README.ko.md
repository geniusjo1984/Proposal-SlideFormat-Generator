# Proposal-SlideFormat-Generator

사용자가 제공한 RfP/RFP 문서를 바탕으로 제안서 장표용 작업 폴더, 제어 문서, 과업별 장표 계획을 만드는 Codex skill 저장소입니다.

영문 문서: [README.md](README.md)

## 구성

- `proposal-slideformat-generator/`
  - `SKILL.md`: skill 트리거 조건과 작업 지침
  - `references/`: `DESIGN.md`, `TASK.md`, `AGENT.md`, 워크플로우 템플릿
  - `scripts/init_project.ps1`: 프로젝트 폴더 초기화 스크립트

## 이 Skill이 하는 일

- 표준 제안서 프로젝트 폴더 구조 생성
- 기본 `DESIGN.md`, `TASK.md`, `AGENT.md` 생성
- `TASK.md`를 고정 파일이 아니라 RfP 기반 프로젝트별 산출물로 취급
- 공공 제안서형, 컨설팅형 장표 기획 워크플로우 지원

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

또는 이미 알고 있는 전체 경로에 바로 생성:

```powershell
.\proposal-slideformat-generator\scripts\init_project.ps1 -ProjectRoot .\projects\client-a-rfp
```

`개요.md`가 필요한 경우에만 추가 생성:

```powershell
.\proposal-slideformat-generator\scripts\init_project.ps1 -ProjectRoot .\projects\client-a-rfp -IncludeOverview
```

## 주의사항

- 고객사 RfP, 내부 템플릿, 저작권 있는 참고자료는 공개 저장소에 올리지 않는 편이 안전합니다.
- 이 저장소에는 재사용 가능한 skill 로직과 템플릿만 유지하는 것이 좋습니다.
- 스크린샷과 고객사별 샘플 자료는 의도적으로 포함하지 않았습니다.
