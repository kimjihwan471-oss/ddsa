# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random
import re
import webbrowser
from urllib.parse import urlparse

HOST = "127.0.0.1"
PORT = 8000


# ============================================================
# 좋은말 데이터
# ============================================================

MESSAGES = {
    "시험": [
        "한 번의 시험이 당신의 가능성을 정하는 것은 아니에요. 오늘까지 노력한 시간도 분명히 의미가 있어요.",
        "잘하지 못한 하루가 있어도 괜찮아요. 다시 시작할 수 있는 내일은 아직 남아 있으니까요.",
        "결과보다 중요한 건 포기하지 않고 여기까지 온 마음이에요. 당신은 생각보다 잘하고 있어요.",
        "이번에 원하는 결과가 아니었더라도, 그것이 당신의 가치까지 낮추는 것은 아니에요."
    ],

    "공부": [
        "오늘 조금밖에 하지 못했다고 해서 아무것도 하지 않은 건 아니에요. 작은 걸음도 앞으로 가는 걸음이에요.",
        "남들보다 느린 것 같아도 괜찮아요. 사람마다 자신의 속도가 있으니까요.",
        "지금 힘들다는 건 그만큼 열심히 해왔다는 뜻일 수도 있어요. 잠시 쉬어가도 괜찮아요.",
        "완벽하게 해내려고 하지 않아도 돼요. 오늘 할 수 있는 만큼이면 충분해요."
    ],

    "친구": [
        "모든 사람과 잘 지낼 필요는 없어요. 당신을 있는 그대로 아껴주는 사람은 분명히 있어요.",
        "친구와의 한 번의 갈등이 지금까지의 모든 좋은 순간을 없애는 것은 아니에요.",
        "상대의 반응 하나만으로 당신의 가치를 판단하지 않았으면 좋겠어요. 당신은 그보다 훨씬 큰 사람이에요.",
        "관계가 잠시 멀어지는 순간에도 당신의 소중함은 변하지 않아요."
    ],

    "싸움": [
        "마음이 복잡할 때 바로 모든 답을 찾지 않아도 괜찮아요. 조금 진정할 시간을 가져도 돼요.",
        "한 번의 말다툼으로 관계의 모든 것이 결정되지는 않아요. 시간이 지나면 보이는 것도 달라질 수 있어요.",
        "지금 속상한 마음을 억지로 괜찮다고 만들 필요는 없어요. 속상할 만큼 속상해도 괜찮아요."
    ],

    "학교": [
        "학교에서 있었던 일이 하루 전체를 결정하게 두지 않아도 괜찮아요. 집에 돌아오면 다시 당신의 시간이 시작돼요.",
        "오늘 학교에서 힘든 일이 있었다면, 그 하루를 견뎌낸 것만으로도 충분히 잘한 거예요.",
        "모두에게 좋은 모습을 보여주려고 애쓰지 않아도 돼요. 있는 그대로의 당신도 충분해요.",
        "오늘이 힘들었다고 내일도 반드시 힘든 것은 아니에요. 하루는 다시 시작될 수 있어요."
    ],

    "실수": [
        "실수는 당신이 부족하다는 증거가 아니라, 무언가를 배우고 있다는 흔적일 수 있어요.",
        "그때의 나에게 너무 엄격하지 않았으면 좋겠어요. 누구나 실수하면서 자라니까요.",
        "지나간 한 장면을 계속 되돌려 보지 않아도 돼요. 이제는 다음 장면을 만들어가면 돼요.",
        "완벽한 사람은 없어요. 실수한 당신도 여전히 충분히 소중한 사람입니다."
    ],

    "실패": [
        "실패했다고 해서 당신이 실패한 사람이 되는 건 아니에요. 하나의 결과일 뿐이에요.",
        "넘어진 자리에서 잠시 쉬어도 괜찮아요. 다시 일어나는 시간까지도 당신의 과정이에요.",
        "이번에 잘되지 않았다는 사실과 앞으로도 잘되지 않을 거라는 생각은 전혀 다른 이야기예요."
    ],

    "지침": [
        "계속 달리지 않아도 괜찮아요. 잠시 멈추는 것도 앞으로 나아가기 위한 시간이니까요.",
        "오늘은 아무것도 완벽하게 해내지 않아도 괜찮아요. 당신에게도 쉬는 시간이 필요해요.",
        "지친 마음을 억지로 끌고 가지 않아도 돼요. 잠깐 쉬고 다시 생각해도 늦지 않아요.",
        "많이 지쳤다면 스스로에게 조금 더 다정해져 주세요. 당신도 위로받을 사람이니까요."
    ],

    "불안": [
        "아직 일어나지 않은 일을 지금 모두 해결하려고 하지 않아도 괜찮아요. 오늘 할 수 있는 것만 생각해요.",
        "걱정이 많아지는 순간에는 모든 것이 더 크게 보일 수 있어요. 천천히 하나씩 바라봐도 괜찮아요.",
        "지금 불안하다고 해서 앞으로도 계속 불안한 것은 아니에요. 마음은 생각보다 많이 변할 수 있어요.",
        "모든 답을 지금 당장 알 필요는 없어요. 모르는 채로 한 걸음씩 가도 괜찮아요."
    ],

    "외로움": [
        "지금 혼자라고 느껴져도 당신이 혼자서 모든 것을 견뎌야 한다는 뜻은 아니에요.",
        "누군가와 연결되고 싶은 마음은 아주 자연스러운 마음이에요. 그런 마음을 부끄러워하지 않아도 돼요.",
        "당신의 이야기를 들어줄 가치가 없는 사람은 없어요. 당신의 마음도 충분히 귀하게 다뤄져야 해요."
    ],

    "자신감": [
        "다른 사람과 비교하지 않아도 괜찮아요. 당신에게는 당신만의 속도와 이야기가 있어요.",
        "당신이 아직 발견하지 못한 장점도 분명히 있어요. 지금의 모습만으로 자신을 판단하지 마세요.",
        "잘하는 것만이 당신의 가치가 아니에요. 노력하고, 배우고, 다시 해보는 마음도 멋진 힘이에요.",
        "스스로를 믿기 어려운 날에는 적어도 스스로를 포기하지 않는 것부터 시작해도 괜찮아요."
    ],

    "가족": [
        "가까운 사람과의 갈등일수록 마음이 더 아플 수 있어요. 지금 힘든 마음은 이상한 것이 아니에요.",
        "가족이라고 해서 항상 서로의 마음을 완벽하게 이해할 수 있는 것은 아니에요.",
        "지금 당장 모든 문제를 해결하지 않아도 괜찮아요. 마음이 조금 편해진 뒤 이야기해도 돼요."
    ],

    "미래": [
        "아직 정해지지 않은 미래를 지금의 모습만 보고 판단하지 않았으면 좋겠어요.",
        "앞으로 어떤 일이 생길지는 아무도 완벽하게 알 수 없어요. 그래서 아직 좋은 가능성도 많이 남아 있어요.",
        "조금 늦게 가도 괜찮아요. 중요한 건 남들과 같은 길이 아니라 당신에게 맞는 길을 찾아가는 거예요."
    ],

    "일반": [
        "오늘의 당신에게 꼭 필요한 건 완벽함이 아니라 조금의 여유일지도 몰라요. 천천히 해도 괜찮아요.",
        "지금의 힘든 감정이 영원히 계속되는 것은 아니에요. 마음도 계절처럼 조금씩 변해가니까요.",
        "당신이 생각하는 것보다 당신은 많은 날을 잘 견뎌왔어요. 오늘도 여기까지 온 것만으로 충분해요.",
        "괜찮지 않은 날에는 괜찮은 척하지 않아도 돼요. 잠시 쉬어가는 것도 삶의 한 부분이에요.",
        "모든 것을 한 번에 해결하지 않아도 돼요. 오늘은 오늘만큼만 살아가도 충분해요.",
        "당신의 속도가 느려진다고 해서 당신의 가치까지 느려지는 것은 아니에요.",
        "지금의 나를 조금 부족하다고 느끼더라도, 그 모습까지 포함해서 당신은 소중한 사람이에요."
    ]
}


