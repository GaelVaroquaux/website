==================================================================
MLOSS 2015: wising up to building open-source machine learning
==================================================================

:date: 2015-11-28
:tags: conferences, science, software, machine learning, reproducible research, scientific software

.. |nbsp| unicode:: U+00A0

.. note::

   *The 2015 edition of the machine learning open
   source software (MLOSS) workshop was full of very mature discussions
   that I strive to report here.*
   
   *I give links to the videos. Some machine-learning researchers have
   great thoughts about growing communities of coders, about code as a
   process and a deliverable.*

I was a co-organizer of the `MLOSS 2015 workshop
<https://mloss.org/workshop/icml15/>`_, held during `ICML 2015
<http://icml.cc/2015/>`_. As I have finally figured out where the
videos are, now is a good time to summarize my impressions on the
workshop.

.. image:: attachments/mloss/mloss_t_shirt_white.png
   :width: 100%

Online videos of the talks
===========================

.. sidebar:: Graphics & T-shirts
   :class: small

   The graphics were printed on T-shirts. We ran out, but the material is
   `here <attachments/mloss/mloss_t_shirt_graphics.zip>`_ for you to
   print.

   *Anyone wants to help making an online T-shirt ordering?*

The videos of all the talks are online:

* `Python and Parallelism or Dask
  <http://k4webcast.mediasite.com/Mediasite/Play/4216268dc28148c89d8b6e4eba1ad6e51d>`_
  by *Matthew Rocklin*

* `Collaborative filtering via matrix decomposition in mlpack
  <http://k4webcast.mediasite.com/Mediasite/Play/afe6f76b3bb1452790fc8982e28112641d>`_
  by *Ryan Curtin*

* `BLOG: a probabilistic programming language for open-universe contingent
  Bayesian networks
  <http://k4webcast.mediasite.com/Mediasite/Play/9cd947554ddf404b9a40ca2601e44b4c1d>`_
  by *Yi Wu*

* `Spotlights 
  <http://k4webcast.mediasite.com/Mediasite/Play/45c3bb312a37491dbce1af25f1aeba001d>`_:

  - Nilearn, machine learning for neuroimaging in Python (Alexandre
    Abraham)
  - KeLP: a Kernel-based Learning Platform in Java (Simone Filice)
  - DiffSharp: Automatic Differentiation Library (Atılım Güneş Baydin)
  - The FAST toolkit for Unsupervised Learning of HMMs (José P.
    González-Brenes)
  - OpenML: a Networked Science Platform for Machine Learning (Joaquin
    Vanschoren)

* `Julia's Approach to Open Source Machine Learning
  <http://k4webcast.mediasite.com/Mediasite/Play/2529ebcb20794942874d5c277c5dcc981d>`_
  by *John Myles White*

* `Do it yourself deep learning with the Caffe community
  <http://k4webcast.mediasite.com/Mediasite/Play/da4f7869f07745f7bbc5a2e5f31761b61d>`_
  by *Evan Shelhamer*

* `From flop to success in academic software development
  <http://k4webcast.mediasite.com/Mediasite/Play/2bc15b283f324784a945d79d9a06c76c1d>`_
  by *Gaël Varoquaux*

MLOSS: a maturing community
=================================

.. Say that I was not enthousiastic, originaly, and say why (typical
   flaws of academic software)

When Antti Honkela and Cheng Soon Ong approached me to co-organize an
MLOSS workshop, I felt that it was important to do it for the sake of
open source scientific software. But it didn't feel very enthousiastic
about the event or the talks themselves. Boy I was wrong.

.. container:: align-right
    
    Huge attendance: open-source ML software is now mainstream.


My first MLOSS workshop was at the ICML 2011 conference, in Haifa. The
workshop was in a tiny cramped room, with a couple of dozens of geeks,
and it felt like a clique of people on the side of the conference. This
year, we had a huge room and more than 200 people showed up.

I am used to talks being about a grad student or young researcher that
has whiped the code of a paper on the web, with an open license but no
vision. This year, people were presenting actual projects, with long-term
goals and the desire to solve a problem large than their latest research.
It might explain why the attendance was huge: people came because talks
might genuinely help them.

|

With Cheng and Antti, we had choosen as a theme *"open ecosystems"*,
because ecosystems are the key to scaling computing and science. Between
us, imposing a theme on a workshop is something challenging, as people
submit abstracts, good or bad, and one has to compose with what one has.
However, at lot of talks mentioned how the projects slot in a wider
picture, and interact with a community. For instance, Evan attributes
part of the success of Cafe to the `"Model Zoo"
<https://github.com/BVLC/caffe/wiki/Model-Zoo>`_ in which the community
contributes fitted models. At the other end of the spectrum, OpenML is a
full online project with the goal to foster collaboration and comparison.
Project developers have shown in their talk that they are very conscious
of other projects that might be used together with their's.

Accepting the sustainability challenges
==========================================

Over the time, I have gradually realized the importance of community
building, *ie* project management and goal setting, more than technical
virtuosity. Historically, the scientific culture of code has put the
emphasis on the genius ideas behind the code, and the craftsmanship of
the implementation, to the cost of sustainability.

.. container:: align-right
    
    Alone, I go fast. Together, we go far.

I was surprised to see that the MLOSS community was growing very aware of
mechanisms of long-term project life, in particular the human factors. 

I was asked by my coorganizers to give `a talk on factors of success of
open source scientific software
<http://k4webcast.mediasite.com/Mediasite/Play/2bc15b283f324784a945d79d9a06c76c1d>`_.
I touched upon **software engineering**, **project vision**,
**licensing**, **governance**, **community building**. All these topics
deemed *"non scientific"* and thus so often despised and left out. I was
astonished to find out that the talks before me were giving very good
advice on these. I found that I only had to summarize and comment what
had been said before. This evolution of the scientific community makes me
very hopeful for the future.

.. epigraph::

    Every line of code you write is dept. You should be ashamed of every line
    of code you have written. [...]

    You have a supply of labor. These are the people who are contributors
    [...].
    The people who are users and not contributors are actually a source of
    demand [...] they mostly consume sources of labor rather than produce it. 
    |nbsp| |nbsp| |nbsp| ---  |nbsp| |nbsp| 
    `John Myles White
    <http://k4webcast.mediasite.com/Mediasite/Play/2529ebcb20794942874d5c277c5dcc981d>`_


|

.. topic:: **Thanks to our sponsors**

   `Facebook <http://www.facebook.com>`_ and `continuum
   <http://www.continuum.io>`_ sponsored the trip for our keynote
   speakers. Thank you very much, the keynotes were great!
   
   The `Paris-Saclay Center for Data Science (CDS)
   <http://www.datascience-paris-saclay.fr/>`_ gave us our main operating
   fund, which is critical for organizing an event. In general, I must
   say that the CDS has been hugely supportive of open source data
   science in the Paris area, having a significant impact on training as
   well as development.

   And also, I must acknowledge support from `Inria
   <http://http://www.inria.fr/>`_ for the accounting and administration
   of the event.

   Finally, **our reviewers were amazing**. Most of them reviewed the
   project, ie its code, its documentation, its support. They arose above
   the typical petty fights that we see in academia and focused on what
   the project was bringing to the scientific community. Often there
   reviews were longer and with more information than the abstract
   submitted.
   

|

.. topic:: **Related posts**:

  * `Software for reproducible science: let's not have a misunderstanding <software-for-reproducible-science-lets-not-have-a-misunderstanding.html>`_

  * `Publishing scientific software matters <../science/publishing_scientific_software_matters.html>`_


