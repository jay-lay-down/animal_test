# animal_test
간단한 심리 테스트 만들기 + Gradio & Gabia로 Web 페이지 UI 구현하기

# 🐾 나만의 테스트 만들기 – 동물 유형 테스트 프로젝트

메타인지 + 상황 판단력을 기반으로, 실제 사회생활 속 패턴을 11가지 "사회적 동물" 타입으로 나누는 재미용 웹 테스트입니다.

"나는 눈치가 빠르다고 생각하는데, 왜 사람 관계는 항상 꼬일까?" 같은 고민을 데이터·알고리즘으로 풀어본 개인 프로젝트입니다.

## 🔗 Demo & Links

- 🧪 **테스트 바로가기**: https://myanimaltest.site/
- 🤗 **Hugging Face Space**: https://huggingface.co/spaces/Jay1121/animal_test
- 📝 **상세 설명 (Velog)**: https://velog.io/@jaylaydown/%EB%82%98%EB%A7%8C%EC%9D%98-%EC%8B%AC%EB%A6%AC-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0-%EB%8F%99%EB%AC%BC-%EC%9C%A0%ED%98%95-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8

> **(Privacy)** 성별 / 연령대 / 문항 응답 외의 개인정보는 저장하지 않습니다.

## 📚 Table of Contents

1. 프로젝트 개요
2. 이론적 배경: 메타인지 vs 상황 판단력
3. 측정 설계 & 점수 구조
4. 타입 분류 로직
5. Tech Stack & 아키텍처
6. UI 구조
7. CSS 커스터마이징 & 동적 HTML
8. 배포: Hugging Face + 가비아 도메인
9. 사용 팁
10. 향후 개선 방향 (Roadmap)
11. 참고 문헌

---

## 🎯 프로젝트 개요

### 문제의식

- 학교에서는 정답/채점 기준이 분명해서, 내 실력이 어느 정도인지 파악하기 쉽다.
- 회사·사회생활에서는:
  - 평가 기준이 상대적 + 주관적
  - 같은 행동도 맥락에 따라 완전히 다르게 해석
  - 정답을 알려주는 사람도 없음

이때 자주 보이는 패턴:
- "나는 분명 눈치가 빠르다고 생각하는데, 왜 주변 사람들은 나에게 자주 화를 낼까?"
- "상황을 잘 읽는 건지, 과하게 해석하는 건지 모르겠어…"
- "왜 나만 이렇게 힘들지? 다른 사람들이 다 이상한 거야."

여기서 핵심 문제는 **'능력' 부족이 아니라**, **(1) 메타인지**와 **(2) 상황 판단력**의 조합이 아닐까? 라는 질문에서 프로젝트가 출발했다.

---

## 💡 이론적 배경: 메타인지 vs 상황 판단력

### 개념 정리

| 구분 | 🧠 메타인지 (Metacognition) | 👥 상황 판단력 (Social Intelligence) |
|------|------------------------------|--------------------------------------|
| **📚 학술적 정의** | "자신의 인지 과정에 대한 인지" (Flavell, 1979) | "타인을 이해하고 관리하며 대인 관계에서 현명하게 행동하는 능력" (Thorndike, 1920) |
| **💡 쉬운 정의** | - 자신의 사고 과정을 모니터링/조절하는 능력<br>- 자신이 타인에게 어떻게 보이는지 아는 것<br>- 자신의 강·약점을 아는 것<br>- 자신이 무엇을 모르는지 아는 것 | - 타인의 내면 상태를 감지하고, 복잡한 사회적 상황을 읽는 능력<br>- 지금 이 상황이 어떤 상황인지 읽는 것<br>- 상대의 진짜 의도와 타이밍, 맥락 이해 |
| **🎯 초점** | 자기 자신 | 외부 상황과 타인 |
| **❓ 핵심 질문** | "나는 어떤 사람인가?"<br>"나는 무엇을 알고/모르는가?" | "지금 무슨 일이 일어나고 있는가?"<br>"상대방의 의도는 무엇인가?" |
| **⚙️ 기능** | 자기 인식 & 자기 조절 | 사회적 맥락 이해 |
| **⚠️ 부족할 때** | - "나는 잘하는데 왜 인정 안 해주지?"<br>- 같은 실수 반복<br>- 피드백을 피드백으로 인식 못함 | - 상황 오독<br>- 타이밍 실수<br>- 맥락 놓침<br>- "왜 갑자기 화를 내지?" |
| **🏢 사회생활에서** | 학교: 객관적 평가 (덜 중요)<br>→ 이미 점수/성적이 피드백 역할 | 회사: 복잡한 맥락 (매우 중요)<br>→ 애매한 신호를 스스로 해석해야 함 |

