Survey of machine-learning experimental methods at NeurIPS2019 and ICLR2020
============================================================================


:date: 2020-01-20
:authors: Xavier Bouthillier & Gaël Varoquaux
:tags: science, research, machine learning, benchmarking, conferences, experimental methods
:status: draft

.. note::

   A simply survey asking authors of two leading machine-learning
   conferences a few quantitative questions on their experimental
   procedures.

How do machine-learning researchers run their empirical validation? In
the context of a push for improved reproducibility and benchmarking, this
question is important to develop new tools for model comparison. We ran a
simple survey asking to authors of two leading conferences, NeurIPS 2019
and ICLR 2020, a few quantitative questions on their experimental
procedures.

A `technical report on arxiv <http://arxiv.org/>`_ summarizes our
finding. It gives a simple picture of how hyper-parameters are set, how
many baselines and datasets are included, or how seeds are used.
Below, we give a very short summary, but please read (and cite) `the full
report <http://arxiv.org/>`__ if you are interested.

|

**Highlights**
The response rates were 35.6% for NeurIPS and 48.6% 334
for ICLR.
A vast majority of empirical works optimize model hyper-parameters,
thought almost half of these use manual tuning and most of the automatic
hyper-parameter optimization is done with grid search. The typical number
of hyper-parameter set is in interval 3-5, and less than 50 model fits
are used to explore the search space. In addition, most works also
optimized their baselines (typically, around 4 baselines).

Finally, studies typically reported 4 results per model per task to provide a measure of variance, and around 50% of them
used a different random seed for each experiment.

**Sample results**

.. class:: side-caption

  .. figure:: ../science/attachments/survey_of_ml_experimental_methods/hyper_parameter_optimization.png
   :align: center
   :width: 400px

   How many papers with experiments optimized hyperparameters.

  .. figure::
   ../science/attachments/survey_of_ml_experimental_methods/tuning_methods.png
   :align: center
   :width: 400px

   What hyperparameter optimization method were used.

  .. figure::
   ../science/attachments/survey_of_ml_experimental_methods/number_datasets.png
   :align: center
   :width: 400px

   Number of different datasets used for benchmarking.

  .. figure::
   ../science/attachments/survey_of_ml_experimental_methods/number_seeds_or_trials.png
   :align: center
   :width: 400px

   Number of results reported for each model (ex: for different seeds)

These are just samples. Read `the full report <http://arxiv.org>`_ for
more results.

|

For reproducibility and AutoML, there is active research in benchmarking
and hyperparameter procedures in machine learning. We hope that the
survey results can help inform this research. As this document is merely
a research report, we purposely refrained from too much interpretation of
the results. However, trends that stand out to our eyes are, *1)* the
simplicity of hyper-parameter tuning strategies (mostly manual search and
grid search) and *2)* the small number of model fits explored during this
tuning (often 50 or less). These practices are most likely due to the
high computational cost of fitting modern machine-learning models.

**Acknowledgments** We are deeply grateful to the participants of
the survey who took time to answer the questions.

