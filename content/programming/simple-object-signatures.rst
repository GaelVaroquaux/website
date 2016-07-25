Simple object signatures
########################
:date: 2010-07-16 23:31
:tags: software engineering, software architecture, design patterns, scientific computing, selected

A *signature* pattern
=====================

There are many libraries around to specify what I call a *'signature'*
for an object, in other words a list of attributes that define its
parameter set. I have heavily used `Enthought's Traits library`_ for
this purpose, but the concept is fairly general and can be found *eg* in
ORMs (Object Relational Mappers) or web frameworks.

Specification of this interface of parameters may be used to answer a
variety of needs:

-  **Typing**: in the case of an ORM, to generate UIs, or for better
   error management, it may be desirable to have some control on the
   types of certain attributes of an object. In this case, specifying
   the signature corresponds to laying out a **data model** for the
   object.
-  **Reactive programming**: using properties to react to changes to
   attributes, one can fully specify the API of an object in terms of
   these attributes. This gives a message-passing like programming style
   that can be very well suited to parallel-computing in particular
   because it can easily be made thread-safe.

Signatures for statistical learning objects
===========================================

Recently, I considered the *signature* pattern in a new context. In the
`scikit-learn`_, we are interested in statistical learning. This entails
fitting models to data and often tuning parameters to select a model
that fits best (a problem called *model selection*). Each of our models
is an object that implements a couple of key methods to fit to the data
and to apply to new data (*fit* and *predict*).

The approach that we are currently taking for model selection is (more
or less) to generate a list of models with different parameters and fit
and test them on the data.

A very nice feature would be to find out the parameters to vary simply
by inspecting the objects, and such a desire recently got us
`discussing`_ of defining *signatures* for our objects. I must confess
that I am a bit weary as this means either depending on a signature
library, or building one. We don't want to grow our dependencies, and
most signature-definition code that I know involve meta-programming
tricks to avoid code duplication.

Solving the simple problem: avoiding type checking
==================================================

Today, I had to bite the bullet, because we were in a situation in which
we had to instantiate new models from the existing one during model
selection. For technical reasons, using a *copy.copy* to create these
new models was not a great idea, and it was better to have the minimal
list of parameters required. Here come signatures again.

After a bit of messing around with the code, I realized that typing
information was useless, and most probably harmful, to our immediate
goals and that I just needed the names of the relevant attributes. I
finally settled down to the following solution (which might still
change):

-  All parameters need to be specified as keyword arguments of the
   *\_\_init\_\_*. The *\_\_init\_\_* may not have positional arguments
   or '\*' arguments. Attributes on the objects have the same names as
   the *\_\_init\_\_* parameters.
-  A simple base class, with couple of methods relying on a simple use
   of the *inspect* module to find the signature of the *\_\_init\_\_*.

--------------

.. code-block:: python

    class BaseEstimator(object):
        @classmethod
        def _get_param_names(cls):
            args, varargs, kw, default = inspect.getargspec(cls.__init__)
            assert varargs is None, (
                'scikit learn estimators should always specify their '
                'parameters in the signature of their init (no varargs).'
                )
            # Remove 'self'
            args.pop(0)
            return args

        def _get_params(self):
            out = dict()
            for key in self._get_param_names():
                out[key] = getattr(self, key)
            return out

        def _set_params(self, **params):
            valid_params = self._get_param_names()
            for key, value in params.iteritems():
                assert key in valid_params, ('Invalid parameter %s '
                    'for estimator %s' %
                    (key, self.__class__.__name__))
                setattr(self, key, value)

The full code can be seen `here`_ and adds a bit more features, such as
a clever *\_\_repr\_\_*.

What I like about this solution is that it (almost) does not use
metaprograming, and avoids code duplication without forcing any specific
pattern on the developer subclassing *BaseEstimator*.

The next step
=============

This approach solves my immediate problem, but not the bigger one of
finding what values can the different parameters take when varied for
model selection. Of course this second problem is much more complicated,
and maybe it is not worth solving it: the framework could very easily be
bringing in more problems than it solves.

However, it seems that a fairly easy way of specifying possible values
for parameters would be to decorate the *\_\_init\_\_*, giving the
possible parameters to be tested during the model selection:

.. code-block:: python

        @cv_params(l1=np.logspace(1e-4, 1, 10))
        def __init__(self, l1=.5, fit_intercept=True)
        # ...

All the decorator has to do is to store the information in an attribute
attached to the *\_\_init\_\_* (and probably to check that the
parameters it was given are valid arguments, in order to raise errors
early). Methods on the class can later inspect this information for
model selection, or GUI building (data-model specification will probably
require some typing language, rather than a simple list of possible
parameters).

Once again, here we would be avoiding the difficulty of specifying type
information in a non restrictive way, but avoiding a problem that we
don't have to solve is probably a good idea.

.. _Enthought's Traits library: http://code.enthought.com/projects/traits
.. _scikit-learn: http://scikit-learn.sourceforge.net/
.. _discussing: http://sourceforge.net/mailarchive/forum.php?thread_name=201007050958.16199.matthieu.perrot%40cea.fr&forum_name=scikit-learn-general
.. _here: attachments/base_estimator.py
