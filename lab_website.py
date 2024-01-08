import streamlit as st
st.set_page_config(layout="centered")
st.get_option("theme.base")

from streamlit_option_menu import option_menu
from web_pages import Research_lines, Contact, Publications, Home, About_us
import utils


# SIDEBAR
with st.sidebar:
    utils.local_css("style/basic.css")
    selected = option_menu(None, ["Home", "Research", "Publications", "Team", "Contact us"],
                           icons=['house', 'search', 'journals', 'person', 'telegram'],
                           styles={"nav-link": {"font-size": "18px",
                                                "text-align": "left",
                                                "margin": "0px",
                                                "font-family": "Arial"},
                                   "nav-link-selected": {"background-color": "#aebcef"}},
                           menu_icon="cast", default_index=0)

# MAIN TOP MENU
if selected == 'Home':
    utils.local_css("style/home_style.css")
    utils.write_title_main(Home.title)

    # Header/ Intro
    data = Home.get_data("1_home/1_home_intro.json")
    st.markdown('{}'.format(Home.intro(data["img_path"], data["who_we_are"], data["mission"])), unsafe_allow_html=True)
    st.markdown('<div style = "text-align: justify; '
                'font-family: Montserrat, sans-serif;"> {} </div>'.format(data["how_we_do_it"]),
                unsafe_allow_html=True)
    st.text("")

    # Brain organoids images
    utils.write_subtitle(Home.title2)
    st.text('')
    st.markdown(Home.get_gallery("1_home/2_gallery.json"),
                unsafe_allow_html=True)
    st.text("")

    # Institutions
    utils.write_subtitle(Home.title3)
    st.markdown(Home.institutions_logo('1_home/3_institutions.json'), unsafe_allow_html=True)
    st.text(""); st.text("")

    # Latest news
    utils.write_subtitle(Home.title4)
    news = Home.latest_news('1_home/4_latest_news.json')
    st.markdown('<div style = "text-align: justify; '
                'font-family: Montserrat, sans-serif;">{}</div>'.format(news),
                unsafe_allow_html=True)


elif selected == 'Research':
    utils.local_css("style/research.css")

    # Research lines
    utils.write_title(Research_lines.title_research)
    st.markdown('<div style = "text-align: justify; font-family: Montserrat, sans-serif;" > {} </div>'.format(
        Research_lines.get_intro('2_research/1_research_intro.txt')),
                unsafe_allow_html=True)

    titles, descriptions = Research_lines.get_research_data('2_research/2_research_lines.json')
    for i in range(len(titles)):
        st.markdown('{}'.format(Research_lines.research_line(titles[i], descriptions[i])),
                    unsafe_allow_html=True)
        st.text("")

    # Funding Agencies
    utils.write_title(Research_lines.title_fundings)
    st.markdown(Research_lines.funding_agencies_logo('2_research/4_funding_agencies.json'), unsafe_allow_html=True)


elif selected == 'Publications':
    utils.local_css("style/basic.css")

    # Publications
    utils.write_title(Publications.title)
    # Publications.publications('2022', '3_publications/publications2022.txt')
    Publications.publications('2021', '3_publications/publications2021.txt')


elif selected == 'Team':
    utils.local_css("style/about_us_style.css")

    # Meet the team: Members presentation. Load data from team members
    utils.write_title(About_us.title1)
    names, roles, photos, bios = About_us.get_data('4_team/2_team_members_data.json')
    # Print data
    for i in range(len(names)-1):
        st.markdown('{}'.format(
            About_us.team_member(photo=photos[i],
                                 name=names[i],
                                 role=roles[i],
                                 bio=bios[i])),
            unsafe_allow_html=True)
        st.text("")
    st.text("")

    # Outside the lab
    utils.write_title(About_us.title3)
    st.text("")
    st.markdown(About_us.gallery, unsafe_allow_html=True)  # Photos


elif selected == 'Contact us':
    # Style
    utils.local_css("style/contact_style.css")

    # Title
    title = utils.write_title(Contact.title)
    st.text("")

    # Contact form
    st.markdown(Contact.contact_form, unsafe_allow_html=True)
    st.text("")

    # Location information
    st.markdown(Contact.location, unsafe_allow_html=True)
    st.text("")

    # Phone number
    # st.markdown(Contact.phone, unsafe_allow_html=True)
