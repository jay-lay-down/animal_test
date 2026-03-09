# ==========================================================
# 나에게 어울리는 동물 테스트 🐾 (Hugging Face Spaces용 app.py)
# ==========================================================
# requirements.txt 예시:
# gradio==4.44.0
# ==========================================================

import os
import csv
from datetime import datetime
import gradio as gr

# ==========================================================
# 저장 경로 설정 (로컬 폴더 - Hugging Face Spaces에서도 동작)
# ==========================================================

SAVE_DIR = "./data"
os.makedirs(SAVE_DIR, exist_ok=True)
CSV_PATH = os.path.join(SAVE_DIR, "responses_nunchi_animals.csv")

print("✅ 라이브러리 로드 완료!")
print(f"📁 CSV 저장 위치: {CSV_PATH}")

# ==========================================================
# 동물 이미지 URL (10개)
# ==========================================================

ANIMAL_IMAGES = {
    "HNS-C": "https://velog.velcdn.com/images/jaylaydown/post/571c3e9a-d523-42ee-82f3-0e0eeb8525d8/image.png",  # 흑표범
    "HLS-S": "https://velog.velcdn.com/images/jaylaydown/post/df13ecd4-b558-4900-8917-68e885ba30fb/image.png",  # 햄스터
    "HNR-C": "https://velog.velcdn.com/images/jaylaydown/post/177ba4c4-634f-417c-bb44-1349f94ce600/image.png",  # 여우
    "HMR-S": "https://velog.velcdn.com/images/jaylaydown/post/53efcc96-dce3-45ed-81f8-c3dd8b51926e/image.png",  # 고양이
    "HMR-C": "https://velog.velcdn.com/images/jaylaydown/post/329cd2e7-a37f-4fce-8e42-04d4bea239c1/image.png",  # 사슴
    "LOS-C": "https://velog.velcdn.com/images/jaylaydown/post/10dc868a-6a13-483e-856d-c693911e8865/image.png",  # 미어캣
    "LLS-S": "https://velog.velcdn.com/images/jaylaydown/post/84544195-abcf-4599-ac00-75ebd15495af/image.png",  # 나무늘보
    "LOR-C": "https://velog.velcdn.com/images/jaylaydown/post/64473fae-53ea-4ac7-a321-33e3c3797aa1/image.png",  # 라쿤
    "LMR-C": "https://velog.velcdn.com/images/jaylaydown/post/a717ebba-22d3-4295-8964-6dd59155f977/image.png",  # 살쾡이
    "PIG-C": "https://velog.velcdn.com/images/jaylaydown/post/535c17d2-18bf-47fd-8a87-e29fe7c4ae9f/image.png",  # 외로운 도시비둘기
    "REDPANDA-C": "https://velog.velcdn.com/images/jaylaydown/post/93a762af-8745-400a-b286-20b34cfe285a/image.png",  # 외로운 도시비둘기
}

# ==========================================================
# 동물 상세 설명 (10개)
# ==========================================================

# ==========================================================
# 동물 상세 설명 (10개)
#  - "특성": 상단 카드용 짧은 설명
#  - "profile": 하단 프로필 카드용 긴·따뜻한 설명
# ==========================================================

