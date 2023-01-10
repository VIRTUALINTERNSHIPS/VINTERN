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
        br(),
        "© 2023 Copyright: 🎓VINTERN"

    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()

with st.sidebar:
    st.button("hi")


colored_header(
    label="FAQ'S",
    description=" ",
    color_name="blue-70",
)    
st.markdown("✅Can we obtain certification?")
st.text("Yes, those who completes their intern will br provided Certifacte.")
add_vertical_space(2)
st.markdown("✅Is it paid or free?")
st.text("Paid. Price varies based on their pack choosen.")
add_vertical_space(2)
st.markdown("✅Is there any 6 month internship program?")
st.text("Internships are avialable from 1 month, 45 days, 2 months, 3 months & 6 months packs.")
add_vertical_space(2)
st.markdown("✅Can we have mentor support?")
st.text("Yes, Mentor support was there 24/7.")
add_vertical_space(2)

