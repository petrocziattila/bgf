import sys
import json

def sentiment(tweet,scores):
  score=0
  words=tweet.split()
  for i in words:
    if i in scores.keys():
      score+=scores[i]
  return score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    
    for line in tweet_file:
      tweet_object=json.loads(line)
      if "text" in tweet_object:
        tweet=tweet_object["text"]
        print sentiment(tweet,scores)
      else:
        print 0
if __name__ == '__main__':
    main()


