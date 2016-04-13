Interested in parallel computing and statistics? We are looking for a post-doc
##############################################################################

:date: 2011-01-30 22:30
:tags: jobs, python, science, scientific computing

`My research group`_ is kick starting a new project, called
**AzureBrain** to do computational analysis of large brain imaging and
genetics population-wise data. One of the goals of the project is to
harness the power of grid computing to do statistical learning on fMRI
data, finding features in an individuals brain images that can be
predicted by his genome. The medical applications cover the wide scope
of genetically-related brain pathologies, such as autism.

Want to work in a dynamic and exiting environment, using Python to solve
challenging data analysis? We are looking for a post-doctoral fellow to
hire in spring/beginning of summer. The ideal candidate would have a
strong background in computational statistics or machine learning, as
well as parallel computing, however we will consider any candidate with
good experience in one or the other and a strong desire to learn.

You would be employed by `INRIA`_, the lead computing research institute
in France. We are a team of computer scientists specialized in image
processing and statistical data analysis, integrated in one of the top
French brain research centers, `NeuroSpin`_, south of Paris. We work
mostly in Python. The team includes core contributors to the
`scikit-learn project`_, for machine learning in Python, and the `nipy
project`_, for NeuroImaging in Python.

Below follows a summary of `the official job announcement`_. Please
contact Bertrand Thirion, (first name \_dot\_ last name \_at\_ inria
\_dot\_ fr) if you are interested, referencing the AzureBrain project.

--------------

Introduction
------------

Imaging genetic studies linking functional MRI data and Single
Nucleotide Polyphormisms (SNPs) data face a dire multiple comparisons
issue. In the genome dimension, genotyping DNA chips allow to record of
several hundred thousands values per subject, while in the imaging
dimension a brain image may contain 100k-1M voxels. Finding the brain
and genome regions that may be involved in this link entails a huge
number of hypotheses, hence a drastic correction of the statistical
significance of pairwise relationships, which in turn reduces crucially
the sensitivity of statistical procedures that aims at detecting the
association. It is therefore desirable to set up as sensitive techniques
as possible to explore where in the brain and where in the genome a
significant link can be detected, while correcting for family-wise
multiple comparisons (controlling for false positive rate). Another
issue is the computational cost of these procedures, that need to be
addressed with adequate algorithmic and computational tools.

Objectives
----------

In this project, we will consider a unique dataset acquired in the
`Imagen project`_, an FP6 project that aims at investigating factors of
addition in a population of adolescents; Imagen’s database contains
multi-modal neuroimaging as well as genetics and psychological data on
about 2000 subjects. This database is hosted and processed at Neurospin
and is available for research purpose. The candidate will be in charge
of:

-  Setting an analysis pipeline (based on code already available to
   analyze neuroimaging/genetics datasets) to extract and pre-process
   the relevant data for statistical analysis.
-  Performing statistical analysis on simulated datasets and sub-parts
   of the whole database in order to set all the computational
   framework. These procedures will include mass-univariate linear
   modeling (with peak- and cluster-level tests), regularized multiple
   regression and a permutation-based assessment framework.
-  Launch data analysis on a large scale grid and cloud environment,
   with the help of the Kerdata researchers (see below).
-  Build the post-analytic framework to ease the interpretation of the
   results in both neuroimaging and genetics domains.

The analysis framework is based on algorithmic tools developed in
C/Python (numpy, scipy and scikit-learn). The candidate will interact i)
with researchers of the Parietal team for algorithmic aspects, but also
ii) with CEA researchers of Neurospin, who will provide expertise in
genetics domain and iii) with the KerData team (INRIA Rennes) and the
Joint MSR-INRIA Research Center (Microsoft Research), that will provide
help and massive computation facilities. The project has an access to
grid/cloud computing facilities to be used in collaboration with
INRIA/Kerdata and MSR-INRIA partners.

The expected results is the discovery of correlation between brain
activation and genetic information.

Required knowledge and background
---------------------------------

The candidate should have at least a basic knowledge of standard
statistical concepts. He or she should have a first significant
experience in parallel computation and with python language. It is
important that he or she has some real interest in genetics and/or brain
imaging in order to have strong interactions with specialists of these
domains. He or she will benefit from the algorithmic tools developed at
Parietal and of the database settings and data pre-processing tools
developed by Neurospin researchers.

.. _My research group: https://parietal.saclay.inria.fr/
.. _INRIA: http://www.inria.fr
.. _NeuroSpin: http://www-dsv.cea.fr/en/instituts/institut-d-imagerie-biomedicale-i2bm/services/neurospin-d.-le-bihan
.. _scikit-learn project: http://scikit-learn.sourceforge.net/
.. _nipy project: http://nipy.sourceforge.net/
.. _the official job announcement: http://parietal.saclay.inria.fr/open-positions/azure-brain-post-doc-proposal
.. _Imagen project: http://www.imagen-europe.com
