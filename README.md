# Text-Summarizer(NLP)
A Text Summarizing program that uses an AI to summarize a given text with the power of **Natural Language Processing**.Built completely using Python and its Natural Language Tool Kil(NLTK) module.This program can summarize an entire paragraph by analysis of the sentences and words in the given text and by running it through an **Data Analysis Algorithm**.

## How It Works?
It uses **Natural Language Processing** and **NLTK** library to basically run the given text through an **algorith** to summarize the text based on importance.In a nutshell-First we remove tokenize the paragraph and remove stopwords and construct a frequency table for data analytics.we get the frequency of every important words and decide on what the sentence is about and how important each sentence is by another frequency table.Then we check how many such important words each sentence posses and grade is sum value accordingly and then gets its average.By which we take the highest ranking sentences of importance and return it to the user.For tokenizing every sentence we use nltk.tokenize functions to tokenize the sentences and the huge nltk's corpus database to find stopwords in the input.

## Modules Used
- nltk(Natural Language Tool-Kit)
- nltk.corpus --> For StopWords
- nltk.tokenize --> For Tokenizing Sentences and Words
