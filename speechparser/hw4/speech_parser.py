"""Speech parser. Written in Python 2.7"""
from __future__ import print_function

def create_list(filename):
    """Takes an text file and turns it into a list of words"""
    output_list = []

    try:
        with open(filename, 'r') as text_file:
            for line in text_file:
                for word in line.split(" "):
                    word = word.replace("\n", "")
                    output_list.append(word)

    except IOError as error:
        print(error)

    finally:
        text_file.close()

    return output_list


def clean_list(input_list, ignore_file):
    """ Sets words to lowercase, removes excluded words and punctuation"""
    # Create a list of punctuation and of exluded words.
    punctuation_list = create_list('punctuation.txt')
    exclude_list = create_list(ignore_file)

    i = 0
    while i < len(input_list):

        input_list[i] = input_list[i].lower() # Set word to lowercase.
        for char in input_list[i]:
            if char in punctuation_list: # Remove punctuation.
                input_list[i] = input_list[i].replace(char, "")

        i += 1

    # Remove excluded words and empty list elements.
    output_list = []
    for item in input_list:
        if item not in exclude_list and len(item) != 0:
            output_list.append(item)

    return output_list


def list_occurences(input_list):
    """Returns a matrix representing the frequency of occurence"""
    output_list = []

    for item in input_list:
        append_list = []
        append_list.append(item)
        append_list.append(input_list.count(item))
        output_list.append(append_list)

    def get_key(item):
        return item[1]

    unique_output_list = []
    for item in output_list:
        if item not in unique_output_list:
            unique_output_list.append(item)

    return sorted(unique_output_list, reverse=True, key=get_key)


def list_top_words(input_list, qty_results):
    """ Displays the top ten words"""
    output_list = []

    i = 0
    while i < qty_results:
        message = "%s: %s - %s" % (i+1, input_list[i][0], input_list[i][1])
        output_list.append(message)
        i += 1

    return output_list


def parse_text(
        filename,
        write_to_file=False,
        output_filename='output.txt',
        ignore_file='ignore.txt',
        top=10):
    """Displays output. Can write to file or not"""

    try:

        with open(output_filename, 'w+') as output_file:

            for item in list_top_words(

                    list_occurences(
                        clean_list(
                            create_list(filename),
                            ignore_file)), top):

                if not write_to_file:
                    print(item)
                if write_to_file:
                    output_file.write("%s\n" % item)

    except IOError as error:
        print(error)

    finally:
        output_file.close()
