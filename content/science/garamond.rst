
==========================================
Garamond fonts for LaTeX
==========================================

:date: 2006-10-01
:tags: latex, publishing, sticky, selected
:summary: An easy to install version of Garamond fonts for LaTeX

`Garamond fonts <http://en.wikipedia.org/wiki/Garamond>`_ are a large
family of fonts. At a friend's request I modified the `URW-garamond
<ftp://dante.ctan.org/tex-archive/fonts/urw/garamond/>`_ fonts to improve
kerning, add old style numbers, and make some letters prettier. These
fonts are available under the `Aladdin Free Public License
<http://www.cs.wisc.edu/~ghost/doc/cvs/Public.htm>`_ , which states, if I
understand it correctly, that you can use and modify the fonts freely for
non commercial purposes.

Here is `a pdf file <attachments/baudelaire.pdf>`_ that gives an example
of the fonts.

.. topic:: Questions and suggestions

   I made this font in 2006. Time has passed, and I have completely
   forgotten the skills required to modify it. I cannot go anywhere
   beyond providing the file for download. Sorry, if you send me a kind
   email mentionning that the accents or the numbers are not right, I am
   unable to address it.

Instructions for use with pdfLaTeX
----------------------------------

The standard procedure for installing new fonts in a LaTeX installation
is quite complicated and varies from one LaTeX distribution to another.

I strongly suggest that you install the fonts only in your documents
folder. This make your document portable: as long as you give the
complete folder to your colleagues, they will be able to compile it.

If you want to install the fonts in the TeXMF (so that all documents
compiled on your installation have access to the fonts) I assume you know
TeX well enough to perform the installation without further help.

Installing in the current folder
=================================

Here is an easy way to install the fonts in your document's folder (this
will only work if you are using pdfLaTeX):

`Here <attachments/garamond.zip>`_ is a package to use these fonts with LaTeX. 

Unzip *garamond.zip* in the same folder than the LaTeX document you
are working on.


Using in a LaTeX document
==========================

In your LaTeX file, include the package "garamond":

.. code-block:: latex

    \usepackage{garamond}

You also need to use the T1 font encoding: 

.. code-block:: latex

    \usepackage[T1]{fontenc}

The garamond package defines a new command ``\garamond`` that switches
the font in the current group to garamond. Here is a minimal example:

.. code-block:: latex

    \documentclass{article}

    \usepackage[T1]{fontenc}
    \usepackage{lmodern}
    \usepackage{garamond}

    \begin{document}

    {\garamond
    The Quick Brown Fox Jumps Over The Lazy Dog. 0123456789 \\
	{\slshape This is garamond slanted} \\
	{\bfseries This is garamond bold face} \\
	{\scshape This is in small caps} \\
	{\slshape \bfseries This is slanted and bold face} \\
    }
    And this is written with the latin modern fonts.

    \garamond

    Here we switch to garamond.
    \ungaramond

    Here we switch back to the default.

    \end{document}

.. image:: attachments/minimal.png
    :alt: minimal example of a LaTeX file using garamond fonts
    :align: center

One remark on this example: you should never, ever, use the standards
out-of-the-box T1 fonts with pdfLaTeX, they look ugly. Always include the
"lmodern" or "pslatex" package, that uses much better postscript fonts.

