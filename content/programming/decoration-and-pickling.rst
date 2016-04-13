Decoration in Python done right: Decorating and pickling
#########################################################

:date: 2009-11-13 00:14
:tags: python, design patterns, software architecture, selected

Decoration is a fantastic pattern in Python that allows for very
light-weight metaprograming with functions rather than objects (see
`this article`_ for an in-depth discussion). However, when decorating,
it is very easy to break another great feature of the language: its
reflectivity and its ability to do static representations of its
internal objects: pickling.

In this blog post, I'd like to rewrite a post I made on the IPython
mailing list a month ago, summing up the few things to have in mind when
decorating a function.

A pattern to avoid?
===================

I have recently been revisiting my decoration code, to fight a common
mistake I had been doing, and it was partly due to the heavy use of a
simplified pattern for decorating:

.. code-block:: python

    def with_print(func):
        """ Decorate a function to print its arguments.
        """

        def my_func(*args, **kwargs):
            print args, kwargs
            return func(*args, **kwargs)

        return my_func

    @with_print
    def f(x):
        print 'f called'

The nice thing about this pattern is that is it quite easy to type, and
to read.

Why it is harmful
=================

The decorated function is actually the function 'my\_func', with a
reference to the original function 'func', a part of the scope of the
decorator 'with\_print', and thus in the closure of the with\_print
function.

The problem is that we have a closure here. Thus we have variables that
are hard to get to (the undecorated function), and the decorated
function is not picklable (which is more and more important to me, e.g.
for parallel computing).

Some solutions
==============

Avoiding the closure
--------------------

Use objects as a scope, rather than a closure:

.. code-block:: python

    class WithPrint(object):
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print args, kwargs
            return self.func(*args, **kwargs)

This solution is not enough: the following code won't pickle:

.. code-block:: python

    @WithPrint
    def g(x):
        print 'g called'

The reason this won't pickle is that we have a name collision: the code
above expands to:

.. code-block:: python

    def g(x):
        print 'g called'

    g = WithPrint(g)

and trying to pickle raises the following PicklingError:

.. code-block:: python

    Can't pickle <function g at 0x6ed2a8>: it's not the same object as __main__.g

If we do:

.. code-block:: python

    def g(x):
        print 'g called'

    h = WithPrint(g)

we can pickle h, hurray!

Using functools.wraps
---------------------

However, Python comes with the answer in the standard libary:
functools.wraps does the name unmangling.

Thus the following code produces a pickleable f:

.. code-block:: python

    from functools import wraps
    def with_print(func):
        """ Decorate a function to print its arguments.
        """
        @wraps(func)
        def my_func(*args, **kwargs):
            print args, kwargs
            return func(*args, **kwargs)
        return my_func

    @with_print
    def f(x):
        print 'f called'

| The pickling works simply because using functools.wraps resets the 
| .func\_name attribute of f to have a well-defined import path. Thus
| pickling works, simply by storing the import path, as all pickling of
| functions.

Notice that there is only a one-line difference with the original code!

I actually tend to use a combination of both solution (an object, using
functools.wraps), to keep a reference on the undecorated functions.

**Note**: Demo code of this blog post can be found `here <attachments/pickling_tests_py>`_.

Take home messages for pickling
===============================

-  Decorators can be more clever than you think, and might not return
   objects as simple as you think
-  Think about pickling, or you'll get bitten at some point (for
   instance when doing parallel computing).

and most important:

-  Use functools.wraps

A remark about object-oriented programming
==========================================

To jump on the band-wagon behind `Travis`_, I believe that this
discussion teaches us a bit about object-oriented programming. When
decorating, we are really taking a callable object, and redefining how
the call is handled.  If we do this the naive way, we loose
introspection (there is no way to access the original callable from
Python), and as a result pickling, and many of the nice feature going
with reflexivity in Python. This is because we trapped information in a
scope that is not accessible by normal Python code (without playing at
the frame level). If on the other hand, we accept that what we have
behind all this are nested scope with a control of lookups, and we
create a full-blown object, we have the benefits of the black box, and
the benefits of reflexivity.

But this is not the point I want to make. The point I want to make is
that, by decorating, we are piggy-backing on an absolutely universal
object/interface: the callable. Everybody knows what a callable is, and
knows how to employ it. From a pure object-oriented point of view,
decorating is simply some kind of proxy design pattern. But, to stress
Travis's point, introducing new objects that have their own behavior
puts cognitive load on the programmer. The real value of decoration is
that it is object-oriented programming without adding any new or
surprising interface. You don't really have to care what is going on,
you can still use the resulting 'proxied' function as the original
function: a simple function.

.. _this article: http://www.ibm.com/developerworks/linux/library/l-cpdecor.html
.. _Travis: http://blog.enthought.com/?p=223
