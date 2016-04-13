Scientific publication for software development
###############################################

:date: 2011-01-08 22:40
:tags: python, science, scientific computing, publishing

The academic community seems to judge the validity and significance of
any contribution by the number of papers published and the number of
citations they get. To find funding, to get credit, you have to
**publish or perish**. However, the natural output of software
development tends not to be an article (people who confuse articles and
documentation do a poor job of both, IMHO).

While I believe that this policy is harmful for the quality of research,
I also know that I cannot fight it, and chances are that many other are
in my situation. As such, we need to publish scientific papers about the
scientific softwares that we develop (such as `Mayavi`_, or
`scikit-learn`_, as far as I am concerned). On the other hand, as an
editor of the `Scipy conference proceedings`_, I have found that the
process of writing a paper on software work and going through peer
review can be greatly beneficial to the software. Indeed, it forces
authors to do a thorough review of the prior work, and to clearly
identify the purpose of the project. Also, such an article can only be
much shorter than a user manual, thus it forces the authors to identify
the key concepts of their software, and explain them clearly. As a
result, it helps finding design and usability flaws and gaining insight
on how the user manual can be structured.

A major challenge to publishing is that most of the highly-ranked
journals tend to disregard software works, unless they are very specific
to a scientific problem, which actually makes them less useful to the
complete ecosystem. Deeply rooted in the minds of the editors and the
reviewers, there tends to be the idea that developing software is easy
compared to doing experiments or proofs. In addition, these top-notch
scientists are not always the most qualified to judge the quality of
software, as they have most often never worked in a major software
project. The good news is that this is slowing changing with the
creation of software tracks in specialized journals, and the development
of new journals focused on scientific software.

Journals for publishing about interdisciplinary scientific software
-------------------------------------------------------------------

In my opinion, interdisciplinary scientific software such as `numpy`_,
the `GSL`_, `octave`_, `scilab`_, `matplotlib`_, or `Fenics`_, are the
most valuable projects, as they provide foundations to build science in
the open. The challenge that these projects have to face are not only
algorithmic or computational, but also deal with providing good user
interfaces, or developing and catering for very large communities of
users. These problems are considered as *solved* in a scientific
context, as they have all been solved at least once, often quite
successfully by commercial products such as Matlab. As a result, it is
hard to get some funding for these projects unless there is a political
reason behind the funding, and IMHO politics tend to produce bad
software. Publishing high-profile articles on interdisciplinary
scientific software is thus hard, but critical. For this we need
journals that accept software papers, but are not only read by
researchers in CS or IT departments.

A couple of years ago, some of us made a review of where it was possible
to publish truly wide-scope scientific software, and we found that there
was pretty much no option. It's crazy to see that things have still not
changed much, and that all lot of major general-purpose widely-used
projects, like the one I cited above, have never been acknowledged by a
publication.

-  `Computing in Science and Engineering`_: a joint publication
   between the AIP (American Institute of Physics) and the IEEE, it is a
   magazine-style journal and it can be seen in many coffee rooms of
   computational-science departments. Thanks to that it gets a lot of
   reading, but the articles cannot be too technical (which might be a
   good thing) and there is room for only few articles.
-  `Open Research Computation (ORC)`_: A newly-created journal, with
   a focus on making computational research reproducible. As such, it
   favors papers about open source scientific software with good
   software-engineering. **Open access**.

In addition to these software-friendly journals, some large-scope
journals on computational science sometime accept software papers,
though software production fall out of their scope:

-  `Journal of Computational Science`_: a very multidisciplinary
   journal.
-  `SIAM Journal on Scientific Computing (SISC)`_: a journal of the
   SIAM (society for industrial and applied mathematics), thus with a
   focus on engineering-type applications.

Journals for publishing domain-specific scientific software
-----------------------------------------------------------

It is usually easier to publish a domain-specific software contribution,
as you can claim that you have solved a well-identified scientific
roadblock. Until recently, it was hard to get such papers in the best
journals of a community, but things have been changing.

-  `Computer Physics Communications`_: for algorithms and packages
   solving numerical and computational problems related to physics.
-  `Bioinformatics`_: accepts software papers on biology-related
   problems.
-  `ACM Transactions On Mathematical Software (TOMS)`_: a journal of
   the ACM (Association for Computing Machinery), thus with a focus on
   algorithms.