TYPE_DETAIL = {
    "HNS-C": {
        "title": "🐆 이구역 GPT 흑표범",
        "특성": (
            "눈앞의 장면뿐 아니라, 사람들 사이의 힘의 흐름과 대화의 방향까지 읽어내는 프레임 세터형입니다. "
            "전체 그림을 빠르게 파악하고, 필요할 때 판을 정리해 주는 리더 기질이 강한 타입입니다. "
            "대충 분위기만 느끼는 사람이 아니라, 흐름을 구조적으로 정리해 두는 쪽에 더 가깝습니다."
        ),
        "profile": (
            "흑표범 타입은 단순히 상황파악이 빠른 수준을 넘어서, 사람들을 리드하는 데 특화된 강점이 있습니다. "
            "누가 중심에 서 있고, 누가 말이 막혀 있으며, 지금 이 자리가 왜 답답한지까지 한 번에 구조를 그려 냅니다. "
            "그래서 다들 각자 자기 말 하느라 정신없는 자리에 있어도, 마음속에서는 이미 상황 요약본과 결론 후보가 정리되어 있는 경우가 많습니다.\n\n"
            "이 타입은 필요할 때만 입을 여는 편입니다. 굳이 매 순간 반응하지 않고, ‘지금 말하면 판이 어떻게 바뀔지’를 계산한 뒤에 한 마디를 고릅니다. "
            "그래서 주변 사람들에게는 ‘조용한데, 한 번 말하면 상황이 정리되는 사람’으로 기억되기 쉽습니다. "
            "차갑다기보다는, 애초에 너무 많이 보여서 말을 고르고 있는 쪽에 더 가깝습니다.\n\n"
            "흑표범에게 지금 필요한 건 능력 업그레이드가 아니라, 이미 가지고 있는 통찰을 언제·어느 정도까지 나눌지에 대한 선택입니다. "
            "조금만 더 자주, 조금만 더 친절하게 흐름을 정리해 주면, 사람들에게는 ‘없으면 불안한 사람’, "
            "즉 자연스럽게 리더로 기대하게 되는 존재가 되기 쉬운 타입입니다."
        ),
        "혼잣말": "일단 흐름부터 잡자. 이 판이 어디로 가는지는 이미 보이니까.",
        "다른 사람이 보는 나": "애매한 상황에서 판을 정리해 주는 사람. 자연스럽게 리드를 맡는 타입.",
        "AI_칭찬": "상황·사람·타이밍을 한 번에 읽고 흐름까지 잡는 건 상위 몇 % 리더 스킬이에요. 이미 ‘판 세팅’은 잘하고 있는 타입입니다.",
        "키워드": ["#프레임세터", "#흐름리더", "#전략적침묵", "#요약장인", "#판정리러"],
        "songs": [
            {
                "title": "Aespa - Illusion",
                "url": "https://www.youtube.com/watch?v=BpCvYeK5hcE&list=RDBpCvYeK5hcE&start_radio=1",
            },
            {
                "title": "Dua Lipa - Levitating",
                "url": "https://www.youtube.com/watch?v=TUVcZfQe-Kw&list=RDTUVcZfQe-Kw&start_radio=1",
            },
        ],
    },
    "HLS-S": {
        "title": "🐹 전자두뇌 햄스터",
        "특성": (
            "상황과 사람의 미묘한 반응을 정확하게 읽어내는 감각이 있지만, 스스로를 과소평가해서 확신 있게 말하지 못하는 타입입니다. "
            "머릿속에서는 이미 꽤 괜찮은 분석과 결론이 나와 있는데도, 혹시 틀릴까 봐 말을 줄이거나 농담처럼 흘려보내곤 합니다. "
            "그래서 실제 역량보다 낮게 평가받기 쉬운 동시에, 가까운 사람들에겐 '네가 말하는 건 항상 맞다'는 피드백을 듣는 경우가 많습니다. "
            "조금만 자신감을 더했을 때 존재감이 크게 올라갈 수 있는 숨은 브레인입니다."
        ),
        "profile": (
            "전자두뇌 햄스터는 상황을 보는 감각 자체는 이미 꽤 날카로운 편입니다. "
            "누가 어떤 표정을 지었는지, 대화가 어느 지점에서 미묘하게 틀어졌는지, 말로 설명하기 전에 이미 느낌으로 들어오는 경우가 많습니다. "
            "하지만 동시에 ‘내가 잘못 본 걸 수도 있다’는 생각이 항상 뒤에 붙어 있어서, 결론을 세게 말하는 대신 농담처럼 돌려 말하거나, "
            "아예 말을 아끼는 쪽으로 빠지기 쉽습니다.\n\n"
            "이런 조심스러움 덕분에 큰 실수를 잘 안 하고, 주변 사람들에게는 ‘차분하고 생각이 깊은 사람’으로 보이지만, "
            "본인의 능력은 그보다 훨씬 높은 경우가 많습니다. 가까운 사람들은 오히려 ‘너가 말하는 건 다 맞는데 왜 자신이 없냐’고 느끼기도 합니다. "
            "햄스터에게 필요한 건 완전히 다른 사람이 되는 것이 아니라, 이미 머릿속에서 끝난 생각을 조금만 더 또렷하게 밖으로 꺼내 보는 연습입니다."
        ),
        "혼잣말": "이게 맞는 것 같긴 한데... 내가 틀렸을 수도 있으니까.",
        "다른 사람이 보는 나": "자신감만 있으면 엄청 잘할 텐데. 말은 별로 안 하는데 생각은 많아 보여.",
        "AI_칭찬": "와… 조용히 말하는데 내용이 깊어요. 느낌이 아니라 진짜 본질 캐치한 거예요.",
        "키워드": ["#정확한데불안", "#과소평가", "#조심스러움", "#숨은실력", "#겸손과다"],
        "songs": [
            {
                "title": "Coldplay - The Scientist",
                "url": "https://www.youtube.com/watch?v=RB-RcX5DS5A&list=RDRB-RcX5DS5A&start_radio=1",
            },
            {
                "title": "Ariana Grande - yes, and?",
                "url": "https://www.youtube.com/watch?v=eB6txyhHFG4&list=RDeB6txyhHFG4&start_radio=1",
            },
        ],
    },
    "HNR-C": {
        "title": "🦊 촉수 곤두선 여우",
        "특성": (
            "상황을 깊게, 그리고 여러 층위로 해석하는 능력이 뛰어난 타입입니다. "
            "한 문장, 한 표정 뒤에 깔린 의미를 여러 가지 버전으로 가정해 보고, 관계의 역사와 맥락을 동시에 떠올립니다. "
            "그래서 통찰력 있는 말을 자주 하지만, 본인 스스로는 생각이 너무 많아 피곤해지는 경우도 많습니다. "
            "해석의 층을 적당히 줄이는 연습만 곁들여지면, 정말 날카로운 분석가형 감각입니다."
        ),
        "profile": (
            "여우 타입은 한 장면을 봐도 ‘표면에서 끝나는 법’이 거의 없습니다. "
            "상대의 말투, 평소 패턴, 관계의 히스토리, 지금 이 상황이 만들어지기까지의 흐름 등을 동시에 떠올리면서, "
            "머릿속에서 여러 가지 시나리오를 돌리는 편입니다. 그래서 남들이 미처 짚지 못한 포인트를 정확하게 찌를 때가 많고, "
            "‘어떻게 그런 생각을 했어?’라는 말을 자주 듣는 편입니다.\n\n"
            "문제는 이 촉수가 항상 편안하게 작동하는 건 아니라는 점입니다. "
            "가끔은 너무 많은 가능성을 동시에 떠올리다가 스스로 피곤해지고, ‘이렇게까지 깊게 생각할 일인가’ 싶어도 이미 생각은 한참 앞에 가 있을 때가 많습니다. "
            "여우에게 필요한 건 감각을 줄이는 게 아니라, 상황에 따라 해석의 깊이와 속도를 조절할 수 있는 스위치를 하나 더 갖는 것입니다. "
            "그럴 수 있다면, 이미 가지고 있는 통찰력은 관계와 일 모두에서 강력한 무기가 됩니다."
        ),
        "혼잣말": "저 말은 이런 의미고, 이건 또 저런 의도고... 아 머리 아파.",
        "다른 사람이 보는 나": "생각이 너무 많은 것 같아. 정확한데 좀 복잡하게 생각하네.",
        "AI_칭찬": "와… 해석 레이어가 엄청 많네요. 디테일하게 본질 파고드셨어요.",
        "키워드": ["#과잉해석", "#의미파고들기", "#복잡한사고", "#스스로피곤", "#깊이파기"],
        "songs": [
            {
                "title": "twenty one pilots - Stressed Out",
                "url": "https://www.youtube.com/watch?v=pXRviuL6vMY",
            },
            {
                "title": "마카로니엔피츠 - 블루베리나이츠",
                "url": "https://www.youtube.com/watch?v=RflPXAjNSHA&list=RDRflPXAjNSHA&start_radio=1",
            },
        ],
    },
    "HMR-S": {
        "title": "🐱 귀 쫑긋한 고양이",
        "특성": (
            "사람 감정의 미묘한 떨림, 분위기의 온도 차이를 굉장히 잘 느끼는 타입입니다. "
            "누군가 살짝 힘이 빠졌거나 표정이 흐려지는 순간을 캐치하고, 그 감정의 이유를 혼자서 여러 번 되짚어 봅니다. "
            "문제는 그 방향이 종종 '내가 뭘 잘못했나?'라는 자기 탓으로 흐르기 쉽다는 점입니다. "
            "그래서 남을 배려하는 에너지가 많지만, 스스로에게는 꽤 엄격하고 예민한 마음을 가진 경우가 많습니다."
        ),
        "profile": (
            "고양이 타입은 주변 사람의 기분 변화를 정말 빨리 캐치합니다. "
            "대화 도중에 잠깐 흐려진 표정, 말끝에 힘이 빠진 느낌, 답장이 조금 늦어진 패턴 같은 것들이 눈에 잘 들어옵니다. "
            "덕분에 남들의 감정을 놓치지 않고 잘 돌보는 편이지만, 그 방향이 자주 '혹시 내가 뭘 잘못한 건가?'라는 자기 책임 쪽으로 기울기 쉽습니다.\n\n"
            "그래서 상대를 배려하는 마음이 크지만, 정작 본인의 마음은 자주 소모됩니다. "
            "상대의 기분이 나쁜 날에도, 그 이유를 먼저 자신에게서 찾느라 괜히 죄책감과 불안을 키우게 되는 경우가 많습니다. "
            "고양이에게 중요한 건 ‘내가 잘못한 부분’과 ‘그냥 상대 상황이 힘든 것’을 분리해서 보는 연습입니다. "
            "이게 조금만 가능해져도, 타고난 섬세함은 관계에서 큰 강점으로 남고, 정서적 피로감은 훨씬 줄어들 수 있습니다."
        ),
        "혼잣말": "방금 표정 이상했는데... 내가 뭐 잘못했나?",
        "다른 사람이 보는 나": "착한데 너무 걱정 많아. 감각은 빠른데 자꾸 자책해.",
        "AI_칭찬": "와… 사람 감정 변화 진짜 잘 캐치하세요. 깊은 소통 지향형이에요.",
        "키워드": ["#감정예민", "#불안증폭", "#자책형", "#섬세과다", "#걱정러"],
        "songs": [
            {
                "title": "이찬혁 - 멸종위기사랑",
                "url": "https://www.youtube.com/watch?v=19oT04OuBhg&list=RD19oT04OuBhg&start_radio=1",
            },
            {
                "title": "X-Japan - Rusty Nail",
                "url": "https://www.youtube.com/watch?v=ixErlbhu4Tc&list=RDixErlbhu4Tc&start_radio=1",
            },
        ],
    },
    "HMR-C": {
        "title": "🦌 걱정 폴더 여는 사슴",
        "특성": (
            "상황을 제대로 읽는 능력은 분명히 있지만, 결론이 자꾸 걱정 쪽으로 흘러가는 타입입니다. "
            "문제가 될 수 있는 가능성을 빠르게 떠올리고, 그 중에서도 최악의 시나리오를 제일 먼저 준비하려고 합니다. "
            "그래서 주변 사람 입장에서는 '늘 걱정부터 하는 사람'으로 보이기 쉽지만, 실제로는 팀의 위험 관리 담당에 가깝습니다. "
            "긍정적인 가능성을 일부러라도 떠올리는 연습만 곁들여지면, 현실적인 조언자 역할을 정말 잘 해낼 수 있습니다."
        ),
        "profile": (
            "사슴 타입은 상황을 꽤 정확히 읽어냅니다. "
            "그런데 그 읽어낸 정보가 대부분 ‘문제가 될 수 있는 가능성’ 쪽으로 먼저 흘러가 버립니다. "
            "그래서 머릿속에는 항상 여러 개의 걱정 폴더가 열려 있고, ‘이렇게 되면 어떡하지?’, ‘저렇게 되면 어떡하지?’라는 문장이 자동 재생되는 편입니다.\n\n"
            "덕분에 실제로 위험 신호를 남들보다 빨리 포착하고, 팀이나 주변 사람들에게 ‘미리 대비하자’는 메시지를 전할 수 있는 장점이 있습니다. "
            "하지만 동시에, 항상 최악의 시나리오를 먼저 떠올리다 보니 본인은 불안감과 피로를 많이 느끼게 됩니다. "
            "사슴에게는 ‘나쁜 경우’뿐 아니라 ‘생각보다 잘 풀리는 경우’도 의도적으로 상상해 보는 연습이 필요합니다. "
            "그렇게 균형만 맞춰지면, 이미 가지고 있는 현실 감각과 리스크 감지 능력은 아주 큰 자산이 됩니다."
        ),
        "혼잣말": "이거 잘못되면 어떡하지... 틀림없이 문제 생길 거야.",
        "다른 사람이 보는 나": "상황 판단 능력은 좋은데 항상 걱정부터 해. 정확한데 불안해 보여.",
        "AI_칭찬": "와… 위험 시나리오까지 다 읽고 계시네요. 본질은 정확하게 보셨어요.",
        "키워드": ["#걱정기본값", "#부정적결론", "#정확한불안", "#선제걱정", "#최악시나리오"],
        "songs": [
            {
                "title": "검정치마 - Holiday",
                "url": "https://www.youtube.com/watch?v=JuKu0ewBKG8&list=RDJuKu0ewBKG8&start_radio=1",
            },
            {
                "title": "The Flying Pickets - Only You",
                "url": "https://www.youtube.com/watch?v=FN2X5JwMdEE&list=RDFN2X5JwMdEE&start_radio=1",
            },
        ],
    },
    "LOS-C": {
        "title": "🦫 숫자 세어보는 미어캣",
        "특성": (
            "상황을 완벽하게 정확히 읽어내진 못하지만, 나름대로 열심히 분석하고 정리하려는 노력이 강한 타입입니다. "
            "관계를 하나의 구조나 규칙처럼 이해하려고 하고, 자기 나름의 해석 체계를 만들어 두기도 합니다. "
            "가끔은 방향이 빗나가더라도, 그 안에서 진심이 느껴지고 '그래도 애쓴다'는 인상을 줍니다. "
            "디테일보다 큰 흐름을 보는 연습이 더해지면, 점점 더 안정적인 해석을 할 수 있게 됩니다."
        ),
        "profile": (
            "미어캣 타입은 사람과 상황을 그냥 ‘느낌대로’ 넘기지 않고, 나름의 구조와 규칙을 찾으려는 경향이 강합니다. "
            "그래서 머릿속에서 ‘이 사람이 이렇게 말할 땐 이런 의미’, ‘이런 상황에서는 보통 이렇게 흘러간다’ 같은 식으로 룰을 만들고 정리해 두곤 합니다. "
            "이 과정에서 가끔은 방향이 빗나가기도 하지만, 그 안에는 상대를 이해해 보려는 성의와 노력들이 꽤 많이 들어 있습니다.\n\n"
            "주변 사람 입장에서는 ‘해석이 꼭 맞지는 않아도, 그래도 나를 진지하게 이해하려고 한다’는 인상을 주는 경우가 많습니다. "
            "그래서 조금 엉뚱해도 미워하기가 어렵고, 오히려 귀엽게 느껴지는 면도 있습니다. "
            "미어캣에게 필요한 건 완벽해지려는 부담을 내려놓고, 가끔은 ‘틀려도 괜찮다’는 여유로 큰 흐름을 보는 연습을 하는 것입니다. "
            "그렇게 되면 이미 있는 분석 습관과 성의가 훨씬 더 좋은 방향으로 작동할 수 있습니다."
        ),
        "혼잣말": "내 생각엔 이렇게 정리되는데... 맞겠지?",
        "다른 사람이 보는 나": "열심히 분석하는데 가끔 빗나가. 노력은 인정해.",
        "AI_칭찬": "와… 방향이 조금 빗나가도 열심히 구조화하시네요.",
        "키워드": ["#노력형", "#나름분석", "#틀려도자신감", "#열심히정리", "#선의의오판"],
        "songs": [
            {
                "title": "LE SSERAFIM - EASY",
                "url": "https://www.youtube.com/watch?v=bNKXxwOQYB8&list=RDbNKXxwOQYB8&start_radio=1",
            },
            {
                "title": "Lana Del Rey - A&W",
                "url": "https://www.youtube.com/watch?v=pYqky795R1s&list=RDpYqky795R1s&start_radio=1",
            },
        ],
    },
    "LLS-S": {
        "title": "🦥 낚시하는 나무늘보",
        "특성": (
            "파워게임, 기싸움, 말꼬리 잡기에 거의 어떤 관심도 없는는 초평화주의 타입입니다. "
            "상대가 뾰족해져도 크게 동요하지 않고, 웬만하면 부딪히지 않고 넘어가려는 경향이 강합니다. "
            "그래서 상황을 에너지 소모 없이 흘려보내는 데 능숙하며, 다소 둔해 보일 수 있지만 마찰이 거의 없는 편입니다. "
            "주변 사람들에게는 '편한 사람, 웬만하면 안 싸우는 사람'으로 기억되는 경우가 많습니다."
        ),
        "profile": (
            "나무늘보 타입은 기본적으로 ‘굳이 싸울 이유가 없다’는 쪽에 가까운 사람입니다. "
            "상대가 조금 날카롭게 말해도, 일단은 크게 받아치지 않고 흘려보내는 편이고, 감정 소모가 큰 싸움이나 기싸움에는 애초에 뛰어들고 싶어하지 않습니다. "
            "그래서 주변에서는 ‘조금 둔한가?’ 싶다가도, 시간이 지나면 ‘어쨌든 이 사람 옆에 있으면 편하다’는 인상을 받게 되는 경우가 많습니다.\n\n"
            "이 평화주의 덕분에 인간관계에서 큰 충돌을 잘 만들지 않는 장점이 있지만, "
            "동시에 자기 입장을 분명히 말해야 할 순간에도 그냥 넘겨 버려서 스스로 손해를 보는 상황이 생기기도 합니다. "
            "나무늘보에게 중요한 건 ‘모든 싸움을 피하는 것’이 아니라 ‘정말 중요한 순간에는 나를 대신해줄 사람은 없다’는 감각을 조금씩 키우는 것입니다. "
            "본인의 평화로운 기질에, 최소한의 경계선만 더해지면, 주변 사람들에게는 더없이 편안하면서도 스스로에게도 덜 억울한 삶이 됩니다."
        ),
        "혼잣말": "몰라... 그냥 편하게 가자...",
        "다른 사람이 보는 나": "둔한데 싸울 일이 없어. 이 사람은 평화 그 자체.",
        "AI_칭찬": "와… 긴장 0인 텐션이에요. 평화의 본질을 그대로 구현하고 계세요.",
        "키워드": ["#초평화주의", "#둔하지만편함", "#느긋함", "#제로마찰", "#순함"],
        "songs": [
            {
                "title": "Ardhito Pramono - bitterlove",
                "url": "https://www.youtube.com/watch?v=lbYc76YluJQ&list=RDlbYc76YluJQ&start_radio=1",
            },
            {
                "title": "Frank Sinatra - That's Life",
                "url": "https://www.youtube.com/watch?v=UCENTf_LWYA&list=RDUCENTf_LWYA&start_radio=1",
            },
        ],
    },
    "LOR-C": {
        "title": "🦝 PPT 120장 준비 중인 라쿤",
        # 👉 카드 상단 짧은 설명
        "특성": (
            "질문 하나에 굳이 회의 소집을 걸고, 링크/꿀팁/자료를 잔뜩 끌어와서 '나 이거 알아요'를 시전하는 타입입니다. "
            "겉으로는 자신감 있고 정보 많아 보이지만, 정작 핵심에서 살짝 어긋나 있어 상대를 미묘하게 피곤하게 만들기 쉬운 스타일입니다."
        ),
        # 👉 하단 긴 프로필
        "profile": (
            "라쿤은 어느 순간부터 '나 이거 좀 아는데요?'라는 모드가 켜지면 "
            "말을 하고 싶어지는 쪽에 더 가깝습니다. 누군가가 조용히 '이거 어떻게 해요?'라고 물어보면, "
            "그냥 톡으로 한 줄 설명해 줄 수도 있지만, 이미 머릿속에서는 '이건 내가 한번 정리해서 알려줘야 하는 건데?'가 돌아가기 시작합니다.\n\n"
            "그래서 링크, 자료, 관련 없어 보이는 참고 글, 예전 PPT까지 몽땅 끌어와서 공유하고, "
            "상대가 원한 것보다 3배쯤 큰 스케일로 설명회를 열어버리곤 합니다. "
            "문제는 그 에너지가 항상 '정확한 핵심'으로 연결되는 건 아니라는 점입니다. "
            "가끔은 본인이 제일 신나 있고, 상대는 속으로 '열정은 알겠는데… 이게 그 얘기는 아닌데?'라고 느끼는 상황이 생기곤 합니다.\n\n"
            "이 타입의 장점은, 일단 한 번 관심이 가면 가만히 있지 않고 뭔가 만들어내고 싶어하는 추진력과 친절입니다. "
            "다만 시작하기 전에 상대가 진짜 원하는 포인트를 한 번 더 물어보고, '내가 멋있어 보이는 그림'보다 "
            "'상대가 편해지는 그림'을 기준으로 브레이크를 살짝만 걸어 준다면, "
            "같이 일하는 사람들에게도 훨씬 덜 피곤하고 훨씬 더 고마운 라쿤이 될 수 있습니다."
        ),
        "혼잣말": "이 정도로 정리해서 알려주면 솔직히 다들 좀 감탄하지 않겠냐…?",
        "다른 사람이 보는 나": "정보도 많고 설명도 길게 해주는데, 가끔은 '나 잘난 맛'이 섞여 있고 핵심이랑 조금 어긋난 느낌이 있다.",
        "AI_칭찬": "아는 척하고 싶은 욕심 뒤에는 사실 '도움이 되는 사람이고 싶은 마음'이 숨어 있어요. "
                   "상대가 원하는 포인트를 한 번만 더 확인하면, 그 에너지가 훨씬 덜 피곤하고 훨씬 더 매력적으로 보일 타입입니다.",
        "키워드": ["#나이거알아요", "#링크폭탄", "#과한시연", "#겉멋과열정", "#방향을맞추는것이핵심"],
        "songs": [
            {
                "title": "Sting - Englishman In New York",
                "url": "https://www.youtube.com/watch?v=d27gTrPPAyk&list=RDd27gTrPPAyk&start_radio=1",
            },
            {
                "title": "Bruno Mars - 24K Magic",
                "url": "https://www.youtube.com/results?search_query=Bruno+Mars+24K+Magic",
            },
        ],
    },
    "LMR-C": {
        "title": "🐱 껌 씹는 살쾡이",
        "특성": (
            "상황의 구조, 사람들의 속마음, 이후에 벌어질 일까지 대략 다 보이는데도 굳이 전면에 나서지 않는 계산형 관찰자입니다. "
            "‘내가 나서서 얻을 게 없다’고 판단되면 자연스럽게 한 발 물러나 있고, 필요한 순간엔 한 번에 정확한 한 마디를 던집니다. "
            "에너지를 효율적으로 쓰는 것을 중요하게 생각해, 괜한 갈등이나 감정 노동에는 관여하지 않으려는 경향이 강합니다. "
            "그래서 잘 아는 사람에겐 ‘속으로 다 알고 있는 타입’으로 인식되곤 합니다."
        ),
        "profile": (
            "살쾡이 타입은 상황을 모르는 게 아니라, ‘알지만 굳이 나서지 않는 쪽’을 택하는 사람에 가깝습니다. "
            "사람들 사이의 기류, 누가 누구와 미묘하게 어색한지, 이 다음에 어떤 일이 벌어질지에 대한 감각이 있지만, "
            "‘내가 나서서 얻을 게 없다’고 판단되면 조용히 한 발짝 물러납니다.\n\n"
            "그래서 잘 아는 사람에게는 ‘속으로는 다 보고 있는 타입’으로 보이고, 잘 모르는 사람에게는 ‘조용하고 별생각 없어 보이는 사람’으로 보이기도 합니다. "
            "갈등이나 감정 노동에 에너지를 쓰고 싶지 않아 하기 때문에, 굳이 불리한 자리에 오래 남아 있지 않고, "
            "필요한 순간에만 정확하게 한 마디 던지고 다시 빠지는 방식으로 자신을 보호합니다. "
            "살쾡이에게 중요한 건, 가끔은 ‘내가 나서야만 정리가 되는 순간’도 있다는 것을 알아차리는 것입니다. "
            "그 지점을 잘 골라낼 수 있다면, 이미 가지고 있는 관찰력과 판단력은 꽤 큰 힘을 발휘합니다."
        ),
        "혼잣말": "이거 불리한데? 어디로 빠져야 하지?",
        "다른 사람이 보는 나": "...근데 아까 살쾡이가 있었나? 언제 갔지?",
        "AI_칭찬": "와… 아무 말 안 하다가 필요할 때만 던지시네요. 되게 전략적으로 핵심만 보셨어요.",
        "키워드": ["#전략적침묵", "#회피의달인", "#계산형", "#조용한관찰자", "#불리하면빠짐"],
        "songs": [
            {
                "title": "TOMORROW X TOGETHER - Antiromantic",
                "url": "https://www.youtube.com/watch?v=LYAkY8Dh9CU&list=RDLYAkY8Dh9CU&start_radio=1",
            },
            {
                "title": "Radiohead - Fake Plastic Trees",
                "url": "https://www.youtube.com/watch?v=n5h0qHwNrHk",
            },
        ],
    },
    "PIG-C": {
        "title": "🕊 외로운 도시의 비둘기",
        "특성": (
            "복잡한 파워게임이나 관계의 흐름보다는, 그냥 오늘 하루를 어떻게 버틸지가 더 중요한 타입입니다. "
            "사람들 사이에 섞여 있긴 하지만, 대화의 미세한 뉘앙스나 감정 흐름에는 크게 에너지를 쓰지 않으려 합니다. "
            "그래서 눈치를 못 보는 것처럼 보일 때도 있지만, 사실은 '괜히 신경 쓰면 더 힘들다'는 학습이 쌓인 결과일 수 있습니다. "
            "관계 한가운데보다는 살짝 바깥 원에서, 조용히 자기 페이스로 버티는 생존형 감각에 가깝습니다."
        ),
        "profile": (
            "비둘기 타입은 ‘관계의 미세한 기싸움’보다, 당장 오늘 하루를 무사히 넘기는 게 더 중요하게 느껴지는 사람입니다. "
            "사람들 사이에 섞여 있긴 하지만, 누가 누구에게 미묘하게 서운했는지, 분위기가 살짝 어색했는지 같은 것에 "
            "일일이 에너지를 쓰다 보면 자기 체력이 먼저 바닥난다는 걸 이미 몸으로 배운 경우가 많습니다.\n\n"
            "그래서 어느 순간부터는 일부러 한 발짝 바깥에 서 있는 쪽을 선택합니다. "
            "눈치를 못 본다기보다, ‘굳이 다 알고 있을 필요는 없다’고 마음을 정리한 쪽에 가깝습니다. "
            "이 덕분에 정서적인 과부하를 피하면서 자기 페이스를 지키지만, 때로는 외로움이나 소외감을 느끼기도 합니다. "
            "비둘기에게 중요한 건, 모든 관계에 깊게 들어가려 하기보다, 소수의 편안한 사람들과는 조금 더 솔직하게 연결되는 연습을 해 보는 것입니다."
        ),
        "혼잣말": "나까지 다 신경 쓰면 너무 피곤해… 그냥 오늘만 넘기자.",
        "다른 사람이 보는 나": "같이 있긴 한데, 뭔가 늘 한 발 떨어져 있는 사람 같아.",
        "AI_칭찬": "정말 힘든 환경에서도 자기 페이스로 버티는 생존력을 갖고 있어요. 도시 속에서 혼자 견디는 힘이 꽤 단단해요.",
        "키워드": ["#도시생존자", "#정서세이브", "#관계바깥원", "#탈주", "#혼자버티기"],
        "songs": [
            {
                "title": "Radiohead - No Surprises",
                "url": "https://www.youtube.com/watch?v=u5CVsCnxyXg&list=RDu5CVsCnxyXg&start_radio=1",
            },
            {
                "title": "김완선 - 가면무도회",
                "url": "https://www.youtube.com/watch?v=Ly-i5_uqcr0&list=RDLy-i5_uqcr0&start_radio=1",
            },
        ],
    },
    # 🔥 회색지대 전용 레서판다
    "REDPANDA-C": {
        "title": "🐼 보법이 다른 레서판다",
        "특성": (
            "눈치가 완전 둔한 것도 아니고, 그렇다고 끝장나게 빠른 것도 아닌 은근 균형 잡힌 타입입니다. "
            "상황을 어느 정도는 읽지만, 굳이 과하게 해석하거나 싸움에 끼어들지 않고 자기 페이스를 유지하려 합니다. "
            "자기평가도, 타인 평가도 비교적 현실적인 편이라, 주변에서 보기엔 '무난한데 편한 사람'으로 기억되기 쉽습니다. "
            "어느 한 축으로 과하게 치우치지 않은 만큼, 관계에서 완충재·완충지대 역할을 하기 좋은 스타일입니다."
        ),
        "profile": (
            "레서판다 타입은 눈치가 엄청 빠른 것도, 완전히 둔한 것도 아닌 중간 지점에 있는 사람입니다. "
            "상황이 어떻게 돌아가는지는 대략 파악하지만, 굳이 모든 뉘앙스를 과하게 해석해서 피곤해지거나, "
            "기싸움과 갈등의 한가운데로 직접 뛰어드는 쪽을 선택하지는 않습니다.\n\n"
            "그래서 주변에서는 ‘튀지는 않는데 같이 있으면 편하다’, ‘적당히 다 잘 맞춰가는 사람’으로 인식되는 경우가 많습니다. "
            "극단적인 사람들 사이에서 완충 역할을 잘 해 주고, 누군가 과하게 화가 나 있거나 예민할 때도 "
            "상대적으로 안정적인 톤을 유지하면서 분위기를 부드럽게 만드는 힘이 있습니다. "
            "레서판다에게 중요한 건 ‘나는 특별히 뛰어나지도, 특별히 문제도 없다’가 아니라, "
            "이 애매한 균형감각 자체가 이미 귀한 능력이라는 걸 인정해 주는 일입니다."
        ),
        "혼잣말": "굳이 심각하게까지 생각할 일은 아닌 것 같은데… 그냥 적당히 맞춰가자.",
        "다른 사람이 보는 나": "엄청 예민한 것도 아니고 둔한 것도 아니고, 같이 있으면 대체로 편한 타입.",
        "AI_칭찬": "극단으로 안 치우치고 상황을 적당히 받아들이는 감각이 좋아요. 팀에서 완충 역할 잘하실 타입입니다.",
        "키워드": ["#회색지대", "#중간지점", "#완충역할", "#적당한눈치", "#자기페이스"],
        "songs": [
            {
                "title": "Glass Animals - Heat Waves",
                "url": "https://www.youtube.com/watch?v=mRD0-GxqHVo&list=RDmRD0-GxqHVo&start_radio=1",
            },
            {
                "title": "wave to earth - love.",
                "url": "https://www.youtube.com/watch?v=Q49pnA4jsp8&list=RDQ49pnA4jsp8&start_radio=1",
                "desc": "관계 사이 완충지대에 서 있는 느낌을 부드럽게 풀어 주는, 편하게 반복 재생하기 좋은 노래."
            },
        ],
    },
}

