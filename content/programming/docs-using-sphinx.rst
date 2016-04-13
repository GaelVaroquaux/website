Docs using Sphinx
#################

:date: 2008-04-28 09:10
:tags: scipy, python, mayavi, scientific computing, publishing

After Ipython and Sympy, Mayavi is now using `sphinx`_ to build its
docs. Sphinx is very neat because it allows for high quality pdf and
html from the same restructured text source. The killer feature is that
the resulting html pages have a builtin search that works with
javascript, and thus works on the client without the need of a server.

In addition, the developer is very reactive and dedicated to making
sphinx versatile-enough to generate high-quality docs for many packages.
As a result many Python projects are switching to sphinx. First Python
itself (that's what sphinx was created for), but now more and more. It
seems that zope is even considering it. One great side effect is that
documentation for different Python modules will be consistent, with the
same look and feel (although you can tweak sphinx output if you want).

We don't have a server serving the html docs yet (it is planned, we just
need a bit of time), but you can check out the pdf generated `here`_.

.. _sphinx: http://sphinx.pocoo.org/
.. _here: https://svn.enthought.com/enthought/browser/Mayavi/branches/enthought.mayavi_2.1.2/docs/build/latex/mayavi_user_guide.pdf?format=raw
