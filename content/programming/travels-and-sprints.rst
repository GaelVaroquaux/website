Of travels and sprints
######################

:date: 2008-04-01 02:13
:tags: scipy, scientific computing, conferences

This month I have traveled a bit for scientific-computing related
reasons.

In England
==========

First of all, I was speaking at the OKcon, `open knowledge conference`_
in London, about Scientific tools in Python in general, and Mayavi in
particular. I jumped on the occasion to visit the Airbus campus in
Bristol. We have had some contacts with these guys, because they use
Mayavi in some of their homegrown applications, and I was curious to put
faces on friendly names on the mailing list. In addition, I was eager to
find out how they were using Mayavi and Python scientific tools in an
industrial environment, as I have never worked in another place than a
physics lab.

Visiting the Airbus campus
--------------------------

The Airbus visit was enlightening: the Bristol campus is a major
research facility (several thousands people) dedicated to wing design. A
good part of the work is done through simulations deployed on big
clusters. These calculations have historically been run in Fortran and
C, but apparently the engineers are switching to a mix of compiled
languages and Python. Moreover, steering of these simulations, through
mesh-design, visualization of the results, analysis of the data, is done
mainly through an interact program, 'flightpad', that is developed fully
in Python, using the Envisage framework to couple together a bunch of
scientific components, including Mayavi. I got to spend a fair amount of
time with the guys doing this, and it was great to see how they did it.
They have a good approach to scientific software design (loosely coupled
components, reuse of all the existing libraries), eventhough their goal
(automatic generation of Python scripts from user interaction) is way
more ambitious than anything I have in mind. I was pleased to see that
they where using Mayavi in a way completely consistent with its design,
and did not have to hack around limitation.

It was really very encouraging to talk with the software strategist. He
obviously completely got it as far as how an open-source model can be
profitable to a company like Airbus. See so many people using open
source tools as their main tools, as well as a manager ready to back
this position, and explaining how it can be beneficial to contribute to
an open-source project, really filled me with hope.

Of course visiting the Airbus campus was not only about software, it was
also about planes (I got a drive around the campus, and it is quite fun
to ride a mini cooper between to 747), and beers (reinventing the world
to make it a better place at the pub, after work). I must say there is
something special about the scientific Python community, it is the
nicest community I know (with the sailing one :->). You meet people that
you have never seen before, and you immediately feel at ease.

Open Knowledge conference
-------------------------

The Open Knowledge conference was fun. Not too much like the geek
conferences I am used to, as here the focus was on the data, and not the
tools , aka the software (for instance, the big deal is when you can get
access to the complete public transport time-tables, and you can make
maps of poorly connected areas). I met `Martin Albrecht`_ from the `sage
project`_. It was very interesting to discuss with him. I generally
consider myself as doing rather fundamental research (Bose-Einstein
condensation), but for him I was in the applied science section, because
I use math and computers to do applied things. This distinction between
applied and fundamental maths yields a distinction in the application of
the code, and therefore the way an open-source scientific project can
survive. It was very interesting to see the way sage's development
process therefore differed from scipy's. I think that both Martin's talk
on sage, and mine on Python and interactive visualization had a lot of
success: the room was full of scholars, and they wanted tools to do
their work.

In London, I had the occasion to catch up with my brother, and Rob, a
former colleague. That was nice too (and yielded more beers).

Paris
=====

Nipy Sprint
-----------

The week after, I was attending a sprint in Paris on `nipy`_:
neuroimaging in Python. We were a bunch of enthusiastic scientific
Python users crammed in a small room during the day. There was the team
from Berkeley with including Jarrod and Fernando, and all their friends.
I got to make new friends, and catch up with old ones. The goal of the
nipy effort is to build a complete processing pipeline for neuroimaging
data, especially fMRI, in Python. This is a lot of work, as many
transformations are applied to the raw data to make it useful for
scientific publications. As the field matures, these transformations
pile up, and the processing pipeline gets more and more complex. There
already exists a good pipeline under MatLab (`SPM`_), the problem is
that, due to the poor language features of MatLab, it is a codebase hard
to extend and to modify. One of the goals of the nipy project is to make
a pluggable architecture, for researcher to be able to replace part of
the pipeline by their own code, and thus explore new methods while
comparing them to the reference one. This means that there are some
interesting software engineering problems in here (pluggable pipelines,
framework..., the kind of stuff I like), however the current focus is to
get the algorithms right, before trying to do software over-engineering.

The Berkeley group got an NSF grant to work on the project and has been
able to hire two developers for two years (Chris Burns and Tom Waite).
The effort is lead by Jarrod Millman, and they have put a lot of work in
making the underlying libraries better (that is improving numpy and
scipy).

I had difficulties contributing any useful code, as I don't know
neuroimaging, but I had the pleasure of seeing people pick up the mayavi
API and use it to quickly build domain-specific tools for displaying
brains and activation regions. As usual this also revealed some
shortcomings in the mlab API that I plan to address ASAP.

IPython Sprint
--------------

The week end after Fernando, Laurent Dufréchou, Stefan van der Waalt and
myself crashed at my parent's place to work on ipython1 and the front
ends. My mother cooked us some fabulous food and I had a great time.

Unfortunately we did get as far as I would have like. The right
abstraction for talking between the ipython1 execution engine, and the
front end are not really easy to get right, as the engine is nothing
more than an abstract execution engine, that basically only has a
namespace and knows how to execute stuff in a non-blocking mode (that's
where it gets hard: how do you know what is going on with your engine
and the commands you have sent to it? How do you deal with
introspections requests such as tab-completion or docstring
exploration). We want as little logics in the front ends as possible:
let us not duplicate tab-completion or history. This is why we are
progressively building an object, that Fernando dubbed
"InputStateManager" that is doing the impedance matching between the
front end and the engine. I am starting to believe that the best way to
connect this object (ISM) to the front end is via a callback-based
mechanism: the front-end calls the ISM methods and gives them a callback
to call when finished (for instance if running in a different thread, a
Wx frontend would pass something based on Wx.CallAfter to display the
result). That way the mechanism is very general, can adapt to
event-driven front ends or readline-based one, and knows nothing about
the front end. Of course not much code got written, because I am way too
slow, and it took me ages to figure this out.

We had a lot of fun, and for me the highlight of the week end was when
my girlfriend joined us to do some hacking on a really cool project
trying to use the scipy.org wiki to edit the numpy docstring.

Fernando has pictures of all these happy moments. and I hope he will
publish them somewhere (Fernando, get a blog :->). Next time I hope
there will be more of us.

**Edit:** `my slides at OKcon`_

.. _open knowledge conference: http://www.okfn.org/okcon/
.. _Martin Albrecht: http://www.informatik.uni-bremen.de/cgi-bin/cgiwrap/malb/blosxom.pl
.. _sage project: http://www.sagemath.org/
.. _nipy: http://neuroimaging.scipy.org/
.. _SPM: http://www.fil.ion.ucl.ac.uk/spm/
.. _my slides at OKcon: http://gael-varoquaux.info/physics/slides_okcon.pdf
