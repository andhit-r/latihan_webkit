import time
from report import report_sxw
from osv import osv

class report_account_move(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_account_move, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'cr':cr,
            'uid': uid,
            'customer_text' : self.get_customer_text,
        })

    def get_customer_text(self):
        res = []
        res.append({'field1' : 'a', 'field2' : 'b'})
        res.append({'field1' : 'c', 'field2' : 'd'})
        return res
		
        
report_sxw.report_sxw('report.report_account_move',
                       'account.move', 
                       'addons/latihan_webkit/report/report_account_move.mako',
                       parser=report_account_move)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
