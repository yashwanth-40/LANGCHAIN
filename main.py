import streamlit as st
import langchain_final

st.title('Cricket Team Building Application')

nation = st.sidebar.selectbox('Pick a Nation', ('India', 'Australia', 'England', 'Pakistan', 'NewZealand', 'West Indies', 'South Africa', 'Bangladesh', 'Afghanistan','Srilanka'))

if nation:
    response = langchain_final.getChatResponse(nation=nation)
    header = 'The Selected players of ' + response['nation'] + ' national team for world cup:'
    st.header(header)
    #st.header(response['nation'])
    selected_players = response['15 players'].split('\n')

    for player in selected_players:
        st.write('* ', player)
    
    click = st.sidebar.button('Give the Playing 11')

    if click:
        header_11 = 'The Best 11 players of ' + response['nation'] + ' national team for world cup:'
        st.header(header_11)
        selected_11_players = response['best 11'].split('\n')
        for player in selected_11_players:
            st.write('* ', player)
