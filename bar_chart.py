import matplotlib.pyplot as plt

# Gender categories and their counts (example data)
genders = ['female', 'Male', 'Non-Binary', 'Other']
counts = [500, 600, 100, 50]

# Create bar chart
plt.figure(figsize=(7, 5))
plt.bar(genders, counts, color='pink')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Gender in a Population')
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines
plt.show()
