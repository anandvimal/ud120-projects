#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated)

        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)

    """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        #words = text_string

        ### split the text string into individual words, stem each word,
        text_string = text_string.split(" ")
        #text_string = text_string.strip()

        print text_string

        for i in range(len(text_string)):
            text_string[i]=text_string[i].strip()

        print text_string

        text_string = filter(None, text_string)

        #stem here
        stemmer = SnowballStemmer("english")
        for i in text_string:
            w = stemmer.stem(i)
            words = words + w + " "
        #make bag of words

        print text_string
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)

    return words


def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text



if __name__ == '__main__':
    main()
