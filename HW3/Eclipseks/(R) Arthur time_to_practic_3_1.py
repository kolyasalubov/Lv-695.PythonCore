zen_Of_Python = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print("\n---Exercise 1---")
print("In 'Zen of Python' the word \"better\" repeat", zen_Of_Python.count("better"), 'times')
print("In 'Zen of Python' the word \"never\" repeat", zen_Of_Python.count("never"), 'times')
print("In 'Zen of Python' the word \"is\" repeat", zen_Of_Python.count("is"), 'times')

print("\n---Exercise 2---")
print(zen_Of_Python.upper()) 


print("\n---Exercise 3---")
print(zen_Of_Python.replace("i","&"))