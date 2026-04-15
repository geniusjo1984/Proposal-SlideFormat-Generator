# TASK.md Template

Use this template to derive a project-specific `TASK.md` from the user's RfP. This file must be much more concrete than a simple outline. It should contain enough instruction that an agent can generate proposal slides without reinterpreting the task structure from scratch.

## Required Principles

- Build `TASK.md` only after confirming that the actual RfP is present in `01.Input_RfP`.
- Build `TASK.md` together with `DESIGN.md` during the baseline-design request.
- Preserve the source section hierarchy unless the user explicitly requests another structure.
- Preserve task-level bullets that the slide set must reflect.
- Keep titles, lead messages, and deliverable logic traceable to the RfP.
- Assume final slide output is `.html` unless the user explicitly requests another native slide format.
- Use `03.Reference_Contents_Main` and `04.Reference_Contents_Assistance` selectively for slide-shaping hints, not for unsupported factual invention.
- Treat this file as the slide-planning authority for the workspace.

## Template

```md
# TASK.md

## 과업 정리

아래 내용은 `[local RfP path]`의 `[governing section name]`을 기준으로 정리한 것이다.

슬라이드 구성안은 아래 자료를 우선 반영하여 작성한다.

- 메인 참고자료: `[03.Reference_Contents_Main에서 우선 반영할 자료]`
- 보조 참고자료: `[04.Reference_Contents_Assistance에서 보조 반영할 자료]`

작성 원칙은 다음과 같다.

- 과업별 `1장 1메시지` 원칙을 기본으로 한다
- 다만 `전체 과업 프레임워크`와 같은 상위 논리 장표는 별도 공통 장표로 둔다
- 과업명은 원문 구조를 보존하되, 슬라이드 제목은 제안서형 리드 메시지로 재구성할 수 있다
- 과업별 필수 하위 항목은 장표 본문에서 누락하지 않는다
- 제목은 가능한 한 `1줄`로 설계한다
- 리드 메시지는 검정 텍스트 기준으로 짧고 명확하게 작성한다
- 본문은 `DESIGN.md`의 고정 존 계약을 넘기지 않도록 장표 밀도를 제어한다
- 푸터 영역은 페이지 번호만 사용한다

## 전체 과업 프레임워크

### 1. 제안서 전체 논리 구조

- 프레임워크명: `[예: 진단 → 분석 → 설계 → 실증 → 사업화 → 정책 고도화]`
- 전체 논리 요약: `[개별 과업이 어떤 연속 체계로 연결되는지 2~3줄]`
- 제안서 설계 원칙: `[예: 각 과업은 독립 장표로 풀되, 전체 흐름은 하나의 운영체계로 읽히도록 설계]`

`Stage 1. [section title]`

- 의미: `[이 단계가 수행하는 역할]`
- 해당 과업: `[과업명 1]`, `[과업명 2]`, `[과업명 3]`

`Stage 2. [section title]`

- 의미: `[이 단계가 수행하는 역할]`
- 해당 과업: `[과업명]`

`Stage 3. [section title]`

- 의미: `[이 단계가 수행하는 역할]`
- 해당 과업: `[과업명]`

반복하여 모든 상위 단계 정리

### 2. 전체 과업 프레임워크 장표 구성안

- 슬라이드 제목: `[전체 과업 프레임워크]`
- 리드 메시지: `[과업 전체를 관통하는 핵심 제안 메시지 1문장]`
- 권장 레이아웃: `[상단/본문/하단 비율과 주요 도식 형식]`
- 상단 자산: `상단바.svg`

본문 구성 예시는 아래 형식으로 정리한다.

- Block 1. `[Stage 또는 섹션명]`
  - `[핵심 과업/하위 메시지]`
  - `[핵심 과업/하위 메시지]`
- Block 2. `[Stage 또는 섹션명]`
  - `[핵심 과업/하위 메시지]`

하단 산출물 라인도 필요 시 함께 정리한다.

- `[Stage 1]`
  - `[주요 산출물]`
  - `[주요 산출물]`
- `[Stage 2]`
  - `[주요 산출물]`

### 3. 공통 장표 템플릿

모든 과업 장표는 아래 공통 템플릿을 기본으로 사용한다.

- 상단: 대분류 캡 + 메시지형 제목 + 리드 메시지
- 좌상단: 과업 목적 또는 문제 정의
- 우상단: 분석 대상 또는 적용 범위
- 본문 중앙: 핵심 프레임워크, 프로세스, 표, 매트릭스, 로드맵 중 가장 적합한 형식
- 하단 좌측: 수행 방법 또는 검토 기준
- 하단 우측: 기대 산출물 또는 의사결정 포인트
- 하단 푸터: 페이지 번호만 배치

### 4. Stitch 입력 공통 지침

- 장표당 하나의 핵심 도식만 배치
- 문단보다 블록 중심으로 구성
- 블록명은 1~3단어의 짧은 라벨 우선
- 표는 가급적 열 `5`개 이내, 행 `6`개 이내에서 시작
- 흐름도는 기본적으로 좌→우 구조
- 도식의 각 블록은 `목적`, `대상`, `기준`, `결과`, `산출물` 중 하나의 역할을 가져야 함
- 첫 번째 내용 장표에서 확정한 스타일을 이후 장표에 반복 적용
- 표 셀은 기본적으로 상하 가운데 정렬
- 단계형/프로세스형 도형은 지정 색상군 안에서 진한 색 → 연한 색의 순서로 단계감을 줌
- 중요한 포인트 라벨은 색상 채움 + 흰색 글씨 칩/헤더탭으로 처리

## 과업별 슬라이드 상세 구성

아래 과업별 내용은 단순 메모가 아니라, Stitch 또는 수동 장표 작성 시 거의 그대로 옮겨 적을 수 있는 수준의 상세 작성 지시를 목표로 한다.

### 과업 1. [RfP task name]

- 대분류: `[상위 섹션명]`
- 상위 문맥 제목: `[예: 1. 물품∙유통 구조 파악 I (1) 계획서 검토]`
- Source section: `[RfP section id and title]`
- 권장 산출물 형식: `[검토 프레임 | 체크리스트 | 프로세스 | 매트릭스 | 로드맵 등]`
- 상단 자산: `상단바.svg`
- 예시 수준: `[실제 제안서 수준의 무엇을 보여줄지]`
- 용어 통일어: `[이 과업에서 반복 사용할 표준 표현 3~5개]`
- 세부 범위:
  - `[RfP 원문 범위 1]`
  - `[RfP 원문 범위 2]`
- 슬라이드 제목: `[메시지형 제목 또는 원문 제목]`
- 리드 메시지: `[이 장표가 직접 주장해야 하는 한 문장]`
- 권장 레이아웃: `[예: 상단 요약 박스 + 중앙 3열 프레임 + 하단 프로세스]`
- 고정 존 주의사항: `[제목 1줄 유지 | 리드 1~2줄 | 본문 body zone 내 수용 | 푸터는 페이지 번호만]`
- top-band 사용 원칙: `사용자가 제공한 상단바.svg를 그대로 사용하고 형상을 재작성하지 않음`

장표에서 답해야 할 핵심 질문:

- `[이 과업에서 반드시 답해야 할 질문 1]`
- `[질문 2]`
- `[질문 3]`

Block 구성:

- Block 1. `[블록명]`
  - `[핵심 요소]`
  - `[핵심 요소]`
- Block 2. `[블록명]`
  - `[핵심 요소]`
  - `[핵심 요소]`
- Block 3. `[블록명]`
  - `[핵심 요소]`

본문에 반드시 들어갈 세부 내용:

- `[반드시 들어가야 할 판단 기준 또는 항목]`
- `[반드시 들어가야 할 범주 구분]`
- `[반드시 들어가야 할 실행/분석 포인트]`
- `[반드시 드러내야 할 차이 또는 비교 축]`

원문에서 반드시 보존할 항목:

- `[RfP bullet 1]`
- `[RfP bullet 2]`
- `[RfP bullet 3]`

장표 문장 구조 예시:

- 상단 메시지: `[짧은 제안서형 문장 예시]`
- 보조 설명문: `[표/도식 옆에 붙일 짧은 설명문 예시]`
- 하단 결론문: `[장표를 닫는 한 문장 예시]`

참고 포인트:

- `[03.Reference_Contents_Main 내 참고 자료와 활용 포인트]`
- `[04.Reference_Contents_Assistance 내 참고 자료와 활용 포인트]`

시각화 포인트:

- `[도식에서 무엇을 가장 크게 보여줄지]`
- `[색상/강조/캡션 처리 방식]`
- `[상단바 자산 사용 여부와 대분류 캡 표기 방식]`

Stitch 입력 키워드:

- `[keyword 1]`
- `[keyword 2]`
- `[keyword 3]`

기대 산출물:

- `[장표 결과로 읽혀야 할 산출물 또는 의사결정 포인트]`

검증 포인트:

- `[이 장표가 과업 요구를 충족하는지 점검할 기준 1]`
- `[기준 2]`

### 과업 2. [RfP task name]

위와 동일한 구조를 반복하되, 과업 특성에 맞게 질문, 블록, 필수 항목, 참고 포인트를 구체적으로 채운다.

### 과업 3. [RfP task name]

동일 구조 반복

모든 과업이 끝날 때까지 같은 형식을 유지한다.
```

## Practical Rule

Do not pre-fill all tasks with invented content. Duplicate the task block and populate it only from the actual RfP, required source bullets, and verified reference materials.