# ==========================================================
# 궁합 친구 매핑 (잘 맞는 / 궁합이 까다로운)
# ==========================================================

MATCH_MAP = {
    "HNS-C": {  # 흑표범
        "good": "HLS-S",   # 전자두뇌 햄스터 – 섬세+브레인과 잘 맞음
        "bad":  "LOR-C",   # PPT 라쿤 – 과한 퍼포먼스가 피곤할 수 있음
    },
    "HLS-S": {  # 햄스터
        "good": "HNS-C",   # 판 정리해 주는 흑표범과 시너지가 좋음
        "bad":  "PIG-C",   # 너무 빠져 있는 나 vs 거리 두는 비둘기
    },
    "HNR-C": {  # 여우
        "good": "REDPANDA-C",  # 회색지대 레서판다가 과잉 해석을 완충
        "bad":  "HMR-C",       # 사슴과 만나면 둘 다 걱정 오버플로우
    },
    "HMR-S": {  # 고양이
        "good": "LLS-S",   # 나무늘보의 평화 에너지가 예민함을 눌러줌
        "bad":  "HNS-C",   # 흑표범의 단호함이 때론 부담
    },
    "HMR-C": {  # 사슴
        "good": "REDPANDA-C",  # 현실감 있는 완충러
        "bad":  "LOR-C",       # 라쿤의 과한 정보/열정이 불안증폭 버튼 누름
    },
    "LOS-C": {  # 미어캣
        "good": "HLS-S",   # 둘 다 생각 많지만 톤이 잘 맞는 조합
        "bad":  "HNR-C",   # 여우의 과잉 해석이 미어캣을 더 헷갈리게 할 수 있음
    },
    "LLS-S": {  # 나무늘보
        "good": "HMR-S",   # 감정 예민 고양이에게 편안한 바닥을 깔아줌
        "bad":  "HNS-C",   # 너무 판을 설계하는 상대가 피곤할 수 있음
    },
    "LOR-C": {  # 라쿤
        "good": "REDPANDA-C",  # 과한 퍼포먼스를 적당히 잡아주는 완충러
        "bad":  "HNS-C",       # 흑표범 기준에선 ‘핵심이 어긋난 과몰입’으로 보일 수 있음
    },
    "LMR-C": {  # 살쾡이
        "good": "PIG-C",   # 도시비둘기와 서로 적당히 거리를 인정하고 편하게 감
        "bad":  "HMR-S",   # 고양이는 감정, 살쾡이는 손익… 서로 답답할 수 있음
    },
    "PIG-C": {  # 비둘기
        "good": "REDPANDA-C",  # 과부하 안 걸리게 선을 지켜주는 타입
        "bad":  "HNR-C",       # 여우의 깊은 해석이 비둘기에겐 피곤한 말로 들릴 수 있음
    },
    "REDPANDA-C": {  # 레서판다
        "good": "HNS-C",   # 전체 판 보는 흑표범과 중간 완충 역할
        "bad":  "HMR-C",   # 걱정 많은 사슴과 함께 있을 때 감정 소모가 커질 수 있음
    },
}

