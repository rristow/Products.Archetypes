import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from common import *
from utils import *

# need this to initialize new BU for tests
from test_classgen import Dummy

from Products.Archetypes.public import *
from Products.Archetypes.config import PKG_NAME
from Products.Archetypes.interfaces.layer import ILayerContainer
from Products.Archetypes.Storage import AttributeStorage, MetadataStorage
from Products.Archetypes import listTypes
from Products.Archetypes.Widget import IdWidget, StringWidget, BooleanWidget, \
     KeywordWidget, TextAreaWidget, CalendarWidget, SelectionWidget
from Products.Archetypes.utils import DisplayList
from Products.CMFCore  import CMFCorePermissions
from Products.Archetypes.ExtensibleMetadata import FLOOR_DATE,CEILING_DATE

from DateTime import DateTime

Dummy.schema = BaseSchema


class BaseSchemaTest(ArchetypesTestCase):

    def afterSetUp(self):
        ArchetypesTestCase.afterSetUp(self)
        registerType(Dummy)
        content_types, constructors, ftis = process_types(listTypes(), PKG_NAME)
        self._dummy = Dummy(oid='dummy')
        self._dummy.initializeArchetype()

    def test_id(self):
        dummy = self._dummy
        field = dummy.getField('id')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0)
        self.failUnless(field.default == None)
        self.failUnless(field.searchable == 0)
        self.failUnless(field.vocabulary == ())
        self.failUnless(field.enforceVocabulary == 0)
        self.failUnless(field.multiValued == 0)
        self.failUnless(field.isMetadata == 0)
        self.failUnless(field.accessor == 'getId')
        self.failUnless(field.mutator == 'setId')
        self.failUnless(field.read_permission == CMFCorePermissions.View)
        self.failUnless(field.write_permission ==
                        CMFCorePermissions.ModifyPortalContent)
        self.failUnless(field.generateMode == 'veVc')
        self.failUnless(field.force == '')
        self.failUnless(field.type == 'string')
        self.failUnless(isinstance(field.storage, AttributeStorage))
        self.failUnless(field.getLayerImpl('storage') == AttributeStorage())
        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.validators == ())
        self.failUnless(isinstance(field.widget, IdWidget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList))
        self.failUnless(tuple(vocab) == ())

    def test_title(self):
        dummy = self._dummy
        field = dummy.getField('title')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 1)
        self.failUnless(field.default == '')
        self.failUnless(field.searchable == 1)
        self.failUnless(field.vocabulary == ())
        self.failUnless(field.enforceVocabulary == 0)
        self.failUnless(field.multiValued == 0)
        self.failUnless(field.isMetadata == 0)
        self.failUnless(field.accessor == 'Title')
        self.failUnless(field.mutator == 'setTitle')
        self.failUnless(field.read_permission == CMFCorePermissions.View)
        self.failUnless(field.write_permission ==
                        CMFCorePermissions.ModifyPortalContent)
        self.failUnless(field.generateMode == 'veVc')
        self.failUnless(field.force == '')
        self.failUnless(field.type == 'string')
        self.failUnless(isinstance(field.storage, AttributeStorage))
        self.failUnless(field.getLayerImpl('storage') == AttributeStorage())
        self.failUnless(field.validators == ())
        self.failUnless(isinstance(field.widget, StringWidget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList))
        self.failUnless(tuple(vocab) == ())

    ### Metadata Properties

    def test_allowdiscussion(self):
        dummy = self._dummy
        field = dummy.getField('allowDiscussion')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0)
        self.failUnless(field.default == None)
        self.failUnless(field.searchable == 0)
        self.failUnless(field.vocabulary == DisplayList(((0, 'Disabled'),
                                                         (1, 'Enabled'),
                                                         (None, 'Default'))))
        self.failUnless(field.enforceVocabulary == 1)
        self.failUnless(field.multiValued == 0)
        self.failUnless(field.isMetadata == 1)
        self.failUnless(field.accessor == 'isDiscussable')
        self.failUnless(field.mutator == 'allowDiscussion')
        self.failUnless(field.read_permission == CMFCorePermissions.View)
        self.failUnless(field.write_permission ==
                        CMFCorePermissions.ModifyPortalContent)
        self.failUnless(field.generateMode == 'mVc')
        self.failUnless(field.force == '')
        self.failUnless(field.type == 'string')
        self.failUnless(isinstance(field.storage, MetadataStorage))
        self.failUnless(field.getLayerImpl('storage') == MetadataStorage())
        self.failUnless(field.validators == ())
        self.failUnless(isinstance(field.widget, SelectionWidget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList))
        self.failUnless(vocab == DisplayList(((0, 'Disabled'),
                                              (1, 'Enabled'),
                                              (None, 'Default'))))

    def test_subject(self):
        dummy = self._dummy
        field = dummy.getField('subject')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0)
        self.failUnless(field.default == [])
        self.failUnless(field.searchable == 0)
        vocab = field.vocabulary
        self.failUnless(vocab == ())
        self.failUnless(field.enforceVocabulary == 0)
        self.failUnless(field.multiValued == 1)
        self.failUnless(field.isMetadata == 1)
        self.failUnless(field.accessor == 'Subject')
        self.failUnless(field.mutator == 'setSubject')
        self.failUnless(field.read_permission == CMFCorePermissions.View)
        self.failUnless(field.write_permission ==
                        CMFCorePermissions.ModifyPortalContent)
        self.failUnless(field.generateMode == 'mVc')
        self.failUnless(field.force == '')
        self.failUnless(field.type == 'lines')
        self.failUnless(isinstance(field.storage, MetadataStorage))
        self.failUnless(field.getLayerImpl('storage') == MetadataStorage())
        self.failUnless(field.validators == ())
        self.failUnless(isinstance(field.widget, KeywordWidget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList))
        self.failUnless(tuple(vocab) == ())

    def test_description(self):
        dummy = self._dummy
        field = dummy.getField('description')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0)
        self.failUnless(field.default == '')
        self.failUnless(field.searchable == 1)
        vocab = field.vocabulary
        self.failUnless(vocab == ())
        self.failUnless(field.enforceVocabulary == 0)
        self.failUnless(field.multiValued == 0)
        self.failUnless(field.isMetadata == 1)
        self.failUnless(field.accessor == 'Description')
        self.failUnless(field.mutator == 'setDescription')
        self.failUnless(field.read_permission == CMFCorePermissions.View)
        self.failUnless(field.write_permission ==
                        CMFCorePermissions.ModifyPortalContent)
        self.failUnless(field.generateMode == 'mVc')
        self.failUnless(field.force == '')
        self.failUnless(field.type == 'text')
        self.failUnless(isinstance(field.storage, MetadataStorage))
        self.failUnless(field.getLayerImpl('storage') == MetadataStorage())
        self.failUnless(field.validators == ())
        self.failUnless(isinstance(field.widget, TextAreaWidget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList))
        self.failUnless(tuple(vocab) == ())

    def test_contributors(self):
        dummy = self._dummy
        field = dummy.getField('contributors')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0)
        self.failUnless(field.default == [])
        self.failUnless(field.searchable == 0)
        vocab = field.vocabulary
        self.failUnless(vocab == ())
        self.failUnless(field.enforceVocabulary == 0)
        self.failUnless(field.multiValued == 0)
        self.failUnless(field.isMetadata == 1)
        self.failUnless(field.accessor == 'Contributors')
        self.failUnless(field.mutator == 'setContributors')
        self.failUnless(field.read_permission == CMFCorePermissions.View)
        self.failUnless(field.write_permission ==
                        CMFCorePermissions.ModifyPortalContent)
        self.failUnless(field.generateMode == 'mVc')
        self.failUnless(field.force == '')
        self.failUnless(field.type == 'lines')
        self.failUnless(isinstance(field.storage, MetadataStorage))
        self.failUnless(field.getLayerImpl('storage') == MetadataStorage())
        self.failUnless(field.validators == ())
        self.failUnless(isinstance(field.widget, LinesWidget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList))
        self.failUnless(tuple(vocab) == ())

    def test_effectivedate(self):
        dummy = self._dummy
        field = dummy.getField('effectiveDate')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0)
        self.failUnlessEqual(field.default, None)
        self.failUnlessEqual(dummy.effective(), FLOOR_DATE)
        self.failUnless(field.searchable == 0)
        vocab = field.vocabulary
        self.failUnless(vocab == ())
        self.failUnless(field.enforceVocabulary == 0)
        self.failUnless(field.multiValued == 0)
        self.failUnless(field.isMetadata == 1)
        self.failUnless(field.mutator == 'setEffectiveDate')
        self.failUnless(field.read_permission == CMFCorePermissions.View)
        self.failUnless(field.write_permission ==
                        CMFCorePermissions.ModifyPortalContent)
        self.failUnless(field.generateMode == 'mVc')
        self.failUnless(field.force == '')
        self.failUnless(field.type == 'datetime')
        self.failUnless(isinstance(field.storage, MetadataStorage))
        self.failUnless(field.getLayerImpl('storage') == MetadataStorage())
        self.failUnless(field.validators == ())
        self.failUnless(isinstance(field.widget, CalendarWidget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList))
        self.failUnless(tuple(vocab) == ())

    def test_expirationdate(self):
        dummy = self._dummy
        field = dummy.getField('expirationDate')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0)
        self.failUnlessEqual(field.default, None)
        self.failUnlessEqual(dummy.expires(), CEILING_DATE)
        self.failUnless(field.searchable == 0)
        vocab = field.vocabulary
        self.failUnless(vocab == ())
        self.failUnless(field.enforceVocabulary == 0)
        self.failUnless(field.multiValued == 0)
        self.failUnless(field.isMetadata == 1)
        self.failUnless(field.mutator == 'setExpirationDate')
        self.failUnless(field.read_permission == CMFCorePermissions.View)
        self.failUnless(field.write_permission ==
                        CMFCorePermissions.ModifyPortalContent)
        self.failUnless(field.generateMode == 'mVc')
        self.failUnless(field.force == '')
        self.failUnless(field.type == 'datetime')
        self.failUnless(isinstance(field.storage, MetadataStorage))
        self.failUnless(field.getLayerImpl('storage') == MetadataStorage())
        self.failUnless(field.validators == ())
        self.failUnless(isinstance(field.widget, CalendarWidget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList))
        self.failUnless(tuple(vocab) == ())

    def test_language(self):
        dummy = self._dummy
        field = dummy.getField('language')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0)
        self.failUnless(field.default == 'en')
        self.failUnless(field.searchable == 0)
        vocab = field.vocabulary
        self.failUnless(vocab == 'languages')
        self.failUnless(field.enforceVocabulary == 0)
        self.failUnless(field.multiValued == 0)
        self.failUnless(field.isMetadata == 1)
        self.failUnless(field.accessor == 'Language')
        self.failUnless(field.mutator == 'setLanguage')
        self.failUnless(field.read_permission == CMFCorePermissions.View)
        self.failUnless(field.write_permission ==
                        CMFCorePermissions.ModifyPortalContent)
        self.failUnless(field.generateMode == 'mVc')
        self.failUnless(field.force == '')
        self.failUnless(field.type == 'string')
        self.failUnless(isinstance(field.storage, MetadataStorage))
        self.failUnless(field.getLayerImpl('storage') == MetadataStorage())
        self.failUnless(field.validators == ())
        self.failUnless(isinstance(field.widget, SelectionWidget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList))
        self.failUnless(vocab == dummy.languages())

    def test_rights(self):
        dummy = self._dummy
        field = dummy.getField('rights')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0)
        self.failUnless(field.default == '')
        self.failUnless(field.searchable == 0)
        vocab = field.vocabulary
        self.failUnless(vocab == ())
        self.failUnless(field.enforceVocabulary == 0)
        self.failUnless(field.multiValued == 0)
        self.failUnless(field.isMetadata == 1)
        self.failUnless(field.accessor == 'Rights')
        self.failUnless(field.mutator == 'setRights')
        self.failUnless(field.read_permission == CMFCorePermissions.View)
        self.failUnless(field.write_permission ==
                        CMFCorePermissions.ModifyPortalContent)
        self.failUnless(field.generateMode == 'mVc')
        self.failUnless(field.force == '')
        self.failUnless(field.type == 'string')
        self.failUnless(isinstance(field.storage, MetadataStorage))
        self.failUnless(field.getLayerImpl('storage') == MetadataStorage())
        self.failUnless(field.validators == ())
        self.failUnless(isinstance(field.widget, TextAreaWidget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList))
        self.failUnless(tuple(vocab) == ())

    # metadata utility accessors (DublinCore)
    def test_EffectiveDate(self):
        dummy = self._dummy
        self.failUnless(dummy.EffectiveDate() == 'None')
        now = DateTime()
        dummy.setEffectiveDate(now)
        self.failUnless(dummy.EffectiveDate() == now.ISO())

    def test_ExpiresDate(self):
        dummy = self._dummy
        self.failUnless(dummy.ExpirationDate() == 'None')
        now = DateTime()
        dummy.setExpirationDate(now)
        self.failUnless(dummy.ExpirationDate() == now.ISO())

    def test_Date(self):
        dummy = self._dummy
        self.failUnless(isinstance(dummy.Date(), str))
        dummy.setEffectiveDate(DateTime())
        self.failUnless(isinstance(dummy.Date(), str))

    def test_contentEffective(self):
        dummy = self._dummy
        now = DateTime()
        then = DateTime() + 1000
        self.failUnless(dummy.contentEffective(now))
        dummy.setExpirationDate(then)
        self.failUnless(dummy.contentEffective(now))
        dummy.setEffectiveDate(now)
        self.failUnless(dummy.contentEffective(now))
        dummy.setEffectiveDate(then)
        self.failIf(dummy.contentEffective(now))

    def test_contentExpired(self):
        dummy = self._dummy
        now = DateTime()
        then = DateTime() + 1000
        self.failIf(dummy.contentExpired())
        dummy.setExpirationDate(then)
        self.failIf(dummy.contentExpired())
        dummy.setExpirationDate(now)
        self.failUnless(dummy.contentExpired())

    def beforeTearDown(self):
        del self._dummy
        ArchetypesTestCase.beforeTearDown(self)

if __name__ == '__main__':
    framework()
else:
    # While framework.py provides its own test_suite()
    # method the testrunner utility does not.
    import unittest
    def test_suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(BaseSchemaTest))
        return suite
