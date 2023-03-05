import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load data from a CSV file.

    Args:
    file_path (str): File path of the CSV file.

    Returns:
    pandas.DataFrame: DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(file_path)


def create_line_plot(df):
    """Create a line plot of the population trends for the top 5 countries.

    Args:
    df (pandas.DataFrame): DataFrame containing the population data.

    Returns:
    None
    """
    for i in range(len(df.index)):
        country = df.iloc[i][5:13].sort_values()
        name = df.iloc[i][2]
        plt.plot(country.index, country, label=name)
    plt.title('Top 5 Countries Population by Years (millions)')
    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.legend()
    plt.show()


def create_bar_chart(df):
    """Create a bar chart of the population trends for a given country.

    Args:
    df (pandas.DataFrame): DataFrame containing the population data.

    Returns:
    None
    """
    for i in range(len(df.index)):
        country = df.iloc[i][5:13].sort_values()
        name = df.iloc[i][2]
        plt.figure(figsize=(10, 5))
        ax = sns.barplot(x=country.index, y=country, palette='bright')
        ax.bar_label(ax.containers[0], fmt='%g', label_type='edge', labels=country / 1000)
        plt.title(str(name) + ' Population by Years (millions)')
        plt.xlabel('Years')
        plt.ylabel('Population')
        plt.show()


def create_pie_chart(df):
    """Create a pie chart of the population ratios for the top 10 countries.

    Args:
    df (pandas.DataFrame): DataFrame containing the population data.

    Returns:
    None
    """
    palette_color = sns.color_palette('bright')
    plt.figure(figsize=(7, 5))
    explode = [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    plt.pie(df['World Population Percentage'][:10], labels=df['Country/Territory'][:10], colors=palette_color,
            explode=explode)
    plt.xticks(rotation=45)
    plt.title('The ratio of the population of the 10 most populous countries to the world population')
    plt.show()


def main():
    df = load_data('world_population.csv')
    print(df.head())

    df_copy = df.copy()
    df_copy = df_copy.sort_values(by='Rank', ascending=True)
    df_copy.columns = ['Rank', 'CCA3', 'Country/Territory', 'Capital', 'Continent',
                       '2022', '2020', '2015',
                       '2010', '2000', '1990',
                       '1980', '1970', 'Area (km²)', 'Density (per km²)',
                       'Growth Rate', 'World Population Percentage']
    print(df_copy.head())

    print('Shape of our data', df_copy.shape)

    create_line_plot(df_copy.head(5))

    create_bar_chart(df_copy.head(1))

    create_pie_chart(df_copy)


if __name__ == '__main__':
    main()