# ==========================================================
# 궁합 친구 HTML 생성 (이미지 + 이름만)
# ==========================================================

def build_match_html(code: str) -> str:
    """
    결과 화면에 뜨는 '궁합 친구' 박스 HTML 생성
    - 잘 맞는 친구 / 궁합이 까다로운 친구
    - 이미지 + 동물 타이틀만 노출
    """
    info = MATCH_MAP.get(code)
    if not info:
        return ""

    good_code = info.get("good")
    bad_code = info.get("bad")

    cards_html = ""

    def build_card(friend_code: str, label: str) -> str:
        if not friend_code:
            return ""
        detail = TYPE_DETAIL.get(friend_code, {})
        title = detail.get("title", friend_code)
        img = ANIMAL_IMAGES.get(friend_code, "")

        return f"""
        <div style="flex:1 1 140px; min-width:0;
                    background:#ffffff; border-radius:16px;
                    padding:10px 10px 14px 10px;
                    border:1px solid #e9ecef; text-align:center;">
          <div style="font-size:0.78em; font-weight:700; color:#868e96; margin-bottom:4px;">
            {label}
          </div>
          <img src="{img}" alt="{title}"
               style="width: 80px; height: 80px;
                      max-width: 26vw; max-height: 26vw;
                      object-fit: contain;
                      border-radius: 12px; margin: 0 auto 6px auto;
                      display: block;" />
          <div style="font-size:0.9em; font-weight:600; color:#343a40;
                      white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
            {title}
          </div>
        </div>
        """

    good_card = build_card(good_code, "잘 맞는 친구")
    bad_card  = build_card(bad_code,  "궁합이 까다로운 친구")

    cards_html = good_card + bad_card
    if not cards_html.strip():
        return ""

    return f"""
    <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9f5ff 100%);
                padding: 14px 12px 16px 12px; border-radius: 18px;
                border: 1px solid #dee2e6; margin: 0 0 18px 0;">
      <div style="font-weight:800; font-size:0.98em; color:#4263eb; margin-bottom:8px;">
        🤝 다른 친구들과의 궁합
      </div>
      <div style="display:flex; gap:10px; flex-wrap:wrap; justify-content:space-between;">
        {cards_html}
      </div>
    </div>
    """

