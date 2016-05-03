# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################
import base64#file encode
import urllib2 #file download from url
import httplib

from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
import logging

_logger = logging.getLogger(__name__)

class product_template(osv.osv):
    _inherit = "product.template"
    _columns = {
        'web':fields.char('Image url', help='Automatically sanitized HTML contents'),
        }
    def onchange_image(self,cr,uid,ids,web,context=None):
        link=web
        if link and link!='':
            try:
                photo = base64.encodestring(urllib2.urlopen(link, timeout=10).read())
                val={
                     'image_medium':photo,
                     }
                return {'value': val}
            except urllib2.HTTPError, e:
                _logger.error('HTTPError = ' + str(e.code)+' when processing this request')
            except urllib2.URLError, e:
                _logger.error('URLError = ' + str(e.reason)+' when processing this request')
            except httplib.HTTPException, e:
                _logger.error('HTTPException'+' when processing product id this request')
            except Exception:
                import traceback
                _logger.error('generic exception: ' + traceback.format_exc()+' when processing this request')
        return True

    def download_product_image(self,cr,uid,ids,context=None):
        for product in self.browse(cr, uid, ids, context=context):
            link = product.web
            if link and link!='':
                try:
                    photo = base64.encodestring(urllib2.urlopen(link, timeout=10).read())
                    val={
                         'image_medium':photo,
                         }
                    product.write(val)
                except urllib2.HTTPError, e:
                    _logger.error('HTTPError = ' + str(e.code)+' when processing product id: '+str(product.id))
                    continue
                except urllib2.URLError, e:
                    _logger.error('URLError = ' + str(e.reason)+' when processing product id: '+str(product.id))
                    continue
                except httplib.HTTPException, e:
                    _logger.error('HTTPException'+' when processing product id: '+str(product.id))
                    continue
                except Exception:
                    import traceback
                    _logger.error('generic exception: ' + traceback.format_exc()+' when processing product id: '+str(product.id))
                    continue
        return True

product_template()
