import streamlit as st

st.set_page_config(page_title="ChatGTPiet")

# Questions & Messages
INTRO = (
    "Lieve Beatrix, \n\n"
    "Het was een grapje - allicht,\n\n"
    "Want voor AI is Sint nog niet gezwicht\n\n"
    "Een nieuw hulpje heeft hij wel,\n\n"
    "Met computers is ChatGTPiet supersnel."
)

Twee = (
    "Zoals altijd, het is zo al een tijdje,"
    "Is Bé weer een bezig bijtje." 
    "Sinds een maandje is er ook een nieuwe gebeurtenis,"
    "Beatrix werkt sinds kort bij Kentalis. "
    "Kinderen helpen met beeldende therapie wil ze graag,"
    "Maar met de computer gaat alles veel te traag. "
    "De Sint snapt dit wel, ook hij vind het onaangenaam,"
    "Maar gelukkig zijn zijn pieten vaak erg behulpzaam."
    "Goed, hij zal er niet mee pochen,"
    "En hoopt dat Bé snel in kan loggen."
)

QUESTION_1 = "Waar heb je je telefoon voor het laatst gezien?"
QUESTION_2 = "Heb je al de badkamer gecheckt?"
QUESTION_3 = "Heb je de WC beneden al gecheckt?"

# Initialise session state
if "state" not in st.session_state:
    st.session_state.state = "intro"
if "answers" not in st.session_state:
    st.session_state.answers = {}

st.title("🎁 ChatGTPiet")


# INTRO ---------------------------------------------------------------------------------------
if st.session_state.state == "intro":
    st.markdown(f"**Sint:** {INTRO}")
    if st.button("Verder"):
        st.session_state.state = "Twee"
        st.rerun()

# Twee
if st.session_state.state == "Twee":
    st.markdown(f"**Sint:** {Twee}")
    if st.button("Klik om in te loggen"):
        st.session_state.state = "q1"
        st.rerun()

# QUESTION 1 ----------------------------------------------------------------------------------
elif st.session_state.state == "q1":
    st.markdown(f"**ChatGTPiet:** {QUESTION_1}")
    answer = st.text_input("Jouw antwoord:")

    if answer:
        st.session_state.answers["q1"] = answer
        st.session_state.state = "q2"
        st.rerun()


# QUESTION 2 ----------------------------------------------------------------------------------
elif st.session_state.state == "q2":
    st.markdown(f"**ChatGTPiet** {QUESTION_2}")
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
    st.markdown(f"**ChatGTPiet:** {QUESTION_3}")
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