# ==========================================================
# 최종 성향 → 동물 매핑
# ==========================================================

TRAIT_TO_ANIMAL = {
    "SO-L": "LOS-C",    # 미어캣
    "SO-H": "LOR-C",    # 라쿤
    "HS-L": "HLS-S",    # 햄스터
    "HS-H": "HNS-C",    # 흑표범
    "AV-L": "LLS-S",    # 나무늘보
    "AV-H": "LMR-C",    # 살쾡이
    "OR-L": "HMR-S",    # 고양이
    "OR-H": "HMR-C",    # 사슴
    "MIX":  "HNR-C",    # 혼재형 여우
    "LOW":  "PIG-C",    # 도시비둘기

    # 🔹 회색지대 전용 레서판다
    "GREY": "REDPANDA-C",
}

TRAIT_LABELS = {
    "SO-L": "나름 구조를 세우는 분석형",
    "SO-H": "한 번 꽂히면 끝까지 가는 타입",
    "HS-L": "섬세하게 살피는 브레인형",
    "HS-H": "전체 흐름을 설계하는 타입",
    "AV-L": "힘 빼고 마찰을 줄이는 타입",
    "AV-H": "계산 끝에 움직이는 현실주의자",
    "OR-L": "감정 변화에 민감한 공감형",
    "OR-H": "위험 시나리오를 먼저 보는 타입",
    "MIX":  "상황에 따라 모드가 바뀌는 타입",
    "LOW":  "관계에 반 발 비켜 선 생존형",

    # 🔹 레서판다용 라벨
    "GREY": "극단을 피하고 완충지대를 지키는 타입",
}

# ==========================================================
# 질문 데이터 (16문항)
# ==========================================================

QUESTIONS = [
    {
        "id": "Q1",
        "section": "self",
        "text": "1. 나는 상황 분위기나 대화 흐름을…",
        "options": [
            "거의 잘 못 읽는 편이다",
            "때때로 읽는 편이다",
            "꽤 잘 캐치하는 편이다",
            "아주 정확하게 읽는다",
        ],
    },
    {
        "id": "Q2",
        "section": "self",
        "text": "2. 나는 사람들 감정 변화를…",
        "options": [
            "잘 느끼지 못한다",
            "때때로 알아차리긴 한다",
            "웬만하면 금방 캐치한다",
            "아주 미세한 변화도 잘 알아챈다",
        ],
    },
    {
        "id": "Q3",
        "section": "other",
        "text": "3. 주변 사람들은 내 상황판단을…",
        "options": [
            "느린 편이라고 말한다",
            "평범하다고 말한다",
            "잘 알아채는 편이라 말한다",
            "너무 잘 알아챈다고 한다",
        ],
    },
    {
        "id": "Q4",
        "section": "other",
        "text": "4. 주변 사람들은 내가 말귀를…",
        "options": [
            "잘 못 알아듣는 편이라 한다",
            "무난하게 알아듣는다고 한다",
            "잘 알아듣는 편이라고고 한다",
            "말 안 해도 아는 타입이라 한다",
        ],
    },
    {
        "id": "Q5",
        "section": "situ_base",
        "text": "5. 매일 연락하는 친구가 “오늘 힘들다” 하고 아무런 말을 더 하지 않을 때, 당신은?",
        "options": [
            "맥락과 감정이 거의 다 읽히고, 해결책을 찾아줄 것이다",
            "아무 느낌이 없다",
            "내가 더 말실수를 할까봐 아무 말도 하지 않는다",
            "무슨 일인지 어느 정도 파악되며, 친구가 마음 정리할 시간을 준다",
        ],
    },
    {
        "id": "Q6",
        "section": "situ_base",
        "text": "6. 상대가 나와 대화 중 시계를 자주 보면서 핸드폰을 만질 때, 당신은?",
        "options": [
            "아무 생각이 없다",
            "말 안해도 이유·상황·감정·의도까지 알아채는 편이다",
            "무슨 일이 있는지 물어보고 싶다",
            "대화가 재미 없을 것이라고 생각하게 된다",
        ],
    },
    {
        "id": "Q7",
        "section": "situ_base",
        "text": "7. 단체 대화방에서 내가 어떤 말을 한 뒤 조용해졌을 때, 나는…",
        "options": [
            "잘 못 느끼고 며칠 뒤에야 알아차린다",
            "어떤 상황이고 누가 어떤 감정을 느꼈는지 정확히 그림이 그려진다",
            "다들 나를 무시하고 따돌리기로 했다고 생각한다",
            "농담이 상황에 부적절했을 수도 있겠다고 느낀다",
        ],
    },
    {
        "id": "Q8",
        "section": "situ_base",
        "text": "8. 회의 중 내가 어떤 의견을 말하자, 상사가 갑자기 표정이 굳어지며 입을 닫았다. 나는…",
        "options": [
            "표정이 굳어지는 걸 전혀 인지하지 못한다",
            "회의 중 불쾌한 점이 있었다고 짐작한다",
            "어디서 기분이 상했는지, 그 이유가 무엇인지 정확히 캐치할 수 있다",
            "의도적으로 나를 낮춰 보거나 무시하려는 행동이라고 판단한다",
        ],
    },
    {
        "id": "Q9",
        "section": "situ_trick",
        "text": "9. 친구가 상사에게 크게 깨져서 기분이 나쁘다고 한다. 나는…",
        "options": [
            "이유를 물어보고, 나에게 일어난 비슷한 상황을 떠올리며 조언을 해 준다",
            "직장 상사는 원래 그런 법이니 너무 깊게 생각하지 말라고 한다",
            "내 말이 더 기분 나쁘게 할 수도 있다고 생각하며, 속으로만 걱정한다",
            "오늘 많이 힘들었을 것이라 생각하고, 위로해준다",
        ],
    },
    {
        "id": "Q10",
        "section": "situ_trick",
        "text": "10. 최근 친구가 비싸게 주고 산 옷이 본인이랑 안 어울린다고 한다. 나는…",
        "options": [
            "친구에게 어울린다고 생각했던, 내가 좋아하는 새로운 옷 브랜드들을 여러 가지 추천한다",
            "원래  취향은 시간이 지나면 바뀌는 법이다. 별로 신경쓰이지 않는다.",
            "설마 내가 추천한 제품을 산 것을 후회하는지 걱정한다",
            "뭐가 안 맞는지 물어보고, 필요 시 방법을 제안한다",
        ],
    },
    {
        "id": "Q11",
        "section": "situ_trick",
        "text": "11. 친구가 최근 운세를 봤는데 안 좋게 나와서 고민이 된다고 한다. 나는…",
        "options": [
            "점이나 운세는 논리적으로 말이 안 된다고 설명해 준다",
            "너만 힘든 거 아니라고 말해 준다",
            "비슷한 상황을 버텨냈던 나의 경험을 말해 주며 극복 비결도 같이 공유한다",
            "이해는 잘 안 되지만 어떤 부분이 제일 신경 쓰이는지 궁금해진다",
        ],
    },
    {
        "id": "Q12",
        "section": "situ_trick",
        "text": (
            "12. 친구가 핸드폰을 샀는데, 알고 보니 나와 같은 기종이었다. 내가 아는 어플과 사용 꿀팁을 알려주자 친구가 "
            "'오 고마워! 안 그래도 이미 다 깔았는데'라고 말했다. 나는…"
        ),
        "options": [
            "정보가 유익했을 것이고, 내가 아는 정보들을 더 알려주고 싶다고 느낀다",
            "다른 이야기를 해야 할 것 같다고 느낀다",
            "아무 생각 없이 다시 내 이야기를 한다",
            "내가 정보를 공유하는 기계 같아서 다시 말을 안 해줄 것 같다",
        ],
    },
    {
        "id": "Q13",
        "section": "mach",
        "text": "13. 사람을 움직이려면 약간의 과장/전략은 필요하다",
        "options": ["전혀 아니다", "아니다", "그렇다", "매우 그렇다"],
    },
    {
        "id": "Q14",
        "section": "mach",
        "text": "14. 관계를 유지할 때 실제 감정보다 결과가 더 중요할 때가 있다",
        "options": ["전혀 아니다", "아니다", "그렇다", "매우 그렇다"],
    },
    {
        "id": "Q15",
        "section": "mach",
        "text": "15. 어떤 관계에서든 나에게 유리한 방향을 먼저 계산한다",
        "options": ["전혀 아니다", "아니다", "그렇다", "매우 그렇다"],
    },
    {
        "id": "Q16",
        "section": "mach",
        "text": "16. 사람들과 가까워질 때 나에게 도움이 될지를 생각하게 된다",
        "options": ["전혀 아니다", "아니다", "그렇다", "매우 그렇다"],
    },
]

