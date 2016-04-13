Pydata: make it boring; stop the arm race
===========================================

Euroscipy: (on an Ubuntu 15.04 install)

* installing bokeh upgrades numpy, and pandas

* various tutorials IPython notebook require 'v4'-compatible IPython
  notebooks

* Juan's widgets in an IPython notebook didn't work on Jupyter because of
  changed import

=> is this really useful?

For the main conf yes, but for the tutorials?

Depends on what our goals are. But I hear motivations such as advancement
of science, reproducible research, or simply making it easier for people
to do their job, ie in companies.

* Counter example: Cython: stringent backward compatibility, support of a
  huge number of compilers, plateforms, and python version => massively
  beneficial to the community

venvs are not the solution for 'production'

parallel with the python standard library ('the standard library is where
code goes to die').

