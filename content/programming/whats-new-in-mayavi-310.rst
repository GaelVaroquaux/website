What's new in Mayavi 3.1.0? 
############################

:date: 2008-12-11 00:56
:tags: scipy, mayavi, scientific computing

Mayavi 3.1.0 has just been released, and I think it is a fantastic
version. We are starting to be able to focus on the details and the
focus. In addition, we are getting user feedback, which helps identify
the pain points.

**Automatic scripting**

This is a huge deal! You now have a `record button`_ on the pipeline
view. In record mode, the modifications that you make to the objects
properties are recorded as valid Python lines: Mayavi tells you what are
the line of code to modify those properties or create new objects. I use
this a lot: I first build a skeletton of a visualization using `mlab`_
but when it comes to tuning parameters, I do it interactively, and
record.

**Much more testing**

We added a huge amount of testing (many thanks to Suyog who contribed
quite few). From an user's point of view this has two consequences. First
the code is more robust (for instance the mlab commands are more flexible
on the shape of the arguments passed in). Second the rendering part of
the Mayavi engine is well-separated from the algorithmes, which means
that the VTK algorithms `can now be used`_ easily to manipulate numpy
arrays through Mayavi.

**Two new mlab functions: barchart and triangular\_mesh**

Mlab has `two new functions`_: one to create nice bar chart, for 2D
histograms displayed in 3D, and one to build meshes defined from their
triangle.

**Control of the pipeline through mlab is easier and more robust**

As the mlab.pipeline is getting more usage, it is being ironed out. For
instance applying a module to a source object (may it be a Mayavi
source, or a vtk dataset) adds it automatically to the figure if it is
not already in it. Also, when adding an additional module on an existing
source, a new module manager (object controlling the colormap) is added
automatically if the colormaps or extents differ. Many modules take
keyword arguments to make common operations easier.

**IPython in Mayavi**

If you have a recent version of IPython installed (> 0.9), Mayavi will
use an IPython widget, instead of the vanilla pyshell.

**mlab.view has now a sensible behavior**

The mlab.view no longer gives a bad roll angle to the camera. This makes
it much easier to do animations during which the camera moves.

**Axes and outline extents**

mlab.axes and mlab.outline now adjust by default to the extents of the
object they are applied on. This removes a bad surprise for people having
tuned the scale of their visualization.

**enthought.tvtk.tools.visual in Mayavi**

enthought.tvtk.tools.visual can now be used inside Mayavi, to provide a
`visual-like`_ API in mayavi.

**Documentation has recieved some love**

Documentation has been added and completed, with a focus on making it
easier for the beginner to discover the features of Mayavi. We try more
and more to walk the user through complete usecases of Mayavi, in a
task-oriented documentation, such as in the introductory examples, or in
`case-studies`_.

**Two new sources**

There are two new sources that do not require data. The first creates
objects, such as an arrow, a cube, or a view of the earth, to be viewed
with a 'surface' module. The second creates image data, such as a disk,
or a 2d gaussian, or (my favorite) the Mandelbrot set. This can be
viewed with an ImageActor, or (even better) with a WarpScalar filter and
a Surface. These sources have been contributed by Suyog.

A word of thanks
================

I am sure I am going to forget some people here, but I'd like to thank a
lot those who have been helping us with getting Mayavi2 going. First of
all, Dave Peterson, who is doing the release management for ETS. This is
a lot of work, and we would never have frequent releases without him.
I'd also like to thank Suyog Jain, who contributed some code. This is
fantastic, and I am sure we are going to have more people contributing
improvements. Finally, I'd like to thank Pierre Raybault, of
Python(x,y), and Varun Hiremath, of Debian. Packaging is very important
to our users, and it is not a trivial piece of work... Hum, I almost
forgot Chris Casey. Chris has been updating the docs on the net and
making sure the docs build well. This is also very important, as the web
page is a major means of communication with our users.

.. _record button: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/automatic_scripting.html%20
.. _mlab: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/mlab.html
.. _can now be used: https://mail.enthought.com/pipermail/enthought-dev/2008-December/018935.html
.. _two new functions: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/mlab.html#d-data
.. _visual-like: https://mail.enthought.com/pipermail/enthought-dev/2008-October/018402.html
.. _case-studies: http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/mlab.html#case-studies-of-some-visualizations
