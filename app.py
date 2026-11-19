# Стартиране:  streamlit run app.py
# (ако Streamlit не е инсталиран:  pip install streamlit)

import time
import streamlit as st

st.set_page_config(page_title="Упражнения по Streamlit", page_icon="🐍")

# ---------------------------------------------------------
# Стилове и анимации (CSS)
# ---------------------------------------------------------
st.markdown(
    """
<style>
@keyframes gradient { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
@keyframes pop { 0% {transform: scale(.3); opacity: 0;} 60% {transform: scale(1.08); opacity: 1;} 100% {transform: scale(1);} }
@keyframes shake { 0%, 100% {transform: translateX(0);} 20%, 60% {transform: translateX(-9px);} 40%, 80% {transform: translateX(9px);} }
@keyframes bounce { 0%, 100% {transform: translateY(0);} 50% {transform: translateY(-12px);} }

.hero { text-align: center; margin-bottom: 10px; }
.hero .snake { font-size: 2.6rem; display: inline-block; animation: bounce 1.4s ease-in-out infinite; }
.hero .title {
    font-size: 2.2rem; font-weight: 800;
    background: linear-gradient(90deg, #ff6b6b, #feca57, #1dd1a1, #48dbfb, #a55eea, #ff6b6b);
    background-size: 300% 300%; animation: gradient 6s ease infinite;
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}

.card { display: flex; align-items: center; gap: 18px; padding: 18px 24px; border-radius: 20px;
        margin: 14px 0; color: #fff; box-shadow: 0 8px 24px rgba(0,0,0,.2); animation: pop .5s ease; }
.card .emoji { font-size: 2.8rem; animation: bounce 1.2s ease-in-out infinite; }
.card .msg { font-size: 1.5rem; font-weight: 800; }
.card .sub { font-size: 1.1rem; opacity: .95; }
.green  { background: linear-gradient(135deg, #11998e, #38ef7d); }
.orange { background: linear-gradient(135deg, #f12711, #f5af19); }
.blue   { background: linear-gradient(135deg, #2193b0, #6dd5ed); }
.purple { background: linear-gradient(135deg, #8e2de2, #4a00e0); }
.red    { background: linear-gradient(135deg, #cb2d3e, #ef473a); }

/* Съобщенията на Streamlit (success, error, warning) изскачат с анимация */
div[data-testid="stAlert"] { animation: pop .5s ease; }
div[data-testid="stAlert"]:has([data-testid="stAlertContentError"]) { animation: shake .5s ease; }

/* Бутоните "подскачат" при посочване с мишката */
div.stButton > button { border-radius: 12px; font-weight: 700; transition: transform .15s, box-shadow .15s; }
div.stButton > button:hover { transform: translateY(-3px) scale(1.05); box-shadow: 0 6px 16px rgba(0,0,0,.25); }
</style>
<div class="hero"><span class="snake">🐍</span> <span class="title">Упражнения по Python и Streamlit</span></div>
""",
    unsafe_allow_html=True,
)


def card(text, emoji, color, sub=""):
    """Показва анимирана цветна карта със съобщение."""
    st.markdown(
        f'<div class="card {color}"><div class="emoji">{emoji}</div>'
        f'<div><div class="msg">{text}</div><div class="sub">{sub}</div></div></div>',
        unsafe_allow_html=True,
    )


# Пет раздела (табове) - по един за всяко упражнение
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🐍 Упр. 1", "🔢 Упр. 2", "🧮 Упр. 3", "🎓 Упр. 4", "🎯 Упр. 5"]
)

# key е нужен, защото имаме няколко еднакви бутона "Провери"
# и Streamlit трябва да ги различава един от друг.


# ---------------------------------------------------------
# Упражнение 1 – Обичаш ли Python?
# ---------------------------------------------------------
with tab1:
    st.header("Упражнение 1 – Обичаш ли Python?")
    st.caption("🟢 Лесно")

    answer = st.radio("Обичаш ли Python?", ["да", "не"], horizontal=True, key="radio1")

    if answer == "да":
        card("Супер!", "🐍💚", "green")
    else:
        card("Ще го харесаш!", "😉✨", "orange")


# ---------------------------------------------------------
# Упражнение 2 – Голямо или малко число?
# ---------------------------------------------------------
with tab2:
    st.header("Упражнение 2 – Голямо или малко число?")
    st.caption("🟢 Лесно")

    number = st.number_input("Въведи число:", value=0, step=1, key="number2")

    if number > 10:
        card("Голямо число", "🐘", "purple", f"{number} е по-голямо от 10")
    else:
        card("Малко число", "🐜", "blue", f"{number} не е по-голямо от 10")


# ---------------------------------------------------------
# Упражнение 3 – Мини тест по математика
# ---------------------------------------------------------
with tab3:
    st.header("Упражнение 3 – Мини тест по математика")
    st.caption("🟡 Средно")

    answer = st.number_input("Колко е 5 × 5?", value=0, step=1, key="number3")

    if st.button("Провери", key="button3", type="primary"):
        if answer == 25:
            st.success("Вярно! Браво!", icon="🎉")
            st.balloons()
        else:
            st.error("Грешно! Опитай отново!", icon="😅")


# ---------------------------------------------------------
# Упражнение 4 – Калкулатор за оценка
# ---------------------------------------------------------
with tab4:
    st.header("Упражнение 4 – Калкулатор за оценка")
    st.caption("🟡 Средно")

    grade = st.number_input(
        "Каква е твоята оценка (от 2 до 6)?",
        min_value=2,
        max_value=6,
        value=2,
        step=1,
        key="number4",
    )

    if st.button("Провери", key="button4", type="primary"):
        # Анимирана лента, която се пълни според оценката
        target = int((grade - 1) / 5 * 100)
        bar = st.progress(0)
        for i in range(0, target + 1, 5):
            bar.progress(i)
            time.sleep(0.03)

        stars = "⭐" * grade

        if grade == 6:
            card("Отличен резултат!", "🏆", "green", stars)
            st.balloons()
        elif grade == 5:
            card("Много добър резултат!", "🥳", "blue", stars)
        elif grade == 4:
            card("Добър резултат!", "😊", "purple", stars)
        elif grade == 3:
            card("Среден резултат!", "🙂", "orange", stars)
        else:
            card("Слаб резултат!", "😬", "red", stars)


# ---------------------------------------------------------
# Упражнение 5 – Познай числото
# ---------------------------------------------------------
with tab5:
    st.header("Упражнение 5 – Познай числото")
    st.caption("🔴 Предизвикателство")

    secret_number = 7  # предварително зададеното число

    # Помним колко опита е направил играчът
    if "tries" not in st.session_state:
        st.session_state.tries = 0

    guess = st.number_input("Въведи число:", value=0, step=1, key="number5")

    if st.button("Провери", key="button5", type="primary"):
        st.session_state.tries += 1
        with st.spinner("Проверявам..."):
            time.sleep(0.6)

        if guess == secret_number:
            st.success("Поздравления! Позна!", icon="🏆")
            st.caption(f"Позна за {st.session_state.tries} опита!")
            st.balloons()
            st.session_state.tries = 0
        elif guess > secret_number:
            st.warning("Опитай с по-малко число!", icon="⬇️")
        else:
            st.warning("Опитай с по-голямо число!", icon="⬆️")

    if st.session_state.tries > 0:
        st.caption(f"Опити досега: {st.session_state.tries}")
