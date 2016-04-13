Mayavi2 in Ubuntu
#################

:date: 2008-01-26 10:10
:tags: scipy, mayavi, scientific computing

After Debian, Mayavi2 has just made it into Ubuntu Hardy
(http://packages.ubuntu.com/hardy/science/mayavi\ 2). From what I can
see, the deps look just good, thanks a lot to Varun for making sure the
Debian package was in shape. This means in April, it will be massively
easier for a lot of people to install an oldish version of Mayavi2.

I am quite happy to say that we did this the right way, by polishing a
Debian package first. Once this once done, getting Mayavi2 in Ubuntu was
trivial. This felt like a well-working machinery.

Now that a Debian package has been done and the Debian QA went over all
the fine details of permissions, license, man pages... it should be much
easier to get Mayavi2 in other distros (anybody for Fedora ?). Having a
binary package in a distro is a major bonus for the users: there is a
world between having to grab and compile the ETS to try out a program,
and being able to install it from the repos. Of course, the package will
always be a bit old and lacking the shiny features that we add in the
SVN. When I find time, I will put myself together and make debs for
Gusty. It not hard, I just have to find the time (yes, promises ...).
