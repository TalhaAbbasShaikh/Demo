import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'test.csv'
data = pd.read_csv(file_path)

# Clean the dataset by removing rows with NaN values
cleaned_data = data.dropna()

# Rename columns for better readability
cleaned_data.columns = [
    'User_ID', 'Age', 'Gender', 'Platform', 'Daily_Usage_Time_Minutes',
    'Posts_Per_Day', 'Likes_Received_Per_Day', 'Comments_Received_Per_Day',
    'Messages_Sent_Per_Day', 'Dominant_Emotion'
]

# Convert numeric columns to appropriate data types
numeric_columns = ['User_ID', 'Age', 'Daily_Usage_Time_Minutes',
                   'Posts_Per_Day', 'Likes_Received_Per_Day',
                   'Comments_Received_Per_Day', 'Messages_Sent_Per_Day']

for column in numeric_columns:
    cleaned_data[column] = pd.to_numeric(cleaned_data[column], errors='coerce')

# Drop rows with NaN values after type conversion
cleaned_data = cleaned_data.dropna()

# Ensure correct data types
cleaned_data['User_ID'] = cleaned_data['User_ID'].astype(int)
cleaned_data['Age'] = cleaned_data['Age'].astype(int)
cleaned_data['Daily_Usage_Time_Minutes'] = cleaned_data['Daily_Usage_Time_Minutes'].astype(int)
cleaned_data['Posts_Per_Day'] = cleaned_data['Posts_Per_Day'].astype(int)
cleaned_data['Likes_Received_Per_Day'] = cleaned_data['Likes_Received_Per_Day'].astype(int)
cleaned_data['Comments_Received_Per_Day'] = cleaned_data['Comments_Received_Per_Day'].astype(int)
cleaned_data['Messages_Sent_Per_Day'] = cleaned_data['Messages_Sent_Per_Day'].astype(int)

# Display the cleaned and organized dataset
print("Cleaned and Organized Data:")
print(cleaned_data.head())

# Summary statistics
print("Summary Statistics:")
print(cleaned_data.describe())

# Plotting histograms and pie charts

# Histogram for Age
plt.figure(figsize=(10, 5))
plt.hist(cleaned_data['Age'], bins=10, edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('age_distribution_histogram.png')
plt.show()

# Pie chart for Gender distribution
gender_counts = cleaned_data['Gender'].value_counts()
plt.figure(figsize=(10, 5))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.savefig('gender_distribution_pie_chart.png')
plt.show()

# Save the cleaned and organized dataset to a new CSV file
cleaned_data.to_csv('cleaned_organized_test.csv', index=False)

print("Cleaned and organized data has been saved to 'cleaned_organized_test.csv'.")
print("Histogram has been saved to 'age_distribution_histogram.png'.")
print("Pie chart has been saved to 'gender_distribution_pie_chart.png'.")
