Error in my article
###################

:date: 2009-01-27 22:00
:tags: scipy, scientific computing

There is an error in a code example in my article that just came out in
Linux Magazine France. I am so ashamed. I did test the code, but I
didn't have automated tests, so I broke it when tweaking it :(. I think
the lesson is that you need to do more than doc-testing articles (it was
doc-tested).

The code example is about calculating the Mandebrot set. The idea is
that you take a grid of the numbers c complex plane, and iterate on it
the function f = lambda z: z\*\*2 + c. You look at the divergence of
this iteration, and plotting a mesure of the divergence gives you a nice
figure. The code I wrote was:

.. code-block:: python

    from numpy import ogrid, zeros, abs, isnan, ones
    c = x + y * 1j
    threshold_time = zeros((500, 500))
    z = zeros((500, 500))
    mask = ones((500, 500), dtype=bool)
    for i in range(50):
        z[mask] = z[mask]**2 + c[mask]
        mask = (abs(z) > 10)
        threshold_time += mask

The error is subtle. First there is the not so subtle mask error: I am
masking the points that diverge, and iterate them even further. This is
exactly the opposite that I meant to do. Then there is the more subtle
bug: the line "z[mask] = z[mask]\*\*2 + c[mask]" is an in-place
assignment. As a result the dtype of z is not modified: z is not
magically cast in a complex. Thus the imaginary information coming from
c is lost. And that information is crucial to Mandelbrot.

The right code is:

.. code-block:: python

    from numpy import ogrid, zeros, abs, isnan, ones, complex
    c = x + y * 1j
    threshold_time = zeros((500, 500))
    z = zeros((500, 500), complex)
    mask = ones((500, 500), dtype=bool)
    for i in range(50):
        z[mask] = z[mask]**2 + c[mask]
        mask = (abs(z) < 10)
        threshold_time += mask

Plot the threshold\_time array with pylab.imshow (from the matlplotlib
project) to get a nice figure.
