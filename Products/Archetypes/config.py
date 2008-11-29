from Products.PortalTransforms.libtransforms import utils as transform_utils

PKG_NAME = "Archetypes"
SKIN_NAME = "archetypes"
TOOL_NAME = "archetype_tool" ## Name the tool will be installed under

UID_CATALOG = "uid_catalog"

REGISTER_DEMO_TYPES = True ##Initialize the demo types
DEBUG =  False ## Hide debug messages
#DEBUG = True  ## See debug messages

RENAME_AFTER_CREATION_ATTEMPTS = 100 
## Try up to -100 at the end of the id when doing title-to-id renaming

##Reference Engine bits
REFERENCE_CATALOG = "reference_catalog"
UUID_ATTR = "_at_uid"
REFERENCE_ANNOTATION = "at_references"

## Debug security settings of Fields, Widgets and Storages?
DEBUG_SECURITY=False

## BBB constants for removed graphviz suppport
GRAPHVIZ_BINARY = None
HAS_GRAPHVIZ = False

## set language default for metadata, it will be overwritten by portal-settings!
LANGUAGE_DEFAULT=u''
