Last login: Wed Mar  9 12:34:58 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
Chels-Macbook-Air:~ chelseachu$ cd documents
Chels-Macbook-Air:documents chelseachu$ cd 'hw 2'
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
I : 8
to : 7
a : 7
that : 7
my : 6
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ nano tracker.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 tracker.py
Traceback (most recent call last):
  File "tracker.py", line 9, in <module>
    def foo(y):
  File "tracker.py", line 6, in func_counter
    return wrapper(x)
NameError: name 'x' is not defined
Chels-Macbook-Air:hw 2 chelseachu$ nano tracker.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 tracker.py
Traceback (most recent call last):
  File "tracker.py", line 9, in <module>
    def foo(y):
  File "tracker.py", line 6, in func_counter
    return wrapper(*args)
NameError: name 'args' is not defined
Chels-Macbook-Air:hw 2 chelseachu$ nano tracker.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 tracker.py
Traceback (most recent call last):
  File "tracker.py", line 12, in <module>
    print(foo(2))
  File "tracker.py", line 4, in wrapper
    counter += 1
UnboundLocalError: local variable 'counter' referenced before assignment
Chels-Macbook-Air:hw 2 chelseachu$ nano tracker.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 tracker.py
Traceback (most recent call last):
  File "tracker.py", line 12, in <module>
    foo(2)
  File "tracker.py", line 4, in wrapper
    counter += 1
UnboundLocalError: local variable 'counter' referenced before assignment
Chels-Macbook-Air:hw 2 chelseachu$ nano tracker.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 tracker.py
Traceback (most recent call last):
  File "tracker.py", line 13, in <module>
    foo(2)
  File "tracker.py", line 5, in wrapper
    counter += 1
UnboundLocalError: local variable 'counter' referenced before assignment
Chels-Macbook-Air:hw 2 chelseachu$ nano tracker.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 tracker.py
Traceback (most recent call last):
  File "tracker.py", line 16, in <module>
    print(foo.counter)
AttributeError: 'function' object has no attribute 'counter'
Chels-Macbook-Air:hw 2 chelseachu$ nano tracker.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 tracker.py
2
Chels-Macbook-Air:hw 2 chelseachu$ nano tracker.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 tracker.py
Traceback (most recent call last):
  File "tracker.py", line 13, in <module>
    foo(2)
  File "tracker.py", line 4, in wrapper
    wrapper.counter += 1
AttributeError: 'function' object has no attribute 'counter'
Chels-Macbook-Air:hw 2 chelseachu$ nano tracker.py
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py

I : 8
to : 7
a : 7
that : 7
my : 6
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ 
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py

I : 8
to : 7
a : 7
that : 7
my : 6
of : 5
and : 5
them : 4
the : 3
A : 2
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py

