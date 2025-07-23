# 📦 Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 Optional: Configure seaborn for better plots
sns.set(style="whitegrid")

# 🧾 Load the dataset
df = pd.read_csv('retail_sales_dataset.csv')  # Use your file name

# 🛠️ Data Preprocessing
df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")
df['Month'] = df['Date'].dt.to_period('M')

# 📊 1. Total Sales by Product Category
plt.figure(figsize=(8, 6))
category_sales = df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False)
sns.barplot(x=category_sales.values, y=category_sales.index, palette="Blues_d")
plt.title('Total Sales by Product Category')
plt.xlabel('Total Sales')
plt.ylabel('Product Category')
plt.tight_layout()
plt.show()

# 📈 2. Monthly Sales Trend
plt.figure(figsize=(10, 6))
monthly_sales = df.groupby('Month')['Total Amount'].sum()
monthly_sales.index = monthly_sales.index.astype(str)  # convert Period to string for x-axis
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 🧑‍🤝‍🧑 3. Sales Distribution by Gender
plt.figure(figsize=(6, 6))
gender_sales = df.groupby('Gender')['Total Amount'].sum()
gender_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#ff9999'])
plt.title('Sales Distribution by Gender')
plt.ylabel('')
plt.tight_layout()
plt.show()

# 🎂 4. Age Distribution of Customers
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=6, kde=True, color='coral')
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()

# 📦 5. Quantity sold per Product Category
plt.figure(figsize=(8, 6))
quantity_data = df.groupby('Product Category')['Quantity'].sum().sort_values()
sns.barplot(x=quantity_data.values, y=quantity_data.index, palette='coolwarm')
plt.title('Total Quantity Sold per Product Category')
plt.xlabel('Total Quantity')
plt.ylabel('Product Category')
plt.tight_layout()
plt.show()
