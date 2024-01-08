import streamlit as st


def write_title(text):
    # title = st.header(text)
    title = st.markdown("<h6 style='text-align: left; "
                        "font-family: Montserrat, sans-serif; "
                        "font-size:35px;'>{}</h6>".format(text),
                        unsafe_allow_html=True)
    return title


def write_title_main(text):
    title = st.markdown("<h1 style='text-align: center; "
                        "color: royalblue; "
                        "font-family: Montserrat, sans-serif; "
                        "font-size:35px;'>{}</h1>".format(text),
                        unsafe_allow_html=True)
    return title


def write_subtitle(text):
    subtitle = st.markdown("<h6 style = 'text-align: left; "
                           "font-size:24px; "
                           "font-family: Montserrat, "
                           "sans-serif;'> {} </h6>".format(text),
                           unsafe_allow_html=True)
    return subtitle


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)