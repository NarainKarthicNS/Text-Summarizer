import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize , sent_tokenize



def summarize_text(text):
    '''Tokenizing the text into words to remove 
    stopwords(meaning-less like a,an,is,for,the ,etx)
    and breakdown sentences into tokens with meaning'''

    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    
    '''Creating Frequency table to analyse frequency
    of reccuring words to find the mean of the words'''

    freq_table = dict()
    for word in words:
        word = word.lower()
        if word in stopWords: # --> If word is a stop word ignore
            continue
        if word in freq_table: # --> If the word is in table then add +1 to val
            freq_table[word] += 1 
        else:
            freq_table[word] = 1 # --> If word is not in table create new key & assign 1 val

    '''Creating Frequency table to analyse the score
    of important sentence using freq_table as source'''

    sentences = sent_tokenize(text)
    sentence_value = dict()

    for sentence in sentences:
        for word,freq in freq_table.items():
            if word in sentence.lower(): # --> if important words are in sentence
                if sentence in sentence_value: # --> and if the sentance already has a val
                    sentence_value[sentence] += freq # --> that is if it has more important words it gets more val
                else:
                    sentence_value[sentence] = freq # --> if it isnt already there then it gets assigned the freq as val
    

    sumValues = 0
    for sentence in sentence_value:
        sumValues += sentence_value[sentence]
    
    #Average value of a sentence from the orginal text
    average = int(sumValues/len(sentence_value))
    
    #storing sentence into our summary
    summary = ""
    for sentence in sentences:
        if (sentence in sentence_value) and (sentence_value[sentence] > (1.2 * average)):
            summary += " " + sentence

    return summary

# TEST

text = input("text: ")
summary = summarize_text(text)
print("------------------------------------------------------------------------- \n")
print(summary) 