# ==========================================================
# 5~12번 문항 → SO / HS / AV / OR 매핑
#   - SO: 자기과시
#   - HS: 정반응(상황판단)
#   - AV: 회피
#   - OR: 과잉반응/과잉해석
# ==========================================================

SITU_CATEGORY = {
    "Q5":  {1: "SO", 2: "AV", 3: "OR", 4: "HS"},
    "Q6":  {1: "AV", 2: "SO", 3: "HS", 4: "OR"},
    "Q7":  {1: "AV", 2: "HS", 3: "SO", 4: "OR"},
    "Q8":  {1: "AV", 2: "HS", 3: "SO", 4: "OR"},
    "Q9":  {1: "SO", 2: "AV", 3: "OR", 4: "HS"},
    "Q10": {1: "SO", 2: "AV", 3: "OR", 4: "HS"},
    "Q11": {1: "AV", 2: "AV", 3: "SO", 4: "HS"},
    "Q12": {1: "SO", 2: "HS", 3: "AV", 4: "OR"},
}


def situ_weight(qid: str, cat: str, opt_idx: int) -> float:
    """
    일반 상황 vs 교묘 상황 가중치.
    - Q5~8: 1.0
    - Q9~12: 자기과시(SO) / 정반응(HS) 가중치 2.0
             (Q12 과잉해석 OR(4번)은 추가 가중치 2.0 유지)
    → 패턴 점수용(로그/추후 분석용)이고,
      동물 분류는 '개수 기반' 규칙으로 따로 갑니다.
    """
    if qid in ("Q5", "Q6", "Q7", "Q8"):
        return 1.0
    if qid in ("Q9", "Q10", "Q11", "Q12"):
        if cat in ("SO", "HS"):
            return 2.0
        if qid == "Q12" and opt_idx == 4:
            return 2.0
        return 1.0
    return 1.0


# ==========================================================
# 채점 로직 (네가 말한 규칙 그대로 + 레서판다 회색지대)
# ==========================================================

def compute_scores(answer_dict):
    # 1) 자기/타인 리포트 평균 (1~4)
    self_vals = [answer_dict.get("Q1", 0), answer_dict.get("Q2", 0)]
    other_vals = [answer_dict.get("Q3", 0), answer_dict.get("Q4", 0)]
    self_mean = sum(self_vals) / 2.0
    other_mean = sum(other_vals) / 2.0

    self_high = self_mean >= 3.0
    other_high = other_mean >= 3.0
    self_low = self_mean < 3.0
    other_low = other_mean < 3.0

    # 2) SITU 패턴 – 점수(가중치) + 개수 둘 다 계산
    pattern_scores = {"SO": 0.0, "HS": 0.0, "AV": 0.0, "OR": 0.0}
    cnt = {"SO": 0, "HS": 0, "AV": 0, "OR": 0}
    total_cnt = 0

    for qid in [f"Q{i}" for i in range(5, 13)]:
        idx = answer_dict.get(qid)
        if not idx:
            continue
        cat = SITU_CATEGORY.get(qid, {}).get(idx)
        if not cat:
            continue

        total_cnt += 1
        cnt[cat] += 1

        w = situ_weight(qid, cat, idx)
        pattern_scores[cat] += w

    n_good = cnt["HS"]    # 정반응 = 눈치
    n_avoid = cnt["AV"]   # 회피
    n_show = cnt["SO"]    # 자기과시
    n_over = cnt["OR"]    # 과잉해석

    # 3) 마키아벨리즘 (0~12)
    mach_score = 0
    for qid in [f"Q{i}" for i in range(13, 17)]:
        val = answer_dict.get(qid)
        if not val:
            continue
        mach_score += (val - 1)

    mach_high = mach_score >= 8
    mach_level = "H" if mach_high else "L"
    mach_mid = 2 <= mach_score <= 9
    mach_low = mach_score < 5

    # =====================================================
    # 4) trait_code (패턴 요약용) – 기존 구조 유지
    #    (동물 분류는 아래에서 override)
    # =====================================================

    scores_sorted = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
    top_trait, top_score = scores_sorted[0]
    second_trait, second_score = scores_sorted[1]
    gap = top_score - second_score
    total_signal = sum(pattern_scores.values())

    # (A) 비둘기 LOW 조건 – 전체 시그널 약하고 자기/타인 평가도 낮음
    if total_signal < 4.0 and self_mean < 2.2 and other_mean < 2.2:
        trait_code = "LOW"

    # (B) MIX 조건 – 골고루 낮은 케이스
    elif gap < 0.4 and top_score < 3.0:
        if top_score >= 3.3:
            trait_code = f"{top_trait}-L"
        else:
            trait_code = "MIX"

    # (C) 일반 H / L (역치 빡세게 4.5 유지)
    else:
        level = "H" if top_score >= 4.5 else "L"
        trait_code = f"{top_trait}-{level}"

    # (D) 극단 회피형 → LOW
    only_av = (
        pattern_scores["AV"] > 0
        and pattern_scores["SO"] == 0
        and pattern_scores["HS"] == 0
        and pattern_scores["OR"] == 0
    )
    if only_av and pattern_scores["AV"] >= 6.0 and self_mean <= 2.5 and other_mean <= 2.5:
        trait_code = "LOW"

    # =====================================================
    # 5) 동물 분류 – 네가 말한 규칙 그대로 구현
    # =====================================================

    animal_code = None

    # 눈치 기준: "눈치 좋고는 4개가 정반응"
    high_nunchi = (n_good >= 4)

    # 5-1) 비둘기 – 모든 기능 낮 + 눈치 0 + 회피 위주
    if animal_code is None and total_cnt > 0:
        wrong_cnt = total_cnt - n_good
        avoid_major = (wrong_cnt > 0 and n_avoid * 2 >= wrong_cnt)
        # "모든 기능이 다 낮아야 해" → 자기/타인 낮 + 마키아도 낮/중
        if (
            n_good == 0
            and self_mean < 2.5
            and other_mean < 2.5
            and n_avoid >= 3
            and avoid_major
            and mach_score <= 7
        ):
            animal_code = "PIG-C"  # 도시 비둘기

    # 5-2) 하이 눈치 루트 (흑표범 / 살쾡이 / 햄스터)
    if animal_code is None and high_nunchi:
        # 눈치 좋고 나도 높게, 남도 높게, 마키아 높음 => 흑표범
        if mach_high and self_high and other_high:
            animal_code = "HNS-C"
        # 눈치 좋고 나도 낮게, 남도 낮게, 마키아 높음 => 살쾡이
        elif mach_high and self_low and other_low:
            animal_code = "LMR-C"
        # 그 외 하이눈치인데 (마키아 낮거나 / 평가 애매) => 햄스터
        else:
            animal_code = "HLS-S"

    # 5-3) 나무늘보 – 눈치 2개 이상 정반응 + 회피 2개 이상 + 자기/타인 낮음
    if animal_code is None and n_good >= 2 and n_avoid >= 2 and self_low and other_low:
        animal_code = "LLS-S"

    # 5-4) 라쿤 – 눈치 3개 이하 + 자기과시 ≥ 50% + 자기/타인 높음 + 마키아 높음
    if animal_code is None and total_cnt > 0 and n_good <= 3:
        show_major = (n_show * 2 >= total_cnt)
        if show_major and self_high and other_high and mach_high:
            animal_code = "LOR-C"

    # 5-5) 미어캣 – 위 조건 + 마키아 낮음/중간
    if animal_code is None and total_cnt > 0 and n_good <= 3:
        show_major = (n_show * 2 >= total_cnt)
        if show_major and self_high and other_high and not mach_high:
            animal_code = "LOS-C"

    # 5-6) 고양이 – 눈치 3개 이상 + 자기과시 0 + 과잉해석 50% 이상 + 자기/타인 높음 + 마키아 높음
    if animal_code is None and total_cnt > 0 and n_good >= 3 and n_show == 0:
        over_major = (n_over * 2 >= total_cnt)
        if over_major and self_high and other_high and mach_high:
            animal_code = "HMR-S"

    # 5-7) 사슴 – 위와 같지만 마키아 낮음/중간
    if animal_code is None and total_cnt > 0 and n_good >= 3 and n_show == 0:
        over_major = (n_over * 2 >= total_cnt)
        if over_major and self_high and other_high and not mach_high:
            animal_code = "HMR-C"

    # 5-8) 여우 – 애매한 불안정: 어느 정도 눈치 + 과잉해석 섞임 + 평가/마키아 중간
    if animal_code is None and total_cnt > 0:
        some_nunchi = (n_good >= 1)
        some_over = (n_over >= 1)
        mid_eval = (2.0 <= self_mean <= 3.5) or (2.0 <= other_mean <= 3.5)
        if some_nunchi and some_over and mach_mid and mid_eval:
            animal_code = "HNR-C"

    # 5-9) 나머지 전부 → 레서판다 (회색지대)
    if animal_code is None:
        animal_code = "REDPANDA-C"

    # trait_code는 기존 TRAIT_TO_ANIMAL 기준으로 역매핑 시도
    trait_code = None
    try:
        for t_code, a_code in TRAIT_TO_ANIMAL.items():
            if a_code == animal_code:
                trait_code = t_code
                break
    except NameError:
        trait_code = None

    if trait_code is None:
        # 못 찾으면 MIX로 처리 (레이블용)
        trait_code = "MIX"

    return {
        "self_mean": self_mean,
        "other_mean": other_mean,
        "pattern_scores": pattern_scores,
        "mach_score": mach_score,
        "mach_level": mach_level,
        "trait_code": trait_code,
        "animal_code": animal_code,
        # 디버깅용 카운트
        "n_good": n_good,
        "n_avoid": n_avoid,
        "n_show": n_show,
        "n_over": n_over,
    }


