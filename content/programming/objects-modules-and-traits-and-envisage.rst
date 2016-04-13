Objects, modules and Traits and Envisage
########################################

:date: 2008-04-05 13:19
:tags: python, scientific computing, software engineering, software architecture

I have been reading an article about a new language paradigm (`Erasmus,
a modular language for concurrent programming`_). The authors discuss
the limitations of objects in terms of modularity. To sum up their point
(and most probably distort it completely), the limitations with objects
comes from the fact that you can't be sure what is modifying what:
suppose you have a method *foo* of an object *bar* that you call in a
method of an object *baz*, you cannot be sure that this method hasn't
modified private attributes of your object *baz*, as *foo* could have
called a method of your object. This does happen in large code bases. Of
course, best practice tries to reduce this to a minimum, but this
reduces modularity, and thus limits both code reuse and concurrency (as
side effects are not well controlled).

Erasmus's solution to is adopt a new container, that they call modules
rather than objects, and that are based on message passing rather than
method calls. These modules live in separate processes and can
themselves be made of more conventional code (I am extrapolating a bit
from the original article here).

This strikes me as being related to a pattern that I see more and more
in my code that uses Traits. The objects deriving from HasTraits have a
very easy and cheap way of coupling callbacks to the modification of
their attributes. This induces a programming style know as reactive
programming that is entirely callback-driven. In addition, this is a
nice way of ensuring that the internal state of an object is always
consistent. This is a first step to message passing and decoupling: you
no longer call methods, you just set attributes and let the object do
the rest. The limitation of this model in a large code base is that you
have to carry around references to the objects you are interested about,
and their attributes. Traits has patterns to help you do this
(delegation, namely), but it is still a limitation.

This is where the `Envisage framework`_ comes into play. Envisage
introduces the notion of plugins which provide extension points. These
extension points are special traits attributes that are published in a
registry (which can be application-wide, or not, in Envisage3). You can
query the registry to retrieve these extension points and contribute to
them. After that, the traits callback mechanism triggers an action in
the plugin contributing the extension point.

This contribution mechanism could be based on message passing between
processes quite easily (although for GUIs it breaks down, because AFAIK
you cannot assemble a consistent GUI from different widgets living in
different process space, without using some Xwindows-specific tricks).
Of course this does not give me hard guaranties of decoupling and
control of the side-effects, as a call to a plugin can induce calls to
other plugins inside it. This is where best practice comes along: core
plugins should be able to run and provide their basic functionality
outside of Envisage, as normal objects. Envisage should only be a thin
wrapper allowing them to expose this functionality and extend other
plugins. This is introducing a distinction between objects and method
calls, that do not need to be arranged in self-consistent entities and
which you use very often , and plugins and extensions contribution, that
form standalone entities and should be used more sparsely.

Of course Envisage cannot go too far in terms of providing guaranties
for decoupling. It gives a mechanism, best practices, could even help
plugin decoupling by having them live in different processes, but as
long as it does not enforce rules in the semantics of the language, it
cannot achieve what projects like Erasmus are trying to do. I however
think it is good to have a look at the work done in these projects to
see what we can learn.

.. _Erasmus, a modular language for concurrent programming: http://users.encs.concordia.ca/~grogono/Erasmus/E01.pdf
.. _Envisage framework: https://svn.enthought.com/enthought/wiki/EnvisageThree
