===============================================================================
Of software and Science. Reproducible science: what, why, and how
===============================================================================

:date: 2015-12-16
:tags: reproducible research, science, software, machine learning, scientific software

.. |nbsp| unicode:: U+00A0


At `MLOSS 15
<mloss-2015-wising-up-to-building-open-source-machine-learning.html>`_ we
brainstormed on reproducible science, discussing **why we care about
software in computer science**. Here is a summary blending `notes from
the discussions
<https://gist.github.com/GaelVaroquaux/33e7a7b297425890fefa>`_ with my
opinion.

.. epigraph::

    "Without engineering, science is not more than philosophy"
    |nbsp| |nbsp| ---  |nbsp| |nbsp|
    `the community <https://twitter.com/GaelVaroquaux/status/619767624654786560>`_


**How do we enable better Science? Why do we do software in science?**
These are the questions that we were interested in.

.. container:: grey

   **Improving reproducility of our scientific studies makes us more
   efficient in the long run** to do good science: even inside a lab, new
   research efforts build upon the previous work.

|

Forms of reproducible science: reproduction, replication, & reuse
====================================================================

`The classic concepts of reproducible science
<https://politicalsciencereplication.wordpress.com/2013/02/24/is-there-a-difference-between-replication-reproduction-and-re-analysis/>`_
are:

* **Reproducibility**: being able to rerun an experiment as it was run,
  for instance by reanalysing data.

* **Replicability**: being able to redo an experiment from scratch.

The *reproducible science* movement argues sharing source code of
experiments is a need for *reproduction*.

For reproduction, fields like computer science (development of methods)
and biology (challenging data acquisition) have very different
constraints, with the complexity allocated differently between data and
code.

.. epigraph::

    "Machine learning people use hugely complex algorithms on trivially
    simple datasets. Biology does trivially simple algorithms on hugely
    complex datasets."
    |nbsp| |nbsp| ---  |nbsp| |nbsp|
    *an MLOSS15 attendee*

|

We felt that computer science needed an additional notion, complementing
replication and reproduction:

* **Reusability**: applying the process to a new yet similar question.
  For instance for a paper contributing data analysis method, applying it
  to new data.

.. container:: align-right

   Reusability is more valuable than reproducibility.

Reproducibility without reusability in method development may hinder the
advancement of science as it pushes people to do all the same
things, *eg* always running experiments on the same data.

Reusability enables results that the original investigator did not have in
mind. It implies that the experimental protocol extends further than the
exact scope of the question initially asked. For software development, it
is also harder, as it implies more robustness and flexibility.

Finally sharing source code is not enough: **readability** of the code is
necessary.

|

Roadblocks to reproducible science
====================================

Man power
----------

Reusability, readability, support of released code, all actually take a
lot of time, even though it is seldom acknowledged in talks about
reproducible science. Given a fixed man power, it is impossible to
achieve reusability and high quality for everything.

Computing power
----------------

Some numerical experiments or complex data analysis require weeks of
cluster to run. These will be much harder to reproduce. Also, rerunning
an analysis from scratch on a regular basis is a good recipe to achieve a
robust path from data to results. The more computing power is a limiting
resource, the more likely it is that a glitch is not detected.

Data availability
------------------

