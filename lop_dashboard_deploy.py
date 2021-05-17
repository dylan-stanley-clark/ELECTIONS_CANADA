import streamlit as st
import pickle5 as pickle
import pandas as pd

#Load dictionary of
with open('data_base_parms.pickle', 'rb') as handle:
    data_base_parms = pickle.load(handle)
#load dictionary of chart iframes
with open('chart_iframes.pickle', 'rb') as handle:
    district_tables = pickle.load(handle)

with open('chart_dataframes.pickle', 'rb') as handle:
    district_dfs = pickle.load(handle)

def main():

    st.set_page_config(page_title="Verify CED")  # , layout="wide")
    election = st.sidebar.selectbox("Election Date", data_base_parms["elections"])
    ridings = data_base_parms[election + " ridings"]

    page = st.sidebar.radio("Page", ["Summary", "Districts"])

    # ---Election SUMMARY PAGE----
    if page == 'Summary':
        info = st.sidebar.radio('Election Info',
                                options=['Districts', 'Incumbents', "Vote Summary"])

        col1, col2 = st.beta_columns(2)
        with col1:
            if info == 'Districts':
                title = election + ", Active Constituencies"
                try:
                    st.markdown(district_tables[title], unsafe_allow_html=True)

                except:
                    st.write("Chart not created yet")

            if info == 'Incumbents':
                title = election + ", Incumbent Elects Seeking Re-Election"
                try:
                    st.markdown(district_tables[title], unsafe_allow_html=True)
                except:
                    st.write("Chart not created yet")

            if info == "Vote Summary":
                title = election + ", provincial summary"
                try:
                    st.markdown(district_tables[title], unsafe_allow_html=True)
                except:
                    st.write(district_dfs[election+district])

    # Contituency level page
    else:

        constituency = st.sidebar.selectbox("Constituency", ridings, index=0)
        title = constituency + ", " + election + " Results"
        try:
            # Reshape
            k = 'width="600" height="262"></iframe>'
            x = district_tables[title][:-len(k)] + """width="800" height="500"></iframe>"""
            st.markdown(x, unsafe_allow_html=True)
        except:
            st.write("no table created yet")

if __name__ == "__main__":
    main()