# ============================================================
# 상황 판단
# ============================================================

KEYWORDS = {
    "시험": ["시험", "점수", "성적", "기말", "중간고사", "모의고사", "등급"],
    "공부": ["공부", "숙제", "과제", "학원", "수업", "공부하기"],
    "친구": ["친구", "절친", "친한", "친구들", "왕따", "따돌림"],
    "싸움": ["싸웠", "싸움", "다퉜", "다툼", "화냈", "화났", "갈등"],
    "학교": ["학교", "선생님", "교실", "등교", "하교", "반", "학생"],
    "실수": ["실수", "잘못했", "망했", "망쳤", "후회", "부끄러", "창피"],
    "실패": ["실패", "떨어졌", "탈락", "안됐", "안되", "실패했"],
    "지침": ["힘들", "지쳤", "지쳐", "피곤", "지겨", "하기 싫", "귀찮", "번아웃"],
    "불안": ["불안", "걱정", "두려", "무서", "긴장", "초조", "떨려", "걱정돼"],
    "외로움": ["외로", "혼자", "쓸쓸", "고립", "아무도", "소외"],
    "자신감": ["자신감", "자존감", "부족", "못난", "잘하는 게", "잘하는것", "비교", "뒤처"],
    "가족": ["엄마", "아빠", "부모님", "가족", "형제", "동생", "언니", "오빠"],
    "미래": ["미래", "진로", "꿈", "대학", "취업", "앞으로", "장래"]
}