### Dunning–Kruger 관점

능력이 낮을수록 자신의 능력을 과대평가하는 경향 (Dunning & Kruger, 1999).

즉, **"실수는 본인이 제일 모르고, 주변은 다 알고 있다"** 라는 비대칭이 존재.

이 테스트는 이 두 축을 동시에 다루어:
- **"나는 눈치가 빠르다고 생각한다"**와
- **"실제 상황에서 눈치를 제대로 보고 있는가"**

의 간극을 가볍게 확인해보는 재미용 도구다.

---

## 📊 측정 설계 & 점수 구조

### 1. 문항 구성

**총 16문항:**

#### 자기보고 파트 (메타인지)
- "나는 상황 판단이 빠른 편이다"
- "나는 사람들의 감정 변화를 잘 캐치한다" 등

#### 타인 평가 추정 파트
- "주변 사람들은 나를 눈치 빠르다고 느끼는 편이다"
- "사람들은 내가 대화 흐름을 잘 이해한다고 말한다" 등

#### 상황 반응 파트 (일반 + 미묘한 상황)
실제 사회적 상황을 제시하고, 그때 가장 가까운 본인의 반응을 선택:
- 정반응
- 자기과시형
- 과잉해석형
- 회피형

#### 전략적 사고(Booster)
장기적 계산/전략 성향을 체크하는 문항들

### 2. 점수 구조

#### 메타인지 점수

높을수록 자기 인식/자기 채점 능력이 높은 편

#### 상황 판단 점수
각 상황에서의 반응을 4가지 패턴으로 분류:
- 정반응
- 자기과시
- 과잉해석
- 회피

상황의 난이도(명확한/미묘한)에 따라 가중치 부여

#### 전략 점수
- 전략적 사고 관련 4문항 평균
- 높을수록 장기적 계산/전략 성향 강함

---

## 🐾 타입 분류 로직

### 핵심 컨셉:
- **메타인지** (High/Low) × **상황 판단력** (High/Low)
- **반응 패턴** (정반응 / 자기과시 / 과잉해석 / 회피)
- **전략 성향** (High/Low)

→ **11가지 동물 타입**으로 매핑

### 개념적 pseudo-code
```python

def compute_scores(answer_dict):
# ① 메타인지
self_eval = score_self_eval(answer_dict)    # Q1Q2
other_eval = score_other_eval(answer_dict)  # Q3Q4
meta_score = (self_eval + other_eval) / 2

# ② 상황 판단력
counts = count_reaction_patterns(answer_dict)  # 정반응/자기과시/과잉해석/회피 개수
situ_score = weighted_situ_score(counts)

# ③ 전략적 사고
strategy_score = mean_strategy_items(answer_dict)  # Q13~Q16

# ④ 조합해서 타입 결정
animal_type = map_to_animal(meta_score, situ_score, counts, strategy_score)
return animal_type

```

### 예시 패턴

#### 예시 1: All High
- 자기평가 ↑, 타인평가추정 ↑
- 실제 상황 정반응 多
- 전략 점수 ↑

→ 실제로도 눈치/메타인지 높고, 주변에서도 그렇게 보며, 자신감도 있는 타입

#### 예시 2: 숨은 고수형
- 자기평가 낮음
- 타인평가추정 중간
- 실제 정반응 多

→ 실제로는 잘 읽는데, 자기 확신이 부족한 타입

#### 예시 3: 자기과시형
- 자기평가 ↑, 타인평가추정 ↑
- 실제 정반응 적고, 자기과시 반응 ≥ 50%

