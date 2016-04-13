===============================================
Improving your programming style in Python
===============================================

:date: 2014-09-29
:tags: python, software engineering, selected
:summary: Some references on software development techniques and patterns to help write better code.

Here are some references on software development techniques and patterns
to help write better code. They are intended for the casual programmer,
and certainly not an advanced developer.

They are listed in order of difficulty.

Software carpentry
------------------

http://swc.scipy.org. 

These are the original notes from Greg Wilson's course on software
engineering at the university of Toronto. This course is specifically
intended for scientists, but not computer science students. It is very
basic and does not cover design issues.

A tutorial introduction to Python
---------------------------------

http://www.informit.com/articles/article.asp?p=23100&seqNum=3&rl=1.

This tutorial is easier to follow than `Guido's tutorial
<http://www.python.org/doc/>`_, thought it does not go as much in depth.

Python Essential Reference
--------------------------

http://www.informit.com/articles/article.asp?p=453682&rl=1

http://www.informit.com/articles/article.asp?p=459269&rl=1

These are two chapters out of David Beazley's excellent book `Python
Essential Reference 
<http://www.amazon.com/Python-Essential-Reference-David-Beazley/dp/0735710910>`_. 
They allow to understand more deeply how python works. I strongly recommend
this book to anybody serious about python.

An Introduction to Regular Expressions
--------------------------------------

http://www.informit.com/articles/article.asp?p=20454&rl=1

If you are going to do any sort of text manipulation, you absolutely need
to know how to use regular expressions: powerful search and replace patterns.

Software design for maintainability
------------------------------------

`My own post <./software-design-for-maintainability.html>`_

A case of shameless plug: this is a post that I wrote a few years ago. I
think that it is still relevant.

Writing a graphical application for scientific programming using TraitsUI
--------------------------------------------------------------------------

http://gael-varoquaux.info/computers/traits_tutorial/index.html

Building interactive graphical application is a difficult problem. I have
found that the traitsUI module provides a great answer to this problem.
This is a tutorial intended for the non programmer.

An introduction to Python iterators
-----------------------------------

http://www.informit.com/articles/article.asp?p=26895&rl=1

This article may not be terribly easy to follow, but iterator are a
great feature of Python, so this is definitely worth reading.

Functional programming
----------------------

http://www.ibm.com/developerworks/linux/library/l-prog.html?open&l=766,t=gr,p=PrmgPyth

Functional programming is a programming style where mathematical
functions are successively applied to immutable objects to go from the
inputs of the program to its outputs in a succession of transformation.
It is appreciated by some because it is easy to analyze and prove.
In certain cases it can be very readable.

Patterns in Python
------------------

http://www.suttoncourtenay.org.uk/duncan/accu/pythonpatterns.html. 

This document exposes a few design patterns in Python. Design patterns
are solutions to recurring development problems using object oriented
programming. I suggest this reading only if you are familiar with OOP.

Idiomatic Python
-----------------

* Jeff Knupp's post, a summary of his book:

  http://www.jeffknupp.com/blog/2012/10/04/writing-idiomatic-python/

* The `scipy-lectures <https://scipy-lectures.github.io>`_ chapter on
  advanced Python:

  https://scipy-lectures.github.io/advanced/advanced_python/index.html

General Object-Oriented programming advice
---------------------------------------------

Designing Object-oriented code actually requires some care: when you are
building your set of abstractions, you are designing the world in which
you are going to be condemned to living (or actually coding). I would
advice people to keep things as simple as possible, and follow the SOLID
principles:

http://mmiika.wordpress.com/oo-design-principles/

Using decorators to do meta-programming in Python
--------------------------------------------------

http://www-128.ibm.com/developerworks/linux/library/l-cpdecor.html.

A very beautiful article for the advanced python user. Meta-programming
is a programming technique that involves changing the program at the 
run-time. This allows to add new abstractions to the code the
programmer writes, thus creating a "meta-language". This article shows
this very well.

A Primer on Python Metaclass Programming
----------------------------------------

http://www.onlamp.com/lpt/a/3388

Metaclasses allow to define new style of objects, that can have different
calling, creation or inheritance rules. This is way over my head, but I
am referencing it here for the record.

Iterators in Python
--------------------

https://docs.python.org/2/library/itertools.html#recipes

Learn to use the itertools (but don't abuse them)!

Related to the producer/consumer problem with iterators, see:

http://www.oluyede.org/blog/2007/04/09/producerconsumer-in-python/

.. vim:spell:spelllang=en_us ft=rst
