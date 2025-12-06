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
    "Zoals altijd, het is zo al een tijdje,\n\n"
    "Is Bé weer een bezig bijtje.\n\n" 
    "Sinds een maandje is er ook een nieuwe gebeurtenis,\n\n"
    "Beatrix werkt sinds kort bij Kentalis. \n\n"
    "Kinderen helpen met beeldende therapie wil ze graag,\n\n"
    "Maar met de computer gaat alles veel te traag.\n\n "
    "De Sint snapt dit wel, ook hij vind het onaangenaam,\n\n"
    "Maar gelukkig zijn zijn pieten vaak erg behulpzaam.\n\n"
    "Goed, hij zal er niet mee pochen,\n\n"
    "En hoopt dat Bé snel in kan loggen.\n\n"
)

Drie = ("Om te ontspannen hoeft Bé gelukkig niet op reis, \n\n"
"Want thuis is het al een heus vogelparadijs\n\n"
"Waterhoen hier, ijsvogel daar,\n\n"
"De age-appropriate hobby kan het hele jaar.\n\n"
"Een vijver zo prachtig, amper te beschrijven \n\n"
"Leuk dat water – maar in de tuin mag het blijven. \n\n"
"Liever niet in huis – want wat is dat voor plek? \n\n"
"Dan maar een zeil, dat is beter dan een lek. \n \n \n"
        "(spot de vogel)"
)

Vier = ("Je bent  vast benieuwd naar je surprise \n\n "
"Daarvoor heeft Sint ChatGTPiet gevraagd naar zijn expertise. \n\n "
"Dit jaar geen knutselwerk, nee, hij wilde iets nuttigs maken \n\n "
"En wat is nou fijn voor iemand die gewoon is vaak haar telefoon kwijt te raken? \n\n "
"Juist, een AI telefoonzoeker is wellicht een goede life-hack, \n\n "
"Die je helpt met zoeken op de juiste plek.  \n\n "
"ChatGTPiet heeft daarvoor alle data geanalyseerd,  \n\n "
"En de computer heeft jouw patronen geleerd. \n\n"
"In theorie heeft de Telefoonzoeker *bijna* altijd gelijk, \n\n "
"Maar wellicht moeten we dat nog testen in de praktijk."
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
    if st.button("Gedicht"):
        st.session_state.state = "Twee"
        st.rerun()

# Twee
if st.session_state.state == "Twee":
    st.markdown(f"**Sint:** {Twee}")
    if st.button("Klik om in te loggen"):
        st.session_state.state = "Drie"
        st.rerun()

# Drie
if st.session_state.state == "Drie":
    st.markdown(f"**Sint:** {Drie}")
    if st.button("🦤"):
        st.session_state.state = "Vier"
        st.rerun()
# Vier
if st.session_state.state == "Vier":
    st.markdown(f"**Sint:** {Vier}")
    if st.button("TELEFOONZOEKER"):
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
        if st.button("Ja, daar ligt hij niet"):
            st.session_state.answers["q2"] = "yes"
            st.session_state.state = "q3"
            st.rerun()

    with col2:
        if st.button("Nee "):
            st.session_state.answers["q2"] = "no"
            st.info("Check de badkamer! Als hij daar niet ligt, klik dan op de andere knop.")
            # Stay on the same question — user can click again


# QUESTION 3 ----------------------------------------------------------------------------------
elif st.session_state.state == "q3":
    st.markdown(f"**ChatGTPiet:** {QUESTION_3}")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Ja, daar ligt hij niet"):
            st.session_state.answers["q3"] = "yes"
            st.session_state.state = "error"
            st.rerun()

    with col2:
        if st.button("Nee"):
            st.session_state.answers["q3"] = "no"
            st.warning("Check de WC beneden! Als hij daar niet ligt, klik dan op de andere knop.")
            # Stay on the same question


# FUNNY ERROR ---------------------------------------------------------------------------------
elif st.session_state.state == "error":
    st.error(
        "🤯 **AI-foutmelding 404: Telefoon Niet Gevonden**\n\n"
        "ChatGTPiet weet het ook niet meer. Deze situatie is niet voorzien \n"
        "Waarschijnlijk leeft je telefoon nu zijn beste leven in een parallel universum."
    )
    st.stop()

