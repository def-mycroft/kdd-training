

# Notes on Speech Parser

This module takes a text file and returns the frequency of occurence of each
word. I don't know how to do this, and will have to figure this out.

Objects:

* A text file that is an input.
* A text file which includes words to be excluded.

* In order to avoid creating a solution that has 300 fucking lines... try to
  think compactly.

* is this something that can be trained a little bit? Should have a fairly
  standard set of syntax for punctuation.


## Load file into program

* have to import and write the files in a manner consistent with Pavel's 
  example.


## Create data structure from the input file

* how to access the words in the file. Are there going to be lines? Or does
  that matter?
* some method of splitting different words into a list or something - how to
  turn the text file into a data structure.
* Should be able to split by spaces.. if there is a space, it is a word.
  Something about a seperator when reading something into a file.


## Clean the data structure

* could remove the excluded words after creatin the data structure.
* punctuation could be just part of the excluded word list... but that
  wouldn't work because if I'm using spaces as a seperator, then the 
  words would include attached punctuation.
* may be able to take every item in the list and strip the punctuation,
  against a list of punctuation.

## Parse the speech and create statistics

* There is a list of words, some of the words recur more than once in the
  list. Want to count the number of times that each of the words appears
  in the list.

  I have a list which represents all words in the article, and this list has
  been cleaned.

  I want to pick out the top ten words by order of occurence.

  What about going through each word, checking the count of this particular
  word, removing the word from the article list, adding the word and it's
  count to another list (as a matrix).

  Create a two dimensional array (list of lists) of the 

  For item in article_list:
      append_list = []
      append__list.append(item)
      append_list.append(article_list.count(item))
      output_list.append(append_list)

Remove duplicates from the output list. 

Sort the append list by the second column.

The first ten values are the top ten values.


  1 ) Create a list of unique words from the article list.

  for item in input_list:
      if item not in word_list:
         word_list.append(item)

  2 ) For each item in the unique list, find the frequency in the article 
      list, and add this to another list.
  
      Outcome is the top ten words, by occurence. 

## Return the top ten list of words

* this should just be putting out a file that is a simple summary, 
  once there is a list this is just a matter of formatting and printing.


