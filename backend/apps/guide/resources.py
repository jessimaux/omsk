from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import ProductGuide, PartnerGuide, ProviderGuide, ContactPartner


class ProductGuideResource(resources.ModelResource):
    class Meta:
        model = ProductGuide
        exclude = ('created_by', 'created_at', 'updated_by', 'updated_at')
        
        
class PartnerGuideResource(resources.ModelResource):    
    class Meta:
        model = PartnerGuide
        exclude = ('created_by', 'created_at', 'updated_by', 'updated_at')
    
    partner_id = fields.Field(column_name='partner_id', 
                              attribute='partner_id', 
                              widget=ForeignKeyWidget(PartnerGuide, field='contact_partner.fio'))
    # fio = fields.Field(widget=ForeignKeyWidget(ContactPartner, field='fio'))
    # role = fields.Field(widget=ForeignKeyWidget(ContactPartner, field='role'))
    # phone = fields.Field(widget=ForeignKeyWidget(ContactPartner, field='phone'))
    # email = fields.Field(widget=ForeignKeyWidget(ContactPartner, field='email'))

class ProviderGuideResource(resources.ModelResource):
    class Meta:
        model = ProviderGuide
        exclude = ('created_by', 'created_at', 'updated_by', 'updated_at')