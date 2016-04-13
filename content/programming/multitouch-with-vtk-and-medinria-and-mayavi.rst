Multitouch with VTK (and MedINRIA and Mayavi)
#############################################

:date: 2010-09-18 09:40
:tags: mayavi, python, scientific computing

If the videos on this post are not showing, click through to see
them.

A colleague of mine, `Pierre Fillard`_, has just integrated multitouch
in the next generation of the VTK-based medical imaging software
`MedINRIA`_. The nice thing is that it works on an Apple laptop out of
the box.

.. raw:: html

   <p>
   <object width="640" height="385">
   <embed src="http://www.youtube.com/v/UyO4KRnYreU?fs=1&amp;hl=en_US" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="640" height="385">
   </embed>
   </object>
   </p>

On `his blog`_, he explain how he did this (warning, it involves C++ and
VTK programming). **He also gives the code for this!** Enjoy.

This reminded me of when the `Enthought guys`_ had rigged up a large
multitouch screen and wired it in `Mayavi`_ for 3D plotting, and in
`chaco`_ for 2D plotting, using only a web-cam, a video projector, and
pure Python image-analysis code:

.. raw:: html

   <p>
   <object width="480" height="385">
   <embed src="http://www.youtube.com/v/bEf3nGjOgpU?fs=1&amp;hl=en_US" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="480" height="385">
   </embed>
   </object>
   </p>

.. _Pierre Fillard: http://sites.google.com/site/pierrefillard/
.. _MedINRIA: http://www-sop.inria.fr/asclepios/software/MedINRIA/
.. _his blog: https://sites.google.com/site/pierrefillard/coding-blog/multi-touchgesturesinvtk
.. _Enthought guys: http://www.enthought.com/
.. _Mayavi: http://code.enthought.com/projects/mayavi/
.. _chaco: http://code.enthought.com/projects/chaco/
