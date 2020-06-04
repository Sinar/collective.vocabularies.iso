# -*- coding: utf-8 -*-

# from plone import api
from collective.vocabularies.iso import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
import pycountry


@implementer(IVocabularyFactory)
class Currencies(object):
    """
    """

    def make_terms(self, items):
        """ Create zope.schame terms from tuples """
        terms = [SimpleTerm(
                             value=triplet[0],
                             token=triplet[1],
                             title=triplet[2])

                 for triplet in items]

        return terms

    def __call__(self, context):

        currencies = []

        for currency in list(pycountry.currencies):
            currencies.append((currency.alpha_3, currency.numeric,
                              currency.name))

        terms = self.make_terms(currencies)

        return SimpleVocabulary(terms)


CurrenciesFactory = Currencies()
