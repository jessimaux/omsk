from import_export import resources, fields, widgets
from .models import ProductGuide, PartnerGuide, ProviderGuide, ContactPartner


class ProductGuideResource(resources.ModelResource):
    name = fields.Field(attribute="name",
                        column_name="name",
                        widget=widgets.CharWidget(), default=None)
    article = fields.Field(attribute="article",
                           column_name="article",
                           widget=widgets.CharWidget(), default=None)

    class Meta:
        model = ProductGuide
        exclude = ('created_by', 'created_at', 'updated_by', 'updated_at')


class PartnerGuideResource(resources.ModelResource):
    class Meta:
        model = PartnerGuide
        exclude = ('created_by', 'created_at', 'updated_by', 'updated_at')

    partner_id = fields.Field(column_name='partner_id',
                              attribute='partner_id',
                              widget=widgets.ForeignKeyWidget(PartnerGuide, field='contact_partner.fio'))


class ProviderGuideResource(resources.ModelResource):
    class Meta:
        model = ProviderGuide
        exclude = ('created_by', 'created_at', 'updated_by', 'updated_at')
