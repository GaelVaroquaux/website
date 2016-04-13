Personal views on scientific computing
-------------------------------------------------------

:slug: view_on_scientific_computing
:tags: science, academia, scientific computing, selected, scientific software
:date: 2010-05-20

My contributions to the scientific computing software ecosystem are
motivated by my vision on computational science.

Scientific research relies more and more on computing. However, most of
the researchers are not software engineers, and as computing is becoming
ubiquitous, the limiting factor becomes more and more the **human
factor** `[G. Wilson, 2006]
<http://software-carpentry.org/articles/amsci-swc-2006.pdf>`_ `[P.
Norvig, 2009]
<http://download.on9pc.com/ebook/programing/Teach%20Yourself%20Programming%20in%20Ten%20Years.pdf>`_. 

.. note::

 To address the needs of computing accross scientific fields, I believe
 that we need a **general-purpose**, **high-level**, **interactive**, and
 **highly-readable** language and set of tools for scientific computing.

* C does not answer my needs: does a molecular biologist know about
  pointers? Should she?

* Matlab does not answer my needs either: scientific work with computers
  is not only about numerical computation. Have you tried writing an
  experiment-control software with Matlab? How about file management?
  Inserting the algorithms in a web server.

We need better teaching material, that sit at interfaces between software
engineer, and general science. Most top notch tools and libraries are
full of domain-specific jargon and conventions.

For reproducible science, we need the code to be readable and to reflect
the corresponding scientific operation. We need it to be unit-tested to
ensure its correctness.

.. note::

 We need to consider scientific libraries as end-result of our
 research with the same importance than articles `[J. Buckheit and D.
 Donoho. 1995]
 <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.53.6201>`_.
 They need to convey a scientific message, to be **understandable** and
 **refutable**. New results should be **reproducible** via published code
 `[CISE Jan. 2009]
 <http://www.computer.org/portal/web/csdl/doi/10.1109/MCSE.2009.14>`_. As
 for established algorithms, scientific libraries with their
 **documentation** and **examples** should be the textbooks of tomorrow.


____


* **Scientific software should be as reusable as possible**, to enable the
  advancement of Science via software, year after year. This means that
  we need to build general-purpose libraries.

* **Code quality and documentation are crucial**, as human factors are
  often the limitation. As a corollary, scientific code should be
  unit-tested to ensure correctness.
 
* **Core scientific software should be open source**, as scientific work
  cannot build on black boxes

* **Algorithms should be written as simply as possible**. A high level of
  sophistication in software engineering should not be a requirement to
  all scientists

* **Prefer high-level languages**. The code should be written at the right 
  level of abstraction.

* **We need to build common and shared tools**. Scientific software
  shouldn't be 'owned' by a lab.

* **The source code should a deliverable of the research**. As a result, it
  should read clearly and be understandable to all.

* **Documentation and examples are the textbooks of tomorrow**.

* **Publications should be reproducible**. Ideally they should become an
  example of the library. This should be mitigated by the fact that code
  maintainance is costly, and achieving good code takes more work that
  publishing. Focus should be on publications that will give rise to reference
  results.

* **Academia need to value sotware maintainance**. It is hard and costly,
  but it determines our future.

* **Tools that develop the environment, rather than a specific algorithm or
  scientific field are crucial** (one example is IPython).

..
 Cite V Stodden

______

Further reading: 

    * Open source Machine Learning software `[S. Sonnenburg et al. 2007]
      <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.77.5605&rep=rep1&type=pdf>`_
    * Open source mathematical sofware `[D. Joyner and W. Stein 2007]
      <http://www.ams.org/notices/200710/tx071001279p.pdf>`_
    * Licensing, intellectual property in scientific work
      `[A. Gonzalez 2006]
      <http://jolt.unc.edu/sites/default/files/7_nc_jl_tech_321.pdf>`_
    * Scientific software development best practices
      `[S. Baxter et al. 2006]
      <http://www.ploscompbiol.org/article/info:doi/10.1371/journal.pcbi.0020087>`_

