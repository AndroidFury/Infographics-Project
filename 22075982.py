# -*- coding: utf-8 -*-
"""
 

@author:
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset - "https://www.kaggle.com/datasets/akshaymalviya/police-department-incidents-previous-year-2016" 
df=pd.read_csv("Police_Department_Incidents_Previous_Year_2016.csv")

# Data Exploration and Summary Statistics
summary_stats = df.describe()

# Create Infographics
plt.figure(figsize=(18, 14))

# Plot 1: Crime Distribution by Category
plt.subplot(2, 3, 1)
crime_category_distribution = df['Category'].value_counts().head(10)
crime_category_distribution.plot(kind='bar', color='skyblue')
plt.title('Top 10 Crime Categories')
plt.xlabel('Crime Category')
plt.ylabel('Number of Incidents')
plt.text(0.5, -0.35, """This plot shows the distribution of the top 10 crime categories in San Francisco.
         The most common crime category is Larceny/Theft, with 40,409 incidents.""", ha='center', transform=plt.gca().transAxes)

# Plot 2: Proportion of Crime on Each Day
plt.subplot(2, 3, 2)
crime_by_day_proportion = df['DayOfWeek'].value_counts(normalize=True)
crime_by_day_proportion.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Proportion of Crime on Each Day')
plt.ylabel("")  
plt.legend(bbox_to_anchor=(1, 0.5), loc="center left")
plt.tight_layout()
plt.text(0.5, -0.15, """This pie chart illustrates the proportion of reported crimes on each day of the week.
         Friday has the highest proportion of crimes at approximately 15.5%.""", ha='center', transform=plt.gca().transAxes)

# Plot 3: Monthly Crime Trends Over Years
plt.subplot(2, 3, 3)
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I:%M:%S %p')
df['Year'] = df['Date'].dt.year
monthly_crime_trends = df.groupby(['Year', df['Date'].dt.month]).size().unstack().T
sns.heatmap(monthly_crime_trends, cmap='YlGnBu')
plt.title('Monthly Crime Trends Over Years')
plt.xlabel('Month')
plt.ylabel('Year')
plt.text(0.5, -0.25, 'This heatmap provides an overview of monthly crime trends over the years.', ha='center', transform=plt.gca().transAxes)

# Plot 4: Crime Distribution by District
plt.subplot(2, 3, 4)
crime_by_district = df['PdDistrict'].value_counts().head(5)
crime_by_district.plot(kind='bar', color='salmon')
plt.title('Top 5 Districts with Highest Crime')
plt.xlabel('Police District')
plt.ylabel('Number of Incidents')
plt.text(0.5, -0.35, """
         
         
         This bar plot highlights the distribution of 
         crimes across the top 5 districts in San Francisco.
         The Southern district has the highest number of reported crimes, 
         by Northern and Mission districts.""", ha='center', transform=plt.gca().transAxes)

# Plot 5: Distribution of Crime Times
plt.subplot(2, 3, 5)
crime_times_distribution = df['Time'].value_counts().head(10)
crime_times_distribution.plot(kind='barh', color='lightgreen')
plt.title('Top 10 Crime Occurrence Times')
plt.xlabel('Number of Incidents')
plt.ylabel('Time of Day')
plt.text(0.5, -0.30, """This horizontal bar plot visualizes the 
         distribution of reported crimes during different times of the day.
         Crimes are most frequently reported around 12:00 PM and 12:01 AM.
         There's a peak in crime occurrences during the evening hours,
         with 18:00 and 19:00 being notable.
           """, ha='center', transform=plt.gca().transAxes)
plt.text(0.5, -0.90, """ Conclusions:
High Crime Districts:The Southern district stands out as the area with the highest reported incidents, followed by other central districts.
Temporal Trends:Crimes are more likely to occur on Fridays and during evening hours.
Common Crime Categories:Larceny/Theft, Other Offenses, and Non-Criminal activities are the most common types of incidents.
Geographical Focus:The dataset is centered around San Francisco, as indicated by the latitude and longitude statistics.
Law Enforcement Insights:The insights can guide law enforcement agencies in allocating resources and planning strategies to address specific crime categories, days, and districts.
         """, ha='center', transform=plt.gca().transAxes)
# Add title
plt.text(0.5, 1, 'San Francisco Crime Analysis', ha='center', fontsize=20, transform=plt.gcf().transFigure)

# Add student information
plt.text(0.5, 1.05, 'Name - Muhammad Furqan ul Hassan\nStudent ID - 22075982', ha='center', fontsize=12, transform=plt.gcf().transFigure)
 
 
# Add padding to prevent text overlap
plt.subplots_adjust(wspace=0.4, hspace=0.6)

# Save the infographic as a PNG file
plt.savefig("22075982.png", dpi=300)
