import streamlit as st 
import streamlit.components.v1 as com
st.set_page_config(layout="wide",page_title='VINTERN', page_icon="👩‍🎓",initial_sidebar_state="expanded")
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

com.html("""

         
         """)
import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        
        "🔍",link("https://vintern-about-us.streamlit.app/", "About us"),
        "            ||  ",
        "📞",link("https://vintern-contact-us.streamlit.app/", "Contact Us"),
        "             ||    ",
        "❓",link("https://vintern-faq.streamlit.app/", "FAQ"),
        "            ||     ",
        "☑",link("https://vintern-terms-and-conditions.streamlit.app/", "Terms-and-Conditions"),
        "            ||     ",
        "🔐",link("https://vintern-privacy-policy.streamlit.app/", "Privacy Policy"),
        "            ||     ",
        "💳",link("https://vintern-refund.streamlit.app/", "Refund"),
        br(),"© 2023 Copyright: 🎓VINTERN"

    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()

with st.sidebar:
    st.button("hi")


colored_header(
    label="REFUND AND CANCELLATION POLICY",
    description=" ",
    color_name="green-70",
)
st.markdown("""RETURN The Company will issue refunds to students who enrolled the course under "100% Feesback offer"(valid from 8th January 2023) where after completing the course they can apply for a refund, other than that company is not liable for a refund in any circumstances.
EXCHANGE 'Exchange' is the action or process of Exchanging of the services provided by the Companyfor any such other services provided by the Company. User can request for an Exchange of Course availed by the User on the platform with another course available on the platform after placing a request for the Course but before accessing and availing the course. An intimation shall be provided by the Company to the User seeking either "Exchange” and the User shall receive a confirmation regarding the replacement. POINTS TO BE NOTED: The user can request for an exchange before accessing the course online on the platform of the User. If the Company disagrees an exchange request due to non-technical issue, User can file a dispute.  We encourage the User to review the course and its subjective nature before making the request to avail such services. User needs to raise the exchange request within 7 days from availing the course online.
REFUND PROCESS(Only enrolled under limited time Feesback Offer)
1. For Refund Request the user may place a request for the same on the chat box of lecture page, the Representative of the Company shall reach out to the User on the Registered number provided by the User on the Platform.
2. The Refund will be processed if the user has completed the course genuinely and submittedall the assignments and projects covered during the course.
3. If it is found that the student is faking the course completion, we have the right to ban the student's account.
4. The Company be at the sole discretion to refund to the User and all refunds shall be processed after such statutory deductions.
5. All refunds shall be credited to the source of the payment received by the Company from the User.""")    
