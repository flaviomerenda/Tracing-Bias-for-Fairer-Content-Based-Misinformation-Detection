import os

import pandas as pd

import plotly.express as px


DATA_DIR = "../data/"
TOP_N = 150

people_df = pd.DataFrame()

for split in ("train", "test"):
    split_df = pd.read_csv(
        os.path.join(DATA_DIR, f"all_ners_{split}.csv"),
        usecols=['NERS','NERSlabel']
    )
    
    split_df = split_df[split_df["NERSlabel"] == 'PERSON']
    
    people_df_split = split_df["NERS"]\
        .value_counts()\
        .to_frame("Counts")\
        .reset_index(names="NERS")

    people_df_split["Split"] = split

    # Add only top N
    people_df_split = people_df_split.head(n=TOP_N)
    print(people_df_split)
    people_df = pd.concat(
        [people_df, people_df_split],
        axis=0,
        ignore_index=True
    )

fig = px.bar(
    data_frame=people_df,
    x="NERS",
    y="Counts",
    color="Split",
    barmode="group",
    title=f"Distribution of counts for top {TOP_N} NERS by split"
)
fig.show()


for split_2 in ("train", "test"):
    split_2 = pd.read_csv(
        os.path.join(DATA_DIR, f"NERScount_split.csv")
    )
        
    print(split_2)


fig2 = px.bar(
    data_frame=split_2,
    x="NERS",
    y="Counts",
    color="Name",
    barmode="group",
    title=f"Distribution of counts for top NERS by Type of Name"
)
fig2.show()

fig3 = px.bar(
    data_frame=split_2,
    x="NERS",
    y="Counts",
    color="Gender",
    barmode="group",
    title=f"Distribution of counts for top NERS by assumed Gender"
)
fig3.show()