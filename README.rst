===========================
collective.vocabularies.iso
===========================

Plone add-on providing ISO standard vocabularies for countries and currencies,
built on the ``pycountry`` library.

Features
--------

- **Countries vocabulary** – ISO 3166-1 country codes (alpha-2, numeric, name)
- **Currencies vocabulary** – ISO 4217 currency codes (alpha-3, numeric, name)
- **Query string fields** – registered as query string vocabularies for use in
  `plone.app.querystring` and Dexterity field widgets
- **Plone 6 compatible** – supports Python 3.8 through 3.12

Installed vocabularies are registered under:

- ``collective.vocabularies.iso.countries``
- ``collective.vocabularies.iso.currencies``

To use them in a Dexterity field::

    from zope import schema
    from zope.schema.vocabulary import SimpleVocabulary

    country = schema.Choice(
        title=u"Country",
        vocabulary="collective.vocabularies.iso.countries",
    )

Examples
--------

This add-on is used in the following projects:

- `sinar.miscbehavior <https://github.com/Sinar/sinar.miscbehavior>`_ – provides
  a ``ICountries`` behavior that adds a multi-select countries field to any
  Dexterity content type, using ``collective.vocabularies.iso.countries``
- `ocds.contenttypes <https://github.com/Sinar/ocds.contenttypes>`_ – uses the
  countries and currencies vocabularies for Open Contracting Data Standard
  content types

Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is
also available online at http://docs.plone.org

Contribute
----------

- Issue Tracker: https://github.com/collective/collective.vocabularies.iso/issues
- Source Code: https://github.com/collective/collective.vocabularies.iso

Support
-------

If you are having issues, please let us know.

License
-------

The project is licensed under the GPLv2.
