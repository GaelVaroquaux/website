Tracking objects in scientific code 
####################################

:date: 2008-12-23 01:26
:tags: python, scientific computing, software engineering, software architecture, selected, joblib

When I started working in my new field (data analysis of functional
brain images), I was surprised to find in our data-analysis scripts what
I thought was a very particular `code smell`_: the numerical code is
always doing a lot of filename and path manipulation, loading and saving
data even in the core routines. I couldn't picture what seemed wrong
with this, but I was uncomfortable with it.

The good
========

Memory management
-----------------

In the data-processing work I am currently doing, we deal with large
objects, mostly huge numpy arrays, though sometimes some domain-specific
data containers creep in. As a result, simple calculations take time (an
SVD is 10 minutes), and I am always fighting with memory.

Saving to disk is a handy way of freeing memory. Moreover, with
memmapping, reading only the relevant parts of pre-calculated arrays
becomes very cheap.

Crash-resistance
----------------

When the simplest operation takes ten minutes, you want to save
intermediate steps, to be able to resume calculations, or to inspect why
the code crashed. And who knows, you might need this intermediate step.

The bad
=======

The immediate apparent problem is that your code becomes riddled with
path-management code. We often joke that once we have figured out the
algorithm, the longest surviving piece of code is the path-related junk.

But, I believe this is only the tip of the iceberg, and that this code
smell hints to deeper problems.

The ugly
========

Loss of scoping
---------------

When I started working on these problems, I was startled to encounter
basic domain-specific algorithmic functions taking input and output data
filenames. It took me a while to realize that the huge problem with this
is that I loose scoping, or in other words naming locality. Let us
pretend that I have a function 'foo' that does basic numerics on large
numpy arrays, but to save memory it takes as a signature the name of the
file where the input array is stored, and the name of the filename where
the output array should be stored. So I have some code that looks like
this:

.. code-block:: python

        def process_sessions(session_files):
            for session_file in session_files:
                foo(session_file, session_file + '.out')

Saving to files in the loop is a huge gain of memory;

Now I decide I want to add a parameter to foo, and vary this parameter,
with, eg:

.. code-block:: python

        for param in params:
            process_sessions(session_files, param)

My code is hard to refactor, because I need to introduce modifications
deep in all subroutines to make sure they do not save their outputs in
the same file.

Suppose session\_files are actually extracted from an upstream dataset,
and now I want to apply my algorithm on a set of these upstream
datasets, and in parallel. Once again I need to generate a score of new
filenames and keep track of them. I can use temporary files, but I need
to keep hold of this information too, and I loose most of my
crash-resistance.

When you think it over, the way programming languages solve this problem
elegantly, is by the rules connecting names to objects, and in
particular scoping: a name corresponds to an object in a given function.
Using files is equivalent to using globals, and we have to cook up our
own scoping rules (which results in a lot of path-massaging code).

No history tracking
-------------------

When I find a file on the disk, I do not really know how it has been
generated. As a results, the crash-resistance is compromised. Moreover,
when tweaking algorithms, we often try to rerun only the necessary parts
of the algorithms, relying on the precomputed parts saved to the disk.
We comment out code, or exercise different code paths. As a result we
often end up in situations where the whole code does not actually run.
And once again refactoring is hard, because we have not expressed the
dependency relations between our intermediate results.

Doing better?
=============

Once again, today I was refactoring my algorithm, or my "pipeline" as we
call it. And once again, I felt the failure to have the proper tools,
the proper abstractions, words, to express the problem in the code.
Manipulating files directly seems wrong, for the reason expressed above.
But can we do better?

The problem, I believe, is that we need a lightweight persistence
framework adapted to scientific purposes. I remember telling Travis
Vaught a few weeks before beginning my new job that scientists had no
problem with their persistence. Well, I was so wrong.

By a persistence framework, I do not mean a persistence mechanism, like
numpy.save, or hdf5, or a database. I am interested in the objects with
which we represent it in the code. How do we solve the scoping problem?
And the history problem? Can we implement a "trajectory tracking", to
reuse the `words of Alexandre Fayolle`_, for our data containers?

I am thinking about a small set of well-thought abstractions, a bit like
the use of ORM (object relational mappers) in web application, that
would take care of the mapping from in-memory objects to objects on the
disk for us.

I am starting to have some ideas. I am thinking in terms of context
objects, with getattr tricks to do the mapping to a database doing the
bookkeeping and the trajectory tracking, and doing the impedance
matching with objects stored as numpy ".npy" files, hdf5 files, nifti
files, or whatever you want. The added value of a database would be that
it would give some robust locking, and possible network abstraction, to
allow for crash-safety, and parallel or distributed computing.

This may sound overkill, or overcomplicated. I've tried simple things.
They all failed.

This is a problem that matters a lot to me. I feel I am loosing a lot of
time on this. However I feel that the effort to do something good is
quite important. I am also afraid of polluting my numerical code with
unnecessary abstractions. The main problem is that attempting to solve
this problem would require a significant investment in time, and I don't
really see where I can find this time.

Have people encountered similar problems? Do you have any suggestions,
any trick to share?

I'd be very happy to read any comments that can move forward my
thinking, even if it is about pointing out problems and not solutions. I
still think I haven't identified the problems well.

**Update**: I have just realized that I will be almost without internet
access for the next week, starting from pretty much now. Looks like it
was a bad moment to start a thrilling discussion. I guess I got carried
away by the discontent of a day doing some bad refactoring. I really
look forward to catching up when I come back. Please forgive me for the
bad timing.

.. topic:: **Update**

    Patterns that derived from this line of thoughts are now implemented
    in the `joblib <https://pythonhosted.org/joblib/>`_ library.

.. _code smell: http://en.wikipedia.org/wiki/Code_smell
.. _words of Alexandre Fayolle: http://article.gmane.org/gmane.comp.python.french/5423
