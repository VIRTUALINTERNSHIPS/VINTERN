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
    label="ABOUT US",
    description=" ",
    color_name="blue-70",
)    
st.markdown("VINTERN is a platform that offers virtual internship opportunities for students. In order to meet the client's needs, we offer real-time issue statements. Based on their interests and available time, the students can work on these issue statements. They will be put on a shortlist for hiring based on their performance.")
add_vertical_space(4)
colored_header(
    label="Our Mission",
    description=" ",
    color_name="red-70",
)   
st.markdown("No matter how different everyone's economic or educational backgrounds are, our mission is to make education and experiential learning accessible and inexpensive to everyone. Since curiosity can't be stifled, we give students the power to demand more than any other platform or institution. A book cannot contain all that learning is. ")
add_vertical_space(4)
colored_header(
    label="Our Services",
    description=" ",
    color_name="green-70",
)   
st.markdown("Virtual Internships")
