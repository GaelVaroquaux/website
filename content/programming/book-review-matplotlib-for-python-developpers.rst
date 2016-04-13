Book review: Matplotlib for Python Developpers
##############################################
:date: 2010-03-26 10:49
:tags: python, scientific computing, books

*Packt publishing* sent me a copy of Sandro Tosi's book `Matplotlib for
Python Developpers`_ a while ago. Unfortunately, it arrived after I had
left for the Christmas break, and I couldn't find time to review it for
a while (I am terribly bad at time-management, and I do too many things,
as I result I am always overworked). 3 months later, I have finally
found time to read it and post a review.

Content
=======

The book introduces `matplotlib`_ which is, for those who don't know, a
truly fantastic library for scientific plotting in Python. Matplotlib is
great because it is really easy to pick up, and can be used to produce
very high-quality plots.

The book starts by progressively introducing the simple, imperative API
for matplotlib, with a focus on getting the user immediately plotting
data. It then moves on to a review of the functionality for plotting in
matplotlib and the object-oriented usage of matplotlib. Finally, Sandro
shows us how to embedded matplotb in various environment such as GUI
toolkits or web development tools.

The last part of the book is, in my opinion the most original and
precious, as these subjects are less well-known and documented in
classical references accessible to people with a scientific computing
background.

Target audience
===============

The book can pretty much be picked by a scientific Python beginner. It
does require some knowledge of the Python language, but if the reader
has programmed in another language, I don't see this as a big problem.
In this regard, the book is especially interesting, as it can lead a
scientist from newbie to writing simple end-user programs. There is a
clear need for more of these documents currently.

The book will also be useful for the experienced Python developers
looking to pick up quickly matplotlib.

Personal comments on the book
=============================

In my experience, exposing a tool such as matplotlib is a challenge:
everybody has different plotting needs and there is an infinity of
variation in ways that you can use a powerful library like matplotlib.
Thus, Sandro's exposition of matlplotlib will not suffice: people should
absolutely read more, and I can't stress too much that the matplotlib
documentation is excellent, and people should read more of it.

In general, I found that the books reads fairly well. Off course, I am
not the best critic in term of ease of read, as I know matplotlib very
well. I do find that the book lacks a *personal touch* such as
interesting examples, or profound insights on specific problems. There
is nothing that got me excited in the book (again, maybe it's because I
know what's in the book quite well).

Once again, in my eyes, the biggest contribution of this book is to put
together an introduction to matplotlib, and examples of application
building using matplotlib. I would especially recommend the book for
people wanting to build simple data visualization GUIs.

--------------

Finally, with regards to interactive data visualization, in my
experience, scientific programmers achieve better productivity when
avoiding to work at the widget level and using an abstraction library. I
strongly recommend looking at `TraitsUI`_ for this purpose. you can find
a tutorial `here`_ (disclaimer: I wrote that tutorial).

Also, if you are going to write a data visualization program that is
interactive in the sens that it enables the user to interact with the
data, using `Chaco`_ instead of matplotlib may make your life easier.
Chaco is not as well polished and documented as matplotlib, and I would
never use it for a quick scripting work, but it has a strong focus on
data interaction, and as such makes it really easy to build very
responsive user interfaces, because it is very fast and has a clear
object-oriented API.

.. _Matplotlib for Python Developpers: http://www.packtpub.com/matplotlib-python-development/book
.. _matplotlib: http://matplotlib.sourceforge.net/
.. _TraitsUI: http://code.enthought.com/projects/traits/docs/html/
.. _here: http://gael-varoquaux.info/computers/traits_tutorial/index.html
.. _Chaco: http://code.enthought.com/chaco/
