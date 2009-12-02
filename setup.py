from setuptools import setup, find_packages

version = '1.6a4'

setup(name='Products.Archetypes',
      version=version,
      description="Archetypes is a developers framework for rapidly "
                  "developing and deploying rich, full featured content "
                  "types within the context of Zope/CMF and Plone.",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
        ],
      keywords='Archetypes Plone CMF Zope',
      author='Archetypes developement team',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/Products.Archetypes',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            'zope.publisher',
            'zope.testing',
            'zope.app.testing',
            'Products.CMFTestCase',
        ]
      ),
      install_requires=[
          'setuptools',
          'zope.component',
          'zope.contenttype',
          'zope.datetime',
          'zope.event',
          'zope.i18n',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.lifecycleevent',
          'zope.schema',
          'zope.site',
          'zope.tal',
          'Products.CMFCalendar',
          'Products.CMFCore',
          'Products.CMFDefault',
          'Products.CMFTestCase',
          'Products.DCWorkflow',
          'Products.GenericSetup',
          'Products.Marshall',
          'Products.MimetypesRegistry',
          'Products.PlacelessTranslationService',
          'Products.PortalTransforms',
          'Products.statusmessages',
          'Products.validation',
          'plone.folder',
          'plone.app.folder',
          'Acquisition',
          'DateTime',
          'ExtensionClass',
          'transaction',
          'ZODB3',
          'Zope2',
      ],
      )
