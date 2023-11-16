```python
from odoo import http
from odoo.http import request

class MainController(http.Controller):

    @http.route('/custom_pc', type='http', auth='user', website=True)
    def custom_pc(self, **kwargs):
        custom_pc = request.env['custom_pc'].search([])
        return request.render('custom_pc_odoo_17_v1.custom_pc_view', {
            'custom_pc': custom_pc
        })

    @http.route('/custom_pc/calculate_total_cost', type='json', auth='user')
    def calculate_total_cost(self, **kwargs):
        try:
            custom_pc = request.env['custom_pc'].browse(kwargs.get('id'))
            total_cost = custom_pc.calculate_total_cost()
            return {'total_cost': total_cost}
        except Exception as e:
            return {'error': str(e)}

    @http.route('/custom_pc/check_compatibility', type='json', auth='user')
    def check_compatibility(self, **kwargs):
        try:
            custom_pc = request.env['custom_pc'].browse(kwargs.get('id'))
            compatibility_status = custom_pc.check_compatibility()
            return {'compatibility_status': compatibility_status}
        except Exception as e:
            return {'error': str(e)}

    @http.route('/custom_pc/customize_pc', type='json', auth='user')
    def customize_pc(self, **kwargs):
        try:
            custom_pc = request.env['custom_pc'].browse(kwargs.get('id'))
            customization_options = kwargs.get('customization_options')
            custom_pc.customize_pc(customization_options)
            return {'success': True}
        except Exception as e:
            return {'error': str(e)}
```