import pandas as pd
import numpy as np
from plotnine import *


def clean_col(pd_series):
    new_col = []
    for val in pd_series:
        if "." in val and "23" in val:
            x = val.split(".")
            new_col.append(".".join(x[0:2]))
        elif "." in val:
            x = val.split(".")
            new_col.append(x[0])
        else:
            new_col.append(val)
    return new_col


def read_data(name):
    df = pd.read_csv(name, index_col=0)
    df = df.T
    df.reset_index(level=0, inplace=True)
    df["index"] = clean_col(df["index"])
    df.columns = df.columns.str.replace('index', 'Tank')
    df[["rhizome (cm)", "leaf 1 (cm)", "leaf 2 (cm)"]] = df[["rhizome (cm)", "leaf 1 (cm)", "leaf 2 (cm)"]].apply(
        pd.to_numeric)
    return df


def boxplot_leaves_size(df, plot_name):
    leaves_df = df[["Tank", "leaf 1 (cm)", "leaf 2 (cm)"]]
    leaves_df_gb = leaves_df.groupby("Tank").mean()
    leaves_df_gb['mean_leaves_cm'] = leaves_df_gb[["leaf 1 (cm)", "leaf 2 (cm)"]].mean(axis=1)
    g = ggplot(leaves_df_gb, aes(leaves_df_gb.index, "mean_leaves_cm")) + geom_col() + \
        xlab("Tank Temperature (Celsius)") + ylab("Mean leaf length (cm)") + \
        ggtitle("Leaf length by temperature\noverall mean") + theme(axis_text_x=element_text(rotation=45, hjust=1))
    g.save(plot_name)


def boxplot_rhizome_size(df):
    rhizome_df = df[["index", "rhizome (cm)"]]


if __name__ == '__main__':
    df = read_data("data_clear.csv")
    boxplot_leaves_size(df, "leaves_total_mean.png")



