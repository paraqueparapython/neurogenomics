mkdir -p ~/.streamlit/
echo "\
[theme]
base='dark'\n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml