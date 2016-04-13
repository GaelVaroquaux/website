A journal promoting high-quality research code: dream and reality
#################################################################

:date: 2012-06-04 21:39
:tags: publishing, science, computational science, programming, python, scientific computing

`Open research computation (ORC)`_ was an attempt to create a scientific
publication promoting **high-quality and open source scientific code**.
The project went public in falls 2010, but last month, facing the low
volume of submission, the editorial board `chose to reorient it`_ as a
special track of an existing journal.

The challenges that we face are discussed in our editorial:

    `Changing computational research. The challenges ahead.`_ C Neylon,
    J Aerts, CT Brown, D Lemire, J Millman, P Murray-Rust, F Perez, N
    Saunders, A Smith, G Varoquaux and E Willighagen, *Source Code for
    Biology and Medicine* 2012, 7:20

Here is my own personal take on the rise and fall of this ideal.

My story with ORC
=================

.. image:: http://www.rcac.net.au/images/Publications1.jpg
    :align: right
    :width: 40%

**From pipe dream to journal -** My involvement with ORC started long
before there was such a thing as ORC. In falls 2008, I had a discussion
with a friend working in the publication industry, telling her how I
believed that the publication system is broken, because it promotes new
results without any interest on whether these can be exported outside
the lab that produced them: **it is currently easier to publish a minor
but novel result than a tool enabling the routine reproduction of
previous results**. This seemed particularly marked in the scientific
software world, as software tools are becoming central to the scientific
workflow, and cost nothing to duplicate when produced under open-source
license. To my surprise, she took me seriously, and asked me to write my
ideas down in an email that she would forward to her colleagues in the
publication industry.

Looking back at the email that I send, my concerns were, back then, to
promote:

-  quality and openness of scientific software
-  basic tools shared across communities
-  recognition of software development as a challenging and worthwhile
   task in academic research

**Shaping the idea -**\ In the year that followed, I had a few
discussions with staff from `BioMedCentral`_, an open-access publisher
in biology and medicine that was looking into expending in the physics
and math related fields. Eventually, my contact there told me that they
had other similar requests and were launching a journal that would be
lead by Cameron Neylon, a British biophysicist and strong advocate of
openness and reproducibility in science. This was the start of ORC, and
for me the chance to meet other people sharing my concerns, some new and
some `already`_ `old`_ `friends`_.


.. figure:: http://www.salinafbc.com/Websites/fbcsalina/images/nerd_computer.gif
    :align: right
    :width: 230px
    
    ORC editor


.. figure:: http://researchsupportgroup.files.wordpress.com/2011/11/kayla1.jpg
    :align: left
    :width: 150px

    Conventional editor

_____


**Setting up the journal -**\ BioMedCentral was instrumental in setting
up the journal project. I quickly learned that, no surprises, a journal
is a product, like anything else, and it must find customers. Here, as
we were launching an open access journal, the customers were authors.
This is where a journal faces a chicken and egg problem: to be
recognised it needs high-visibility publications, but authors will
submit only to journals that they know. The main tool to overcome this
challenge are communication and advocacy. I then realized that these
really weren't my strong points. Cameron Neylon absolutely shined on
this side, with very enthusiastic `communications`_ and an incredibly
active `twitter account`_. On my side, I am a slow writer, and I tend to
speak Python code better than English language, which is not a strong
asset to be a journal editor.

**Wild editorial discussions -** The discussions in the editorial board
really thrilled me because they were centered on how to set standards to
improve the quality of code published. Looking in my mailbox, I see
discussions about code repositories, software testing, documentation or
licensing issues. This is not that surprising, given that a lot of the
editors where actually contributors to major software projects. It made
me very happy, as I have the feeling that, so far, most committees or
decision makers are clueless about software.

Sand in the gears: the lack of uptake
=====================================

**A false start -**\ So ORC was launched late 2010 and we had fantastic
feedback. I had the feeling that people were `genuinely`_ `excited`_
about our program: changing the way computational science worked from
the inside, through the review process. The idea was that we had opened
a pre-submission call, and were waiting for a few good papers to be
submitted to launch the journal. However, it turned out that the papers
were slow to come. It took me a while to realize that there was
something wrong. But slowly we had to face the truth: many people were
excited about the journal, but most were sending their papers elsewhere.

**What went wrong? -**\ If I really knew what went wrong, I would
probably not be discussing it here, but rather changing the world.
However, I can come up with a few guesses:

-  **Working across communities is harder.** From the beginning we had
   wanted to position the journal across communities, in order to foster
   the sharing of tools for a greater good. The challenge is that a
   central role of publication is nowadays to provide recognition. It is
   much easier to achieve recognition in a given community than across
   communities, and authors always preferred submitting their work to a
   non-software oriented journal in their field. We couldn't fight
   together the battle for software quality and the battle for
   inter-community work.
-  **Setting the bar too high.** Many felt that the submission
   requirements that where too demanding, as expressed on a NeuroImaging
   forumn to quote a researcher: `"I think it's setting the bar
   unrealistically high for most neuroimaging software"`_. While we had
   originally shot for a very high test coverage (probably too high), we
   had scaled it back quickly, simply stressing that editors and
   reviewers would be looking closely at test coverage, documentation
   and ease of installation. That said, the average researcher did not
   share our ideals of raising the quality of scientific software.
   Trying to ask only for excellent publications in a new and unproven
   journal was probably unrealistic.
-  **Editors not willing to game the system.** I have watched a few
   journal launches, and it seems to me that a common trick is to line
   up articles that are created by the editors and their friends
   specifically for the new journal. People come up with *opinion
   papers*, *reviews*, *commentaries* that only serve to generate an
   identity to the journal. This did not happen for ORC, and I believe
   that it is because `the editors themselves`_ were not huge fans of
   the low signal-to-noise ratio in modern scientific publishing
   practice.

The times they are a changing
=============================

.. image:: http://www.pictures88.com/p/success/success_005.jpg
   :align: right
   :width: 35%

**ORC is dead, long live ORC -** We did get a few submissions. ORC is
not coming to an end, it is morphing into a special thematic series in
`source code for biology and medicine`_. This solution is not completely
satisfactory, as it pushes what should have been a forum for exposing
good practices and good software into a smaller community. But at least
there is now a venue in which people can publish a paper about software
that they have been improving and maintaining, and not only about a new
algorithm.

**Changing practices across the board -** Among the reasons for which we
had a hard time making a breakthrough, is that authors where sending
their software papers to other journals, in particular journals not
specialized on software. While these papers are not getting the
attention of a review and editorial team expert on software development,
as we are setting up with ORC, this is still a good thing. Indeed it
shows that the times are changing and that recognition of software as a
scientific work is improving. I have been impressed to see that many
high profile journals have changed their editorial policies to
specifically accept software papers, or have create tracks dedicated to
software.

Software is being slowly recognized as a pillar of modern scientific
research. We need to keep pushing to make sure that quality standards
are set and that the open-source scientific software grows into a mature
ecosystem focused on problem solving.

.. _Open research computation (ORC): http://www.openresearchcomputation.com/
.. _chose to reorient it: http://blogs.openaccesscentral.com/blogs/bmcblog/entry/open_research_computation_thematic_series
.. _Changing computational research. The challenges ahead.: http://www.scfbm.org/content/7/1/2/abstract
.. _BioMedCentral: http://www.biomedcentral.com
.. _already: http://fperez.org/
.. _old: http://jarrodmillman.com/
.. _friends: http://ivory.idyll.org
.. _communications: http://cameronneylon.net/blog/open-research-computation-an-ordinary-journal-with-extraordinary-aims/
.. _twitter account: https://twitter.com/#!/CameronNeylon
.. _genuinely: http://neuralensemble.blogspot.fr/2010/12/open-research-computation-new-journal.html
.. _excited: https://twitter.com/vaguery/status/15402390589018112
.. _"I think it's setting the bar unrealistically high for most neuroimaging software": http://www.nitrc.org/forum/message.php?msg_id=3674
.. _the editors themselves: http://cameronneylon.net/blog/open-research-computation-an-ordinary-journal-with-extraordinary-aims
.. _source code for biology and medicine: http://www.scfbm.org/

