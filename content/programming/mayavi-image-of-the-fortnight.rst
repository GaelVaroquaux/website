Mayavi image of the fortnight
#############################

:date: 2009-01-25 19:21
:tags: python, science, mayavi

It's been two weeks since I posted a 'Mayavi image of the week'. Prabhu
has made a really cool example of integrating trajectories in a 3D
vector field, using, of course, the `Lorenz equation <http://en.wikipedia.org/wiki/Lorenz_system>`_ for the 3D field.
With nice colors, it makes a new fantastic image:

.. image:: {filename}attachments/lorentz_mayavi.png

The green surface represented is an isosurface of the z component of the
vector field: on this surface, the z-component changes sign. This can be
seen from the trajectories, as they start going up once they pass the
surface. The script generating this image is checked in as an example:
https://svn.enthought.com/enthought/browser/Mayavi/trunk/examples/mayavi/lorenz.py

