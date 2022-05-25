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


def create_boxplot(path_name, save_name, x, y, color, title_input, xlab_input, ylab_input):
    """
    :param path_name: full path to file
    :param save_name: png name of file to save
    :param x: x var name
    :param y: y var name
    :param color: color var name
    :param title_input: title name of plot
    :param xlab_input: x label of plot
    :param ylab_input: y label of plot
    """
    df = pd.read_csv(path_name)
    df[f"{x}"] = df[f"{x}"].apply(str)
    g = ggplot(df, aes(x=x, y=y, color=color)) + geom_boxplot() + \
        ggtitle(title_input) + xlab(xlab_input) + ylab(ylab_input) + geom_jitter(height=0) + theme_bw()
    g.save(save_name)


def boxplot_pam(path_name, save_name):
    """
    :param path_name: name of the datatable
    :param save_name: name of the plot
    :return:
    """
    df = pd.read_csv(path_name)
    df.tank = df.tank.apply(str)
    g = ggplot(df, aes(x="tank", y="Fv/Fm", color='tank')) + geom_boxplot() + \
        ggtitle("Fv/Fm by temperature\nDay time") + xlab("Temperature") + ylab("Fv/Fm") + theme_bw()
    g.save(save_name)


if __name__ == '__main__':
    # df = read_data("data_clear.csv")
    # boxplot_leaves_size(df, "leaves_total_mean.png")
    # boxplot_pam("Seagrasses data - photosynthesis.csv", "fv_fm_day_time.png")


    # pam boxplot
    create_boxplot("Seagrasses data - photosynthesis.csv", r"Plots/fv_fm_day_time.png", "tank", "Fv/Fm", "tank",
                   "Fv/Fm by temperature\nDay time", "Temperature", "Fv/Fm")
    # rhizome boxplot
    create_boxplot("Seagrasses data - rhizome.csv", r"Plots/rhizome_length.png", "Tank", "Rhizome Length (cm)", "Tank",
                   "Rhizome growth by temperature", "Temperature", "Growth (cm)")
    # Chlorophyll reading graph
    # Chlorophyll A
    create_boxplot("Chlorophyll readings excel sheet from hung.csv", r"Plots/Chlorophyll_a.png", "Tank no", "Chl a mg/g FW",
                   "Tank no", "Chlorophyll A by temperature", "Temperature", "Chl a mg/g FW")
    # Chlorophyll B
    create_boxplot("Chlorophyll readings excel sheet from hung.csv", r"Plots/Chlorophyll_b.png", "Tank no", "Chl b mg/g FW",
                   "Tank no", "Chlorophyll B by temperature", "Temperature", "Chl b mg/g FW")

    # Chlorophyll A+B
    create_boxplot("Chlorophyll readings excel sheet from hung.csv", r"Plots/Chlorophyll_a_b.png", "Tank no", "Chl a+b mg/g FW",
                   "Tank no", "Chlorophyll A+B by temperature", "Temperature", "Chl a+b mg/g FW")

    # Carotenoids
    create_boxplot("Chlorophyll readings excel sheet from hung.csv", r"Plots/Carotenoids.png", "Tank no",
                   "Carotenoids mg/g FW",
                   "Tank no", "Carotenoids by temperature", "Temperature", "Carotenoids mg/g FW")