# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random
import os
from urllib.parse import urlparse


# =========================================================
# Render 서버 설정
# =========================================================

HOST = "0.0.0.0"

# Render가 PORT 환경변수를 자동으로 넣어줌
PORT = int(os.environ.get("PORT", 8000))

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# =========================================================
# 좋은말 데이터
# =========================================================

MESSAGES = {

    "시험": [
        "한 번의 시험이 당신의 가능성을 정하는 것은 아니에요.\n오늘까지 노력한 시간도 분명히 의미가 있어요.",

        "원하는 결과가 나오지 않았다고 해서 당신의 가치까지 낮아지는 것은 아니에요.\n다시 시작할 수 있는 기회는 아직 많이 남아 있어요.",

        "시험 하나로 자신의 모든 가능성을 판단하지 마세요.\n당신에게는 아직 보여주지 않은 모습이 훨씬 많으니까요.",

        "이번 결과가 마음에 들지 않아도 괜찮아요.\n결과는 당신의 한 부분일 뿐, 당신의 전부가 아니에요."
    ],


    "공부": [
        "오늘 조금밖에 하지 못했다고 해서 아무것도 하지 않은 건 아니에요.\n작은 걸음도 분명 앞으로 가는 걸음이에요.",

        "남들보다 느린 것 같아도 괜찮아요.\n사람마다 자신의 속도가 있으니까요.",

        "완벽하게 해내려고 하지 않아도 괜찮아요.\n오늘 할 수 있는 만큼이면 충분해요.",

        "공부가 잘되지 않는 날도 있어요.\n그런 날의 당신까지 부족한 사람인 것은 아니에요."
    ],


    "친구": [
        "한 번의 갈등이 당신이라는 사람 전체를 설명해주지는 않아요.\n당신의 소중함은 그대로예요.",

        "모든 사람과 잘 지낼 필요는 없어요.\n당신을 있는 그대로 아껴주는 사람도 분명히 있어요.",

        "관계가 잠시 흔들리는 순간에도 당신의 가치는 변하지 않아요.\n조금 천천히 생각해도 괜찮아요.",

        "친구의 말이나 행동 하나가 당신의 가치를 결정하지 않아요.\n당신은 그보다 훨씬 더 많은 이야기를 가진 사람이에요."
    ],


    "싸움": [
        "지금 당장 모든 것을 해결하려고 하지 않아도 괜찮아요.\n마음이 조금 가라앉은 뒤 생각해도 늦지 않아요.",

        "속상한 마음을 억지로 괜찮다고 만들 필요는 없어요.\n지금은 그냥 속상해도 괜찮아요.",

        "한 번의 말다툼으로 관계의 모든 것이 결정되는 것은 아니에요.\n시간이 지나면 다르게 보이는 것도 있어요."
    ],


    "학교": [
        "오늘 학교에서 힘든 일이 있었다면,\n그 하루를 견뎌낸 것만으로도 충분히 잘한 거예요.",

        "학교에서 있었던 일이 하루 전체를 결정하게 두지 않아도 괜찮아요.\n오늘의 하루는 여기서 끝나고 다시 시작할 수 있어요.",

        "모두에게 좋은 모습을 보여주려고 애쓰지 않아도 돼요.\n있는 그대로의 당신도 충분히 소중해요.",

        "오늘 학교에서 조금 힘들었다면 잠시 내려놓아도 괜찮아요.\n내일은 또 다른 하루가 될 수 있으니까요."
    ],


    "실수": [
        "실수는 당신이 부족하다는 증거가 아니에요.\n무언가를 배우고 있다는 흔적일 수도 있어요.",

        "지나간 한 장면을 계속 되돌려 보지 않아도 괜찮아요.\n이제는 다음 장면을 만들어가면 돼요.",

        "그때의 나에게 너무 엄격하지 않았으면 좋겠어요.\n누구나 실수하면서 조금씩 자라니까요.",

        "한 번의 실수보다 그 이후의 당신이 더 중요해요.\n다시 해볼 기회는 아직 있어요."
    ],


    "실패": [
        "실패했다고 해서 당신이 실패한 사람이 되는 건 아니에요.\n그저 하나의 결과일 뿐이에요.",

        "이번에 잘되지 않았다는 사실과 앞으로도 잘되지 않을 거라는 생각은 전혀 다른 이야기예요.\n아직 많은 가능성이 남아 있어요.",

        "원했던 결과를 얻지 못한 날에도 배운 것은 남아요.\n그 경험은 언젠가 당신의 힘이 될 수 있어요."
    ],


    "지침": [
        "계속 달리지 않아도 괜찮아요.\n잠시 멈추는 것도 앞으로 나아가기 위한 시간이니까요.",

        "오늘은 아무것도 완벽하게 해내지 않아도 괜찮아요.\n당신에게도 쉬어갈 시간이 필요해요.",

        "많이 지쳤다면 스스로에게 조금 더 다정해져 주세요.\n당신도 위로받을 사람이니까요.",

        "쉬고 싶다는 마음은 나약함이 아니에요.\n지친 마음에도 휴식이 필요해요."
    ],


    "불안": [
        "아직 일어나지 않은 일을 지금 모두 해결하려고 하지 않아도 괜찮아요.\n오늘 할 수 있는 것만 생각해요.",

        "걱정이 많아지는 순간에는 모든 것이 더 크게 보일 수 있어요.\n천천히 하나씩 바라봐도 괜찮아요.",

        "모든 답을 지금 당장 알 필요는 없어요.\n모르는 채로 한 걸음씩 가도 괜찮아요.",

        "지금 불안하다는 것이 앞으로도 계속 불안할 거라는 뜻은 아니에요.\n마음은 생각보다 많이 변할 수 있어요."
    ],


    "외로움": [
        "지금 혼자라고 느껴져도 모든 것을 혼자 견뎌야 한다는 뜻은 아니에요.\n당신의 마음도 충분히 귀하게 다뤄져야 해요.",

        "누군가와 연결되고 싶은 마음은 아주 자연스러운 마음이에요.\n그런 마음을 부끄러워하지 않아도 괜찮아요.",

        "지금 외롭다는 이유만으로 당신이 사랑받지 못하는 사람인 것은 아니에요.\n당신의 소중함은 그대로예요."
    ],


    "자신감": [
        "다른 사람과 비교하지 않아도 괜찮아요.\n당신에게는 당신만의 속도와 이야기가 있어요.",

        "잘하는 것만이 당신의 가치가 아니에요.\n배우고 다시 해보는 마음도 아주 멋진 힘이에요.",

        "스스로를 믿기 어려운 날에는,\n적어도 스스로를 포기하지 않는 것부터 시작해도 괜찮아요.",

        "지금의 자신을 아직 완전히 알지 못할 뿐이에요.\n당신 안에는 앞으로 발견할 모습도 많이 남아 있어요."
    ],


    "가족": [
        "가까운 사람과의 갈등일수록 마음이 더 아플 수 있어요.\n지금 힘든 마음은 이상한 것이 아니에요.",

        "가족이라고 해서 항상 서로의 마음을 완벽하게 이해할 수 있는 것은 아니에요.\n조금씩 이야기해도 괜찮아요.",

        "지금 당장 모든 문제를 해결하지 않아도 괜찮아요.\n마음이 조금 편해진 뒤 이야기해도 늦지 않아요."
    ],


    "미래": [
        "아직 정해지지 않은 미래를 지금의 모습만 보고 판단하지 않았으면 좋겠어요.\n아직 만들어갈 수 있는 시간이 있으니까요.",

        "앞으로 어떤 일이 생길지는 아무도 완벽하게 알 수 없어요.\n그래서 아직 좋은 가능성도 많이 남아 있어요.",

        "조금 늦게 가도 괜찮아요.\n중요한 건 남들과 같은 속도가 아니라 나에게 맞는 길을 찾아가는 거예요."
    ],


    "일반": [
        "오늘의 당신에게 꼭 필요한 건 완벽함이 아니라 조금의 여유일지도 몰라요.\n천천히 해도 괜찮아요.",

        "지금의 힘든 감정이 영원히 계속되는 것은 아니에요.\n마음도 계절처럼 조금씩 변해가니까요.",

        "당신이 생각하는 것보다 많은 날을 잘 견뎌왔어요.\n오늘도 여기까지 온 것만으로 충분해요.",

        "괜찮지 않은 날에는 괜찮은 척하지 않아도 돼요.\n잠시 쉬어가는 것도 삶의 한 부분이에요.",

        "모든 것을 한 번에 해결하지 않아도 돼요.\n오늘은 오늘만큼만 해도 충분해요.",

        "당신의 속도가 느려진다고 해서 당신의 가치까지 느려지는 것은 아니에요.",

        "지금의 나를 조금 부족하다고 느끼더라도,\n그 모습까지 포함해서 당신은 소중한 사람이에요.",

        "오늘 하루를 완벽하게 보내지 않아도 괜찮아요.\n무사히 하루를 지나온 것만으로도 충분한 날이 있어요."
    ]

}


