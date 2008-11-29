"""
Backward compatibility module.
"""
import ReferenceEngine
import UIDCatalog

# don't break existing ZODB instances of UID catalog
ReferenceEngine.UIDBaseCatalog = UIDCatalog.UIDBaseCatalog
ReferenceEngine.UIDCatalog = UIDCatalog.UIDCatalog
