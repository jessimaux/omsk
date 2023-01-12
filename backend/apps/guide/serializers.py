from rest_framework import serializers

from .models import ProductGuide, PartnerGuide, ProviderGuide, ContactPartner, ContactProvider


class ContactPartnerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = ContactPartner
        exclude = ['partner']
    
        
class ContactProviderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = ContactProvider
        exclude = ['provider']
        

class ProductGuideSerializer(serializers.ModelSerializer):
    provider = serializers.StringRelatedField(read_only=True)
    provider_id = serializers.IntegerField()
    
    # logs
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()

    class Meta:
        model = ProductGuide
        fields = '__all__'


class ProductGuideImportSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)


class PartnerGuideSerializer(serializers.ModelSerializer):
    contacts = ContactPartnerSerializer(many=True, source='contact_partner')
    
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()

    class Meta:
        model = PartnerGuide
        fields = '__all__'
        
    def create(self, validated_data):
        contacts = validated_data.pop('contact_partner')
        partner_obj = PartnerGuide.objects.create(**validated_data)
        for contact in contacts:
            contact_obj = ContactPartner.objects.create(partner_id=partner_obj.id, **contact)
        return partner_obj
    
    def update(self, instance, validated_data):
        contacts = validated_data.pop('contact_partner')
        super().update(instance, validated_data)
        contacts_from_db = ContactPartner.objects.filter(partner_id=instance.id).values_list('id', flat=True)
        contacts_id_pool = []
        
        for contact in contacts:
            if "id" in contact.keys() and ContactPartner.objects.filter(id=contact['id']).exists():
                contact_obj = ContactPartner.objects.get(id=contact['id'])
                contact_obj.fio = contact.get('fio', contact_obj.fio)
                contact_obj.role = contact.get('role', contact_obj.role)
                contact_obj.phone = contact.get('phone', contact_obj.phone)
                contact_obj.email = contact.get('fio', contact_obj.email)
                contact_obj.save()
            else:
                contact_obj = ContactPartner.objects.create(partner_id=instance.id, **contact)
                        
            contacts_id_pool.append(contact_obj.id)
        
        for contact_id in contacts_from_db:
            if contact_id not in contacts_id_pool:
                ContactPartner.objects.filter(id=contact_id).delete()
        return instance
    
    
class PartnerGuideImportSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)


class ProviderGuideSerializer(serializers.ModelSerializer):
    contacts = ContactProviderSerializer(many=True, source='contact_provider')
    
    created_by = serializers.HiddenField(default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()))
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.SkipField()
    updated_at = serializers.SkipField()

    class Meta:
        model = ProviderGuide
        fields = '__all__'

    def create(self, validated_data):
        contacts = validated_data.pop('contact_provider')
        provider_obj = ProviderGuide.objects.create(**validated_data)
        for contact in contacts:
            contact_obj = ContactProvider.objects.create(provider_id=provider_obj.id, **contact)
        return provider_obj
    
    def update(self, instance, validated_data):
        contacts = validated_data.pop('contact_provider')
        super().update(instance, validated_data)
        contacts_from_db = ContactProvider.objects.filter(provider_id=instance.id).values_list('id', flat=True)
        contacts_id_pool = []
        
        for contact in contacts:
            if "id" in contact.keys() and ContactProvider.objects.filter(id=contact['id']).exists():
                contact_obj = ContactProvider.objects.get(id=contact['id'])
                contact_obj.fio = contact.get('fio', contact_obj.fio)
                contact_obj.role = contact.get('role', contact_obj.role)
                contact_obj.phone = contact.get('phone', contact_obj.phone)
                contact_obj.email = contact.get('fio', contact_obj.email)
                contact_obj.save()
            else:
                contact_obj = ContactProvider.objects.create(provider_id=instance.id, **contact)
                        
            contacts_id_pool.append(contact_obj.id)
        
        for contact_id in contacts_from_db:
            if contact_id not in contacts_id_pool:
                ContactProvider.objects.filter(id=contact_id).delete()
        return instance
    
    
class ProviderGuideImportSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)
