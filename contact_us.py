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
        
        "🔍",link("https://twitter.com/ChristianKlose3", "About us"),
        "            ||  ",
        "📞",link("https://twitter.com/ChristianKlose3", "Contact Us"),
        "             ||    ",
        "❓",link("https://twitter.com/ChristianKlose3", "FAQ"),
        "            ||     ",
        "☑",link("https://twitter.com/ChristianKlose3", "Terms-and-Conditions"),
        "            ||     ",
        "🔐",link("https://twitter.com/ChristianKlose3", "Privacy Policy"),
        "            ||     ",
        "💳",link("https://twitter.com/ChristianKlose3", "Refund"),
        br(),
        "© 2023 Copyright: 🎓VINTERN"

    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()

with st.sidebar:
    st.button("hi")


colored_header(
    label="CONTACT US",
    description=" ",
    color_name="orange-70",
)    
st.markdown("Email : vintern@gmail.com")
st.markdown("Whatsapp: 8328677950")
st.markdown("Instagram:vintern")

