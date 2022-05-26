import pandas as pd
from plotnine import *
from scipy.stats import ttest_ind

DRY_WET_CONVERTER = 3.5208


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


def create_boxplot_dry_wet(path_name, save_name, x, y, color, title_input, xlab_input, ylab_input):
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
    df["Dry"] = df[y] / DRY_WET_CONVERTER
    g = ggplot(df, aes(x=x, y="Dry", color=color)) + geom_boxplot() + ggtitle(title_input) + \
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
    g = ggplot(df, aes(x=x, y=y, color=color, fill=x)) + geom_col() + \
        geom_errorbar(aes(x=x, ymin="Prot_Conc-sd", ymax="Prot_Conc+sd")) + \
        ggtitle(title_input) + \
        xlab(xlab_input) + ylab(ylab_input) + theme_bw()
    g.save(save_name)


def create_scatter_line(path_name, save_name, x, y, color, title_input, xlab_input, ylab_input, sd):
    """
    creates a scatter and line plot and saves it by the following parameters
    :param path_name: full path to file
    :param save_name: png name of file to save
    :param x: x var name
    :param y: y var name
    :param color: color var name
    :param title_input: title name of plot
    :param xlab_input: x label of plot
    :param ylab_input: y label of plot
    :param sd: standard deviation
    """
    df = pd.read_csv(path_name)
    df[f"{color}"] = df[f"{color}"].apply(str)
    g = ggplot(df, aes(x=x, y=y, color=color, fill=color)) + \
        geom_point() + \
        geom_smooth() + \
        geom_errorbar(aes(x=x, ymin="rETR-STD", ymax="rETR+STD", width=50)) + \
        ggtitle(title_input) + \
        xlab(xlab_input) + \
        ylab(ylab_input) + \
        theme_bw()
    g.save(save_name)


def od_to_concentration(od):
    """
    convert optic density to protein concentration
    :param od: optic density
    :return: protein concentration
    """
    return (od - 0.564)/0.5161


if __name__ == '__main__':
    # rhizome boxplot
    create_boxplot(r"Data/Seagrasses data - rhizome.csv", r"Plots/rhizome_elongation.png", "Tank",
                   "average length per day",
                   "Tank", "Rhizome average daily elongation", "Temperature (Celsius)",
                   "Rhizome average daily elongation (cm/day)")

    # Chlorophyll reading graph
    # Chlorophyll A
    create_boxplot_dry_wet(r"Data/Chlorophyll readings excel sheet from hung.csv", r"Plots/Chlorophyll_a.png",
                           "Tank no",
                           "Chl a mg/g FW",
                           "Tank no", "Chlorophyll A", "Temperature (Celsius)", "Chl a mg/g DW")

    # Chlorophyll B
    create_boxplot_dry_wet(r"Data/Chlorophyll readings excel sheet from hung.csv", r"Plots/Chlorophyll_b.png",
                           "Tank no",
                           "Chl b mg/g FW",
                           "Tank no", "Chlorophyll B", "Temperature (Celsius)", "Chl b mg/g DW")

    # Chlorophyll A+B
    create_boxplot_dry_wet(r"Data/Chlorophyll readings excel sheet from hung.csv", r"Plots/Chlorophyll_a_b.png",
                           "Tank no",
                           "Chl a+b mg/g FW",
                           "Tank no", "Chlorophyll A+B", "Temperature (Celsius)", "Chl a+b mg/g DW")

    # Carotenoids
    create_boxplot_dry_wet(r"Data/Chlorophyll readings excel sheet from hung.csv", r"Plots/Carotenoids.png", "Tank no",
                           "Carotenoids mg/g FW",
                           "Tank no", "Carotenoids", "Temperature (Celsius)", "Carotenoids mg/g DW")

    # Leaf mass
    create_boxplot(r"Data/Seagrasses data - leaf mass.csv", r"Plots/leaf_mass.png", "treatment [C]",
                   "average mass per day [gr]", "treatment [C]",
                   "Above ground mass accumulation", "Temperature (Celsius)",
                   "Average daily added mass (gr/day)")

    # Leaf internodes
    create_boxplot(r"Data/Seagrasses data - leaf mass.csv", r"Plots/leaf_internodes.png", "treatment [C]",
                   "internodes",
                   "treatment [C]", "New internodes", "Temperature (Celsius)",
                   "# New Internodes")

    # Protein content
    create_colplot(r"Data/Protein_Conc_full.csv", r"Plots/protein_concentration.png", "Tank",
                   "Prot_Conc",
                   "Tank", "Protein content", "Temperature (Celsius)",
                   "Protein concentration (mg/ml)")

    # night Fv/Fm
    create_boxplot(r"Data/Seagrasses data - Night Fv_Fm.csv", r"Plots/fv_fm_night_time.png", "Tank", "Fv/Fm", "Tank",
                   "Fv/Fm\nNight time", "Temperature (Celsius)", "Fv/Fm")

    # day Fv/Fm
    create_boxplot(r"Data/Seagrasses data - Day Fv_Fm.csv", r"Plots/fv_fm_day_time.png", "Tank", "Fv/Fm", "Tank",
                   f"$\Delta$Fv/Fm'\nDay time", "Temperature (Celsius)", f"$\Delta$Fv/Fm'")

    # Light Curve
    create_scatter_line(r"Data/std_light_curve.csv", r"Plots/light_curve.png", "1:PAR", "rETR", "Tank",
                        "Light Curve", "PAR", "rETR", "STD")