→ "알고 있다"고 생각하지만, 실제로는 과도하게 개입하는 패턴

#### 예시 4: 과잉해석형
- 자기/타인평가 낮~중
- 정반응 적음 + 과잉해석 반응 多

→ 불안을 키우는 쪽으로 상황을 해석하는 타입

회색지대는 완전히 자르지 않고, "가장 가까운 동물" 쪽으로 매핑하도록 설계했다.

---

## 💻 Tech Stack & 아키텍처

### Tech Stack

- **Language**: Python 3.12
- **Framework**: gradio==4.44.0
- **Frontend**: Custom CSS + 동적 HTML
- **Deployment**: Hugging Face Spaces (Pro)
- **Data 저장**: 로컬 CSV
  - (성별 / 연령대 / 응답 내용만 저장, 추가 개인정보 없음)

### 전체 아키텍처

---

## 💻 Tech Stack & 아키텍처

### Tech Stack

- **Language**: Python 3.12
- **Framework**: gradio==4.44.0
- **Frontend**: Custom CSS + 동적 HTML
- **Deployment**: Hugging Face Spaces (Pro)
- **Data 저장**: 로컬 CSV
  - (성별 / 연령대 / 응답 내용만 저장, 추가 개인정보 없음)

### 전체 아키텍처
```
┌──────────────────────────────┐
│     사용자의 브라우저          │
└──────────────────────────────┘
              │
              ▼
┌──────────────────────────────┐
│    Gradio 웹 인터페이스        │
│    - 16문항 질문 UI           │
│    - 결과 페이지 전환          │
│    - 반응형 레이아웃(CSS)     │
└──────────────────────────────┘
              │
              ▼
┌──────────────────────────────┐
│   Python 알고리즘 엔진         │
│    - 점수 계산                │
│    - 패턴 분석                │
│    - 동물 타입 매핑            │
│    - 결과 HTML 템플릿 렌더링   │
└──────────────────────────────┘
              │
              ▼
┌──────────────────────────────┐
│      CSV 데이터 저장          │
│    - 응답 로그                │
│    - 타입 분포 분석용          │
└──────────────────────────────┘
```

---

## 🧩 UI 구조

Gradio Blocks 기반으로, 질문 영역과 결과 영역을 분리:
```python
import gradio as gr

with gr.Blocks(
    theme=gr.themes.Soft(primary_hue="purple"),
    css=custom_css,
) as demo:
    # 헤더
    gr.HTML("나를 닮은 사회적 동물은?")
    
    # 질문 영역
    with gr.Column(visible=True) as question_area:
        age = gr.Dropdown(["10대", "20대", "30대", "40대 이상"], label="연령대")
        gender = gr.Dropdown(["여성", "남성", "기타"], label="성별(선택)")
        
        question_widgets = {}
        for q in QUESTIONS:
            question_widgets[q["id"]] = gr.Radio(
                q["options"],
                label=q["text"],
                elem_classes=["q-block"],
            )
        
        submit_btn = gr.Button("결과 확인하기")
    
    # 결과 영역 (초기에는 숨김)
    result_html = gr.HTML(visible=False)
    
    # 버튼 클릭 시 → 질문 영역 숨기고 결과만 보여주도록 핸들러에서 처리
```

---

## 🎨 CSS 커스터마이징 & 동적 HTML

### 기본 스타일링
```css
/* 전체 컨테이너 */
.gradio-container {
    font-family: "Noto Sans KR", sans-serif;
    max-width: 760px !important;
}

/* 문항 카드 스타일 */
.q-block {
    background: #f3e8ff !important;
    border-radius: 14px !important;
    padding: 18px !important;
}

/* 모바일 최적화 */
@media (max-width: 540px) {
    .gradio-container {
        max-width: 100% !important;
    }
    img {
        max-width: 80vw !important;
    }
}
```

