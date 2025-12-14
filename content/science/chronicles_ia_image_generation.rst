============================
How do AI generate images?
============================

:date: 2025-10-14
:tags: science, research, AI, chronicle, AI chronicle
:status: draft

.. image:: ../science/attachments/robot_painting.jpg
   :align: right
   :scale: 15 %
   :class: small
   :alt: Image generated with Mistral, with the prompt "Please generate an image of a cute robot painting a picture"

In a blink, generative AI creates images from just a few words. What are the mechanisms behind this apparent magic?


.. note::

   This post was originally published in French as part of my scientific
   chronicle in the print version of *Les Echos*.


How can an AI generate images from words? If you try doing this yourself,
with a pencil or brush, you immediatly feel the complexity of image
creation. If an AI can do it, it’s because it has seen a vast number of
images paired with associated words. The fundamental building block of
image synthesis boils down to the following task: given a collection of
images associated with a specific word, how to create new images that
appear to belong to the original collection?

Say, for instance, that I want to create images of cats. If I simply
overlay a few cat images downloaded from the internet, I won’t get a
realistic-looking cat image, as illustrated by the figure below. Indeed,
in the original images, cats vary in color, size, and posture. Combining
these images --whether by semi-transparent overlay or by patching
together sections-- isn’t straightforward. A given image comes with
coherence across different spatial scales.

.. figure:: attachments/average_cat_image_with_checkboard.jpg

   Left: average of 20 cat images downloaded from Internet -- Right: a
   view of 4 of these images

Digital images are made up of tiny colored dots arranged on a
grid: pixels. But we cannot reason at the pixel level by taking one pixel
from one image and its neighbor from another. If you were to draw a cat,
you probably wouldn’t start with the details but with the general
outlines. Moreover, the semantic content of an image doesn’t change if a
part of it is shifted by a pixel or two. To manipulate and generate
images, we use convolutional networks --functions that represent
information across neighborhoods of pixels in a way that is invariant to
small shifts. A pyramid of such functions, applied sequentially, captures
different scales.

To create a machine that generates images from a collection, we start by
training a convolutional network to transform each image into a kind of
QR code. This code describes the information in the original image but
has lost all spatial structure. We then reverse the transformation, going
from the QR code back to images. We generate new images simply by
providing new QR codes. If our transformation has captured well the
particularities of the original collection, the new images will remain
faithful to it.

|

Modern models use more complex functions than convolutional networks,
capable of transforming --and even partially memorizing-- parts of images.
These internal representations give them incredible semantic richness,
enabling them to generate fictional people in the style of an artist like
Van Gogh, for example. However, as a result, they may retain elements of
the original training images, sometimes producing images that closely
resemble the works of known artists. This raises questions about
attribution and intellectual property.

Finally, image generation models consume a lot of energy. Creating a
single image, for instance, could drain a smartphone battery, though we
do not realize it, as the process is typically done in the cloud.

|

.. topic:: AI chronicles

    Find all my AI chronicles `here <https://gael-varoquaux.info/tag/ai-chronicle.html>`_

    The goals of these "AI chronicles" is to introduce concepts of AI to a broader public, staying at a very very high level.