-  `Journal of statistical Software`_: this journal comes from the
   community of people who wrote the R language. They know that open
   source scientific software is hard and important. **Open access**.
-  `Journal of Machine Learning Research (JMLR), Machine Learning Open
   Source (MLOSS) track`_: reference journal in the machine learning
   community, the MLOSS track cares strongly about documentation,
   packaging and usability of the software. **Open access**.
-  `Computers & Geoscience`_: computational geoscience journal that
   accepts software papers (thanks Michael Aye for the pointer).
-  `Computer Applications in Engineering Education`_: a journal
   about education with computers. AFAIK, no special focus on open
   source or software-engineering quality (thanks Doug Holton for the
   pointer).
-  `NeuroInformatics`_ and `Frontiers NeuroInformatics`_ (**open
   access**): two journals on computer-related issues in neuroscience
   that accept software papers. I have the feeling that the latter is a
   bit warmer to open source that the former (thanks Andrew Davison for
   the pointer).
-  `Computers and Electronics in Agriculture`_: for publishing
   agriculture-related software (thanks John B. Cole for the pointer).

I should stress that, in my opinion, journals such as `PLOS
computational biology`_, or the `Journal of Computational Physics`_, or
are not great venues for software papers, as they tend to emphasize what
I would call *proof of principle*, and not packaged and maintained
software.

**I have the feeling that there is need for more communication on
scientific software. The list above is, of course, incomplete. If you
have extra ideas, please do not hesitate to contact me.**

As a conclusion, I would like to point out that conferences are also a
good way to advertise scientific software. You may even get approached
by the editor of a journal to open the door for a journal article. Last
year I was at `ESCO`_, a coupled problems conference, and there was a
track on Python in science. All in all the conference was a huge amount
of fun, and I learned a lot on practical aspects of numerical methods,
given the amount of numerical computing geeks that were around. The same
community is organizing `FEMTEC`_ in Lake Tahoe (California) this year.
If you are in any field related to FEM or multiphysics, you should
consider it.

**Update: added links suggested by Doug Holton, Michael Aye, Andrew
Davison, and John B. Cole**

.. _Mayavi: http://code.enthought.com/projects/mayavi/
.. _scikit-learn: http://scikit-learn.sourceforge.net/
.. _Scipy conference proceedings: http://conference.scipy.org/proceedings.html
.. _numpy: http://numpy.scipy.org/
.. _GSL: http://www.gnu.org/software/gsl/
.. _octave: http://www.gnu.org/software/octave/
.. _scilab: http://www.scilab.org/
.. _matplotlib: http://matplotlib.sourceforge.net/
.. _Fenics: http://www.fenicsproject.org
.. _Computing in Science and Engineering: http://cise.aip.org/
.. _Open Research Computation (ORC): http://www.openresearchcomputation.com/
.. _Journal of Computational Science: http://www.elsevier.com/locate/jocs/
.. _SIAM Journal on Scientific Computing (SISC): http://www.siam.org/journals/sisc.php
.. _Computer Physics Communications: http://www.elsevier.com/locate/cpc
.. _Bioinformatics: http://bioinformatics.oxfordjournals.org/
.. _ACM Transactions On Mathematical Software (TOMS): http://toms.acm.org/
.. _Journal of statistical Software: http://www.jstatsoft.org/
.. _Journal of Machine Learning Research (JMLR), Machine Learning Open Source (MLOSS) track: http://jmlr.csail.mit.edu/mloss/
.. _Computers & Geoscience: http://www.elsevier.com/wps/find/journaldescription.cws_home/398/description#description
.. _Computer Applications in Engineering Education: http://onlinelibrary.wiley.com/journal/10.1002/%28ISSN%291099-0542
.. _NeuroInformatics: http://www.springer.com/biomed/neuroscience/journal/12021
.. _Frontiers NeuroInformatics: http://www.frontiersin.org/neuroinformatics
.. _Computers and Electronics in Agriculture: http://www.elsevier.com/wps/find/journaldescription.cws_home/503304/description#description
.. _PLOS computational biology: http://www.ploscompbiol.org
.. _Journal of Computational Physics: http://www.elsevier.com/wps/find/journaldescription.cws_home/622866/description#description
.. _ESCO: http://hpfem.org/events/esco-2010/
.. _FEMTEC: http://hpfem.org/events/femtec-2011/
