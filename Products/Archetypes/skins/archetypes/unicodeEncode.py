## Script (Python) "unicodeEncode"
##title=Test if a unicode string is in a unicode list
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=value

charset = context.portal_properties.site_properties.default_charset

if not hasattr(value, 'strip'): # not type(value) in (type(''), type(u''))
    value = str(value)
    
if hasattr(value, 'decode'): # type(value) is type('')
    for charset in [site_charset, 'latin-1', 'utf-8']:
        try:
            value = unicode(value, charset)
            break
        except UnicodeError:
            pass
    else:
        raise UnicodeError('Unable to decode %s' % value)

# don't try to catch unicode error here
# if one occurs, that means the site charset must be changed !
return value.encode(site_charset)
