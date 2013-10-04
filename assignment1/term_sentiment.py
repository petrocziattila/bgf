import sys
import json

def sentiment(tweet,scores):
  score=0
  count=0
  words=tweet.split()
  for i in words:
    if i in scores.keys():
      score+=scores[i]
      count+=1
  return float(score)/max(count,1)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = float(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    wordbook={}
    wordbook_count={}
    for line in tweet_file:
      tweet_object=json.loads(line)
      if "text" in tweet_object:
        tweet=tweet_object["text"]
        tweet_sentiment=sentiment(tweet,scores)
        words=tweet.split()
        for i in words:
          if i in scores.keys():
            i=i
          elif i in wordbook.keys():
            wordbook[i]=(wordbook_count[i]*float(wordbook[i])+tweet_sentiment)/(wordbook_count[i]+1)
            wordbook_count[i]+=1
          else:
            wordbook[i]=tweet_sentiment
            wordbook_count[i]=1

    for i in wordbook:
      print i, wordbook[i]

if __name__ == '__main__':
    main()


