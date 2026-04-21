import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


os.chdir("D:\Desktop\IBI\IBI1_2025-26\Practical10")  

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print("Data read successfully!")
print("Basic Data Information：")
dalys_data.info()
print("\n" + "="*50 + "\n")


print("Top 10 rows of data (Year and DALYs)：")
print(dalys_data.iloc[0:10, [2, 3]])  
print("\n")

# afghanistan
afghanistan = dalys_data.loc[dalys_data["Entity"] == "Afghanistan"].head(10)
print("Afghanistan data from the first 10 years：")
print(afghanistan[["Year", "DALYs"]])


max_year_afg = afghanistan.loc[afghanistan["DALYs"].idxmax()]
print(f"\n The year with the highest DALYs in Afghanistan in the first 10 years：{max_year_afg['Year']}，number：{max_year_afg['DALYs']}")
print("\n" + "="*50 + "\n")


my_columns = [True, True, True, True]
zimbabwe = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe"]
zimbabwe_filtered = zimbabwe.iloc[:, my_columns]

print("All data of Zimbabwe (Boolean index filtering)：")
print(zimbabwe_filtered[["Year", "DALYs"]].head())  # Show the first 5 lines

min_year_zim = zimbabwe["Year"].min()
max_year_zim = zimbabwe["Year"].max()
print(f"\n Zimbabwe data year range：{min_year_zim} Year — {max_year_zim} ")
print("\n" + "="*50 + "\n")


data_2019 = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

# highest/lowest
highest_2019 = data_2019.loc[data_2019["DALYs"].idxmax()]
lowest_2019 = data_2019.loc[data_2019["DALYs"].idxmin()]

print("2019 Global DALYs Statistics：")
print(f"Higest country：{highest_2019['Entity']}，number：{highest_2019['DALYs']}")
print(f"lowest country：{lowest_2019['Entity']}，number：{lowest_2019['DALYs']}")
print("\n" + "="*50 + "\n")


country_high = highest_2019['Entity']
data_high = dalys_data.loc[dalys_data["Entity"] == country_high]

plt.figure(figsize=(10, 5))
plt.plot(data_high["Year"], data_high["DALYs"], 'r-o', linewidth=2, markersize=6)
plt.title(f"{country_high} DALYs Time trend", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("DALYs ", fontsize=12)
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# I draw the picture of England, for example
uk_data = dalys_data.loc[dalys_data["Entity"] == "United Kingdom"]
plt.figure(figsize=(10, 5))
plt.plot(uk_data["Year"], uk_data["DALYs"], 'b-o')
plt.title("England DALYs trend", fontsize=14)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.show()


print(" Custom question: What is the trend of DALYs in China over time?？")
china_data = dalys_data.loc[dalys_data["Entity"] == "China"]
print("China Data Display (First 5 Rows）：")
print(china_data[["Year", "DALYs"]].head())

# China chart
plt.figure(figsize=(10, 5))
plt.plot(china_data["Year"], china_data["DALYs"], 'g-o', linewidth=2)
plt.title("Trends of DALYs over time in China", fontsize=14)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.show()

