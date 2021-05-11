import pandas as pd
def load_incum_table():
    """
    Uses Excel sheet from Parlinfo.ca on incumbents that sought re-election
    Removes duplciates, and rows for seperating elections
    :return:

    Library of Parliament (2021) , Elections and Ridings: Incumbents who did seek re-election at the next General Election. lop.parl.ca (Accessed on 11 May 2021)
    """

    incum = pd.read_excel("Incumbents.xlsx")
    print("Raw: # of incumbents =", len(incum))
    #drop all duplicate rows
    incum = pd.DataFrame.drop_duplicates(incum)
    incum.to_csv("with_nas.csv")
    #drop all rows with na in Constituency at Next Election
    incum.dropna(subset=['Constituency at Next Election'], inplace=True)
    print("Without Duplicates &nas: # of incumbents :", len(incum))
    print("table column names", list(incum))

    return incum

def add_incumbents_district(incum,df):
    """
    Links cleaned incumbent data frame with candidate dataframe that both of UIDS
    :param incum: pandas data frame created from load_incum_table() & with uid
    :param df: pandas data frame loaded from lop candidate data & with uid
    :return: pandas data frame of all candidate data with new incumbent column that equals 'incumbent' if true
    """
    for i, date in enumerate(list(df["Election_Date"].unique())):
        incum2 = incum[df_incum['Date of Next Election'] == date]
        #get all unique ids for this election
        names = list(incum2["uid"].unique())
        if i == 0:
            #create new dataframe to add all subsequent data to
            df2 = df[df['Election_Date'] == date]
            #Create new column called incumbency for all uids that match incumbent uid list
            df2['incumbency'] = df2["uid"].apply(lambda x: "incumbent" if x in names else 0)
        else:
            df3 = df[df['Election_Date'] == date]
            # Create new column called incumbency for all uids that match incumbent uid list
            df3['incumbency'] = df3["uid"].apply(lambda x: "incumbent" if x in names else 0)
            df2 = df2.append(df3)

    return df2




df_incum = load_incum_table()
#Data cleaned from LOP table 'candidates' to link with incumbent table
df = pd.read_csv("FED_1867_present.csv")
#only looking at general elections for now
df = df[df['Election_Type'] == "General"]

#Create unique ids
df_incum["uid"] = df_incum["Name"] + df_incum["Constituency at Next Election"] + df_incum['Political Affiliation']
df["uid"] = df["Candidate"] + df['Constituency'] + df['Political_Affiliation']

df2 = add_incumbents_district(df_incum,df)
df2.to_csv("clean_incumbent.csv")

