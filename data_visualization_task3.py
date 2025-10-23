# ...existing code...
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Option: set to True to save figures instead of showing them
SAVE_FIGS = False

# ...existing code...
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [15000, 18000, 22000, 25000, 27000, 30000],
    'Profit': [4000, 5000, 7000, 8000, 9000, 10000]
}

df = pd.DataFrame(data)

# 1. Bar Chart: Monthly Sales
plt.figure(figsize=(8,5))
sns.barplot(x='Month', y='Sales', data=df, palette='Blues_d')
plt.title('Monthly Sales Overview')
plt.xlabel('Month')
plt.ylabel('Sales (in ₹)')
if SAVE_FIGS:
    plt.savefig('fig_bar.png', bbox_inches='tight')
    plt.close()
else:
    plt.show()

# 2. Line Chart: Sales vs Profit
plt.figure(figsize=(8,5))
plt.plot(df['Month'], df['Sales'], marker='o', label='Sales')
plt.plot(df['Month'], df['Profit'], marker='o', label='Profit')
plt.title('Sales vs Profit Trend')
plt.xlabel('Month')
plt.ylabel('Amount (₹)')
plt.legend()
plt.grid()
if SAVE_FIGS:
    plt.savefig('fig_line.png', bbox_inches='tight')
    plt.close()
else:
    plt.show()

# 3. Pie Chart: Contribution of Each Month to Total Sales
plt.figure(figsize=(6,6))
plt.pie(df['Sales'], labels=df['Month'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Sales Distribution by Month')
if SAVE_FIGS:
    plt.savefig('fig_pie.png', bbox_inches='tight')
    plt.close()
else:
    plt.show()

# 4. Heatmap (Correlation between Sales and Profit)
plt.figure(figsize=(5,4))
sns.heatmap(df[['Sales', 'Profit']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
if SAVE_FIGS:
    plt.savefig('fig_heatmap.png', bbox_inches='tight')
    plt.close()
else:
    plt.show()
# ...existing code...