import pandas as pd
import numpy as np
from plotnine import *
from scipy.stats import ttest_ind


def create_boxplot(path_name, save_name, x, y, color, title_input, xlab_input, ylab_input):
    """
    Creates a boxplot comparison and saves the result by the following parameters
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
    g = ggplot(df, aes(x=x, y=y, color=color)) + geom_boxplot() + ggtitle(title_input) + \
        xlab(xlab_input) + ylab(ylab_input) + geom_jitter(height=0) + theme_bw()
    g.save(save_name)


def create_colplot(path_name, save_name, x, y, color, title_input, xlab_input, ylab_input):
    """
    creates a barplot (or column plot) and saves it by the following parameters
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
    g = ggplot(df, aes(x=x, y=y, color=color, fill=x)) + geom_col() + ggtitle(title_input) + \
        xlab(xlab_input) + ylab(ylab_input) + theme_bw()
    g.save(save_name)


if __name__ == '__main__':
    # # pam boxplot
    # create_boxplot("Seagrasses data - photosynthesis.csv", r"Plots/fv_fm_day_time.png", "tank", "Fv/Fm", "tank",
    #                "Fv/Fm by temperature\nDay time", "Temperature (Celsius)", "Fv/Fm")

    # rhizome boxplot
    create_boxplot("Seagrasses data - rhizome.csv", r"Plots/rhizome_elongation.png", "Tank", "average length per day",
                   "Tank", "Rhizome average elongation by temperature\n10 days period", "Temperature (Celsius)",
                   "Rhizome average daily elongation (cm)")

    # # Chlorophyll reading graph
    # # Chlorophyll A
    # create_boxplot("Chlorophyll readings excel sheet from hung.csv", r"Plots/Chlorophyll_a.png", "Tank no",
    #                "Chl a mg/g FW",
    #                "Tank no", "Chlorophyll A by temperature", "Temperature (Celsius)", "Chl a mg/g FW")

    # # Chlorophyll B
    # create_boxplot("Chlorophyll readings excel sheet from hung.csv", r"Plots/Chlorophyll_b.png", "Tank no",
    #                "Chl b mg/g FW",
    #                "Tank no", "Chlorophyll B by temperature", "Temperature (Celsius)", "Chl b mg/g FW")

    # # Chlorophyll A+B
    # create_boxplot("Chlorophyll readings excel sheet from hung.csv", r"Plots/Chlorophyll_a_b.png", "Tank no",
    #                "Chl a+b mg/g FW",
    #                "Tank no", "Chlorophyll A+B by temperature", "Temperature (Celsius)", "Chl a+b mg/g FW")

    # # Carotenoids
    # create_boxplot("Chlorophyll readings excel sheet from hung.csv", r"Plots/Carotenoids.png", "Tank no",
    #                "Carotenoids mg/g FW",
    #                "Tank no", "Carotenoids by temperature", "Temperature (Celsius)", "Carotenoids mg/g FW")

    # Leaf mass
    create_boxplot("Seagrasses data - leaf mass.csv", r"Plots/leaf_mass.png", "treatment [C]",
                   "average mass per day [gr]", "treatment [C]",
                   "Leaves average mass accumulation by temperature\n10 days period", "Temperature (Celsius)",
                   "Leaf average daily added mass (gr)")

    # # Leaf internodes
    # create_boxplot("Seagrasses data - leaf mass.csv", r"Plots/leaf_internodes.png", "treatment [C]",
    #                "internodes",
    #                "treatment [C]", "Leaf number of internodes by temperature", "Temperature (Celsius)",
    #                "# Internodes")

    # # Protein content
    # create_colplot("Seagrasses data - protein content.csv", r"Plots/protein_concentration.png", "treatment",
    #                "concentartion [mg/ml]",
    #                "treatment", "Protein content by temperature", "Temperature (Celsius)",
    #                "concentration (mg/ml)")
    #
    # # night Fv/Fm
    # create_boxplot("Seagrasses data - Night Fv_Fm.csv", r"Plots/fv_fm_night_time.png", "Tank", "Fv/Fm", "Tank",
    #                "Fv/Fm by temperature\nNight time", "Temperature (Celsius)", "Fv/Fm")
