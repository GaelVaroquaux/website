Rendering static pages with Turbogears
######################################

:date: 2008-09-07 07:12
:tags: python, publishing, web

Turbogears hack
===============

Suppose you have a dynamic website using turbogears, and you want to
publish part of the content of this dynamic site to a static website,
for instance to garanty its perenity. Well turbogears makes it really
hard for you to do this. On the mailing lists they pretty much advise
you to create a webserver and crawl it. Ugly. So here is the code
required to render the kid templates that you have been using with
turbogears to an html string (consider this as a brain dump, so that
Google picks this up, hopefuly to help somebody not to loose a
day like I did):

.. code-block:: python

    # First set up the environment you need for your webapp:
    import turbogears
    turbogears.update_config(configfile="dev.cfg",
                             modulename="sanum.config")

    from itertools import izip
    import turbogears.view
    turbogears.view.load_engines()

    import turbogears.util as tg_util
    from turbogears.widgets import js_location

    engine = turbogears.view.engines.get('kid')

    def render_static(data_dict, template):
        """ Render a given template + its data dictionnary to a static html.
        """
        data_dict['tg_css'] = tg_util.setlike()
        data_dict['tg_flash'] = False
        js = dict(izip(js_location, iter(tg_util.setlike, None)))

        for l in iter(js_location):
            data_dict["tg_js_%s" % str(l)] = js[l]

        return engine.render(data_dict, template=template)

You can call this function with data\_dict being a dictionary as
returned by your controller methods, and template the path to your
template, as in the expose decorator.

