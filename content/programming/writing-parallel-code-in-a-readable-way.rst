Writing parallel code in a readable way
#######################################

:date: 2009-11-09 00:10
:tags: python, scientific computing, scipy, software engineering, joblib

Although I often have embarrasingly parallel problems (data parallel),
and I have an 8-CPU box at work, I used to frown on writing parallel
computing code when doing exploratory coding. We now have fantastic
parallel computing facilities in Python (amongst other,
`multiprocessing`_, `IPython`_, and `parallel Python`_). However, in my
opinion, there are two reasons to hesitate to use them, especially when
the code is very imature (which is almost always my case, in research
settings):

#. It makes the code look less like the ideas it is trying to express.
   Peter Norvig made `a pretty convincing case`_ for scientific code
   reading like math at `SciPy2009`_.
#. Because parallel computing is out of process, in Python, it is simply
   harder to debug (though I hear that the IPython guys are on that).

I have progressively developed a tiny tool to adress both problems, at
least for my embarrasingly-parallel problems. I address the second
problem by having a trivial switch to run my code without importing any
fancy parallel computing tools. And I address the first problem using
syntactic sugar to be able to type in map/reduce code that actually
looks like standard procedural code:

.. code-block:: python

    results = Parallel(n_jobs=2)(
                delayed(my_calculation)(data1, data2,
                                        parameter1=1, parameter2=2)
                for data1 in store1 for data2 in store2)

There are several tricks here:

#. I use a '*delayed*\ ' decorator that creates the argument list and
   keyword argument dictionary for me so that I can type something that
   really looks like a function call. Also, the decorator checks to see
   if the function and the arguments can be pickled, because if not the
   parallel computing libraries will raise errors, sometimes with
   hard-to-understand messages.
#. I use list comprehension to create the list to apply the map/reduce
   onto. List comprehension is really readable, and very powerful.
#. The '*Parallel*\ ' object hides all the cleverness. If the
   '*n\_jobs*\ ' parameter is set to 1, it does not call any parallel
   computing library. If it is set to -1, all the CPUs are used. The
   object instantiates the parallel computing context and also destroys
   it. While this is inefficient, it is great for catching errors early.
   And finally, while I have implemented this only for the
   multiprocessing module, any fork/join-based parallel computing
   library could be encapsulated the same way, thus providing a uniform
   API to do multi-node parallel computing or single-computer shared
   memory (as multi-processing uses the Unix fork call, and all modern
   Unices implement copy on write of memory pages, you get some shared
   memory for free without worrying about race conditions).

.. topic:: **Update**

    This pattern has actually evolved in the `joblib project
    <https://pythonhosted.org/joblib/>`_ ,
    which provides a lot of cleverness under the hood.


.. _multiprocessing: http://docs.python.org/library/multiprocessing.html
.. _IPython: http://ipython.scipy.org/doc/rel-0.9.1/html/parallel/index.html
.. _parallel Python: http://www.parallelpython.com/
.. _a pretty convincing case: http://www.archive.org/details/scipy09_day1_03-Peter_Norvig
.. _SciPy2009: http://conference.scipy.org/
.. _here: attachments/parallel.py
