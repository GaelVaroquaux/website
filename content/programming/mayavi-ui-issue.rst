Mayavi UI issue
###############

:date: 2009-02-18 09:25
:tags: mayavi, scientific computing

I have been wanting to change slightly the design of a Mayavi dialog for
a while. Here is the issue: when you create a visualization, eg throught
the command line in `IPython`_, whith `mlab`_, you get a nice and small
window with only your visualization, and a toolbar. If you want to
change the properties of the objects on the visualization, or add some
more, you need to click on a button on the toolbar, which displays a
dialog, from which you can open more dialogs to edit the objects:

.. image:: http://gael-varoquaux.info/blog/wp-content/uploads/2009/02/mayavi_old_ui.png
   :target: http://gael-varoquaux.info/blog/wp-content/uploads/2009/02/mayavi_old_ui.png
   :align: center

I am thinking to changing this to a single dialog:

.. image:: http://gael-varoquaux.info/blog/wp-content/uploads/2009/02/mayavi_new_ui.png
   :target: http://gael-varoquaux.info/blog/wp-content/uploads/2009/02/mayavi_new_ui.png
   :align: center

The single-object-editing dialogs could still be opened by
double-clicking on the pipeline.

I am not going to discuss why I believe the new version would be better
than the old one, because I do not want to bias people. However, I would
prefer not making the decision to change based only on my feelings. So I
ask everybody, users of Mayavi or not: what do you think is better? And
why? I will probably leave an option to have the old behavior, anyhow,
but the default is very important.

.. _IPython: http://ipython.scipy.org/
.. _mlab: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/mlab.html

