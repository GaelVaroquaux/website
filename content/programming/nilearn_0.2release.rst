Nilearn 0.2: more powerful machine learning for neuroimaging
==============================================================

:date: 2015-12-13
:tags: neuroimaging, python, scientific computing, scipy

.. sidebar:: Nilearn's goals 
   :class: small
   
   Make advanced machine learning techniques easy for neuroimaging
   research.


After 6 months of efforts, We just released version 0.2 of `nilearn
<http://nilearn.github.io>`_, dedicated to making **machine learning in
neuroimaging easier and more powerful**.

This release integrates the features of the `july sprint
<nilearn_july_2015_sprint.html>`_, and `more 
<http://nilearn.github.io/whats_new.html>`_.

Highlights
-----------

**Better documentation with narrative examples**

The example can now be broken down into blocks (as `here
<http://nilearn.github.io/auto_examples/connectivity/plot_signal_extraction.html#sphx-glr-auto-examples-connectivity-plot-signal-extraction-py>`_)
for a better narration (thanks to `sphinx-gallery
<http://sphinx-gallery.readthedocs.org/en/latest/>`_).

____

.. figure:: http://nilearn.github.io/_images/sphx_glr_plot_mixed_gambles_space_net_001.png
    :align: right
    :target: http://nilearn.github.io/auto_examples/decoding/plot_mixed_gambles_space_net.html

**Space net: spatial regularizations in decoding**

The `"SpaceNet" decoder
<http://nilearn.github.io/decoding/space_net.html>`_ does spatial
regularizations such as TV-l1 or Graph-Net to identify predictive regions
in decoding.

____

.. figure:: http://nilearn.github.io/_images/sphx_glr_plot_compare_resting_state_decomposition_002.png
    :align: right
    :target: http://nilearn.github.io/auto_examples/connectivity/plot_compare_resting_state_decomposition.html


**Dictionnary learning for resting-state parcellations**

Dictionnary learning is a `promising alternative to ICA to learn networks
<http://nilearn.github.io/connectivity/resting_state_networks.html#beyond-ica-dictionary-learning>`_.

____

.. figure:: http://nilearn.github.io/_images/sphx_glr_plot_prob_atlas_003.png
    :align: right
    :target: http://nilearn.github.io/auto_examples/manipulating_visualizing/plot_prob_atlas.html#sphx-glr-auto-examples-manipulating-visualizing-plot-prob-atlas-py

**Plotting sets of probabilistic maps**

With `a simple function
<http://nilearn.github.io/manipulating_visualizing/plotting.html#different-plotting-functions>`_,
you can plot outlines for multiple maps.

____

.. figure:: http://nilearn.github.io/_images/sphx_glr_plot_extract_rois_statistical_maps_003.png
    :align: right
    :target: http://nilearn.github.io/auto_examples/manipulating_visualizing/plot_extract_rois_statistical_maps.html
    
**Separating regions out of maps**

We have a set of functions to `separate regions on maps <http://nilearn.github.io/auto_examples/manipulating_visualizing/plot_extract_rois_statistical_maps.html>`_ or `turn networks into a probabilistic parcellation <http://nilearn.github.io/auto_examples/connectivity/plot_extract_regions_canica_maps.html>`_.

____

**Classification on connectomes**

We now have advanced connectivity measures to do `comparisons across
connectomes for classification
<http://nilearn.github.io/auto_examples/connectivity/plot_connectivity_measures.html>`_.

____

.. topic:: Thanks

    Thanks to Alexandre Abraham who lead the effort, and `all the
    contributors
    <http://nilearn.github.io/whats_new.html#contributors>`_.

