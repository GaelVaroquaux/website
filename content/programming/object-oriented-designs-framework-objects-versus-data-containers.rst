Object-oriented design: framework objects versus data containers
#########################################################################

:date: 2009-07-01 05:13
:tags: python, scientific computing, software engineering, software architecture

I find that in object oriented design, there are two kinds of objects:

-  A first kind is the object encoding logics. This is an object for
   which clever and complex design will hold together the logics of a
   state-full application. It can often be part of a forest of objects
   that are linked together via design patterns. The interfaces of these
   objects are driven by their active role in the application. These
   objects are prominently present in interactive application and
   interactive application. They are mostly particular to an application
   or a framework, and are mostly implementation-defined.

-  The second type of object is a data container. It strives to expose a
   data model that can be of use in various situations, as it is the
   link between different parts of the code that do not talk to each
   other apart through data. It is responsible for loose coupling
   (something that is very important to achieve a maintainable code
   base) by having a light and shallow interface. It must be
   interfaced-designed, rather than implementation-designed. One should
   very easily get a grasp, an almost physical feeling, for the object
   by simple interaction with it. I have what I call the 'explaining
   test' for these objects: can I explain fully and completely to
   somebody what the object does, and any possible caveat, without being
   sidetracked into special discussions? If not, back to the drawing
   board: the object will not gain acceptance. In my experience, only
   the objects of the second kind can easily be shared between different
   projects.

