Pycon FR: presentations and tutorials
#####################################

:date: 2009-05-16 16:25
:tags: python, scipy, conferences, scientific computing, software engineering

May 30th and 31st the French Python conference, `Pycon FR`_, will be
held at 'la citée des sciences', la Villette, in Paris.

The first day, I will be giving a one-hour-long tutorial (in French) on
numpy, scipy, and all the Python for Science jazz. On the following day,
I will be giving a half-hour-long talk to ilustrate the use of Python in
my current work: statistical analysis and modelling of brain activity.

I'll be giving my tutorial in one room, while David Larlet (the famous
Biologeek) will be giving one on Django in another room. Tough
competition :-P .

The `program`_ of the conference is very eclectic, ranging from general
programming talks, to GUIs or web development. While this might deter
the pure scientific computing folks, I strongly encourage you to attend.
Indeed, a lot of the development, packaging, quality assurance, ...
problems encountered in scientific computing are universal in computing.

You might think that you are only interested in writing algorithms,or
processing data, but this code will have to live on. My experience is
that it is terribly hard to have code in a lab that can be somewhat
shared and live on when people move away to another lab, or stop having
time to maintain the code. Talks like

-  `Correction d'un bug et naissance d'une nouvelle fonctionnalité dans
   CPython`_
-  `Contrôle de versions de source: pourquoi? comment?`_
-  `De la qualité dans un projet en Python`_
-  `Amusez-vous à tester avec les objets farceurs (mock)`_

can probably be of some use.

Also, don't underestimate the fact that some other communities might
have solved some of the issues you struggle with. When dealing with
real-world problems, and not only developing algorithms on a few set of
test data, a large fraction of the code lines and related to IO,
interfaces, data massaging... Two years ago, I remember that I was not
terribly interested in the web-development talks. I tried to be
open-minded and listen to them, but... Now I have done a bit of web
development myself, and I have played with some of the famous 'web
frameworks'. I can tell you, there are some really interesting concepts
there. The web guys have managed to extract a set of patterns from the
problems they face and provide excellent abstracts to data handling and
display. Can we learn from them? I am especially interested in getting
more insight from things like ORMs (object relational mappers), and
understanding better the web frameworks:

-  `Django-ROA pour une architecture orientée ressources`_
-  `PyQt4: Un exemple de sur-mesure en Model/View/Delegate`_ (this is
   not about web, but MVC/MVD pattern has been used in web a lot and is
   universal and very important, IMHO).

-  `Oubliez le sql avec SQLAlchemy`_
-  `Developpement d'applications maintenables avec Django`_
-  `Turbogears 2, présentation et introduction (tutoriel)`_
-  `Programmer CouchDB avec couchdbkit`_
-  `Réflexion sur l'utilisation de python pour le développement d'une
   plateforme web d'annotation`_\ `génomique`_
-  `Oubliez le sql avec
   SQLAlchemy <http://fr.pycon.org/sessions/seances/django_par_la_pratique%2C_premiers_pas>`__
-  `Django par la pratique`_
-  `Python et les bases de données non sql.`_

And finally, one more reason to come: it is so nice to actually get to
meet in real life people, and have a chat.

So, see you there, for those who live in France.

.. _Pycon FR: http://fr.pycon.org
.. _program: http://fr.pycon.org/sessions
.. _Correction d'un bug et naissance d'une nouvelle fonctionnalité dans CPython: http://fr.pycon.org/sessions/seances/correction_d'un_bug_et_naissance_d'une_nouvelle_fonctionnalité_dans_cpython
.. _`Contrôle de versions de source: pourquoi? comment?`: http://fr.pycon.org/sessions/seances/contrôle_de_versions_de_source%3A_pourquoi%3F_comment%3F
.. _De la qualité dans un projet en Python: http://fr.pycon.org/sessions/seances/de_la_qualité_dans_un_projet_en_python
.. _Amusez-vous à tester avec les objets farceurs (mock): http://fr.pycon.org/sessions/seances/amusez-vous_à_tester_avec_les_objets_farceurs_(mock)
.. _Django-ROA pour une architecture orientée ressources: http://fr.pycon.org/sessions/seances/django-roa_pour_une_architecture_orient%C3%A9e_ressources
.. _`PyQt4: Un exemple de sur-mesure en Model/View/Delegate`: http://fr.pycon.org/sessions/seances/django-roa_pour_une_architecture_orient%C3%A9e_ressources
.. _Oubliez le sql avec SQLAlchemy: http://fr.pycon.org/sessions/seances/oubliez_le_sql_avec_sqlalchemy
.. _Developpement d'applications maintenables avec Django: http://fr.pycon.org/sessions/seances/developpement_d'applications_maintenables_avec_django
.. _Turbogears 2, présentation et introduction (tutoriel): http://fr.pycon.org/sessions/seances/turbogears_2%2C_présentation_et_introduction_(tutoriel)
.. _Programmer CouchDB avec couchdbkit: http://fr.pycon.org/sessions/seances/programmer_couchdb_avec_couchdbkit
.. _Réflexion sur l'utilisation de python pour le développement d'une plateforme web d'annotation: http://fr.pycon.org/sessions/seances/réflexion_sur_l'utilisation_de_python_pour_le_développement_d'une_plateforme_web_d'annotation_génomique
.. _génomique: http://fr.pycon.org/sessions/seances/réflexion_sur_l'utilisation_de_python_pour_le_développement_d'une_plateforme_web_d'annotation_génomique
.. _Django par la pratique: http://fr.pycon.org/sessions/seances/django_par_la_pratique%2C_premiers_pas
.. _Python et les bases de données non sql.: http://fr.pycon.org/sessions/seances/python_et_les_bases_de_données_non_sql.
