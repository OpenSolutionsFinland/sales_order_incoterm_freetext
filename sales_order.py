from osv import fields, osv
from datetime import datetime as dt
from datetime import date
from datetime import timedelta

class sale_order_ssv(osv.osv):
    _name='sale.order'
    _inherit='sale.order'
    
    _columns= {
        'incoterm_text': fields.char('Incoterms Extra', required=False),
    }

    _defaults = {
        
    }

sale_order_ssv()

