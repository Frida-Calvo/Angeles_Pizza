import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud




tweetFile = open("tweets.json", "r")#read the file stream
TweetData = json.load(tweetFile)#loading data from file stream into the var TweetData
tweetFile.close()

#Textblob sample:
#empty lists 
polarity=[]
subjectivity=[]

#gets the pol and subj of each tweet and stores it in lists
##for text in TweetData:
##    tb = TextBlob(text["text"])
##    polarity.append(tb.polarity)
##    subjectivity.append(tb.subjectivity)
##print("polarity", polarity)
##print("subjectivity", subjectivity)

largeString=[]
for yeet in TweetData:
    a = TextBlob(yeet["text"])
    largeString.append(a)


filteredWords[word] = count





#this gets the average of polarity and subjectivity
##print(sum(polarity)/len(polarity))
##print(sum(subjectivity)/len(subjectivity))


##plt.hist(subjectivity)
##plt.xlabel("Subjectivity")
##plt.ylabel("Frequency")
##plt.show()
##
##
##plt.hist(polarity)
##plt.xlabel("Polarity")
##plt.ylabel("Frequency")
##plt.show()

##x = polarity
##y = subjectivity
##plt.xlabel("Polarity")
##plt.ylabel("SubjectivityS")
##plt.scatter(x, y,alpha=0.5)
##plt.show()
