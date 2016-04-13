ICA versus PCA in the scikit-learn: the value of code over pictures
###################################################################

:date: 2010-11-20 16:12
:tags: python, science, scientific computing

When I was trying to get an intuitive feeling of the difference between
**Independent Component Analysis** (ICA) and **Principal Component
Analysis** (PCA), I wrote a few Python scripts producing `some
visualizations explaining the difference`_ that have had a bit of
success.

During the last sprint on `scikit-learn`_, a machine learning
toolkit in Python, we cleaned up the ICA code that I had been using, and
we added it to the scikit, along with `an example`_ inspired from this
earlier toy problem.

.. image:: http://scikit-learn.org/stable/_images/plot_ica_vs_pca.png
   :target: http://scikit-learn.org/stable/auto_examples/plot_ica_vs_pca.html
   :align: center

While the pictures are not as pretty as the initial ones I had done
(because we wanted to keep the example as simple as possible), I am very
happy that this discussion is know more than a set of static pictures,
but comes with runnable code.

This illustrates very well my feelings on the future of scientific code
and scientific research: paper, books, teaching materials, on numerical
methods or computational science are greatly enhanced when they come
with highly-readable code that illustrates their purpose, because the
reader can start asking questions to the algorithm. Hopefully, **the
documentation of scientific programming toolkits will become the
textbooks of tomorrow**. We still have a lot of work to.

____


It's funny, I just realized that my vision on software might have been
strongly influenced by the fact that my mother, a high-school math
teacher, spent endless nights when I was a teenager working on
`Geoplan`_, a software for teaching geometry by interaction with
figures.

.. _some visualizations explaining the difference: http://gael-varoquaux.info/scientific_computing/ica_pca/index.html
.. _scikit-learn: http://scikit-learn.sourceforge.net/
.. _an example: http://scikit-learn.sourceforge.net/auto_examples/plot_ica_vs_pca.html
.. _Geoplan: http://fr.wikipedia.org/wiki/G%C3%A9oplan


