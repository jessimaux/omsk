from django.db import transaction
from tempfile import NamedTemporaryFile

from openpyxl import Workbook, load_workbook

from .models import PartnerGuide, ContactPartner


def contact_handle(row, partner_id):
    contact_fields = ['partner_id', 'fio', 'role', 'phone', 'email']
    
    if row[0]:
        contact_obj = ContactPartner.objects.get(id=row[0])
        for index, attribute in enumerate(contact_fields):
            setattr(contact_obj, attribute, row[index+1])
        contact_obj.save()
    else:
        ContactPartner.objects.create(partner_id=partner_id, fio=row[2], role=row[3], phone=row[4], email=row[5])

def import_partners(upload_file):
    wb = load_workbook(upload_file)
    ws = wb.active
    
    partners_fields = ['name', 'inn', 'region', 'discount']
    
    # if something wrong transacation will rollback
    with transaction.atomic():
        partner_id = None
        for row in ws.iter_rows(min_row=2, values_only=True):
            # check for empty partner row
            flag_empty = False
            for attr in row[0:5]:
                if attr:
                    flag_empty = True
                    break
           
            # if flag not empty - handle partner, else handle only contact
            if flag_empty:
                if row[0]:
                    partner_obj = PartnerGuide.objects.get(id=row[0])
                    partner_id = row[0]
                    for index, attr in enumerate(partners_fields):
                        setattr(partner_obj, attr, row[index+1])
                    partner_obj.save()
                    contact_handle(row[5:11], partner_id)
                else:
                    partner_obj = PartnerGuide.objects.create(name=row[1], inn=row[2], region=row[3], discount=row[4])
                    partner_id = partner_obj.id
                    contact_handle(row[5:11], partner_id)
            else:
                contact_handle(row[5:11], partner_id)
            
def export_partners():
    wb = Workbook()
    
    partners_query = PartnerGuide.objects.all()
    
    partners_fields = ['id', 'name', 'inn', 'region', 'discount']
    contact_fields = ['id', 'partner_id', 'fio', 'role', 'phone', 'email']
        
    with NamedTemporaryFile() as tmp:
        ws = wb.active
        
        # header
        for col, title in enumerate(partners_fields+contact_fields):
            ws.cell(row=1, column=col+1, value=title)
        
        # body
        row = 2
        for partner in partners_query:
            for col, attr in enumerate(partners_fields):
                ws.cell(row=row, column=col+1, value=getattr(partner, attr))
            for contact in partner.contact_partner.all():
                for col, attr in enumerate(contact_fields):
                    ws.cell(row=row, column=len(partners_fields)+col+1, value=getattr(contact, attr))
                row += 1
                    
        # save as stream
        wb.save(tmp.name)
        tmp.seek(0)
        stream = tmp.read()

    return stream