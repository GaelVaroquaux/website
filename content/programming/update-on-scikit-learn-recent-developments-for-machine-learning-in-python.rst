Update on scikit-learn: recent developments for machine learning in Python
##########################################################################

:date: 2012-05-09 00:12
:tags: machine learning, python, science, scikit-learn, sprint

Yesterday, we released version 0.11 of the `scikit-learn`_ toolkit for
machine learning in Python, and there was much rejoincing.

Major features gained in the last releases
------------------------------------------

In the last 6 months, there have been many things happening with the
scikit-learn. While I do not whish to give an exhaustive summary of
features added (it can be found `here`_), let me list a few of the
additions that I personnally find exciting.

Non-linear prediction models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For complex prediction problems where there is no simple model
available, as in computer vision, non-linear models are handy. A good
example of such models are those based on decisions trees and model
averaging. For instance random forests are used in the Kinect to locate
body parts. As they are intrinsically complex, they may need a large
amount of training data. For this reason, they have been implemented in
the scikit-learn with special attention to computational efficiency.

-  `Randomized Forests and extra-trees`_
-  `Gradient boosted regression trees`_

Dealing with unlabeled instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is often easy to gather unlabeled observations than labeled
observation. While prediction of a quantity of interest is then harder
or simply impossible, mining this data can be useful.

`Semi-supervised learning`_: using unlabeled observations together with
labeled ones for better prediction.


--------------

`Outlier/novelty detection`_: detect deviant observations.

--------------
 
`Manifold learning`_: discover a non-linear low-dimensional structure in
the data.

--------------

`Clustering`_ with `an algorithm`_ that can scale to really large
datasets using an online approach: fitting small portions of the data on
after the other (Mini-batch k-means).

--------------


`Dictionary learning`_: learning patterns in the data that represent it
sparsely: each observation is a combination of a small number patterns.


Sparse models: when very few descriptors are relevant
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In general, finding which descriptors are useful when there are many of
them is like find a needle in a haystack: it is a very hard problem.
However, you know that only a few of these descriptors actually carry
information, you are in a so-called *sparse* problem, for specific
approaches can work well.


`Orthogonal matching pursuit`_: a greedy and fast algorithm for very
sparse linear models


--------------


`Randomized sparsity (randomized Lasso)`_: selecting the relevant
descriptors in noisy high-dimensional observations


--------------

`Sparse inverse covariance`_: learning graphs of connectivity from
correlations in the data


Getting developpers together: the Granada sprint
================================================

.. raw:: html

   <p>
   <object width="400" height="300" align="right">
   <embed type="application/x-shockwave-flash" src="http://www.flickr.com/apps/slideshow/show.swf?v=109615" allowfullscreen="true" flashvars="offsite=true⟨=en-us&amp;page_show_url=%2Fsearch%2Fshow%2F%3Fq%3Dscikit-learn%26m%3Dtags%26w%3D66885349%2540N03&amp;page_show_back_url=%2Fsearch%2F%3Fq%3Dscikit-learn%26m%3Dtags%26w%3D66885349%2540N03&amp;method=flickr.photos.search&amp;api_params_str=&amp;api_tags=scikit-learn&amp;api_tag_mode=bool&amp;api_user_id=66885349%40N03&amp;api_safe_search=3&amp;api_content_type=7&amp;api_media=all&amp;api_sort=date-posted-desc&amp;jump_to=&amp;start_index=0" width="400" height="300">
   </embed>
   </object>
   </p>

Of course, such developments happen only because we have a great team of
`dedicated coders`_.

Getting along and working together is a critical part of the project. In
December 2011, we held the first international `scikit-learn`_ sprint in
Granada, on the side of the `NIPS conference`_. That was a while ago,
and I haven't found time to blog about it, maybe because I was too busy
merging in the code produced :). Here is a small report from my point of
view. Better late than never.

Participants from all over the globe
------------------------------------

This sprint was a big deal for us, because for the first time, thanks to
sponsor money, we were able to fly contributors from overseas and meet
the team in person. For the first time I was able to see the faces
behind many of the fantastic people that I knew only from the mailing
list.

I really think that we must thank our sponsors, **Google** and
**tinyclues**, but also The PSF, that is in particular Jesse Noller but
especially **Steve Holden**, whose help was absolutely instrumental in
getting sponsor money. This money is what made it possible to unite a
good fraction of the team, and it opened the door to great moments of
coding, and more.

Producing code lines and friendship
-----------------------------------

An important aspect of the sprint for me was that I really felt the team
being united. Granada is a great city and we spent fantastic moments
together. Now when I review code, I can often put a face on the author
of that code and remember a walk below the Alhambra or an evening in a
bar. I am sure it helps reviewing code!

Was it worth the money?
-----------------------

.. image:: http://gael-varoquaux.info/blog/wp-content/uploads/2012/skl_activity.png
   :width: 90%


I really appreciate that the sponsors did not ask for specific returns on
investment beyond acknowledgments, but I think that it is useful for us
to ask the question: was it worth the money? After all, we got around
$5000, and that's a lot of money. First of all, as a side effect of the
sprint, people who had invested a huge amount of time in a machine
learning toolkit without asking anything in return got help to go to a
major machine learning conference.

But was there a return over investment in terms of code? If you look at
the number of lines of code modified weekly (figure on the right), there
is a big spike in December 2011. That's our sprint! Importantly, if you
look at the months following the sprint, there still is a lot of activity
in the months following the sprint. This is actually unusual, as the
active developments happen more in the summer break than during the
winter, as our developpers are busy working on papers or teaching.

The explaination is simple: we where thrilled by the sprint. Overall, it
was incredibly beneficial to the project. I am looking forward to the
next ones.

.. _*scikit-learn*: http://scikit-learn.org
.. _here: http://scikit-learn.org/stable/whats_new.html
.. _Randomized Forests and extra-trees: http://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees
.. _Gradient boosted regression trees: http://scikit-learn.org/stable/modules/ensemble.html#gradient-tree-boosting
.. _Semi-supervised
 learning: http://scikit-learn.org/stable/modules/label_propagation.html
.. _Outlier/novelty detection: http://scikit-learn.org/stable/modules/outlier_detection.html
.. _Manifold learning: http://scikit-learn.org/stable/modules/manifold.html
.. _Clustering: http://scikit-learn.org/stable/modules/clustering.html
.. _an algorithm: http://scikit-learn.org/stable/modules/clustering.html#mini-batch-k-means
.. _Dictionary learning: http://scikit-learn.org/stable/modules/decomposition.html#dictionarylearning
.. _Orthogonal matching pursuit: http://scikit-learn.org/stable/modules/linear_model.html#orthogonal-matching-pursuit-omp
.. _Randomized sparsity (randomized Lasso): http://scikit-learn.org/stable/modules/feature_selection.html#randomized-sparse-models
.. _Sparse inverse covariance: http://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphLasso.html#sklearn.covariance.GraphLasso
.. _dedicated coders: https://github.com/scikit-learn/scikit-learn/graphs/contributors
.. _scikit-learn: http://scikit-learn
.. _NIPS conference: http://nips.cc
