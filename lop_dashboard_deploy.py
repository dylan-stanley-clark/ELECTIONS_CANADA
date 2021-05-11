import streamlit as st
import pickle5 as pickle
import pandas as pd
import SessionState




# import SessionState

# state = SessionState.get(position=0)

with open('data_base_parms.pickle', 'rb') as handle:
    data_base_parms = pickle.load(handle)

with open('district_table_iframes.pickle', 'rb') as handle:
    district_tables = pickle.load(handle)


def main():

    st.set_page_config(page_title="Verify CED")  # , layout="wide")


    election = st.sidebar.selectbox("Election Date", data_base_parms["elections"])
    ridings = data_base_parms[election + " ridings"]

    page = st.sidebar.radio("Page", ["Summary", "Districts"])

    # ---Election SUMMARY PAGE----
    if page == 'Summary':
        info = st.sidebar.radio('Election Info',
                                options=['Districts', 'Incumbents', "Vote Summary", "Conflicts", "Verification"])

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
                    st.write("Chart not created yet")

            if info == "Conflicts":
                title = election + ", conflict summary"
                x = """<iframe title="Conflicts With Canadian Election Database" aria-label="chart" id="datawrapper-chart-JZdUB" src="https://datawrapper.dwcdn.net/JZdUB/2/" scrolling="no" frameborder="0" style="border: none;" width="400" height="315"></iframe>"""

                st.markdown(x, unsafe_allow_html=True)

                x2 = """<iframe title="Existing Conflicts Between LOP &amp;amp; CED" aria-label="table" id="datawrapper-chart-YpJ5o" src="https://datawrapper.dwcdn.net/YpJ5o/1/" scrolling="no" frameborder="0" style="border: none;" width="600" height="720"></iframe>"""
                st.markdown(x2, unsafe_allow_html=True)

    # Contituency level page
    else:
        #Give ability to navigate with buttons etc
        query_params = st.experimental_get_query_params()
        app_state = st.experimental_get_query_params()

        session_state = SessionState.get(first_query_params=query_params)
        first_query_params = session_state.first_query_params
        if "district" in app_state:
            default_index = eval(first_query_params["district"][0])
        else:
            default_index = 0


        col1, col2 = st.beta_columns(2)
        with col2:
            button = st.button("Next District")

        if button:
            default_index = int(app_state["district"][0])+1
        constituency = st.selectbox("Constituency", ridings, index=default_index)

        app_state["district"] = ridings.index(constituency)
        st.experimental_set_query_params(**app_state)

        constituency2 = ridings[app_state["district"]]
        title = constituency2 + ", " + election + " Results"
        try:
            # Reshape
            k = 'width="600" height="262"></iframe>'
            x = district_tables[title][:-len(k)] + """width="800" height="500"></iframe>"""
            st.markdown(x, unsafe_allow_html=True)
        except:
            st.write("no table created yet")



if __name__ == "__main__":
    main()
