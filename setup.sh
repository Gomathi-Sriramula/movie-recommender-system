mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = 8501\n\
" > ~/.streamlit/config.toml