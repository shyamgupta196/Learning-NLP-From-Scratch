These fancy terms needs to be explained properly, or else you will end up in an endless loop of tutorials.

Tokenization - Say you have a pizza, you cannot consume whole pizza at once, can you ? So, we break it into pieces. similarly, we break sentences into small chunkiesss, called <i>'tokens'</i>.


1. tfidf - Helps us figure out, most important words in a text. its like VIP list of words.

2. stemming & lemmatization - This is where you take 'tokens' to their base form. example- 'boys are running on field' -> 'boy run on field'. Stemming does not preserve the original structure of the 'token', example- 'running' -> 'runn', hence we prefer <b>'lemma' with 'tokens'</b>. Breaking lego pieces into constituents.

3. word embeddings - these are used for representing words as numbers.

Bag of words, TF-IDF, N_grams are all used for converting words into vectors.

Unigrams, Bigrams, and Ngrams -  these are used for grouping words together, for example- 
Unigrams - will have one word in a group. 'cat' or 'dog'.
bigrams - will have 2 related words in a group. 'smelly cat' 
n-grams - can have n related words in a group. 'blah blah blah blah blah '

word2vec - will convert a word to numerical format, to represent in vector space.

average word2vec - Taking Word2Vec numbers for a bunch of words and averaging them out. It's like if you had a bunch of friends with different nicknames, and you wanted to come up with an overall nickname for your whole group of friends. You might call them "The Crew" or something like that. [img](../temps/tapu-sena.jpg)

GLOVE - """ open contributions (should be explainable to a child [short and crisp]) """

Named entities - They represent a string for a real world concept like a "person","organisation","Place", etc.

NOW, It is recommended to get your hands dirty, 

## To get my hands dirty I will refer a book NLP with Pytorch by O'reilly publishers

