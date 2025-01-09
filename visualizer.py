import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset():
    """Load the dataset from a CSV file."""

    # Load the dataset
    df = pd.read_csv('shopping_trends.csv')
    return df

def show_dataset_info(df):
    """Display information about the dataset."""

    # Display the first 5 rows of the dataset
    print(df.head())

    # Display descriptive statistics of the dataset
    print(df.describe())

    # Display information about the dataset
    print(df.info())

    # Check for missing values
    print(df.isnull().sum())  

def visualize_data_1(df):
    """Simple visualization of the dataset"""

    # Create a new figure
    plt.figure(figsize=(20, 10))

    # Histogram of Age
    plt.subplot(3, 2, 1)
    sns.histplot(df['Age'], bins=30, kde=True)
    plt.title('Distribution of Age')
    plt.xlabel('Age')
    plt.ylabel('Frequency')

    # Pie Chart of Gender
    plt.subplot(3, 2, 2)
    gender_counts = df['Gender'].value_counts()
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
    plt.title('Gender Distribution')

    # Bar Chart of Most Popular Item Purchased
    plt.subplot(3, 2, 3)
    sns.countplot(y='Item Purchased', data=df, order=df['Item Purchased'].value_counts().index)
    plt.title('Most Popular Item Purchased')
    plt.xlabel('Frequency')
    plt.ylabel('Item')  

    # Count Chart for Category
    plt.subplot(3, 2, 4)
    sns.countplot(y='Category', data=df, order=df['Category'].value_counts().index)
    plt.title('Category Distribution')
    plt.xlabel('Frequency')
    plt.ylabel('Category')

    # Box Plot of Purchase Amount (USD)
    plt.subplot(3, 2, 5)
    sns.boxplot(y='Purchase Amount (USD)', data=df)
    plt.title('Purchase Amount')
    plt.ylabel('Purchase Amount (USD)')

    # Line Plot of Average Purchase Amount by Season
    plt.subplot(3, 2, 6)
    sns.lineplot(x='Season', y='Purchase Amount (USD)', data=df, estimator='mean', ci=None, marker='o')
    plt.title('Average Purchase Amount by Season')
    plt.xlabel('Season')
    plt.ylabel('Average Purchase Amount (USD)')

    # Display the plots
    plt.tight_layout()
    plt.show()
    
def visualize_data_2(df):
    """More advanced visualization of the dataset."""

    # Create a new figure
    plt.figure(figsize=(20, 10))

    # Scatter Plot of Age vs Review Rating
    plt.subplot(3, 1, 1)
    sns.scatterplot(x='Age', y='Review Rating', data=df)
    plt.title('Age vs Review Rating')
    plt.xlabel('Age')
    plt.ylabel('Review Rating')
    # Findings: 
    # No clear relationship between Age and Review Rating
    # The points are scattered without any pattern, indicating that age does not significantly influence review ratings.

    # Violin Plot of Purchase Amount(USD) vs Category
    plt.subplot(3, 1, 2)
    sns.violinplot(x='Category', y='Purchase Amount (USD)', data=df)
    plt.title('Purchase Amount vs Category')
    plt.xlabel('Category')
    plt.ylabel('Purchase Amount (USD)')
    # Findings: 
    # Clothing: Wide in the middle, indicating a higher concentration of purchase amounts around the median value.
    # Footwear: Similar to Clothing, with a wide middle section, showing a higher concentration of purchase amounts near the median and more variability overall.
    # Outerwear: Narrower and tighter shape, suggesting purchase amounts are more consistent and less spread out, with fewer extreme values.
    # Accessories: Narrower shape, like Outerwear, indicating more consistent and predictable purchase amounts, with less spread in the data.

    # Boxen Plot of Purchase Amount(USD) vs Item Purchased
    plt.subplot(3, 1, 3)
    sns.boxenplot(x='Item Purchased', y='Purchase Amount (USD)', data=df)
    plt.title('Purchase Amount vs Item Purchased')
    plt.xlabel('Item Purchased')
    plt.ylabel('Purchase Amount (USD)')
    plt.xticks(rotation=45)
    # Findings: 
    # Some items have higher median purchase amounts, indicating they are generally more expensive
    # There are some outliers, indicatred by circle above or below the main body of the plot
    # The boxes get smaller as they move away from the median, indicating less data in those regions

    # Display the plot
    plt.tight_layout()
    plt.show()

def main():
    # Load the dataset
    df = load_dataset()

    # Display information about the dataset
    show_dataset_info(df)

    # Visualize the data
    visualize_data_1(df)
    visualize_data_2(df)

if __name__ == '__main__':
    main()




