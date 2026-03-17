import matplotlib.pyplot as plt

heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

total_patients = len(heart_rates)
average_heart_rate = sum(heart_rates) / total_patients


print(f"Total number of patients in dataset: {total_patients}")
print(f"Average heart rate of patients: {average_heart_rate:.2f} beats per minute (bpm)")


low_hr_count = 0    # Low: <60 bpm
normal_hr_count = 0 # Normal: 60-120 bpm
high_hr_count = 0   # High: >120 bpm

for hr in heart_rates:
    if hr < 60:
        low_hr_count += 1
    elif hr > 120:
        high_hr_count += 1
    else:
        normal_hr_count += 1

# Print category counts
print("\nHeart rate category statistics:")
print(f"Low heart rate (<60 bpm): {low_hr_count} patients")
print(f"Normal heart rate (60-120 bpm): {normal_hr_count} patients")
print(f"High heart rate (>120 bpm): {high_hr_count} patients")

# Find the category with the most patients
category_counts = {"Low": low_hr_count,"Normal": normal_hr_count,"High": high_hr_count}
largest_category = max(category_counts, key=category_counts.get)
print(f"\nCategory with the most patients: {largest_category}")


plt.figure(figsize=(8, 6))
labels = ["Low", "Normal", "High"]
sizes = [low_hr_count, normal_hr_count, high_hr_count]
colors = ["#FF9999", "#66B2FF", "#99FF99"]  
explode = (0.05, 0.05, 0.05) 


plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct="%1.1f%%", shadow=True, startangle=90 ) 
plt.axis("equal")  # Ensure pie chart is a perfect circle
plt.title("Distribution of Patients by Heart Rate Category", fontsize=14)  # Chart title
plt.show()  # Display the chart