### 결과 페이지 HTML 생성
```python
def build_result_html(animal_code):
    title = TYPE_DETAIL[animal_code]["title"]
    desc = TYPE_DETAIL[animal_code]["특성"]
    inner = TYPE_DETAIL[animal_code]["혼잣말"]
    others = TYPE_DETAIL[animal_code]["다른 사람이 보는 나"]
    praise = TYPE_DETAIL[animal_code]["AI_칭찬"]
    img_url = ANIMAL_IMAGES[animal_code]
    
    return f"""
    
        
        {title}
        
        
        
        
        
            이 타입의 특징
            {desc}
        
        
        
        
            
                내 속마음
                {inner}
            
            
                다른 사람이 보는 나
                {others}
            
        
        
        
        
            AI가 보는 장점
            {praise}
        
    
    """
```

---

## 🌐 배포: Hugging Face + 가비아 도메인

### 1️⃣ Hugging Face에서 Custom Domain 설정

1. Hugging Face Space 접속:
   - https://huggingface.co/spaces/Jay1121/animal_test

2. Settings → Custom domain 메뉴 이동

3. `myanimaltest.site` 입력

4. Hugging Face가 알려주는 CNAME 대상 값 확인
   - 예: `xxx-username-xxx.hf.space`
   - 이 값이 도메인이 가리킬 주소 (타깃)

### 2️⃣ 가비아 DNS 설정

가비아 도메인 관리 → DNS 관리에서 CNAME 레코드 추가.

루트 도메인 (`myanimaltest.site`)을 바로 스페이스로 연결:
```
Type  : CNAME
Host  : @   # 루트 도메인
Value : {Hugging Face에서 받은 hf.space 주소}
TTL   : 기본값
```

**선택 사항**: `www.myanimaltest.site`도 연결하고 싶다면 한 개 더 추가:
```
Type  : CNAME
Host  : www
Value : {같은 hf.space 주소}
TTL   : 기본값
```

### 3️⃣ Hugging Face에서 인증 완료

1. DNS 전파 후 (실제로는 몇 분 안에 반영됨)

2. Hugging Face Custom domain 화면에서 Verify / Connect 클릭

3. `myanimaltest.site` → 스페이스 연결 완료

이제 사용자는 Hugging Face를 몰라도, 브라우저에 `myanimaltest.site`만 입력해 바로 테스트에 접속할 수 있다.

---

## ⏱️ 사용 팁

- **직관대로 빠르게 답하기** (정답 찾으려 하지 않기)
- **여러 번 반복해서 "치트"하지 않기**
- **실제 경험을 떠올리면서 응답하기**
- 결과는 어디까지나 **재미 + 자기 이해용**
- **"좋은 타입 / 나쁜 타입"이 아니라** 내 패턴을 가볍게 들여다보는 거울 정도로 사용하기

---

## 🔮 향후 개선 방향 (Roadmap)

- [ ] 문항 신뢰도 / 타당도 정량 검증
- [ ] 개념의 조작적 정의 정교화
- [ ] 사회적 바람직성(social desirability) 보정 로직 추가
- [ ] UI/UX 개선 (반응형, 접근성, 애니메이션 등)
- [ ] 테스트 링크 확산 및 유입 채널 실험
- [ ] 시계열로 동일 사용자 변화 추적 기능 (토큰/쿠키 기반)
- [ ] 응답 데이터 기반 통계 대시보드 (타입 분포, 연령/성별별 특징 등)
- [ ] 다국어 버전 (영어 등) 확장

---

## 💭 마치며

> **"Know thyself (너 자신을 알라)"** – 소크라테스

2,500년 전 테스형의 말은 2024년에도 여전히 어렵다.  
이 테스트는 그 어려운 걸 조금은 웃으면서 들여다보자는 시도다.

---

## 📖 참고 문헌

- Flavell, J. H. (1979). Metacognition and cognitive monitoring: A new area of cognitive-developmental inquiry. *American Psychologist*, 34(10), 906–911. https://doi.org/10.1037/0003-066X.34.10.906

- Thorndike, E. L. (1920). Intelligence and its uses. *Harper's Magazine*, 140(837), 227–235.

- Goleman, D. (2006). *Social intelligence: The new science of human relationships*. Bantam Books.

- Dunning, D., & Kruger, J. (1999). Unskilled and unaware of it: How difficulties in recognizing one's own incompetence lead to inflated self-assessments. *Journal of Personality and Social Psychology*, 77(6), 1121–1134.



