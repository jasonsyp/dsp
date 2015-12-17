# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequence structures that contain zero or more elements, and the elements can be of different types.  However, lists are mutable, meaning you can insert and delete or overwrite existing elements.  Whereby, tuples are immutable, meaning that can't be modified after creation.  Tuples also take up less memory than lists.  A dictionary key can be any immutable type, therefore, tuples can be used as keys (if all the elements of the tuple are themselves immutable).  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Like lists, sets are mutable.  Unlike lists, sets are unordered collections of elements with no duplicate values.  Sets are like dictionaries with the values thrown away, leaving just the keys.  Performance wise, if we assume "finding an element" refers to checking for membership, then the operation is much more efficient using sets.   Sets are implemented as hash tables, thereby the code to test for membership can be implemented much more efficiently using the 'in' operator versus having to iterate across all n indexes of a list, worst case.
Reference: https://wiki.python.org/moin/PythonSpeed, "Membership testing with sets and dictionaries is much faster, O(1), than searching sequences, O(n).  When testing 'a in b', b should be a set or dictionary instead of a list or tuple."  See also, Time Complexity at https://wiki.python.org/moin/TimeComplexity

    '''  
    my_list = ['Mets', 'Nationals', 'Braves', 'Phillies', 'Marlins']  
    for team in my_list:  
        print(team)  
    '''
    my_set = {'Mets', 'Nationals', 'Braves', 'Phillies', 'Marlins'}  
    print ("There are", len(my_set), "teams in the NL East")  
    '''
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lambda function is an anonymous function (i.e. doesn't have a name) expressed as a single statement.  It is useful in cases in which you would otherwise have to define many tiny functions and remember what you called them all.  

    '''  
    team_wins = [('Nationals', 83), ('Phillies', 63), ('Marlins', 71), ('Mets', 90), ('Braves', 67)]  
    sorted(team_wins, key=lambda team: team[1], reverse=True) # sort by number of wins  
    '''

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





