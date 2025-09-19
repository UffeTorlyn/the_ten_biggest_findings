import streamlit as st
from data.quiz import quiz_questions
# import random
# import copy


# def get_shuffled_questions(quiz_questions, fund):
#     quiz_key = f"shuffled_{fund}"
#     if quiz_key not in st.session_state:
#         # Deep copy to avoid mutating original questions
#         questions = copy.deepcopy(quiz_questions[fund])
#         for q in questions:
#             options = q["options"]
#             answer_idx = q["answer"]
#             correct_answer = options[answer_idx]
#             random.shuffle(options)
#             q["options"] = options
#             q["answer"] = options.index(correct_answer)
#         st.session_state[quiz_key] = questions
#     return st.session_state[quiz_key]

st.set_page_config(page_title="Quiz om fundene", layout="wide", initial_sidebar_state="collapsed")
st.title("Quiz: De ti største fund i 2024")

# Vælg fund
fund_names = list(quiz_questions.keys())
valgt_fund = st.selectbox("Vælg et fund for at tage quizzen:", fund_names)

if valgt_fund:
    # st.subheader(f"Quiz om: {valgt_fund}")
    # st.write(fund_data[valgt_fund]["lang_info"])
    # st.write(f"[Læs mere her]({fund_data[valgt_fund]['url']})")

    quiz_key = f"quiz_{valgt_fund}"

    # Initialize state if needed
    if quiz_key not in st.session_state:
        st.session_state[quiz_key] = {"active": True, "q": 0, "score": 0, "answers": []}

    questions = quiz_questions.get(valgt_fund, [])
    q_idx = st.session_state[quiz_key]["q"]
    score = st.session_state[quiz_key]["score"]
    answers = st.session_state[quiz_key]["answers"]

    if q_idx < len(questions):
        q = questions[q_idx]
        st.write(f"Spørgsmål {q_idx+1} af {len(questions)}:")
        user_answer = st.radio(q["question"], q["options"], key=f"{quiz_key}_q{q_idx}", index=None)
        if st.button("Svar", key=f"{quiz_key}_answer{q_idx}"):
            if user_answer is None:
                st.warning("Vælg et svar før du fortsætter.")
            else:
                correct = q["options"].index(user_answer) == q["answer"]
                answers.append({"question": q["question"], "your": user_answer, "correct": q["options"][q["answer"]]})
                if correct:
                    st.session_state[quiz_key]["score"] += 1
                    st.success("Korrekt!")
                else:
                    st.error(f"Forkert. Rigtigt svar: {q['options'][q['answer']]}")
                st.session_state[quiz_key]["q"] += 1
                st.rerun()
    else:
        if score == len(questions):
            st.balloons()
            st.success(f"Quiz færdig! Du fik {score} ud af {len(questions)} rigtige.")
        elif score == 0:
            st.error(f"Quiz færdig! Du fik {score} ud af {len(questions)} rigtige.")
            st.snow()
            st.info("Bedre held næste gang! Prøv igen og se om du kan få flere rigtige.")
        else:
            st.warning(f"Quiz færdig! Du fik {score} ud af {len(questions)} rigtige.")
            st.info("Bedre held næste gang! Prøv igen og se om du kan få flere rigtige.")


        st.markdown("### Dine svar")
        for idx, a in enumerate(answers, 1):
            is_correct = a['your'] == a['correct']
            icon = "✅" if is_correct else "❌"
            st.markdown(
            f"**{idx}. {a['question']}**  \n"
            f"{icon} Dit svar: <span style='color:{'green' if is_correct else 'red'}'>{a['your']}</span>  \n",
            # f"Rigtigt svar: <span style='color:green'>{a['correct']}</span>",
            unsafe_allow_html=True
            )
        if st.button("Prøv igen", key=f"{quiz_key}_restart"):
            st.session_state[quiz_key]["active"] = True
            st.session_state[quiz_key]["q"] = 0
            st.session_state[quiz_key]["score"] = 0
            st.session_state[quiz_key]["answers"] = []
            st.rerun()
