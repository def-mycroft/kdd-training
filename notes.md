
Rules for this homework:

* Can only use one line of code in the body of each function.
* Cannnot use functions like min() or max() or any library functions.

#Topics for this Homework:

## map

The map() function takes a function and applies it to every member of an input
list:

    map(function, list_of_inputs)

## filter

The filter() function returns a list of values from an input list for which 
a function returns True.

    map(function, list_of_inputs)

The filter and map function are similar concepts. The map function applies a 
function to each member of a list and returns the output as a list, while the
filter function applies a boolean function to each member of a list and returns
the values (from the input list) for which the boolean function returns True.

## reduce

Reduce passes the current value of a list with the next value of the same list.

In this manner:

    output = reduce(function(x,y), list)

Therefore, for example, a formula for the product of a list of numbers would 
look like this:

    factorial = reduce(lambda x,y: x*y, list)

Note that unlike map and filter, the reduce function returns a single number.
The map and filter functions return a list of numbers.

## slicing tools

This is syntax that allows for manipulating lists in various ways.

There is a simple syntax that can be used:

    * start_to_end = list[start:end]
    Refers to the list from the argument start to the argument end, exclusive.

    * list[start::]
    * list[::end]
    * list[start:end:step]

## list/dict comprehension

List/dict comprehension is a way to construct lists or dicts, similar to the
way that mathematicians construct sets using set notation.

http://www.secnetix.de/olli/Python/list_comprehensions.hawk

Here are a couple of examples:

    \# Creates a list of numbers up to 999
    * numbers_to_1thousand = [x for x in range(1000)]

The above creates a list of numbers from (about) 1 to (about) 1000 (I'm not
sure if the list is comprehensive or not.)

    * [x for x in range(1000) if x % 2]

Above is a list of odd numbers to 1000. 


## lambdas

A lambda is a short function that is not named. 

Lambdas are used in the form:

    lambda para1, para2: [function of para1 and para2]

For example: 

    labmda x,y: x + y


This is useful for creating small, throwaway functions which are made up on
the spot.

## recursion

