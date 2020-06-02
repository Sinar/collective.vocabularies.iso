# -*- coding: utf-8 -*-

# from plone import api
from collective.vocabularies.iso import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from p01.vocabulary.country import ISO3166Alpha2CountryVocabulary

@implementer(IVocabularyFactory)
class Countries(object):
    """
    """

    def __call__(self, context):
        return ISO3166Alpha2CountryVocabulary(context)

CountriesFactory = Countries()
