import streamlit as st

title = 'Publications &#128466'


def publications(year, pubs_file_path):
    pubs = _get_publications(pubs_file_path)
    st.markdown("<h6 style='text-align: left; "
                "font-family: Montserrat, sans-serif; "
                "font-size:20px;'>{}</h6>".format(year),
                unsafe_allow_html=True)
    st.markdown('<div style = "text-align: justify; '
                'font-family: Montserrat, sans-serif;">{}</div>'.format(_get_pubs_list(pubs)),
                unsafe_allow_html=True)


def _get_publications(file_path):
    with open(file_path, encoding='utf8') as f:
        pubs = f.readlines()
    return pubs


def _get_pubs_list(elements):
    string = "<ul>\n"
    for s in elements:
        string += "<li>" + str(s) + "</li><br/>"
    string += "</ul>"
    return string