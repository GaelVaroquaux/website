New Mayavi release
##################

:date: 2010-03-14 12:58
:tags: python, science, mayavi

A week ago, the Peter Wang released a new version of the `Enthought Tool
Suite (ETS)`_. With it came a new version of `Mayavi2`_.

Prabhu and I have been horribly busy we real life, and I had the bad
feeling that we were not giving enough love to Mayavi. I was surprised
when I put together the list of features and bugs fixes that went in
Mayavi for the last two releases. The full list can be found `in the
documentation`_.

Contributors
============

We are not being terribly good at tracking external ideas and patches,
so I hope that I haven't forgotten anybody, but I am very happy to say
that Prabhu and I have received a fair amount of help from non core
contributors:

-  Chris Colbert
-  Darren Dale
-  Dave Martin
-  Dave Peterson
-  Emmanuelle Gouillart
-  Erik Tollerud
-  Evan Patterson
-  Gary Ruben
-  Kyle Mandli
-  Michele Mattioni
-  Ondrej Certik
-  Ram Rachum
-  Robert Kern
-  Scott Warts
-  Suyog Jain

On top of these people, I wish to thank the people making sure that the
Mayavi packages are available in the different Linux distributions:
Varun Hiremath, Lev Givon, Andrea Colangelo, Rakesh Pandit, as well as
Pierre Raybault for integrating in `Pythonxy`_.

Important features added in 3.3.0
=================================

3.3.0 was released last fall. We had not compiled the list of changes at
the time, I am giving it here:

-  An `example gallery`_ in the documentation.
-  A `sync\_camera`_ helper function to synchronize camera between two
   scenes.
-  A `text3d`_ module, for position text in 3D that is scaled and hidden
   like a data object.
-  A `close`_ function to close scenes, similar to that in pylab or
   matlab.
-  A new filter to crop datasets: *DataSet Clipper*. This filter is
   terribly useful.
-  All the `mlab.pipeline`_ functions now take a *figure=* keyword
   argument. This is very useful when coding with several figures
   embedded in GUIs, as in a GUI you can't rely on a context. This is
   illustrated in this `example`_.

Important features added in 3.3.1
=================================

In latest release the following important features were added:

-  `mlab.savefig`_ can now reliably save images of a size larger than
   the window.
-  The interactive VTK documentation browser is now available in the
   GUI.
-  New functions added to `mlab`_ to control position of the camera:
   `move`_, `yaw`_, and `pitch`_. These complement the existing `view`_
   and `roll`_.
-  Make the lines smoother when using `mlab.plot3d`_ (use a VTK Stripper
   filter)
-  Add a `screenshot`_ function to mlab for easy screen capture as a
   numpy array. This is very useful when creating figures that combine
   3D using Mayavi and 2D using pylab. I use it all the time.
-  Add a `probe\_data`_ function to return the data values of Mayavi
   objects at given locations as numpy arrays. This is very useful to
   combine numerics with Mayavi.
-  Add a auto mode to `mlab.view`_ to compute position and distance
   based on the objects on the image.
-  Add a helper function to easily interact with the data: a callback
   can easily be registered to picking data with the mouse. `Two
   examples`_ illustrate this new functionality. This is a major step
   forward in making life easier for people using Mayavi to build custom
   interfaces.

.. _Enthought Tool Suite (ETS): http://code.enthought.com/
.. _Mayavi2: http://code.enthought.com/projects/mayavi/
.. _in the documentation: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/changes.html
.. _Pythonxy: http://pythonxy.com
.. _example gallery: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/examples.html
.. _sync\_camera: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_figure.html#sync-camera
.. _text3d: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_other_functions.html#text3d
.. _close: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_figure.html#close
.. _mlab.pipeline: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/mlab_pipeline_reference.html
.. _example: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/example_multiple_mlab_scene_models.html
.. _mlab.savefig: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_figure.html#savefig
.. _mlab: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/mlab.html
.. _move: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_camera.html#move
.. _yaw: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_camera.html#yaw
.. _pitch: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_camera.html#pitch
.. _view: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_camera.html#view
.. _roll: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_camera.html#roll
.. _mlab.plot3d: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_helper_functions.html#enthought.mayavi.mlab.plot3d
.. _screenshot: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_figure.html#enthought.mayavi.mlab.screenshot
.. _probe\_data: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_pipeline_data.html#probe-data
.. _mlab.view: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/mlab_camera.html#view
.. _Two examples: https://svn.enthought.com/enthought/browser/Mayavi/trunk/examples/mayavi/data_interaction/