def detect_category(text):
    scores = {}

    for category, words in KEYWORDS.items():
        score = 0

        for word in words:
            if word in text:
                score += 1

        if score > 0:
            scores[category] = score

    if not scores:
        return "일반"

    return max(scores, key=scores.get)


def get_message(text, emotion):
    combined = text + " " + emotion

    category = detect_category(combined)

    messages = MESSAGES.get(category, MESSAGES["일반"])

    # 같은 문장이 연속해서 나오지 않도록 랜덤 선택
    return random.choice(messages)


# ============================================================
# HTML
# ============================================================

HTML = r'''
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>오늘의 한마디</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    font-family: "Malgun Gothic", "Apple SD Gothic Neo", sans-serif;
    background:
        radial-gradient(circle at 20% 20%, rgba(255,255,255,.9), transparent 30%),
        radial-gradient(circle at 80% 10%, rgba(220,230,255,.7), transparent 35%),
        linear-gradient(135deg, #eef3ff, #f8f3ff, #edf9ff);
    color: #34364a;
}

.container {
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
    padding: 55px 22px 60px;
}

.header {
    text-align: center;
    margin-bottom: 35px;
}

.small-title {
    font-size: 14px;
    color: #8b91aa;
    letter-spacing: 3px;
    margin-bottom: 12px;
}

h1 {
    font-size: 42px;
    margin: 0;
    color: #3d405b;
    font-weight: 700;
}

.subtitle {
    margin-top: 14px;
    color: #777d96;
    font-size: 16px;
    line-height: 1.7;
}

.card {
    background: rgba(255,255,255,.76);
    border: 1px solid rgba(255,255,255,.9);
    border-radius: 28px;
    padding: 34px;
    box-shadow: 0 15px 50px rgba(71,77,120,.12);
    backdrop-filter: blur(12px);
}

.label {
    font-size: 15px;
    font-weight: bold;
    color: #555b75;
    margin-bottom: 12px;
}

textarea {
    width: 100%;
    height: 180px;
    resize: vertical;
    border: 1px solid #e0e3ef;
    border-radius: 18px;
    background: rgba(250,251,255,.9);
    padding: 18px;
    font-size: 16px;
    font-family: inherit;
    outline: none;
    color: #3d405b;
    transition: .2s;
}

textarea:focus {
    border-color: #aeb8e8;
    box-shadow: 0 0 0 4px rgba(174,184,232,.15);
}

textarea::placeholder {
    color: #a9aec0;
    line-height: 1.7;
}

.emotions {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    margin: 15px 0 25px;
}

.emotion {
    border: 1px solid #e0e3ef;
    background: white;
    border-radius: 30px;
    padding: 10px 16px;
    cursor: pointer;
    font-size: 14px;
    color: #62687e;
    transition: .2s;
}

.emotion:hover {
    transform: translateY(-2px);
    border-color: #b8c0e8;
}

.emotion.selected {
    background: #e8ebff;
    border-color: #aeb7e8;
    color: #4c568f;
    font-weight: bold;
}

.button {
    width: 100%;
    border: 0;
    border-radius: 17px;
    padding: 17px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    color: white;
    background: linear-gradient(135deg, #8998dc, #a493d6);
    box-shadow: 0 10px 25px rgba(121,131,202,.25);
    transition: .2s;
}

.button:hover {
    transform: translateY(-2px);
    box-shadow: 0 13px 30px rgba(121,131,202,.3);
}

.button:active {
    transform: translateY(0);
}

.result {
    display: none;
    margin-top: 25px;
    padding: 28px;
    border-radius: 22px;
    background: linear-gradient(135deg, #f8f6ff, #f1f7ff);
    border: 1px solid #e2e5f4;
    animation: appear .45s ease;
}

.result.show {
    display: block;
}

.result-title {
    text-align: center;
    font-size: 14px;
    color: #888da5;
    margin-bottom: 16px;
}

.message {
    text-align: center;
    font-size: 20px;
    line-height: 1.8;
    color: #41455e;
    font-weight: 600;
    white-space: pre-line;
}

.again {
    display: block;
    margin: 22px auto 0;
    padding: 10px 18px;
    border-radius: 30px;
    border: 1px solid #dfe2ef;
    background: white;
    color: #69708a;
    cursor: pointer;
}

.again:hover {
    background: #f7f8fd;
}

.footer {
    text-align: center;
    margin-top: 30px;
    color: #a0a5b8;
    font-size: 12px;
    line-height: 1.7;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(12px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media (max-width: 600px) {

    .container {
        padding: 35px 15px;
    }

    h1 {
        font-size: 32px;
    }

    .card {
        padding: 22px;
        border-radius: 22px;
    }

    textarea {
        height: 160px;
    }

    .message {
        font-size: 18px;
    }
}

</style>
</head>

<body>

<div class="container">

    <div class="header">
        <div class="small-title">A LITTLE WORD FOR YOU</div>

        <h1>오늘의 한마디 🌿</h1>

        <div class="subtitle">
            마음이 조금 무거운 날,<br>
            당신에게 필요한 말을 찾아드릴게요.
        </div>
    </div>


    <div class="card">

        <div class="label">
            지금 어떤 일이 있었나요?
        </div>

        <textarea
            id="situation"
            placeholder="예시)
오늘 학교에서 발표를 했는데 너무 긴장했어.
말을 제대로 못한 것 같아서 계속 신경 쓰여..."
        ></textarea>


        <div class="label">
            지금 내 마음은 어떤가요?
        </div>

        <div class="emotions">

            <button class="emotion" data-emotion="슬퍼요">😢 슬퍼요</button>
            <button class="emotion" data-emotion="지쳤어요">😞 지쳤어요</button>
            <button class="emotion" data-emotion="답답해요">😣 답답해요</button>
            <button class="emotion" data-emotion="불안해요">😰 불안해요</button>
            <button class="emotion" data-emotion="화나요">😡 화나요</button>
            <button class="emotion" data-emotion="외로워요">🥺 외로워요</button>
            <button class="emotion" data-emotion="자신감이 없어요">😔 자신감이 없어요</button>
            <button class="emotion" data-emotion="그냥 그래요">🙂 그냥 그래요</button>

        </div>


        <button class="button" onclick="getGoodWord()">
            ✨ 나에게 필요한 말 받기
        </button>


        <div class="result" id="result">

            <div class="result-title">
                ✨ 지금 당신에게 전하고 싶은 말
            </div>

            <div class="message" id="message"></div>

            <button class="again" onclick="getGoodWord()">
                다른 말 하나 더 받기
            </button>

        </div>

    </div>


    <div class="footer">
        오늘도 여기까지 온 당신을 응원해요.<br>
        모든 것을 한 번에 해결하지 않아도 괜찮아요.
    </div>

</div>


<script>

let selectedEmotion = "";


// 감정 선택
document.querySelectorAll(".emotion").forEach(button => {

    button.addEventListener("click", function() {

        document.querySelectorAll(".emotion").forEach(btn => {
            btn.classList.remove("selected");
        });

        this.classList.add("selected");

        selectedEmotion = this.dataset.emotion;
    });

});


// 좋은말 요청
async function getGoodWord() {

    const situation =
        document.getElementById("situation").value.trim();

    if (!situation && !selectedEmotion) {

        alert("지금 어떤 마음인지 조금만 알려주세요 🌿");

        document.getElementById("situation").focus();

        return;
    }


    const response = await fetch("/goodword", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            situation: situation,
            emotion: selectedEmotion
        })

    });


    const data = await response.json();


    document.getElementById("message").textContent =
        data.message;


    const result =
        document.getElementById("result");

    result.classList.remove("show");

    // 애니메이션 다시 실행
    void result.offsetWidth;

    result.classList.add("show");

    result.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });
}

</script>

</body>
</html>
'''


