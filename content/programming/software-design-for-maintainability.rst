Software design for maintainability
###################################

:date: 2010-08-01 23:47
:updated: 2014-10-02
:tags: software engineering, software architecture, python, selected

I have just spent the best part of my Sunday fixing a bug that turned
out being a `seemingly-trivial two-liner`_. Such unpleasant experiences
are all too frequent, and weight a lot on my view of code design.

My stance on code design
------------------------

.. image:: {filename}attachments/software_design_for_maintainability/cool-car-drawing-5.jpg
    :align: right
    :width: 30%

I call *code design* the process of designing the architecture of a
piece of software: what are the objects it uses? how do they interact?
how is the information passed around?...

My view of code design and software engineering has progressively
evolved to favor **extreme simplicity** over sophistication. I believe
that a good programmer should know `design patterns`_, `powerful
language features`_, `libraries dark corners`_, and *not use them unless
absolutely necessary*.

Some rules of thumb
-------------------

Here are some rules that I apply nowadays when writing code that I would
like to last (I am aware that some of them go against well-advertised
best practices).

-  **Keep it as simple a possible, really!** Experimental results have
   shown that the tractability of a code base goes down as the square of
   the number of interactions, and thus much quicker than the number of
   lines in a project. Each time you add a line, think about it: can you
   make simpler? If not you'll have to find resources to maintain your
   project as fixing bugs or adding features will grow harder.
-  **Design for the 80% usecases.** In the same vein, a small decrease
   in the requirements can make your project much simpler
   `[Woodfield1979]`_. Corner cases and minor usecases should not make
   the whole project complex and hard to maintain. If you can, give up
   on what is bringing in complexity. If you cannot, isolate it, and
   don't let it sit at the core of your design.
-  **Don't design for the future.** Again the same core idea: don't
   start planing for all the usecases, and all the difficulties that you
   haven't encountered, you will most certainly design wrong, and
   chances are that you'll add complexity that you do not use. Design
   simple, design cleanly and refactor as you go, based on concrete
   problems. This is known as the `"YAGNI principle"
   <http://en.wikipedia.org/wiki/You_aren't_gonna_need_it>`_.

.. image:: {filename}attachments/software_design_for_maintainability/howtobuildmvp.gif
    :align: center
    :width: 60%

-  **Don't be clever.** Each time you do a clever trick, whoever has to
   read and maintain this code will have to understand it (that person
   may be you, in a few years). Chances are that they'll get it wrong
   and start by loosing a lot of time.
-  **Repeating yourself may actually be OK.** This is a case of
   *practicality beats purity*. Repeating code is really a bad thing in
   software design, because it leads to an increased number of lines to
   debug, and tends to hinder reusability. However, adding complexity in
   order to save a few lines of duplicated code will cost you more in
   the long run.
-  **Use objects sparingly.** Object are great, but are they always
   need? An object with a single method *eval* can probably simply be
   implemented by a function. The limitation of objects is that they all
   have a different behavior. As a result, the users and maintainers of
   your codebase will first have to understand how all your classes
   interact before understanding your code. This also means that there
   is a lot of benefit in making many different classes that have the
   same interface.
-  **Avoid abstractions and levels of indirection.** The more levels of
   code piled on top one of the other, the more layers your maintainer
   is going to have to inspect to find were the bug might be. An
   abstraction hides another object or algorithm. To debug code, chances
   are that all the black boxes will first have to be opened.

Coding for others to debug
--------------------------

.. epigraph::

    "Debugging is twice as hard as writing the code in the first place.
    Therefore, if you write the code as cleverly as possible, you are,
    by definition, not smart enough to debug it." - Brian W. Kernighan

.. image:: {filename}attachments/software_design_for_maintainability/auto-graveyard-1.jpg
    :align: right
    :width: 40%

You may think that I am overemphasizing simplicity at the cost of
functionality. Well, think about the future of your code. The net is
full of unmaintained and abandoned code. If you want your project to
grow and have a future, you will probably need people to help you. For a
given purpose, the easiest the code is to read and debug, the more
chances you will have to pick momentum.

--------------

Some external references I like (about software engineering, rather than
debugging):

- Edmon Lau: `Hidden costs that engineers ignore
  <http://www.theeffectiveengineer.com/blog/hidden-costs-that-engineers-ignore>`_
  (**Read this**)
-  Titus Brown: `Writing (Python) Code that Doesn't Suck`_
-  Peter Norvig: `Teach yourself programming in 10 years`_
-  Paul Stachour and David Collier-Brown: `You Don't Know Jack About
   Software Maintenance`_
-  Greg Wilson: `Software carpentry: a course in software engineering`_

.. _seemingly-trivial two-liner: https://svn.enthought.com/enthought/changeset/25699/
.. _design patterns: http://en.wikipedia.org/wiki/Design_pattern_%28computer_science%29
.. _powerful language features: http://gael-varoquaux.info/computers/python_advanced/index.html
.. _libraries dark corners: http://scipy2010.blogspot.com/2010/06/tutorials-day-1-advanced-numpy.html
.. _[Woodfield1979]: http://ieeexplore.ieee.org/Xplore/login.jsp?url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5%2F32%2F35909%2F01702600.pdf%3Farnumber%3D1702600&authDecision=-203
.. _Writing (Python) Code that Doesn't Suck: http://ivory.idyll.org/blog/sep-07/not-sucking-v2
.. _Teach yourself programming in 10 years: http://norvig.com/21-days.html
.. _You Don't Know Jack About Software Maintenance: http://cacm.acm.org/magazines/2009/11/48444-you-dont-know-jack-about-software-maintenance/fulltext
.. _`Software carpentry: a course in software engineering`: http://software-carpentry.org/

