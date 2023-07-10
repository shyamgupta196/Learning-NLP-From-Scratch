from nltk.tokenize import TweetTokenizer
tweet=u"Snow White and the Seven Degrees\
#MakeAMovieCold@midnight:­)"
tokenizer = TweetTokenizer()
print(tokenizer.tokenize(tweet.lower()))