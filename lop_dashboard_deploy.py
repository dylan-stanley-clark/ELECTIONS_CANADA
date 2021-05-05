import streamlit as st
import pickle5 as pickle

with open('data_base_parms.pickle', 'rb') as handle:
    data_base_parms = pickle.load(handle)

with open('district_table_iframes.pickle', 'rb') as handle:
    district_tables = pickle.load(handle)

def main():

    st.set_page_config(page_title="Verify CED", layout="wide")

    election = st.sidebar.selectbox("Election Date", data_base_parms["elections"])
    ridings = data_base_parms[election + " ridings"]
    
    summary = st.radio("Page",["Summary","Districts"])


    # ---SUMMARY PAGE----
    if summary == 'Summary':
        col1, col2= st.beta_columns(2)
        # with col1:
        #     title = election + ", provincial summary"
        #     x = district_tables[title]#[:-46] + """width="700" height="900"></iframe>"""
        #     st.markdown(x, unsafe_allow_html=True)
        with col1:
            title = election+", Active Constituencies"
            x = district_tables[title]#[:-46] + """width="2000" height="900"></iframe>"""
            st.markdown(x, unsafe_allow_html=True)

        with col2:
            title = election + ", Incumbent Elects Seeking Re-Election"
            st.markdown(district_tables[title] , unsafe_allow_html=True)

    #Contituency level page
    else:
        #"District Table"
        constituency = st.selectbox("Constituency", ridings, index=len(ridings) - 1)
        col1, col2, col3 = st.beta_columns(3)
        with col2:
            title = constituency + ", " + election + " Results"
            k ='width="600" height="262"></iframe>'
            x = district_tables[title][:-len(k)] + """width="800" height="500"></iframe>"""

        st.markdown(x, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


