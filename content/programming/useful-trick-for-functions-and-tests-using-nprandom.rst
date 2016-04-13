Useful trick for functions and tests using np.random
####################################################

:date: 2009-08-29 16:00
:tags: python, scientific computing, software engineering, design patterns, selected
:summary: How to test functions that use the numpy random number generator

Recently, listening to Robert Kern taught a new useful trick to use when
you write functions that use the numpy random number generator:

As always, when using random number generation in code, the problem is
to get 'repeatable results'. Of course, you want only repeatable
statistics, and with statistics, the problem is to define what
repeatable is. Anyhow, for various reasons, it is useful to be able to
reproduce exactly runs, for instance when testing, fine tuning, or
debugging. That is why you would like to be able to control the seed of
your random number generation. Robert Kern showed us (at the SciPy
conference tutorial) a way to control the pseudo random number generator
(PRNG) in a function, without affecting the rest of the code. This does
not involve setting the seed of the global PRNG, as this is evil,
because it has global effects. The idea is to pass in to your functions
a PRNG instance (by default the global one):

.. code-block:: python

    def test(prng=np.random):
        print pnrg.rand(10)

if you want to use your function with a controlled PRNG, you can
instantiate one with a specific seed:

.. code-block:: python

    prng = np.random.RandomState(seed=0)

and pass it to your function.
