=========================================
What makes great online coding tutorials
=========================================

:tags: scikit-learn, machine learning, python, documentation, teaching

.. :date: 2015-08-29

.. |nbsp| unicode:: U+00A0

.. note::

    Greg Wilson's `talk yesterday
    <https://www.euroscipy.org/2015/schedule/presentation/68/>`_, and the
    spur of activity on `scipy-lectures <http://scipy-lectures.github.io/>`_
    due to `teaching at Euroscipy
    <https://www.euroscipy.org/2015/schedule/esp2015-tutorials/>`_, have
    gotten me thinking on *what I feel makes great online materials to teach
    a computing environment*.


Good tutorial materials and documentation are a really hard problem,
especially when they grow big. They are also very important.

This post is very much inspired by our experience building, teaching and
maintaining the `scipy-lectures <http://scipy-lectures.github.io/>`_, but
also documenting the `scikit-learn project
<http://scikit-learn.org/stable>`_. As a result, a lot of the technical
solutions rely on `sphinx <http://sphinx-doc.org/>`_ --which is really
awesome-- but in my opinion, the core ideas are universal.

Editorial choices and accessible content
==========================================

A tutorial is not a full documentation. It needs to be **progressive and
not exhaustive**. In other words, a beginner shouldn't have to fully
comprehend intricated details such as how a compiler works, in the first
lesson.

.. note::
    :class: align-right

    Jargon is to be avoided at all cost

We have find that the typical unit (ie a tutorial, or a chapter in the
scipy-lectures) should be readable or doable as a tutorial in 1.5 hours
to 2 hours maximum. This does imply limiting the amount of information.

Linking is crucial
===================

As mentionned above, in a given page the information is limited, for a
reason of scope, for also of maximum attentional span of the reader. For
this reason, **links to other materials matter hugely**.

In a large online material, we find 3 types of links:

- Internal links across chapters / sections in the given material
- Link to pages explaining general concepts (typical Wikipedia)
- Links to other technical documentation (typically package documentation
  or API references).

In our age of fast-evolving Internet, URL-rot (URLs that change and link
that break) is a major problem.

In a full documentation addresses that fact that people looking for info
don't land on the right page (eg googling, or going from examples to
narrative documention, to the API reference, and back to the examples
showing the use of of an object).

The use of intersphinx to link across projects

Reliability: code that actually works
=======================================

.. epigraph::

    "If it ain’t tested, it’s broken"
    |nbsp| |nbsp| ---  |nbsp| |nbsp|
    *Bruce Eckel*


Doctests, and continuous integration

Examples that are run (sphinx gallery, it actually answers a lot the
linking problems)

The use of examples to generate figures (ie: figure are not allowed to be
checked in)

Also implies some constraint on the language and the API of the libraries
you are trying to document: a few lines of code should give you a visible
result. But this is actually an important factor of success for a
computing environement.

Sidebar: change in API / language features make it really hard, as if the
tutorial uses many different packages, as in a big-picture tutorial,
their is a combinatorial explosion in APIs.

Layout: break monotony, but don't make a expressionist painting
================================================================

Formatting: 

The use of restructured text directives, such as topic, note, seealso,
tip, sidebar, is strongly encouraged



