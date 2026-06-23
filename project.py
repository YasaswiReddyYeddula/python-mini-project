import plotly.express as px

df = px.data.iris()
print(df)

#PART 1: Dataset Exploration -------------------------------------------------
#Task 1 
#Display first 5 records. 
print(df.head())

#Task 2 
#Display last 5 records. 
print(df.tail())

#Task 3 
#Display dataset dimensions. 
print(df.shape)

#Task 4 
#Display dataset information.
print(df.info())

#Task 5 
#Display column names. 
print(df.columns)

#Task 6 
#Display data types.
print(df.dtypes)



#PART 2: Data Analysis ---------------------------------------------------------

#Task 1 
#Find average sepal length. 
Avg_sepal_length = df["sepal_length"].mean()
print(Avg_sepal_length)

#Task 2 
#Find average petal length. 
Avg_petal_length = df["petal_length"].mean()
print(Avg_petal_length)

#Task 3 
#Find maximum sepal length.
max_sepal_length = df["sepal_length"].max()
print(max_sepal_length)

#Task 4 
#Find minimum petal width. 
min_petal_width = df["petal_width"].min()
print(min_petal_width)

#Task 5 
#Find total number of flower species. 
total_flower_species = df["species"].nunique()
print(total_flower_species)

flower_species = len(df["species"])
print(flower_species)

#Task 6 
#Find count of each species.
species_count = df["species"].value_counts()
print(species_count)


#PART 3: NumPy Practice-----------------------------------------------------------------------
#Convert the following columns into NumPy arrays. 
df["sepal_length"] 
df["petal_length"] 

import numpy as np

sepal_length = np.array(df["sepal_length"])
print(sepal_length)

petal_length = np.array(df["petal_length"])
print(petal_length)

#Task 1 
#Find mean. 
sl_mean = df["sepal_length"].mean()
print(sl_mean)

pl_mean = df["petal_length"].mean()
print(pl_mean)

#Task 2 
#Find median. 
sl_median = df["sepal_length"].median()
print(sl_median)

pl_median = df["petal_length"].median()
print(pl_median)

#Task 3 
#Find maximum value. 
sl_max = df["sepal_length"].max()
print(sl_max)

pl_max = df["petal_length"].max()
print(pl_max)

#Task 4 
#Find minimum value. 
sl_min = df["sepal_length"].min()
print(sl_min)

pl_min = df["petal_length"].min()
print(pl_min)

#Task 5 
#Find standard deviation.
sl_std = df["sepal_length"].std()
print(sl_std)

pl_std = df["petal_length"].std()
print(pl_std)


#PART 4: Visualization using Matplotlib--------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("Iris.csv")
print(df)
df.columns

#CHART 1: LINE CHART
plt.figure(figsize = (10,8))
plt.plot(df.index, df["SepalLengthCm"], marker='o', color="Green")
plt.title("Sepal Length by index")
plt.xlabel("Index")
plt.ylabel("Sepal_length")
plt.grid(True)
Line_chart_Path = "Sepal_Lengt_Line_Chart.png"
plt.savefig(Line_chart_Path, bbox_inches = 'tight')
plt.show()
plt.close()

#CHART 2: BAR CHART
species_count = df["Species"].value_counts()

plt.figure(figsize = (10,8))
plt.bar(species_count.index, species_count.values, color="Blue")
plt.title("Count of Species")
plt.xlabel("Species")
plt.ylabel("Species Count")
Bar_chart_Path = "Species_count_Bar_Chart.png"
plt.savefig(Bar_chart_Path, bbox_inches = 'tight')
plt.show()
plt.close()

#CHART 3: SCATTER PLOT
plt.figure(figsize = (10,8))
plt.scatter(df["SepalLengthCm"], df["PetalLengthCm"], marker='o', color="Red")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.grid(True)
Scatter_chart_Path = "SP_Length_scatter_Chart.png"
plt.savefig(Scatter_chart_Path, bbox_inches = 'tight')
plt.show()
plt.close()


#CHART 4: HISTOGRAM
plt.figure(figsize = (10,8))
plt.hist(df["SepalWidthCm"], bins = 20, color = "SkyBlue" )
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
Histogram_chart_Path = "Sepal_width_Histogram.png"
plt.savefig(Histogram_chart_Path, bbox_inches = 'tight')
plt.show()
plt.close()

print("Histogram is saved at:", Histogram_chart_Path)


#PART 5: Visualization using Plotly----------------------------------------------------------------------------
import plotly.express as px

#Chart 1 : Interactive Scatter Plot 
Fig = px.scatter(
    df,
    x = "sepal_length",
    y = "petal_length",
    color = "species",
    title = "Sepal Length vs Petal Length_Scatter Plot"
)
Fig.show()

#CHART 2 : Box Plot 

bx = px.box(
    df,
    x = "species",
    y = "petal_length",
    color = "species",
    title = "Species vs Petal Length Box Plot"
)
bx.show()

#CHART 3 : HISTOGRAM
hist = px.histogram(
    df,
    x = "sepal_length",
    nbins = 20,
    title = "Distribution of sepal length"
)
hist.show()

#CHART 4: PIE CHART
species_count = df["species"].value_counts().reset_index()
species_count.columns = ["species", "count"]

pie_chart = px.pie(
    species_count,
    names = "species",
    values = "count",
    title = "Total Distribution of Species"
)
pie_chart.show()



#PART 6: Python Fundamentals --------------------------------------------------------------------------
#Create a Python list: 
marks = [78, 82, 91, 65, 88] 

#Task 1 
#Add a new mark. 
new_mark = marks.append(50)
print(marks)

#Task 2 
#Remove a mark. 
remove_mark = marks.remove(50)
print(marks)

#Task 3 
#Sort marks. 
sort_marks = marks.sort()
print(marks)

#Task 4 
#Find highest mark. 
highest_mark = max(marks)
print(highest_mark)

#Task 5 
#Find lowest mark. 
lowest_mark = min(marks)
print(lowest_mark)



#BONUS CHALLENGE--------------------------------------------------------------------------
'''Create a dashboard summary showing: 
• Total Records 
• Number of Species 
• Average Sepal Length 
• Average Petal Length '''

print("Iris Dataset Analysis Report")
print("Total Records :", len(df))
print("Species Count :", df["species"].nunique())
print("Average sepal Length :", df["sepal_length"].mean())
print("Average Petal Length :", df["petal_length"].mean())
