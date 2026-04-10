import matplotlib.pyplot as plt

population_data = {"UK":     {"2020": 66.7,  "2024": 69.2},
            "China":  {"2020": 1426,  "2024": 1410},
            "Italy":  {"2020": 59.4,  "2024": 58.9},
            "Brazil": {"2020": 208.6, "2024": 212.0},
            "USA":    {"2020": 331.6, "2024": 340.1}}

percentage_change = {}
for country, data in population_data.items():
    pop_2020 = data["2020"]
    pop_2024 = data["2024"]
    change = ((pop_2024 - pop_2020) / pop_2020) * 100
    percentage_change[country] = change

print("Population Percentage Change (2020-2024) is")

for country, pct in percentage_change.items():
    print(f"{country}: {pct:.2f}%")

sorted_countries = sorted(percentage_change.items(), key=lambda x: x[1], reverse=True)


print("\nSorted by Percentage Change (Largest Increase to Largest Decrease) is ")
for country, pct in sorted_countries:
    print(f"{country}: {pct:.2f}%")


largest_increase_country = sorted_countries[0][0]
largest_decrease_country = sorted_countries[-1][0]
print(f"\nCountry with the largest population increase: {largest_increase_country}")
print(f"Country with the largest population decrease: {largest_decrease_country}")


countries = [item[0] for item in sorted_countries]
changes = [item[1] for item in sorted_countries]


plt.figure(figsize=(10, 6))
bars = plt.bar(countries, changes, color="Blue")

plt.axhline(y=0, color="black", linestyle="-", linewidth=0.8)

plt.title("Population Percentage Change (2020-2024)", fontsize=14)
plt.ylabel("Percentage Change (%)", fontsize=12)
plt.xlabel("Country", fontsize=12)
plt.xticks(rotation=15) 
plt.grid(axis="y", linestyle="--", alpha=0.7)  

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.,height + (0.1 if height >= 0 else -0.5),  f"{height:.2f}%",ha="center", va="bottom" if height >= 0 else "top")

plt.tight_layout()  
plt.show()