# =========================================================
# 키워드
# =========================================================

KEYWORDS = {

    "시험": [
        "시험",
        "점수",
        "성적",
        "기말",
        "중간고사",
        "모의고사",
        "등급"
    ],

    "공부": [
        "공부",
        "숙제",
        "과제",
        "학원",
        "수업"
    ],

    "친구": [
        "친구",
        "절친",
        "친한",
        "친구들",
        "왕따",
        "따돌림"
    ],

    "싸움": [
        "싸웠",
        "싸움",
        "다퉜",
        "다툼",
        "갈등",
        "화냈",
        "화났"
    ],

    "학교": [
        "학교",
        "선생님",
        "교실",
        "등교",
        "하교",
        "반"
    ],

    "실수": [
        "실수",
        "잘못했",
        "망했",
        "망쳤",
        "후회",
        "부끄러",
        "창피"
    ],

    "실패": [
        "실패",
        "떨어졌",
        "탈락",
        "안됐"
    ],

    "지침": [
        "힘들",
        "지쳤",
        "지쳐",
        "피곤",
        "지겨",
        "하기 싫",
        "귀찮",
        "번아웃"
    ],

    "불안": [
        "불안",
        "걱정",
        "두려",
        "무서",
        "긴장",
        "초조"
    ],

    "외로움": [
        "외로",
        "혼자",
        "쓸쓸",
        "고립",
        "아무도",
        "소외"
    ],

    "자신감": [
        "자신감",
        "자존감",
        "부족",
        "못난",
        "잘하는 게",
        "비교",
        "뒤처"
    ],

    "가족": [
        "엄마",
        "아빠",
        "부모님",
        "가족",
        "형제",
        "동생",
        "언니",
        "오빠"
    ],

    "미래": [
        "미래",
        "진로",
        "꿈",
        "대학",
        "취업",
        "앞으로",
        "장래"
    ]
}


