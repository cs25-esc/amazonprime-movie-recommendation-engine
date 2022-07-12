# amazonprime-movie-recommendation-engine by content based filering using streamlit application.


first of all imported the dataset from the kaggle link - https://www.kaggle.com/datasets/shivamb/amazon-prime-movies-and-tv-shows

eda-
the dataset contains some unncessary features like show_id,country and duration which i felt not requried to the user in this level.
I have some important features like director of the movie, cast and description or overview of the movie.

I have decided to create tags for each movie and find the similarity between every movie with one another based on their respective tags.

-data cleaning:

  i have kept the director column as it is.
  there are many cast for each movie so i have extracted only the first three.
  
  
finally i have merged the director,cast and description as kept in the same file as tags column and removed the same.

--i have noticed there are many words in the tags column needed to be stemmed, for this i have imported PorterStemmer function from nltk.

this PorterStemmer helps to stem the words like (caring , cared , care) --> 'care'

now, there are around 10 thousand movies the count tags will be some lakhs, so i have decided to import CountVectorizer feature from sklearn.feature_extraction.text
this takes an integer input and allows us to extract the top words in the column based on its frequency(number of occurances).

i have extracted top 10 thousand words in the all the tags for 9668 movies in the dataset.
i have fitted and transformed the tags column, now i got an 2 - D array of size 9668 X 10000 where each integer in the array specifies
the number of words in the tags column mapped with each word in top 10 thousand words.

example:

if the movies are ['Avatar' , 'Batman' , 'Rangasthalam'] and the tags of this movies in the top ten words for this 3 movies tags are 
['village' , 'drama' , 'adventure' , 'billionaire' , 'pandora' , 'spaceship' , 'brother' , 'revenge'] if we map movies titls with this list we get.

                  village     drama    adventure   billionaire    pandora    spaceship    brother     revenge
avatar                0         1         1           0              2          5            0          2
batman                0          0         1           3              0         1            0           2
rangasthalam           5         2         0           0              0         0             4          3

avatar array - [0,1,1,0,2,5,0,2]
batman array - [0,0,1,3,0,1,0,2]
rangasthalam array - [5,2,0,0,0,0,4,3]

like this we have generated arrays of length ten thousand for all 9668 movies


evreything upto feature making is completed, now its turn for the most interesting part - we need to find the similarity between two movies based on the tags.
if we use euclidian distance it will be a most computationally hectic process so i have used cosine similarity.

in simple terms we can explain like the less the angle between two vectors the more the similar the two vectors(here movies) are.

after applying the cosine similarity function we get a 9668 X 9668 matrix just like correlation matrix but here the movie similarity with each other.

process:
first we select a movie
we extract the similarity vector of that movie with all the other movies in the list.
we can sort the vector in descending order and we can pick the first 5 movies which gives the  similar movies to the movie we have provided.


building appliaction using streamlit:

i have dumped all the necessary files(pickle file format) from notebook to my project in pycharm.
followed the streamlit documentation to frame the website which is very easy to follow and implement.

![image](https://user-images.githubusercontent.com/68850280/178451695-4e4881bc-0aea-46f9-a18f-ac42178bb18a.png)


and later i tried to deploy the application in Heroku platform but my file limit exceeded 1GB.
only the similarity vector pickle file size is almost 800 mb.









