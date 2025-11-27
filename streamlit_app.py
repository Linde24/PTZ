import streamlit as st

st.set_page_config(page_title="Sint Chatbot")

# Questions & Messages
INTRO = (
    "Lieve Beatrix, mijn pieten hebben heel hard gewerkt en na honderden uren "
    "analyse door supercomputers is het ze gelukt om een programma te maken dat "
    "altijd weet waar je telefoon ligt."
)

QUESTION_1 = "Waar heb je je telefoon voor het laatst gezien?"
QUESTION_2 = "Heb je al de badkamer gecheckt?"
QUESTION_3 = "Heb je de WC beneden al gecheckt?"

# Initialise session state
if "state" not in st.session_state:
    st.session_state.state = "intro"
if "answers" not in st.session_state:
    st.session_state.answers = {}

st.title("🎁 Chat met Sint")


# INTRO ---------------------------------------------------------------------------------------
if st.session_state.state == "intro":
    st.markdown(f"**Sint:** {INTRO}")
    if st.button("Verder"):
        st.session_state.state = "q1"
        st.rerun()


# QUESTION 1 ----------------------------------------------------------------------------------
elif st.session_state.state == "q1":
    st.markdown(f"**Sint:** {QUESTION_1}")
    answer = st.text_input("Jouw antwoord:")

    if answer:
        st.session_state.answers["q1"] = answer
        st.session_state.state = "q2"
        st.rerun()


# QUESTION 2 ----------------------------------------------------------------------------------
elif st.session_state.state == "q2":
    st.markdown(f"**Sint:** {QUESTION_2}")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Ja ✔️"):
            st.session_state.answers["q2"] = "yes"
            st.session_state.state = "q3"
            st.rerun()

    with col2:
        if st.button("Nee ❌"):
            st.session_state.answers["q2"] = "no"
            st.info("Check de badkamer!")
            # Stay on the same question — user can click again


# QUESTION 3 ----------------------------------------------------------------------------------
elif st.session_state.state == "q3":
    st.markdown(f"**Sint:** {QUESTION_3}")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Ja ✔️"):
            st.session_state.answers["q3"] = "yes"
            st.session_state.state = "error"
            st.rerun()

    with col2:
        if st.button("Nee ❌"):
            st.session_state.answers["q3"] = "no"
            st.warning("Check de WC beneden!")
            # Stay on the same question


# FUNNY ERROR ---------------------------------------------------------------------------------
elif st.session_state.state == "error":
    st.error(
        "🤯 **AI-foutmelding 404: Telefoon Niet Gevonden**\n\n"
        "Sint concludeert dat je telefoon officieel *vermist* is.\n"
        "Waarschijnlijk leeft hij nu zijn beste leven in een parallel universum."
    )
    st.stop()
