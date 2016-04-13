Long sys.path and consequences, one more reason not to use easy_install
#######################################################################

:date: 2009-04-09 08:43
:tags: python

For those who don't know, sys.path is the path that the Python
interpreter traverse at each module import to look for the module file
imported.

This blog post is about the consequences of having a long sys.path. I'll
try and make it short, but I would have a lot to say. I am just reacting
on `Noah Gift's post on performance improvement`_, not making a full
essay on why overloading sys.path is considered harmful.

When using easy\_install (or setuptools), each new project is installed
in a different directory, and the directory is added at runtime to the
sys.path (the addition at runtime confuses many users who are not aware
of it). As a result, you quickly end up with more than 40 directory on
your sys.path. These directories are 'stat-ed' one after the other on
each module import. Thus if you have a long sys.path, there are a large
amount of system calls to read directories. To check this out, simply
try:

.. code-block:: shell

    strace python -c "import foobar" 2>&1 | less

You can see the amount of noise created by a simple (failing) import
statement. On a system with high latency (such as an NFS, as we use at
work), this is very costly.

Noah joyfully reports performance improvements by hijacking the Python
import mechanism. I claim that part of what Noah has done is not really
hijacking the import mechanism, it is undoing the hijacking performed by
setuptools.

I know I am being rude, but many people raised this point before, and it
is not getting any traction from the setuptools maintainer. I claim that
you should not be using setuptools or easy\_install if you want
performance or control. I claim that you should not be using setuptools
unless you understand well what you are doing (which defeats the name
easy\_install).

The way I install packages when I want good control via easy\_install is
in a virtual environment to discovered the dependencies, and then:

.. code-block:: shell

    easy_install -Zeab . package_name

to download the package for each required package, and

.. code-block:: shell

    python setup.py install --single-version-externally-managed --record ./foobar

if the package itself is using setuptools.

As you can see, setuptools make it really hard to do a clean install.
Its a design choice :(.

Another alternative is to use `pip`_ which I strongly encourage.

.. _Noah Gift's post on performance improvement: http://artificialcode.blogspot.com/2009/04/short-circuiting-python-module-lookup.html
.. _pip: http://pypi.python.org/pypi/pip