# =========================================================
# 상황 분석
# =========================================================

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


    return max(
        scores,
        key=scores.get
    )


# =========================================================
# 좋은말 선택
# =========================================================

def generate_goodword(
    situation,
    emotion
):

    text = (
        situation
        + " "
        + emotion
    )

    category = detect_category(text)

    messages = MESSAGES.get(
        category,
        MESSAGES["일반"]
    )

    return random.choice(messages)


# =========================================================
# 파일 읽기
# =========================================================

def read_file(filename):

    path = os.path.join(
        BASE_DIR,
        filename
    )

    if not os.path.isfile(path):

        return None


    with open(
        path,
        "rb"
    ) as file:

        return file.read()


# =========================================================
# HTTP 서버
# =========================================================

class GoodWordHandler(
    BaseHTTPRequestHandler
):


    # -----------------------------------------------------
    # 공통 응답
    # -----------------------------------------------------

    def send_data(
        self,
        data,
        content_type,
        status=200
    ):

        self.send_response(status)

        self.send_header(
            "Content-Type",
            content_type
        )

        self.send_header(
            "Content-Length",
            str(len(data))
        )

        self.send_header(
            "Cache-Control",
            "no-cache"
        )

        self.end_headers()

        self.wfile.write(data)


    # -----------------------------------------------------
    # GET
    # -----------------------------------------------------

    def do_GET(self):

        path = urlparse(
            self.path
        ).path


        # 메인 페이지
        if path == "/":
            filename = "index.html"
            content_type = (
                "text/html; charset=utf-8"
            )


        # CSS
        elif path == "/style.css":
            filename = "style.css"
            content_type = (
                "text/css; charset=utf-8"
            )


        # JavaScript
        elif path == "/script.js":
            filename = "script.js"
            content_type = (
                "application/javascript; charset=utf-8"
            )


        # favicon 요청
        elif path == "/favicon.ico":

            self.send_data(
                b"",
                "image/x-icon",
                204
            )

            return


        else:

            self.send_data(
                b"Not Found",
                "text/plain; charset=utf-8",
                404
            )

            return


        data = read_file(filename)


        if data is None:

            error_message = (
                f"{filename} 파일을 찾을 수 없습니다."
            )

            self.send_data(
                error_message.encode("utf-8"),
                "text/plain; charset=utf-8",
                404
            )

            return


        self.send_data(
            data,
            content_type
        )


    # -----------------------------------------------------
    # POST
    # -----------------------------------------------------

    def do_POST(self):

        path = urlparse(
            self.path
        ).path


        if path != "/api/goodword":

            self.send_data(
                b"Not Found",
                "text/plain; charset=utf-8",
                404
            )

            return


        try:

            content_length = int(
                self.headers.get(
                    "Content-Length",
                    0
                )
            )


            # 너무 큰 요청 방지
            if content_length > 15000:

                self.send_data(
                    b"Request Too Large",
                    "text/plain; charset=utf-8",
                    413
                )

                return


            body = self.rfile.read(
                content_length
            )


            data = json.loads(
                body.decode("utf-8")
            )


            situation = str(
                data.get(
                    "situation",
                    ""
                )
            ).strip()


            emotion = str(
                data.get(
                    "emotion",
                    ""
                )
            ).strip()


            # 입력 길이 제한
            situation = situation[:1000]
            emotion = emotion[:100]


            if not situation and not emotion:

                message = (
                    "지금 어떤 마음인지 조금만 알려주세요.\n"
                    "천천히 이야기해도 괜찮아요."
                )

            else:

                message = generate_goodword(
                    situation,
                    emotion
                )


            response = json.dumps(
                {
                    "success": True,
                    "message": message
                },
                ensure_ascii=False
            ).encode("utf-8")


            self.send_data(
                response,
                "application/json; charset=utf-8"
            )


        except Exception as error:

            print(
                "SERVER ERROR:",
                error
            )


            response = json.dumps(
                {
                    "success": False,
                    "message":
                        "잠시 문제가 생겼어요.\n"
                        "조금 뒤 다시 시도해주세요."
                },
                ensure_ascii=False
            ).encode("utf-8")


            self.send_data(
                response,
                "application/json; charset=utf-8",
                500
            )


    # -----------------------------------------------------
    # 로그
    # -----------------------------------------------------

    def log_message(
        self,
        format,
        *args
    ):

        print(
            "%s - %s"
            % (
                self.address_string(),
                format % args
            )
        )


# =========================================================
# 서버 실행
# =========================================================

def main():

    server = HTTPServer(
        (HOST, PORT),
        GoodWordHandler
    )


    print("")
    print("=" * 60)
    print("                 마음한줄")
    print("=" * 60)
    print("")
    print(
        f"Server running on port {PORT}"
    )
    print(
        f"Host: {HOST}"
    )
    print("")
    print(
        "서버가 시작되었습니다."
    )
    print(
        "Ctrl + C 로 종료할 수 있습니다."
    )
    print("")


    try:

        server.serve_forever()


    except KeyboardInterrupt:

        print("")
        print(
            "서버를 종료합니다."
        )


    finally:

        server.server_close()


if __name__ == "__main__":

    main()