No access, or restricted access, to data is a show stopper for
reproducibility. Data sharing requirements are becoming common --from
funding agencies, or journals. However, privacy concerns, or confidential
information get in the way of making data public, for instance in medical
research or micro-economy. Often, these concerns serve as a pretext
to people who actually do not want to relinquish *control* [#]_.

.. [#] A related post by Deevy Bishop: `Who's afraid of open data
   <http://deevybee.blogspot.co.uk/2015/11/whos-afraid-of-open-data.html?m=1>`_


Incentives problem
-------------------

Fancy new results are what matters for success in academia. "High impact"
journals such as Nature or Science accept papers that amaze and impress,
often with subpar inspection of the materials and methods [#]_. The rate of
publication in many leading groups is incompatible with consolidation
efforts required for strong reproducibility.

On the other hand, it is hard to tell beforehand if a new idea is a good
one. Hence letting imagination forward to foster impossible and
improbable ideas is a good path to innovation. The underlying questions
are: What are the best community rules for the advancement of knowledge?
What do we want from the way science moves forward? Rapid publication of
many incremental ideas, *eg* at a conference, gives food for thoughts,
possibly at the sake of reproducibility.

.. [#] "Science, Nature and Cell, had a higher rate of retractions" --
   `Wikipedia: Invalid science <https://en.wikipedia.org/wiki/Invalid_science>`_

|

How to improve the situation
=============================

Docker, containers, and virtual machines
-----------------------------------------

Docker, or other virtual machine technologies, enable shipping a software
environment. It diminishes the challenges of building software and
setting up an analysis. Virtual machines are used as a way to avoid
software packaging issues. This seems to me as a plaster on a wooden leg.

.. container:: align-right

    Containers give easy reproduction, to the cost of hard
    replication and reuse.

Indeed, an analysis that lives in a box can be reproduced, but can it be
understood, modified, or applied to new data? New science is likely going
to come from modifying this analysis, or combining it with other tools,
or new data. If these other tools live in a different virtual machine,
the combination will be challenging.

In addition, people are using containers as an excuse to avoid tackling
the need for proper documentation of requirements, and the process to set
them up. They sometimes even try justify binary blobs [#]_. This is
wrong. An analysis should be runnable without requiring the stars to
align, and it should be understandable.

.. [#] See also Titus Brown's post: `The post-apocalyptic world of binary
   containers <http://ivory.idyll.org/blog/2014-containers.html>`_


Version control: wear your seatbelt
------------------------------------


`Version control
<https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control>`_
is like a time machine: if used with regular commits, it enables rolling
back to any point in time. For my work, it's always been a crucial aspect
to reproducing what me or my students did a while ago. I often meet
researchers that feel they lack time to learn it. I really cannot support
this position. http://try.github.io is an easy way to learn version
control.

*Hint*: use a "tag" to pin-point a position in the history that you might
want to repeat, such as making a figure or the publication of an article.

Sotware libraries, curated and maintained
------------------------------------------

Consolidating an analysis pipeline, a standard visualization, or any
computational aspect of a paper into a software library is a sure way to
make the paper more reproducible. It will also make the steps reusable,
and a replication easier. If continued effort is put in the library,
chances are that computational efficiency will improve over time, thus
helping in the long run with the challenge of computing power.

.. container:: align-right
   
   Tough choices: not every variant of an analysis can be forever
   reproducible.

Maintaining the library will ensure that results are still reproducible
on new hardware, or with evolution of the general software stack (a new
Python or Matlab release, for instance). Documentation and curated
examples will lower the bar to reuse and facilitate replication of the
original scientific results.

To avoid feature creep and technical debt, a library calls for focused
efforts on selecting the most important operations.


Datasets, serving as model experiments, tractable and open
-----------------------------------------------------------

Sometimes researchers create a toy data, with a well-posed question, that
is curated and open, small enough to be tractable yet large enough to be
relevant to the application field. This is an invaluable service to the
field. One example is the `netflix prize
<https://en.wikipedia.org/wiki/Netflix_Prize>`_ in machine learning,
which led to a standard dataset. Unfortunately, the dataset was taken
down some years later due to copyright concerns. But it has been
replaced, *eg* by the `movielens dataset
<http://grouplens.org/datasets/movielens/>`_. For computer vision, a
series of datasets --`Caltech101
<http://www.vision.caltech.edu/Image_Datasets/Caltech101/>`_, `CIFAR
<https://www.cs.toronto.edu/~kriz/cifar.html>`_, `ImageNet
<http://www.image-net.org/>`_...-- have led to continuous progress of the
field. In bioinformatics, standard data are regularly created, for
instance by the `DREAM challenges <http://dreamchallenges.org/>`_.

These reference open datasets serve as benchmarks and therefore foster
competition. They also define a canonical experiment, helping a wider
scientific community understand the questions that they ask. Ultimately,
they result in better software tools to solve the problem at hand, as
this problem becomes a standard example and application of tools.

`Sage bionetworks <https://en.wikipedia.org/wiki/Sage_Bionetworks>`_, for
instance, is a non-profit that collects and make biomedical data 
available. These people believe, as I do, that such data will lead to
better medical care.

Changing incentives: setting the right goals
---------------------------------------------

Making sustainable, quality scientific work that facilitates reproduction
needs to be a clearly-visible benefit to researchers, young and senior.
Such contributions should help them get jobs and grants.

An unsophisticated publication count is the basis of scientific
evaluation. We need to accept publications about data, software, and
replication of prior work in high-quality journals. They need to be
strictly reviewed, to establish high standards on these contributions.
This change is happening. `Gigascience
<http://www.gigasciencejournal.com/>`_, amongst other venues, publishes
data. The `MLOSS (machine learning open source software) track
<http://jmlr.org/mloss/>`_ of the JMLR (journal of machine learning
research) publishes software, with a tough review on the software quality
of the project.

.. container:: align-right

    Researchers should cite the software they use.

Yet software is still often under cited: many will use a software
implementing a method, and only cite the original paper that proposed the
method. Another remaining challenge is: how to give credit for continuing
development and maintenance.

Fast-paced science is probably useful even if fragile. But the difference
between a quick proof of concept and solid, reproducible and reusable
work needs to be acknowledged. It is important to select for publication
not only impressive results, but also sound reusable material and
methods. The latter are the foundation of future scientific developments,
but high-impact journals tend to focus on the former.

|

.. topic:: **Related posts**:

  * `Software for reproducible science: let's not have a misunderstanding <software-for-reproducible-science-lets-not-have-a-misunderstanding.html>`_

  * `MLOSS 2015: wising up to building open-source machine learning <mloss-2015-wising-up-to-building-open-source-machine-learning.html>`_



