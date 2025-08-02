import pandas as pd
import numpy as np
df=pd.read_excel("linkedin_job_posts_insights.xlsx")
print("Shape of dataset: ", df.shape)
print("\n Column names: ")
print(df.columns)#column names
print("\n First five rows: ")
print(df.head())
df=df.dropna(subset=['job_title'])#delete rows with empty job titles
df=df.drop_duplicates(subset=['job_title'])#delete rows with duplicate job titles
df['job_title']=df['job_title'].str.strip().str.replace('\n',' ',regex=True)# remove extra spaces and \n
df['industry']=df['industry'].astype(str).str.strip().str.replace('\n',' ',regex=True)# remove extra spaces and \n
print("\n Cleaned dataset shape:", df.shape)
print("\n Top 10 job titles:")
print(df['job_title'].value_counts().head(10))
import matplotlib.pyplot as plt
# visualization of job titles
top_jobs =df['job_title'].value_counts().head(10)
plt.figure(figsize=(10,6))
top_jobs.plot(kind='barh', color='skyblue' )
plt.title("Top 10  In-Demand job titles")
plt.xlabel("Number of listings")
plt.ylabel("job titles")
plt.gca().invert_yaxis()# highest will be on top
plt.tight_layout()
plt.show()
#visualisation of industries
print("\n generating pie chart for industries.....")
top_industries = df['industry'].value_counts().head(10)
plt.figure(figsize=(8,8))
plt.pie(top_industries, labels=top_industries.index, autopct="%1.1f%%", startangle=140,textprops={'fontsize': 9})
plt.title("top 10 hiring industries(percentage)")
plt.axis('equal')# equal aspect ratioto make pie look perfect
plt.tight_layout()
plt.show()
# visualization for seniority level
# Clean seniority_level values
df['seniority_level'] = df['seniority_level'].astype(str).str.strip().str.replace('\n', '', regex=True)

# Filter out irrelevant or misclassified entries
irrelevant = ['Full-time', 'Part-time', 'Not Applicable', 'None', 'null', 'nan']
df = df[~df['seniority_level'].isin(irrelevant)]

# Recalculate top 10 after cleaning

top_seniority = df['seniority_level'].value_counts().head(10)
print("\n Top 10 sinority levels: ")
print(top_seniority)

plt.figure(figsize=(10,6))
plt.plot(top_seniority.index, top_seniority.values, marker='o',color='purple')
plt.title("top 10 in demand seniority levels")
plt.xlabel("seniority level")
plt.ylabel("number of listing")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#visualize job functions
df['job_function'] = df['job_function'].dropna().astype(str).str.strip().str.lower().str.title()

top_functions = df['job_function'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10,6))
ax.set_facecolor('#f9f9f9')  # light background
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#FFA07A', '#00CED1',
          '#FFD700', '#E9967A', '#20B2AA', '#9370DB', '#F08080']

top_functions.plot(kind='barh', color=colors, ax=ax)

ax.set_title("Top 10 In-Demand Job Functions", fontsize=16, fontweight='bold')
ax.set_xlabel("Number of Listings", fontsize=12)
ax.set_ylabel("Job Functions", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)
ax.invert_yaxis()

# Annotate bars
for i, v in enumerate(top_functions):
    ax.text(v + 0.5, i, str(v), color='black', va='center', fontweight='bold')

plt.tight_layout()
plt.show()

# visualize location 

# Clean the location column
df['location'] = df['location'].astype(str).str.strip().str.replace('\n', '', regex=True)

# Get top 10 most common locations
top_locations = df['location'].value_counts().head(10)
print("\nTop 10 job locations:")
print(top_locations)

# Plot
plt.figure(figsize=(10, 6))
top_locations.plot(kind='barh', color='teal')
plt.gca().invert_yaxis()  # highest at the top
plt.title("Top 10 Job Locations")
plt.xlabel("Number of Listings")
plt.ylabel("Location")
plt.tight_layout()
plt.show()


print("RESULT OF THE ANALYSIS IS AS FOLLOWING")
print("1. The most in demand job skill AKA job title is Software Developer")
print("2. The most hiring industries are Technology,information and internet and IT services and IT consulting")
print("3. The most prefferd sinority level MID-SENIOR LEVEL")
print("4. Engineering and Information Technology is most in demand job Functions")
print("5. the top job locations are Bengaluru and Karnatka in India")