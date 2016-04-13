============================================
joblib: Simple patterns for performance
============================================

.. :date: 2015-08-29

.. :tags: joblib, performance, python, scipy

Trivial code: nothing to learn
===============================

`joblib.Memory`: don't run that computation twice
--------------------------------------------------

::

    >>> mem = joblib.Memory(cachedir='/tmp/joblib')
    >>> square = mem.cache(np.square)
    >>> b = square(a)                                   
    ___________________________________________________________________________
    [Memory] Calling square...
    square(array([[...]]))
    _____________________________________________________square - 0...s, 0.0min
    >>> c = square(a)

`joblib.Parallel`: make this `for` loop parallel
-------------------------------------------------

::

    >>> joblib.Parallel(n_jobs=1)(joblib.delayed(sqrt)(i**2)
    ...                           for i in range(10))
    [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]


Performant: clever behind the hood
===================================

`joblib.Memory` is **Concurrent-safe** (used it on thousand nodes grid)

`joblib.Parallel`, much more than a `for` loop:

* loop expanded lazily

* bunching of fast iterations to avoid overhead

* large arrays memmapped to save memory

_____

*We strive to never crash & not to have you modify code*

