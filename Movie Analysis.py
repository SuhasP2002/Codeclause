import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv(r"IMDB-Movie-Data.csv")
data.head(10)
data.tail(10)
data.shape
print("Number of Rows in the Dataset",data.shape[0])
print("Number of Columns in the Dataset",data.shape[1])
data.info()
print("Any Missing values",data.isnull().values.any())
data.isnull().sum()
data.dropna(axis=0,inplace=True)
data
print("Any duplicate values",data.duplicated().any())
data.describe(include="all")
data.columns
#Title of the movie which has runtime more than 180 minutes
data[data["Runtime (Minutes)"]>=180][["Title","Runtime (Minutes)"]]
# In which year there was the highest average voting
data.groupby("Year")["Votes"].mean().sort_values(ascending=False)
sns.barplot(x="Year",y="Votes",data=data)
plt.title("Votes by year")
plt.show()
#in which year there was highest average revenue
data.groupby("Year")["Revenue (Millions)"].mean().sort_values(ascending=False)
sns.barplot(x="Year",y="Revenue (Millions)",data=data)
plt.title("Revenue by Year")
plt.show()
#finding the average rating for each director
data.groupby("Director")["Rating"].mean().sort_values(ascending=False)
sns.barplot(x="Director",y="Rating",data=data)
plt.title("Rating for directors")
plt.show()

#displaying top 10 lengthy movies title and runtime
top10_len=data.nlargest(10,"Runtime (Minutes)")[["Title","Runtime (Minutes)"]].set_index("Title")
top10_len
sns.barplot(x="Runtime (Minutes)",y=top10_len.index,data=top10_len)
#Display number of movies per year
data["Year"].value_counts()
sns.countplot(x="Year",data=data)
plt.title("Number of movies per year")
plt.show()
#Find most popular Movie Title
data[data["Revenue (Millions)"].max()==data["Revenue (Millions)"]]["Title"]
#Finding top 10 rating movie Titles and Directors
top10_rat=data.nlargest(10,"Rating")[["Title","Rating","Director"]].set_index("Title")
top10_rat
sns.barplot(x="Rating",y=top10_rat.index,data=top10_rat)
plt.title("Highest rating")
plt.show()
#Display top 10 highest revenue movie titles
top10_rev=data.nlargest(10,"Revenue (Millions)")[["Title","Revenue (Millions)"]].set_index("Title")
top10_rev
sns.barplot(x="Revenue (Millions)",y=top10_rev.index,data=top10_rev)
plt.title("Highest revenue movies")
plt.show()

#Finding avearae rating of movie year wise
data.groupby("Year")["Rating"].mean().sort_values(ascending=False)
#Does rating effect Revenue
sns.scatterplot(x="Revenue (Millions)",y="Rating",data=data)
plt.title("rating vs revenue")
plt.show()
#classifying movies based as rating
def rating(rating):
    if rating>=7.0:
        return "Excellent"
    elif rating>=6.0:
        return "Good"
    else:
        return "Average"
data["data_categories"]=data["Rating"].apply(rating)
data
#count number of action movies
len(data[data["Genre"].str.contains("Action",case=False)])
#Find unique values from Genre
data["Genre"]
list1=[]
for i in data["Genre"]:
    list1.append(i.split(","))
list1
oned=[]
for i in list1:
    for j in i:
        oned.append(j)
oned
uni=[]
for i in oned:
    if i not in uni:
        uni.append(i)
uni
len(uni)
#How many films of each genre
from collections import Counter
Counter(oned)

