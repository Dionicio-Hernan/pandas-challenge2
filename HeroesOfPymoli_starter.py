#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

# Display headers
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[2]:


# Display total number of players
purchase_data ["SN"].head()


# In[13]:


# Calculate total number of unique players based on screen name
unique_players = purchase_data["SN"].unique()
unique_players


# In[14]:


player_count = purchase_data["SN"].value_counts()
player_count


# In[20]:


# Insert total number of unique players into a simple data frame
frame_df = pd.DataFrame({"Player Count": ["576"]})
frame_df


# In[ ]:





# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[6]:


# Determine number of unique items
unique_items = purchase_data["Item Name"].value_counts()
count


# In[7]:


# Determine average price
average = purchase_data["Price"].mean()
average


# In[8]:


# Determine number of purchases
count = purchase_data["Purchase ID"].value_counts()
count


# In[21]:


# Determine total revenue
total_revenue = purchase_data["Price"].sum()
total_revenue


# In[22]:


# Insert findings into a simple data frame
frame_df = pd.DataFrame ({
    "Number of Unique Items": ["179"],
    "Average Price": ["$3.05"],
    "Number of Purchases": ["780"],
    "Total Revenue": ["$2,379.77"]
})
frame_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[58]:





# In[59]:


# Screen name by gender
total_count_gender = gender_stats.nunique()["SN"]
total_count_gender.to_frame()


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[81]:


# Group data by females
only_female_purch_count = purchase_data.loc[purchase_data["Gender"] == "Female"]
print(only_female_purch_count)


# In[149]:


# Create DataFrame of data above
# only_female_purch_count.loc[:, ["Purchase ID", "SN", "Item ID", "Price"]].head()


# In[86]:


# Calculate female average purchase price
female_avg_purch_price = only_female_purch_count.loc[:, ["Price"]].mean()
print(female_avg_purch_price)


# In[87]:


# Calculate female purchase count
female_purch_count = only_female_purch_count.loc[:, ["Item ID"]].count()
print(female_purch_count)


# In[88]:


# Calculate female total purchase value
female_total_purch_value = only_female_purch_count.loc[:, ["Price"]].sum()
print(female_total_purch_value)


# In[89]:


# Calculate female average per person
# female_avg_purch = only_female_purch_count.loc[:, ["Price"]].mean()


# In[90]:


# Group data by males
only_male_purch = purchase_data.loc[purchase_data["Gender"] == "Male"]
print(only_male_purch)


# In[150]:


# Create DataFrame of data above
# only_male_purch.loc[:, ["Purchase ID", "SN", "Item ID", "Price"]].head()


# In[93]:


# Calculate male average purchase price
male_avg_purch = only_male_purch.loc[:, ["Price"]].mean()
print(male_avg_purch)


# In[94]:


# Calculate male purchase count
male_purch_count = only_male_purch.loc[:, ["Item ID"]].count()
print(male_purch_count)


# In[95]:


# Calculate male total purchase value
male_total_purch_value = only_male_purch.loc[:, ["Price"]].sum()
print(male_total_purch_value)


# In[152]:


# Create DataFrame for data above 
purch_analysis_gender_df = pd.DataFrame (
    {"Gender": ["Female", "Male", "Other/Non-Disclosed"],
    "Purchase Count": ["113", "652", "15"],
    "Average Purchase Price": ["$3.20", "$3.02", "$3.35"],
    "Total Purchase Value": ["$361.94", "$1,967.64", "$50.19"],
    "Avg Total Purchase per Person": ["0", "0", "0"]
    }
)
     
purch_analysis_gender_df

# Could not compute avg total purchase per person


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[104]:





# In[120]:


# Establish bins for ages
age_bins = [0, 9.9, 14.9, 19.9, 24.9, 29.9, 34.9, 39.9, 40]

# Create names for the bins
age_bin_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

pd.cut(purchase_data["Age"], age_bins, labels=age_bin_names).head()


# In[117]:


# Place the data series into a new column inside of the DataFrame
purchase_data["Age Group"] = pd.cut(purchase_data["Age"], age_bins, labels=age_bin_names)
purchase_data.head()


# In[118]:


# Create a GroupBy 
age_group = purchase_data.groupby("Age Group")

# Find how many rows fall into each bin
print(age_group["Age"].count())


# In[124]:


# Create DataFrame to hold results
age_demographics_df = pd.DataFrame (
    {"Age Group": ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"],
    "Total Count": ["23", "28", "136", "365", "101", "73", "41", "6"],
    "Percentage of Players": ["2.95%", "3.82%", "18.58%", "44.79%", "13.37%", "9.03%", "5.38%", "2.08%"] 
    }
)
     
age_demographics_df

# Need to figure out how to calculate percentages of numbers above into DataFrame without doing it manually


# In[131]:


range_purchase_count = print(age_group["Purchase ID"].count())


# In[133]:


# Get the average of each column within the GroupBy object
range_avg_price = print(age_group["Price"].mean())


# In[134]:


range_purch_value = print(age_group["Price"].sum())


# In[139]:


# avg_per_person = print(age_group["Price"])/(purchase_data["Purchase ID"])


# In[154]:


# Create summary DataFrame for purchasing analysis by age
purch_analysis_df = pd.DataFrame (
    {"Age Ranges": ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"],
    "Purchase Count": ["23", "28", "136", "365", "101", "73", "41", "6"],
    "Average Purchase Price": ["$3.35", "$2.96", "$3.04", "$3.05", "$2.90", "$2.93", "$3.60", "$2.79"],
    "Total Purchase Value": ["$77.13", "$82.78", "$412.89", "$1,114.06", "$293.00", "$214.00", "$147.67", "$16.71"],
    "Avg Total Purchase per Person": ["0", "0", "0", "0", "0", "0", "0", "0"]
    }
)
     
purch_analysis_df


# In[156]:


# Done


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[155]:


# Top Spenders


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[148]:


# Set index to "SN"
# purchase_data_sn_index = purchase_data.set_index("SN")
# purchase_data_sn_index.head()


# In[147]:


# Lisosia_to_Iskadarya = purchase_data.loc[[["Lisosia93"count(), ["Idastidru52"].count(), ["Chamjask73"].count(), ["Iral74"].count(), ["Iskadarya95"].count()]
# print(lisosia_to_Iskadarya)


# In[ ]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[160]:


# Retrieve list of all unique values in "Item ID"
purchase_data["Item Name"].unique()


# In[171]:


# Sort the DataFrame by the values in the Item ID column
highest_item_name = purchase_data.sort_values("Item Name")
highest_item_name.head()


# In[172]:


# Reset the index so that the index is now based on the Item Name
# highest_item_name = purchase_data.sort_values("Item Name" ascending=False)

highest_item_name.head()


# In[ ]:


# Identify purchase count
# Calculate average item price
# total purchase value


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[10]:


# Sort above table by total purchase value in descending order

