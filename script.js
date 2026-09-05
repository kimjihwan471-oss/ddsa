const situationInput =
    document.getElementById("situation");

const characterCount =
    document.getElementById("characterCount");

const emotionButtons =
    document.querySelectorAll(".emotion");

const goodWordButton =
    document.getElementById("goodWordButton");

const anotherButton =
    document.getElementById("anotherButton");

const copyButton =
    document.getElementById("copyButton");

const result =
    document.getElementById("result");

const message =
    document.getElementById("message");

const toast =
    document.getElementById("toast");


let selectedEmotion = "";


// ======================================================
// 글자 수
// ======================================================

situationInput.addEventListener("input", function () {

    characterCount.textContent =
        this.value.length;

});


// ======================================================
// 감정 선택
// ======================================================

emotionButtons.forEach(button => {

    button.addEventListener("click", function () {

        emotionButtons.forEach(item => {
            item.classList.remove("selected");
        });

        this.classList.add("selected");

        selectedEmotion =
            this.dataset.emotion;

    });

});


// ======================================================
// 좋은말 받기
// ======================================================

goodWordButton.addEventListener(
    "click",
    getGoodWord
);

anotherButton.addEventListener(
    "click",
    getGoodWord
);


async function getGoodWord() {

    const situation =
        situationInput.value.trim();


    if (!situation && !selectedEmotion) {

        showToast(
            "지금 어떤 마음인지 조금만 알려주세요 🌿"
        );

        situationInput.focus();

        return;
    }


    setLoading(true);


    try {

        const response =
            await fetch("/api/goodword", {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({

                    situation:
                        situation,

                    emotion:
                        selectedEmotion

                })

            });


        if (!response.ok) {

            throw new Error(
                "서버 오류"
            );

        }


        const data =
            await response.json();


        message.textContent =
            data.message;


        result.classList.remove("show");


        // CSS 애니메이션 재실행
        void result.offsetWidth;


        result.classList.add("show");


        setTimeout(() => {

            result.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

        }, 100);


    } catch (error) {

        console.error(error);

        showToast(
            "잠시 문제가 생겼어요. 다시 시도해주세요."
        );

    } finally {

        setLoading(false);

    }

}


// ======================================================
// 로딩
// ======================================================

function setLoading(loading) {

    if (loading) {

        goodWordButton.classList.add(
            "loading"
        );

        goodWordButton.disabled =
            true;

        goodWordButton.querySelector(
            "span:last-child"
        ).textContent =
            "당신에게 필요한 말을 찾는 중...";

    } else {

        goodWordButton.classList.remove(
            "loading"
        );

        goodWordButton.disabled =
            false;

        goodWordButton.querySelector(
            "span:last-child"
        ).textContent =
            "나에게 필요한 말 받기";

    }

}


// ======================================================
// 문장 복사
// ======================================================

copyButton.addEventListener(
    "click",
    async function () {

        const text =
            message.textContent.trim();


        if (!text) {
            return;
        }


        try {

            await navigator.clipboard.writeText(
                text
            );

            showToast(
                "문장이 복사되었어요."
            );

        } catch (error) {

            showToast(
                "복사하지 못했어요."
            );

        }

    }
);


// ======================================================
// 토스트
// ======================================================

let toastTimer;


function showToast(text) {

    toast.textContent = text;

    toast.classList.add("show");


    clearTimeout(toastTimer);


    toastTimer = setTimeout(() => {

        toast.classList.remove("show");

    }, 2200);

}