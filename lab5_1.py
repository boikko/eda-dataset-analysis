import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 1. Reading the dataset
df = pd.read_csv('data.csv')

print("--- First 5 rows of the DataFrame ---")
print(df.head())
print("\n--- DataFrame Shape ---")
print(df.shape)
print("\n--- Column Names ---")
print(df.columns)
print("\n--- Data Types ---")
print(df.dtypes)
print("\n--- DataFrame Info ---")
df.info()
print("\n--- Descriptive Statistics ---")
print(df.describe())

# Set seaborn theme
sns.set_theme(style="whitegrid")

# 2. Combining static plots into a clean 2x2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(16, 11), constrained_layout=True)
fig.suptitle('Exploratory Data Analysis: Statistical Overview', fontsize=16, fontweight='bold')

# Plot 1: Scatter plot (Lower vs Upper by Sex)
sns.scatterplot(
    data=df, x='lower', y='upper', hue='sex', alpha=0.6, ax=axes[0, 0]
)
axes[0, 0].set_title('Lower vs Upper Bounds by Sex', fontsize=12, fontweight='bold', pad=10)
axes[0, 0].set_xlabel('Lower Bound')
axes[0, 0].set_ylabel('Upper Bound')

# Plot 2: Histogram with KDE for 'val'
sns.histplot(
    df['val'],
    kde=True,
    bins=30,
    color='skyblue',
    ax=axes[0, 1]
)
axes[0, 1].set_title('Distribution of Value (Histogram & KDE)', fontsize=12, fontweight='bold', pad=10)
axes[0, 1].set_xlabel('Value (val)')
axes[0, 1].set_ylabel('Count')

# Plot 3: Boxplot of 'val' by 'sex'
sns.boxplot(
    data=df, x='sex', y='val', hue='sex', palette='Set2', legend=False, ax=axes[1, 0]
)
axes[1, 0].set_title('Distribution of Value by Sex', fontsize=12, fontweight='bold', pad=10)
axes[1, 0].set_xlabel('Sex')
axes[1, 0].set_ylabel('Value (val)')

# Plot 4: Value vs Upper Bound colored by Year
sns.scatterplot(
    data=df, x='val', y='upper', hue='year', palette='viridis', alpha=0.5, ax=axes[1, 1]
)
axes[1, 1].set_title('Value vs Upper Bound by Year', fontsize=12, fontweight='bold', pad=10)
axes[1, 1].set_xlabel('Value (val)')
axes[1, 1].set_ylabel('Upper Bound')

# Save dashboard image for GitHub README
plt.savefig('eda_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()

# 3. Jointplot with proper top margin so the title is fully visible
g = sns.jointplot(data=df, x='val', y='upper', kind='reg', color='teal', height=7)
g.figure.subplots_adjust(top=0.92)  # Leaves space at the top for the title
g.figure.suptitle('Joint Distribution of Value and Upper Bound', fontsize=13, fontweight='bold')
g.set_axis_labels('Value (val)', 'Upper Bound (upper)')

# Save jointplot image for GitHub README
plt.savefig('joint_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. Pairplot for numeric columns
numeric_cols = ['year', 'val', 'upper', 'lower']
p = sns.pairplot(df[numeric_cols], diag_kind='kde')
p.figure.subplots_adjust(top=0.93)
p.figure.suptitle('Pairwise Relationships of Numeric Features', fontsize=14, fontweight='bold')
plt.show()

# 5. Interactive Plotly scatter plot
fig_plotly = px.scatter(
    df.sample(n=1000, random_state=42),
    x='val',
    y='upper',
    color='sex',
    hover_data=['cause', 'year', 'location'],
    title='Interactive Scatter Plot: Value vs Upper Bound',
    labels={'val': 'Value (val)', 'upper': 'Upper Bound (upper)', 'sex': 'Sex'}
)

fig_plotly.update_layout(template='plotly_white')
fig_plotly.show()