# ==========================================================
# 로그 저장
# ==========================================================

def log_response(age_group, gender, answer_dict, score_dict):
    try:
        row = {
            "timestamp_utc": datetime.utcnow().isoformat(),
            "age_group": age_group,
            "gender": gender,
            "self_mean": f"{score_dict['self_mean']:.2f}",
            "other_mean": f"{score_dict['other_mean']:.2f}",
            "SO_score": f"{score_dict['pattern_scores']['SO']:.2f}",
            "HS_score": f"{score_dict['pattern_scores']['HS']:.2f}",
            "AV_score": f"{score_dict['pattern_scores']['AV']:.2f}",
            "OR_score": f"{score_dict['pattern_scores']['OR']:.2f}",
            "mach_score": f"{score_dict['mach_score']:.2f}",
            "mach_level": score_dict["mach_level"],
            "trait_code": score_dict["trait_code"],
            "animal_code": score_dict["animal_code"],
            "n_good": score_dict.get("n_good", ""),
            "n_avoid": score_dict.get("n_avoid", ""),
            "n_show": score_dict.get("n_show", ""),
            "n_over": score_dict.get("n_over", ""),
        }

        for q in QUESTIONS:
            qid = q["id"]
            row[qid] = answer_dict.get(qid, "")

        file_exists = os.path.isfile(CSV_PATH)
        fieldnames = list(row.keys())

        with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(row)

        print(f"✅ 데이터 저장 완료: {CSV_PATH}")
    except Exception as e:
        print(f"❌ 로그 저장 오류: {e}")


# ==========================================================
# 결과 텍스트 빌더
# ==========================================================

def build_profile_text(code: str) -> str:
    # code는 animal_code (HNS-C, LMR-C, REDPANDA-C 등)
    detail = TYPE_DETAIL.get(code, {})

    # profile(긴 설명)이 있으면 그걸 우선 사용, 없으면 특성(짧은 설명)로 fallback
    긴설명 = detail.get("profile", detail.get("특성", ""))

    혼잣말 = detail.get("혼잣말", "")
    others = detail.get("다른 사람이 보는 나", "")
    ai = detail.get("AI_칭찬", "")
    키워드 = " ".join(detail.get("키워드", []))

    profile = f"""[특성]
{긴설명}
[내 속마음]
{혼잣말}
[다른 사람이 보는 나]
{others}
[AI 한 줄 칭찬]
{ai}
[키워드]
{키워드}
"""
    return profile

def build_song_html(code: str) -> str:
    """
    타입별 노래 추천 박스 HTML 생성
    - TYPE_DETAIL[code]["songs"]가 있으면 최대 2곡까지 렌더링
    - 없으면 아무 것도 안 띄움
    """
    detail = TYPE_DETAIL.get(code, {})
    songs = detail.get("songs")

    # 노래 정보가 없으면 표시 안 함
    if not songs or not isinstance(songs, list):
        return ""

    # 최대 2곡만 보여주기
    songs = songs[:2]

    items_html = ""
    for s in songs:
        title = (s.get("title") or "").strip()
        url = (s.get("url") or "").strip()
        desc = (s.get("desc") or "").strip()

        if not title:
            continue

        # 링크가 있으면 a 태그, 없으면 텍스트만
        if url:
            title_html = (
                f'<a href="{url}" target="_blank" '
                f'style="color:#f5576c; font-weight:700; text-decoration:none;">'
                f'{title}</a>'
            )
        else:
            title_html = f'<span style="color:#f5576c; font-weight:700;">{title}</span>'

        desc_html = (
            f'<div style="font-size:0.92em; color:#495057; '
            f'line-height:1.6; margin-top:3px;">{desc}</div>'
            if desc
            else ""
        )

        items_html += f"""
        <li style="margin-bottom:10px;">
          {title_html}
          {desc_html}
        </li>
        """

    if not items_html.strip():
        return ""

    song_html = f"""
    <div style="background: linear-gradient(135deg, #fff4e6 0%, #ffe8cc 100%);
                padding: 14px 14px 14px 14px; border-radius: 16px;
                border: 2px solid #ffc078; margin: 0 0 16px 0; text-align:left;">
      <div style="font-weight:800; font-size:1.02em; color:#f08c00; margin-bottom:6px;">
        🎧 이 타입과 어울리는 플레이리스트
      </div>
      <ul style="padding-left:18px; margin:6px 0 0 0; list-style-type:disc;">
        {items_html}
      </ul>
    </div>
    """
    return song_html


def process_test(age_group, gender, *answers):
    """
    메인 처리 로직:
    - 연령/성별 체크
    - 응답 → answer_dict로 매핑
    - 점수 계산 → animal_code, trait_code
    - 결과 HTML 생성 (타입 설명 + 노래 + 궁합친구 + 프로필)
    """
    # -------------------------------
    # 1) 기본 입력 검증
    # -------------------------------
    if not age_group or str(age_group).strip() == "":
        return False, "❌ 연령대를 선택해주세요."
    if not gender or str(gender).strip() == "":
        return False, "❌ 성별을 선택해주세요."

    # -------------------------------
    # 2) 응답 수집 (QUESTIONS와 매핑)
    # -------------------------------
    answer_dict = {}
    for i, q in enumerate(QUESTIONS):
        if i >= len(answers):
            continue

        sel = answers[i]

        # checkbox / multiselect 대응: 1개만 허용
        if isinstance(sel, list):
            if len(sel) > 1:
                return False, f"❌ '{q['text']}' 문항은 하나만 선택할 수 있어요."
            sel = sel[0] if sel else None

        if not sel:
            continue

        try:
            # options 리스트에서 몇 번째인지 → 1,2,3,4 점수
            idx = q["options"].index(sel) + 1
        except ValueError:
            continue

        answer_dict[q["id"]] = idx

    # 문항 일부라도 비어 있으면 에러
    if len(answer_dict) < len(QUESTIONS):
        return False, "❌ 모든 문항에 응답해 주세요!"

    # -------------------------------
    # 3) 점수 계산 및 타입 결정
    # -------------------------------
    scores = compute_scores(answer_dict)
    animal_code = scores.get("animal_code")
    trait_code = scores.get("trait_code")

    detail = TYPE_DETAIL.get(animal_code, {})
    title = detail.get("title", "❓ 알 수 없는 타입")
    desc = detail.get("특성", "")
    animal_img = ANIMAL_IMAGES.get(animal_code, "")

    trait_label = TRAIT_LABELS.get(trait_code, "혼합형")
    animal_profile = build_profile_text(animal_code)
    song_html = build_song_html(animal_code)      # 🎧 타입별 노래 추천
    match_html = build_match_html(animal_code)    # 🤝 궁합 친구 카드

    # -------------------------------
    # 4) 응답 로그 저장
    # -------------------------------
    log_response(age_group, gender, answer_dict, scores)

    # -------------------------------
    # 5) 결과 HTML 구성
    # -------------------------------
    result_html = f"""
<div style="text-align: center; padding: 32px 12px 36px 12px; 
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
            border-radius: 24px; margin: 8px 0 18px 0; 
            box-shadow: 0 18px 40px rgba(240,147,251,0.35); 
            font-family: 'Noto Sans KR', 'Noto Sans', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
            box-sizing: border-box;">
  <h1 style="color: #fff; font-size: 2.1em; margin: 0 0 8px 0; font-weight: 900; text-shadow: 1px 2px 6px rgba(0,0,0,0.35);">
    🎉 당신을 닮은 동물은...
  </h1>
  <p style="color: rgba(255,255,255,0.9); margin: 0 0 20px 0; font-size: 1em;">
    (주요 패턴: <b>{trait_label}</b>)
  </p>
  <div style="background: rgba(255,255,255,0.96); padding: 24px 16px 28px 16px; border-radius: 22px; margin: 0 auto; max-width: 640px; box-shadow: 0 8px 26px rgba(0,0,0,0.18);">
    <h2 style="color: #f5576c; font-size: 2em; margin: 0 0 14px 0; font-weight: 900;">
      {title}
    </h2>
    <img src="{animal_img}" alt="{title}"
         style="width: 220px; height: 220px;
                max-width: 60vw; max-height: 60vw;
                object-fit: contain;
                margin: 0 auto 18px auto; display: block;
                border-radius: 18px; box-shadow: 0 6px 20px rgba(0,0,0,0.15);" />
    <div style="background: linear-gradient(135deg, #fff5f5 0%, #ffe5e5 100%);
                padding: 16px 12px; border-radius: 18px;
                margin: 4px 0 20px 0; border: 2px solid #ffc9c9;">
      <p style="color: #495057; font-size: 1.0em; line-height: 1.7; margin: 0;
                font-weight: 500; white-space: pre-line;">
{desc}
      </p>
    </div>
    {song_html}   <!-- 🎧 타입별 플레이리스트 -->
    {match_html}  <!-- 🤝 궁합 친구 박스 -->
    <div style="border-top: 2px solid #f093fb; margin: 18px 0 16px 0;"></div>
    <h3 style="color: #f5576c; font-size: 1.35em; margin: 0 0 12px 0; font-weight: 800;">
      {title} 프로필
    </h3>
    <div style="background: #ffffff; padding: 16px 12px; border-radius: 15px;
                border: 2px solid #f093fb; text-align: left;">
      <p style="color: #495057; font-size: 0.98em; line-height: 1.8; margin: 0;
                white-space: pre-line;">
{animal_profile}
      </p>
    </div>
  </div>
</div>
"""
    return True, result_html


