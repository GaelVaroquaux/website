Nilearn sprint: hacking neuroimaging machine learning
------------------------------------------------------

:date: 2015-08-04
:tags: neuroimaging, python, scientific computing, scipy


A couple of weeks ago, we had in Paris the second international `nilearn
<http://nilearn.github.io>`_ sprint, dedicated to making **machine learning
in neuroimaging easier and more powerful**.

It was such a fantastic experience, as nilearn is really shaping up as a
simple yet powerful tool, and there is a lot of enthusiasm. For me, this
sprint is a turning point, as I could see people other than the original
core team (that spanned out of `our research team
<https://team.inria.fr/parietal/>`_) excited about the project's future.
Thank you to all who came:


.. class:: columns

  * Ahmed Kanaan
  * Andres Hoyos Idrobo
  * Alexandre Abraham
  * Arthur Mensch
  * Ben Cipolli (remote)
  * Bertrand Thirion
  * Chris Filo Gorgolewski
  * Danilo Bzdok
  * Elvis Dohmatob
  * Julia Hutenburg
  * Kamalaker Dadi
  * Loic Esteve
  * Martin Perez
  * Michael Hanke
  * Oscar Nájera, working on
    `sphinx-gallery <http://sphinx-gallery.readthedocs.org/>`_

.. image:: attachments/nilearn_july_2015_sprint/nilearn_sprint.jpg
    :width: 100%

The sprint was a joint sprint with the `MNE-Python
<http://martinos.org/mne/stable/mne-python.html>`_ team, that makes MEG
processing awesome. We also need to thank `Alex Gramfort
<http://alexandre.gramfort.net>`_, who did most of the work to set up the
sprint, as well as `NeuroSaclay
<https://www.universite-paris-saclay.fr/en/research/project/lidex-neurosaclay>`_
for funding, and `La paillasse <http://lapaillasse.org/>`_, `Telecom
<http://www.telecom-paristech.fr>`_, and `INRIA
<http://www.inria.fr/en/centre/saclay>`_ for hosting.

Highlights of the sprints results
==================================

**Plotting of multiple maps**

  .. image:: attachments/nilearn_july_2015_sprint/plot_canica_resting_state_001.png
    :align: right
    :width: 200px
    :target: https://circle-artifacts.com/gh/nilearn/nilearn/128/artifacts/0/home/ubuntu/nilearn/doc/_build/html/auto_examples/connectivity/plot_canica_resting_state.html

  A function to visualize overlays of various maps, eg for a
  probabilistic atlas, with defaults that try to adapt to the number of
  maps (see the `example
  <https://circle-artifacts.com/gh/nilearn/nilearn/128/artifacts/0/home/ubuntu/nilearn/doc/_build/html/auto_examples/manipulating_visualizing/plot_prob_atlas.html>`__).
  It's very useful for example for `easy visualizing of ICA components
  <https://circle-artifacts.com/gh/nilearn/nilearn/128/artifacts/0/home/ubuntu/nilearn/doc/_build/html/auto_examples/connectivity/plot_canica_resting_state.html>`_.

**Sign of activation in glass brain**

  .. image:: attachments/nilearn_july_2015_sprint/plot_demo_glass_brain_extensive_005.png
    :align: right
    :width: 200px
    :target: https://circle-artifacts.com/gh/nilearn/nilearn/287/artifacts/0/home/ubuntu/nilearn/doc/_build/html/auto_examples/manipulating_visualizing/plot_demo_glass_brain_extensive.html

  Our glass brain plotting was greatly improved adding amongst other
  things the option to capture the sign of the activation in the color
  (see this `example
  <https://circle-artifacts.com/gh/nilearn/nilearn/287/artifacts/0/home/ubuntu/nilearn/doc/_build/html/auto_examples/manipulating_visualizing/plot_demo_glass_brain_extensive.html>`__).

**Spatially-regularized decoder**

  .. image:: attachments/nilearn_july_2015_sprint/plot_haxby_space_net_002.png
    :align: right
    :width: 200px
    :target: https://circle-artifacts.com/gh/nilearn/nilearn/287/artifacts/0/home/ubuntu/nilearn/doc/_build/html/auto_examples/decoding/plot_haxby_space_net.html

  Decoders based on GraphNet and total variation have finally landed in
  nilearn. This has required a lot of work to get fast convergence and
  robust parameter selection. At the end of the day, it is much slower
  than an SVM, but the maps look splendid
  (see this `example
  <https://circle-artifacts.com/gh/nilearn/nilearn/287/artifacts/0/home/ubuntu/nilearn/doc/_build/html/auto_examples/decoding/plot_haxby_space_net.html>`__).

**Sparse dictionary learning**

  .. image::
     attachments/nilearn_july_2015_sprint/plot_dict_learning_resting_state_001.png
    :align: right
    :width: 200px
    :target: https://circle-artifacts.com/gh/nilearn/nilearn/282/artifacts/0/home/ubuntu/nilearn/doc/_build/html/auto_examples/connectivity/plot_dict_learning_resting_state.html

  We have almost merged sparse dictionnary learning as a alternative to ICA.
  Experience shows that on resting-state data, it gives more contrasted
  segmentation of networks
  (see this `example <https://circle-artifacts.com/gh/nilearn/nilearn/282/artifacts/0/home/ubuntu/nilearn/doc/_build/html/auto_examples/connectivity/plot_dict_learning_resting_state.html>`__).


**New installation docs**

  New webpage layout using tabs to display only the installation
  instruction relevant to the OS of the user (see `here
  <https://circle-artifacts.com/gh/nilearn/nilearn/287/artifacts/0/home/ubuntu/nilearn/doc/_build/html/introduction.html#installation>`_).
  The results are more compact and more clear instructions, that I hope
  will make our users' life easier.


**CircleCI integration**

  We now use `CircleCI <https://circleci.com/gh/nilearn/nilearn>`_ to 
  run the examples and build the docs. This is challenging because our
  examples are real cases of neuroimaging data analysis, and thus require
  heavy datasets and computing horse power.

**Neurodebian packaging**

  There are now `neurodebian packages
  <http://neuro.debian.net/pkgs/python-nilearn.html>`_ for nilearn.

And much more!

.. warning::

   Features listed above are **not** in the released version of nilearn.
   You need to wait a month or so.



