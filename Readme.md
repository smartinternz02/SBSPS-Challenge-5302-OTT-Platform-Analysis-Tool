# OTT Platform Analysis Tool
* This tool is to show how well the OTT platforms have 
performed so far
## Note: Do not overuse the published Heroku site because CUH(Capicity unit Hour) decreases and I already have less, Thank you
## Published ML model on Heroku
* Find out which OTT platform will you watch with simple 
* Form provided.
[Link to Website](https://guess-api-1.herokuapp.com/)
* Enjoy the latest release
## Can Check or Rerun the project
* Step 1: Go to [IBM Pak Data](https://www.ibm.com/in-en/products/cloud-pak-for-data) and Login with IBM Id
* Step2: Start to create a new Project
* Step3: Choose import from file
* Step4: Upload the zip file in **Project_files/IBM Pak Data**
* Step5: Give the project a name and click create
* **Follow if you want to associate ML Service**
* Step6: Go to [IBM Cloud](https://cloud.ibm.com/login) and login with IBM Id
* Step7: Create a new ML service
* Step8: Go to your project in IBM Pak Data and associate a service with it
## Link to Video
[Link to video](https://drive.google.com/file/d/1sHebBsqFtZ4VKB0hS_6WkdFsPNwsnrMX/view?usp=sharing "Video on project") \
\
![Workflow](Workflow_OTT.jpg "Workflow of OTT plaform")
## Netflix data
* Basic analysis on netflix data and reviews are analyzed with help of customer statisfaction opinions resource in IBM Watson.
* Current Analysis is on 25 % data.
### Word Cloud
![WordCloud](Output_Screenshots/Netflix/WordCloud.jpg "Shows what word is used")
* Above word cloud is from the Anaylzed data, which provides the count of words which are conceptually 
sensible
* When WordCloud was given a deeper analysis we attain the following graph
### In depth-Word Cloud
![DeeperWords](Output_Screenshots/Netflix/Deeper_Word.jpg "Word Cloud with deeper analysis")
* Lead roles was used too much, which can be conclusion of how in general public talks about the protagonist/antagonist much more than side roles
* Meanwhile "friend","family" were also used in greater %.
### PieChart of Reviews
![PieChart](Output_Screenshots/Netflix/Piechart.jpg "Shows what is the tag for Review")
* Pie Chart shows the distribution of audience in general on the platform(Netflix)
* Showing maximum as Negative(Sad) Content is not likeable
* But there isn't much differnce between negative and positive maintaining a netural status.
### Tree Based Analysis
![Tree](Output_Screenshots/Netflix/TreeBased.jpg "Shows how the type of movie/TV Show is")
* Different Watch ratings shown with whether the "content" is a Movie or T.V. Show.
* It is amazing that Movies are distributed in all categories meanwhile most T.V. Shows are at least 13+.
### PieChart on Netflix
![Pies](Output_Screenshots/Netflix/Pies.jpg "Showing movies/T.V.shows data is divided in top 10 countries")
* More than 50% of movies/ T.V. shows in Netflix are from U.S.
* Showing how dominant the Hollywood industry in OTT platforms.
* And next comes Indian Content which has 22% presence in the dataset(25 % sampled).
### Distribution of Words in Reviews
![Words_in_Reviews](Output_Screenshots/Netflix/GoodWords.jpg "Showing what words were dominant in Positive reviews")
* The above Graph shows Positive reviews has "love" word used dominantly.
* Some of the words include "love","excellent","rich","large".
* Intresting "love" was used 868 times out of 3380 uses, which is 25.68 %.
### 75 % Word Cloud
![BetterWordCloud](Output_Screenshots/Netflix/Netflix75perWordCloud.jpg "Shows how much the data is diversed")
* When 75 % data was considered Word Cloud changed, Which introduced some new words into light
* In the above cloud, which shows life, family, women and staff are top 4 topics
* Considering the limit of data collected from 1900 to 2020, life was most sought out topic
* Family and Women came up after 2004 and so.
### Scatter plot
![Scatter](Output_Screenshots/Netflix/Scatter-Netflix.jpg "Scatter plot of Year/ Time")
* This helps to determine which years were dominant in production of content.
* Also gradient of points define how much the content is famous.
* We can see from graph that T.V. shows were around 118 mins long or 4 seasons mostly.
* Also domination of 2000 to 2020 is fantastic in content production
* While most points lies on 80 to  140 mins, showing the length of movie/T.V. shows not less than 1:20 hrs and greater than 2:20hrs on average
* Intrestingly a T.V. show was made in early 1940s which seems to be earliest T.V. Show.
### BarChart with emotional Tags
![Barchart_emotes](Output_Screenshots/Netflix/Bar_emotes.jpg "Bar chart with Emotions are good")
* The above bar chart shows how emotions are tagged with plot of the movie Showing what is Prevaliving in the comments.
* The Negative Features are dominating,  whereas Positive Features just next Negative One's
* Buying, Date Unknown are some of the common tags in the textual analysis.
## Amazon Prime Data
* The sample is 66% taken randomly out the dataset
* Below are the Graphs and what analysis of data shows is listed below
### BarChart for Year and Maturity
![Barchart](Output_Screenshots/Amazon/Barchart.jpg "Year with Maturity rating graph")
* The above barchart shows the distribution of T.V. shows/ Movies based on year Split with Maturity rating
* Most movies made every year are 13+.
* Concerntration of most movies are from (2016-2020)
* Intrestingly most 18+ movies are made in 2016.
### TreeMap on Maturity vs Language
![TreepMaps](Output_Screenshots/Amazon/TreeMapAmazon.jpg "Amazon data language tree map")
* From the above Tree Map we can see "English", "Hindi" and "Tamil" have made Shows/Movies in all categories of Maturity.
* Meanwhile "Punjabi" has Only two categories that are "13+" and "All"
* As from the above Bar Chart 13+ is dominant which is evidently shown in the treemap.
### Language vs Maturity explained with relations
![Relations](Output_Screenshots/Amazon/Relations.jpg "Shows a relationship graph between two")
* This is more insightful than TreeMap, and thus provides more deeper view of  films/TV.shows.
* Shows how language affects the maturity rating of the content
* Notice 13+ as the biggest bubble with NR as second most occuring maturity type
* Also Hindi,English are two dominant languages in the Amazon dataset.
* Most 18+ are made in English,Hindi and Tamil. 
### 3D Scatter Chart
![3DChart](Output_Screenshots/Amazon/Amazon3d.jpg "3d scatter plot")
* The above chart shows how 3 factors relate to each other graphically, and cocerntration of points in the place
* We can see that 7.5 was the modal rating with English,Telegu,Bengali,Tamil languages
* Also we see that each movie or T.V. show was 1:30 hrs to 2:00 hrs long in the Concerntrated area
* A Tamil movie had a rating of 1.4, which can conclude that there is an outlier, also highest rating is 8.9.
* There is maturity diversity, but mostly 13+,16+ and 18+ categories are dominant.
### BarChart Language with Maturity rating
![Barchrt](Output_Screenshots/Amazon/Multi_graph.jpg "Multi graph")
* English is dominating in dataset considering the bargraph shown above with having 13+ maturity as maximum, whilist 18+ as the second best rating in movies plublished on Amazon.
* Next Comes Hindi Movies on Amazon Prime where again The domination of 13+ movies is 60% which is lot considering other categories
* All of the punjabi movies are rated 13+ which is wierd showing they do not produce adult or children movies but a moderately happy movies
* Also 7+ is the scarce category to found having < 5 % share in each of the Languages.
## Misc Graphs
* This section covers the overall analytical dataset found in kaggle which tells in general how population percieves OTT platform.
*  With Different graphs we could reach better conclusions and get a better understanding of social stand point in for OTT platforms.
### PieChart for Age group
![PieChart](Output_Screenshots/Misc_visuals/Pie-for-ott.jpg "Pie Chart for age group")
* From the above graph we can see that teenagers watches OTT platform at most from the sample collected. Numerically 64.74% population from the sample.
* And the least is Above 50 years of age, Well we can speculate that old people do not appriciate the newer steps
* Although working population, is above 20  and less than 50 which subsumes around 20%  of the whole sample collected.
* Conclusively, Teenagers are the most watchers reasons can be pyschological pressure, anexity, entertainment and A better choice of tailored shows.
