Windows binaries for the scientific Python ecosystem
####################################################

:date: 2011-02-15 09:02
:tags: python, scipy, mayavi

I just realized yesterday that Christoph Gohlke has `a repository of
binary installers`_ (*.exe*) for Windows 32 and 64bit with almost all
the scientific Python packages that you can dream of:

-  `numpy`_, `scipy`_ and `matplotlib`_, of course (compiled
   with the MKL)
-  `cython`_
-  the `ETS`_, including `Mayavi`_
-  **VTK**, with the Python bindings
-  a variety of `scikits`_ (including the `scikit-learn`_,
   hurray!)


These binaries are incredibly useful, as building all these packages
under Windows does requires some skills, and a compiler. They complement
very well fully-fledge scientific Python distributions such as EPD or
Python(x,y), as they can be installed on top of an existing Python
installation.

--------------

I should say that I discovered this thanks to a long email discussion in
which Christoph Gohlke and Yakub Nowacki helped me debug a nasty Mayavi
bug on Windows 64bit that I couldn't reproduce as I don't have a Windows
64bit available. That was particularly helpful.

.. _a repository of binary installers: http://www.lfd.uci.edu/~gohlke/pythonlibs/
.. _numpy: http://numpy.scipy.org
.. _scipy: http://www.scipy.org/
.. _matplotlib: http://matplotlib.sourceforge.net/
.. _cython: http://cython.org/
.. _ETS: http://enthought.github.com/
.. _Mayavi: http://enthought.github.com/mayavi/mayavi/
.. _scikits: http://scikits.appspot.com/
.. _scikit-learn: http://scikit-learn.sourceforge.net/
