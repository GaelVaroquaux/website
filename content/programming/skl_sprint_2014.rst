===================================
Scikit-learn 2014 sprint: a report
===================================

:date: 2014-07-25
:tags: sprint, scikit-learn, python, machine learning

A week ago, the 2014 edition of the
`scikit-learn <http://scikit-learn.org>`__ sprint was held in Paris.
This was the third time that we held an internation sprint and it was
hugely productive, and great fun, as always.

Great people and great venues
=============================

.. image:: https://pbs.twimg.com/media/BsqD4BeCQAEnT6w.jpg
   :align: center
   :width: 65%

We had a mix of core contributors and newcomers, which is a great
combination, as it enables us to be productive, but also to foster the
new generation of core developers. Were present:

-  Laurent Direr
-  Michael Eickenberg
-  Loic Esteve
-  Alexandre Gramfort
-  Olivier Grisel
-  Arnaud Joly
-  Kyle Kastner
-  Manoj Kumar
-  Balazs Kegl
-  Nicolas Le Roux
-  Andreas Mueller
-  Vlad Niculae
-  Fabian Pedregosa
-  Amir Sani
-  Danny Sullivan
-  Gabriel Synnaeve
-  Roland Thiolliere
-  Gael Varoquaux

.. image:: https://pbs.twimg.com/media/BsqRedvCEAE5Opw.jpg
   :align: center
   :width: 65%

As the sprint extended through a French bank holiday and the week end,
we were hosted in a variety of venues:

-  `La paillasse <http://lapaillasse.org>`__, a Paris bio-hacker space
-  `INRIA <http://www.inria.fr>`__, the French computer-science national
   research, and the place where I work :)
-  `Criteo <http://www.criteo.com>`__, a French company doing word-wide
   add-banner placement. The venue there was absolutely gorgeous, with a
   beautiful terrace on the roofs of Paris. And they even had a social
   event with free drinks one evening.
-  `Tinyclues <http://www.tinyclues.com>`__, a French startup mining
   e-commerce data.

I must say that we were treated like kings during the whole stay; each
host welcoming us as well they could. Thank you to all of our hosts!

Sponsored by the Digicosm Labex
=====================================================

Beyond our hosts, we need to thank the `Digicosme Labex
<https://digicosme.lri.fr/tiki-index.php>`__.
Digicosm gave us funding that covered some of the lunches, accomodations,
and travel expenses to bring in our contributors from abroad.

Achievements during the sprint
==============================

The first day of the sprint was dedicated to polishing the `0.15
release <http://www.scikit-learn.org/stable/whats_new.html>`__, which
was finally released on the morning of the second day, after 10 months
of development.

A large part of the efforts of the sprint were dedicated to improving
the coding base, rather than directly adding new features. Some files
were reorganized. The input validation code was cleaned up (opening the
way for better support of pandas structures in scikit-learn). We hunted
dead code, deprecation warnings, numerical instabilities and tests
randomly failing. We made the test suite faster, and refactored our
common tests that scan all the model.

Some work of our GSOC student, Manoj Kumar, was merged, making some
linear models faster.

Our `online documentation <http:/scikit-learn.org/dev>`__ was improve
with the `API
documentation <http://scikit-learn.org/stable/modules/classes.html>`__
pointing to examples and source code.

Still work in progress:

-  Faster stochastic gradient descent (with AdaGrad, ASGD, and one day
   SAG)
-  Calibration of probabilities for models that do not have a
   'predict\_proba' method
-  Warm restart in random forests to add more estimators to an existing
   ensemble.
-  Infomax ICA algorithm.

