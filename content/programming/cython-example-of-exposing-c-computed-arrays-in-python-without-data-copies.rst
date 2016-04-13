Cython example of exposing C-computed arrays in Python without data copies
##########################################################################

:date: 2011-09-28 23:42
:tags: scipy, cython, python, scientific computing, selected

Some advice on passing arrays from C to Python avoiding copies. I use
Cython as I have found the code to be more maintainable than hand-written
Python C-API code.

I found out that there was no self-contained example of creating numpy
arrays from existing data in Cython. Thus I created my own. The full code
with readme build and demo scripts is available on a `gist`_. Here I only
give an executive summary.

The core functionality is implemented by the
`PyArray\_SimpleNewFromData`_ function of the C API of numpy that can
create an ndarray from a pointer to the data, a simple data type, and
the shape of the data. The Cython file just builds around that function:

.. raw:: html

   <p>
   <script src="https://gist.github.com/1249305.js?file=cython_wrapper.pyx"></script>
   </p>

.. _gist: https://gist.github.com/1249305
.. _PyArray\_SimpleNewFromData: http://docs.scipy.org/doc/numpy/user/c-info.how-to-extend.html#PyArray_SimpleNewFromData
