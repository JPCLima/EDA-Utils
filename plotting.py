import matplotlib.pyplot as plt
import seaborn as sns

def plot_corr(x, y, df):
    """ 
    Returns a barplot using the x and y from the dataframe provided. With this plot we can see the correlations between the x and y
    """
    fig = plt.figure(figsize = (10,6))
    sns.barplot(x = x, y = y, data = df).set_title(y)
    plt.show()