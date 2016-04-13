Scikit Learn coding sprint
##########################

:date: 2010-09-04 17:43
:tags: python, scientific computing, scikit-learn

We have been really crap at communicating the next `scikit-learn`_
coding sprint. It's next week!

The coding sprint will take place the 8 and 9 September at `INRIA
Saclay`_, near Paris, in the room K110 (building K).

For those who cannot make it, it will be possible to participate using
the IRC chan (#scikit-learn on irc.freenode.net).

We will start at 9am (Paris time), and a sketch of the planning can be
found `here`_. In particular:

-  More docs! we still need tutorials: features selection, model
   selection, cross-validation, etc..
-  Make the `pipeline object`_ really work + illustration in different
   contexts.
-  Clean up and doc for bayesian approaches.
-  Implementation of PCA (fit + transform).
-  FastICA (adapt the `CanICA`_ code)
-  LDA : Covariance estimators (Ledoit-Wolf) and add transform.
-  `Preprocessing routines`_ (center, standardize) with fit transform.
-  Anything that you have a particular interest in.

Do not hesitate to send on the `mailing list`_ some advices on this
(incomplete...) list, and see you next week!

--------------

`scikit-learn`_ is a Python module for efficient and easy machine
learning using scipy and numpy.

.. _scikit-learn: http://scikit-learn.sourceforge.net/
.. _INRIA Saclay: http://maps.google.fr/maps/place?oe=utf-8&rls=com.mandriva:en-US:official&client=firefox-a&um=1&ie=UTF-8&q=inria+saclay&fb=1≷=fr&hq=inria&hnear=Saclay&cid=14838681423181723946
.. _here: http://sourceforge.net/apps/trac/scikit-learn/wiki/SprintPlanning
.. _pipeline object: http://github.com/scikit-learn/scikit-learn/blob/master/scikits/learn/pipeline.py
.. _CanICA: http://github.com/GaelVaroquaux/canica/blob/master/canica/algorithms/fastica.py
.. _Preprocessing routines: http://github.com/scikit-learn/scikit-learn/blob/master/scikits/learn/preprocessing.py
.. _mailing list: https://lists.sourceforge.net/lists/listinfo/scikit-learn-general