(There : 1
A : 2
Corbusier : 1
Explorer. : 1
I : 8
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
{'I': 8, 'to': 7, 'a': 7, 'that': 7, 'my': 6}
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
['I', 'a', 'my', 'that', 'to']
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
[('I', 8), ('a', 7), ('my', 6), ('that', 7), ('to', 7)]
Chels-Macbook-Air:hw 2 chelseachu$ ano document_analyzer.py
-bash: ano: command not found
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
[('I', 8), ('a', 7), ('my', 6), ('that', 7), ('to', 7)]
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
['I', 'a', 'my', 'that', 'to']
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
Traceback (most recent call last):
  File "document_analyzer.py", line 31, in <module>
    print(sorted(newSort,key=lambda x:x[1]))
  File "document_analyzer.py", line 31, in <lambda>
    print(sorted(newSort,key=lambda x:x[1]))
IndexError: string index out of range
Chels-Macbook-Air:hw 2 chelseachu$ key=lambda x:x[1]
-bash: x:x[1]: command not found
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python document_analyzer.py
Traceback (most recent call last):
  File "document_analyzer.py", line 31, in <module>
    print(newSort.sort())
AttributeError: 'dict' object has no attribute 'sort'
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python document_analyzer.py
Traceback (most recent call last):
  File "document_analyzer.py", line 31, in <module>
    print(newSort.items.sort())
AttributeError: 'builtin_function_or_method' object has no attribute 'sort'
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python document_analyzer.py
Traceback (most recent call last):
  File "document_analyzer.py", line 12, in <module>
    sorted_dict = sorted(wordDict, key=lambda x:x[1], reverse=True)
  File "document_analyzer.py", line 12, in <lambda>
    sorted_dict = sorted(wordDict, key=lambda x:x[1], reverse=True)
IndexError: string index out of range
Chels-Macbook-Air:hw 2 chelseachu$ sorted_dict = sorted(wordDict.items(), key=lambda x:x[1], reverse=True)
-bash: syntax error near unexpected token `('
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python document_analyzer.py
Traceback (most recent call last):
  File "document_analyzer.py", line 32, in <module>
    print(newSort.items.sort())
AttributeError: 'builtin_function_or_method' object has no attribute 'sort'
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
Traceback (most recent call last):
  File "document_analyzer.py", line 34, in <module>
    print(newSort.items.sort())
AttributeError: 'builtin_function_or_method' object has no attribute 'sort'
Chels-Macbook-Air:hw 2 chelseachu$ sorted_dict = sorted(wordDict.items(), key=lambda x:x[1], reverse=True)
-bash: syntax error near unexpected token `('
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
[('I', 8), ('a', 7), ('that', 7), ('to', 7), ('my', 6), ('and', 5), ('of', 5), ('them', 4), ('the', 3), ('A', 2), ('few', 2), ('for', 2), ('gave', 2), ('in', 2), ('it', 2), ('on', 2), ('was', 2), ('(There', 1), ('Corbusier', 1), ('Explorer.', 1), ('Le', 1), ('Lenox', 1), ('Mars', 1), ('Morty”', 1), ('NeverLikedItAnyway.com,', 1), ('Trump', 1), ('Viking', 1), ('Web', 1), ('added', 1), ('after', 1), ('ago,', 1), ('ago.', 1), ('amusing', 1), ('an', 1), ('antique', 1), ('are', 1), ('arrived', 1), ('as', 1), ('assortment', 1), ('away,', 1), ('because', 1), ('bed', 1), ('belonged', 1), ('blankets', 1), ('boyfriend’s', 1), ('buy', 1), ('by', 1), ('cake', 1), ('china', 1), ('clothes', 1), ('could', 1), ('cracked,', 1), ('deaccession', 1), ('decided', 1), ('donating,', 1), ('dormitory’s', 1), ('engagement', 1), ('ex’s', 1), ('feasible:', 1), ('fraction', 1), ('from', 1), ('galore;', 1), ('gathered', 1), ('giving', 1), ('glass', 1), ('grandmother', 1), ('grate', 1), ('have', 1), ('how', 1), ('into', 1), ('is', 1), ('jumble:', 1), ('large', 1), ('learned', 1), ('leavings,', 1), ('living', 1), ('losing', 1), ('lounger.', 1), ('me,', 1), ('means', 1), ('mine;', 1), ('months', 1), ('mother,', 1), ('mother;', 1), ('never', 1), ('new', 1), ('next', 1), ('not', 1), ('or', 1), ('paper', 1), ('piled', 1), ('planned', 1), ('ranging', 1), ('recycling,', 1), ('reserving', 1), ('rings', 1), ('rolls', 1), ('room.', 1), ('saved', 1), ('sculpture', 1), ('selling,', 1), ('set', 1), ('sets', 1), ('seven', 1), ('several', 1), ('sheet', 1), ('sites,', 1), ('size', 1), ('socks.)\n', 1), ('someday,', 1), ('spot', 1), ('stands', 1), ('stove', 1), ('subway,', 1), ('such', 1), ('things', 1), ('thought', 1), ('toilet', 1), ('too', 1), ('unwanteds', 1), ('used;', 1), ('weld', 1), ('weld;', 1), ('were', 1), ('what', 1), ('whatever', 1), ('which', 1), ('who', 1), ('will', 1), ('wish', 1), ('worth', 1), ('wrongly', 1), ('years', 1), ('your', 1), ('“Rick', 1)]
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
  File "document_analyzer.py", line 36
    
                       ^
SyntaxError: unexpected EOF while parsing
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
  File "document_analyzer.py", line 36
    
                       ^
SyntaxError: unexpected EOF while parsing
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
I : 8
a : 7
that : 7
to : 7
my : 6
Chels-Macbook-Air:hw 2 chelseachu$ sorted_dict = sorted(wordDict.items(), key=lambda x:x[1], reverse=True)
-bash: syntax error near unexpected token `('
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
I : 8
a : 7
that : 7
to : 7
my : 6
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
I : 8
a : 7
that : 7
to : 7
my : 6
{'A': 2, 'few': 2, 'months': 1, 'ago,': 1, 'I': 8, 'decided': 1, 'to': 7, 'deaccession': 1, 'an': 1, 'assortment': 1, 'of': 5, 'my': 6, 'things': 1, 'by': 1, 'whatever': 1, 'means': 1, 'feasible:': 1, 'selling,': 1, 'donating,': 1, 'recycling,': 1, 'giving': 1, 'them': 4, 'away,': 1, 'losing': 1, 'on': 2, 'the': 3, 'subway,': 1, 'or': 1, 'reserving': 1, 'a': 7, 'spot': 1, 'for': 2, 'next': 1, 'Mars': 1, 'Explorer.': 1, 'gathered': 1, 'unwanteds': 1, 'and': 5, 'piled': 1, 'in': 2, 'living': 1, 'room.': 1, 'fraction': 1, 'what': 1, 'was': 2, 'that': 7, 'jumble:': 1, 'seven': 1, 'antique': 1, 'glass': 1, 'cake': 1, 'stands': 1, 'belonged': 1, 'mother;': 1, 'dormitory’s': 1, 'worth': 1, 'new': 1, 'sheet': 1, 'sets': 1, 'blankets': 1, 'bed': 1, 'size': 1, 'is': 1, 'not': 1, 'mine;': 1, 'set': 1, 'Lenox': 1, 'china': 1, 'grandmother': 1, 'gave': 2, 'mother,': 1, 'who': 1, 'it': 2, 'me,': 1, 'never': 1, 'used;': 1, 'clothes': 1, 'galore;': 1, 'Viking': 1, 'stove': 1, 'grate': 1, 'arrived': 1, 'cracked,': 1, 'which': 1, 'saved': 1, 'because': 1, 'planned': 1, 'weld': 1, 'into': 1, 'sculpture': 1, 'someday,': 1, 'after': 1, 'learned': 1, 'how': 1, 'weld;': 1, 'several': 1, 'rolls': 1, 'Trump': 1, 'toilet': 1, 'paper': 1, 'wrongly': 1, 'thought': 1, 'were': 1, 'amusing': 1, 'years': 1, 'ago.': 1, 'wish': 1, 'could': 1, 'have': 1, 'added': 1, 'boyfriend’s': 1, 'too': 1, 'large': 1, 'Le': 1, 'Corbusier': 1, 'lounger.': 1, '(There': 1, 'are': 1, 'Web': 1, 'sites,': 1, 'such': 1, 'as': 1, 'NeverLikedItAnyway.com,': 1, 'will': 1, 'buy': 1, 'your': 1, 'ex’s': 1, 'leavings,': 1, 'ranging': 1, 'from': 1, 'engagement': 1, 'rings': 1, '“Rick': 1, 'Morty”': 1, 'socks.)\n': 1}
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
('I', 8)
('a', 7)
('that', 7)
('to', 7)
('my', 6)
{'A': 2, 'few': 2, 'months': 1, 'ago,': 1, 'I': 8, 'decided': 1, 'to': 7, 'deaccession': 1, 'an': 1, 'assortment': 1, 'of': 5, 'my': 6, 'things': 1, 'by': 1, 'whatever': 1, 'means': 1, 'feasible:': 1, 'selling,': 1, 'donating,': 1, 'recycling,': 1, 'giving': 1, 'them': 4, 'away,': 1, 'losing': 1, 'on': 2, 'the': 3, 'subway,': 1, 'or': 1, 'reserving': 1, 'a': 7, 'spot': 1, 'for': 2, 'next': 1, 'Mars': 1, 'Explorer.': 1, 'gathered': 1, 'unwanteds': 1, 'and': 5, 'piled': 1, 'in': 2, 'living': 1, 'room.': 1, 'fraction': 1, 'what': 1, 'was': 2, 'that': 7, 'jumble:': 1, 'seven': 1, 'antique': 1, 'glass': 1, 'cake': 1, 'stands': 1, 'belonged': 1, 'mother;': 1, 'dormitory’s': 1, 'worth': 1, 'new': 1, 'sheet': 1, 'sets': 1, 'blankets': 1, 'bed': 1, 'size': 1, 'is': 1, 'not': 1, 'mine;': 1, 'set': 1, 'Lenox': 1, 'china': 1, 'grandmother': 1, 'gave': 2, 'mother,': 1, 'who': 1, 'it': 2, 'me,': 1, 'never': 1, 'used;': 1, 'clothes': 1, 'galore;': 1, 'Viking': 1, 'stove': 1, 'grate': 1, 'arrived': 1, 'cracked,': 1, 'which': 1, 'saved': 1, 'because': 1, 'planned': 1, 'weld': 1, 'into': 1, 'sculpture': 1, 'someday,': 1, 'after': 1, 'learned': 1, 'how': 1, 'weld;': 1, 'several': 1, 'rolls': 1, 'Trump': 1, 'toilet': 1, 'paper': 1, 'wrongly': 1, 'thought': 1, 'were': 1, 'amusing': 1, 'years': 1, 'ago.': 1, 'wish': 1, 'could': 1, 'have': 1, 'added': 1, 'boyfriend’s': 1, 'too': 1, 'large': 1, 'Le': 1, 'Corbusier': 1, 'lounger.': 1, '(There': 1, 'are': 1, 'Web': 1, 'sites,': 1, 'such': 1, 'as': 1, 'NeverLikedItAnyway.com,': 1, 'will': 1, 'buy': 1, 'your': 1, 'ex’s': 1, 'leavings,': 1, 'ranging': 1, 'from': 1, 'engagement': 1, 'rings': 1, '“Rick': 1, 'Morty”': 1, 'socks.)\n': 1}
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
{'I': 8, 'a': 7, 'that': 7, 'to': 7, 'my': 6}
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
  File "document_analyzer.py", line 38
    print i, " ", newSort[i]
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i, " ", newSort[i])?
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py
Chels-Macbook-Air:hw 2 chelseachu$ python3 document_analyzer.py
{'I': 8, 'a': 7, 'that': 7, 'to': 7, 'my': 6}
I : 8
a : 7
that : 7
to : 7
my : 6
Chels-Macbook-Air:hw 2 chelseachu$ nano document_analyzer.py

  GNU nano 2.0.6              File: document_analyzer.py                                   

sorted_items = sorted_dict.items()
top_five = list(sorted_items)[:5]

sorted_list = []
sorted_list.append(sorted_dict.copy())

for i in range(5):
        print(sorted_list[i])

print(sorted_dict[0])
"""
# print()
newSort = {}
for i in sorted_dict[0:5]:
        newSort[i[0]] = i[1]

#print(newSort.items.sort())
#print(sorted_dict)
print(newSort)
for i in newSort:
        print (i, ":", newSort[i])