# ==========================================================
# Gradio에서 페이지 전환처럼 보이게 하는 wrapper
# ==========================================================

def process_and_route(age_group, gender, *answers):
    success, html_or_error = process_test(age_group, gender, *answers)

    if not success:
        # 에러도 result_html 안에 그냥 보여 주도록
        error_html = f"<div style='color:red; font-size:1.02em; font-weight:600; margin-bottom:10px;'>{html_or_error}</div>"
        return (
            gr.update(value=error_html, visible=True),  # 결과 영역: 에러 메시지 보여줌
            gr.update(visible=True),                    # 질문 영역: 계속 보이게
        )
    else:
        # 정상 결과일 때는 질문 영역 숨기고 결과만 보여주기
        return (
            gr.update(value=html_or_error, visible=True),  # 결과 HTML 표시
            gr.update(visible=False),                      # 질문 영역 숨기기
        )

# ==========================================================
# 관리자 다운로드 (PW = NO1JAYLAYDOWN)
# ==========================================================

ADMIN_PW = "NO1JAYLAYDOWN"

def admin_download(pw):
    pw = (pw or "").strip()

    if pw != ADMIN_PW:
        msg = "<span style='color:red; font-weight:600;'>❌ 비밀번호가 올바르지 않습니다.</span>"
        return msg, None

    if not os.path.exists(CSV_PATH):
        msg = "<span style='color:#495057;'>아직 저장된 데이터가 없습니다.</span>"
        return msg, None

    msg = "<span style='color:green; font-weight:600;'>✅ CSV 파일을 다운로드할 수 있습니다.</span>"
    return msg, CSV_PATH


# ==========================================================
# 🎨 UI 전체 개편 - custom CSS (최종)
# ==========================================================

custom_css = """
/* 전체 레이아웃 (기존 유지) */
.gradio-container {
    font-family: "Noto Sans KR", sans-serif;
    max-width: 760px !important;
    margin: 0 auto !important;
    padding: 8px !important;
    background: transparent !important;
}
/* 기본 박스 제거 (기존 유지) */
.gr-block {
    background: transparent !important;
    box-shadow: none !important;
}
/* 문항 박스 (기존 유지) */
.q-block {
    background: #f3e8ff !important;
    border-radius: 14px !important;
    border: 1px solid #e5d4ff !important;
    padding: 18px !important;
    margin: 18px 0 !important;
}
/* 문항 텍스트 (기존 유지) */
.q-label {
    font-weight: 700;
    font-size: 1.05em;
    margin-bottom: 12px;
}
/* 보기 세로 정렬 (기존 유지) */
.q-radio .wrap,
.q-radio .gr-radio {
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 8px !important;
}
/* 제출 버튼 (기존 유지) */
.gr-button-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    padding: 14px !important;
    border-radius: 12px !important;
    border: 0 !important;
    font-weight: 800 !important;
    font-size: 1.05em !important;
}
/* =========================
   📱 모바일(폰) 전용 오버라이드
   - 아이폰/갤럭시 세로 기준 (가로 <= 540px)
   ========================= */
@media (max-width: 540px) {
    /* 폰에서는 화면 폭 꽉 채우기 */
    .gradio-container {
        max-width: 100% !important;
        width: 100% !important;
        padding: 10px 10px !important;
    }
    /* 문항 카드 살짝 컴팩트하게 */
    .q-block {
        margin: 12px 0 !important;
        padding: 14px !important;
    }
    .q-label {
        font-size: 0.98em;
        line-height: 1.5;
    }
    .q-radio .wrap,
    .q-radio .gr-radio {
        gap: 6px !important;
    }
    /* 버튼은 폰에서 가로 꽉 채우기 */
    .gr-button-primary {
        width: 100% !important;
        padding: 12px !important;
        font-size: 1.0em !important;
    }
}
"""

# ==========================================================
# ✨ Gradio UI 전체 (완성본)
# ==========================================================

with gr.Blocks(
    theme=gr.themes.Soft(primary_hue="purple", secondary_hue="pink"),
    css=custom_css,
    title="나에게 어울리는 동물 테스트 🐾"
) as demo:

    # 상단 헤더 (원래 버전 복원)
    gr.HTML(
        """
    <div style="text-align: center; padding: 26px 16px 22px 16px; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 20px; margin-bottom: 18px; 
                box-shadow: 0 12px 24px rgba(0,0,0,0.15); color: white;">
        <h1 style="margin: 0; font-size: 2em; font-weight: 900;">동물 테스트 🐾</h1>
        <p style="margin-top: 6px; font-size: 1.1em;">
            16문항으로 알아보는 나의 상황 판단 · 감정 캐치 타입
        </p>
        <div style="display: flex; justify-content: center; gap: 10px; margin-top: 10px; flex-wrap: wrap;">
            <div style="background: rgba(255,255,255,0.18); padding: 6px 14px; border-radius: 999px; font-size: 0.85em; font-weight: 600;">
                📝 총 16문항
            </div>
            <div style="background: rgba(255,255,255,0.18); padding: 6px 14px; border-radius: 999px; font-size: 0.85em; font-weight: 600;">
                ⏱️ 예상 소요 시간 약 5분
            </div>
            <div style="background: rgba(255,255,255,0.18); padding: 6px 14px; border-radius: 999px; font-size: 0.85em; font-weight: 600;">
                ✨ 기획·제작: Jay
            </div>
        </div>
        <p style="margin-top: 8px; font-size: 0.8em; opacity: 0.85;">
            * 재미 + 자기이해용 테스트입니다. 편하게 직관대로 골라주세요 :)
        </p>
    </div>
    """
    )

    question_blocks = []

    # 문항 영역
    with gr.Column(visible=True) as question_area:

        # 기본정보: 별도 박스 없이 드롭다운 두 개
        with gr.Row():
            age = gr.Dropdown(
                ["10대", "20대", "30대", "40대", "50대 이상"],
                label="연령대",
                interactive=True,
            )
            gender = gr.Dropdown(
                ["여성", "남성", "기타"],
                label="성별",
                interactive=True,
            )

        # 16문항 (연보라 q-block)
        for q in QUESTIONS:
            with gr.Group(elem_classes="q-block"):
                gr.HTML(f'<div class="q-label">{q["text"]}</div>')
                comp = gr.Radio(
                    q["options"],
                    label="",
                    elem_classes="q-radio",
                )
                question_blocks.append(comp)

        submit_btn = gr.Button("결과 확인하기", elem_classes="gr-button-primary")

    # 결과 화면
    result_html = gr.HTML(visible=False)

    # 관리자 영역
    with gr.Accordion("🔧관리자 전용", open=False):
        admin_pw = gr.Textbox(label="관리자 비밀번호", type="password")
        admin_msg = gr.HTML()
        download_btn = gr.File(label="데이터 다운로드", visible=False)

    # 제출 → 결과
    submit_btn.click(
        fn=process_and_route,
        inputs=[age, gender] + question_blocks,
        outputs=[result_html, question_area],
    )

    # 관리자 다운로드
    admin_pw.change(
        fn=admin_download,
        inputs=admin_pw,
        outputs=[admin_msg, download_btn],
    )


if __name__ == "__main__":
    demo.launch()