# ============================================================
# 서버
# ============================================================

class Handler(BaseHTTPRequestHandler):

    def send_cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")


    def do_GET(self):

        path = urlparse(self.path).path

        if path == "/":

            content = HTML.encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()

            self.wfile.write(content)

        else:

            self.send_response(404)
            self.end_headers()


    def do_POST(self):

        path = urlparse(self.path).path

        if path != "/goodword":

            self.send_response(404)
            self.end_headers()
            return


        try:

            length = int(self.headers.get("Content-Length", 0))

            body = self.rfile.read(length)

            data = json.loads(body.decode("utf-8"))

            situation = data.get("situation", "")
            emotion = data.get("emotion", "")

            message = get_message(situation, emotion)

            result = json.dumps({
                "message": message
            }, ensure_ascii=False).encode("utf-8")


            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )

            self.send_header(
                "Content-Length",
                str(len(result))
            )

            self.end_headers()

            self.wfile.write(result)


        except Exception as e:

            result = json.dumps({
                "message": "괜찮아요. 잠시 천천히 숨을 고르고 다시 이야기해도 돼요."
            }, ensure_ascii=False).encode("utf-8")

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )

            self.send_header(
                "Content-Length",
                str(len(result))
            )

            self.end_headers()

            self.wfile.write(result)


# ============================================================
# 실행
# ============================================================

def main():

    server = HTTPServer((HOST, PORT), Handler)

    url = f"http://{HOST}:{PORT}"

    print("")
    print("=" * 55)
    print("       🌿 오늘의 한마디 웹사이트")
    print("=" * 55)
    print("")
    print(f"사이트 주소 : {url}")
    print("")
    print("브라우저가 자동으로 열립니다.")
    print("사이트를 종료하려면 이 창에서 Ctrl + C를 누르세요.")
    print("")

    webbrowser.open(url)

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        print("\n서버를 종료합니다.")

    finally:
        server.server_close()


if __name__ == "__main__":
    main()