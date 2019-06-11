# Generated by Django 2.1.7 on 2019-06-09 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0002_addplane'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addplane',
            name='destination',
            field=models.CharField(choices=[('Delhi, India(DEL)', 'Delhi, India(DEL)'), ('Mumbai, India(BOM)', 'Mumbai, India(BOM)'), ('Bangalore, India(BLR)', 'Bangalore, India(BLR)'), ('Pune, India(PNQ)', 'Pune, India(PNQ)'), ('Hyderabad, India(HYD)', 'Hyderabad, India(HYD)'), ('Kolkata, India(CCU)', 'Kolkata, India(CCU)'), ('Chennai, India(MAA)', 'Chennai, India(MAA)'), ('Goa, India(GOI)', 'Goa, India(GOI)'), ('New York, United State(NYC)', 'New York, United State(NYC)'), ('Bankkok, Thailand(BKK)', 'Bankkok, Thailand(BKK)'), ('Singapore, Singapore(SIN)', 'Singapore, Singapore(SIN)'), ('Kathmandu, Nepal(KTM)', 'Kathmandu, Nepal(KTM)'), ('Varansi, India (VNS)', 'Varansi, India (VNS)')], default='Varansi, India (VNS)', max_length=30),
        ),
        migrations.AlterField(
            model_name='addplane',
            name='echonomy',
            field=models.CharField(choices=[('Echonomy', 'Echonomy'), ('Premium Echonomy', 'Premium Echonomy'), ('Business', 'Business')], default='Echonomy', max_length=30),
        ),
        migrations.AlterField(
            model_name='addplane',
            name='source',
            field=models.CharField(choices=[('Delhi, India(DEL)', 'Delhi, India(DEL)'), ('Mumbai, India(BOM)', 'Mumbai, India(BOM)'), ('Bangalore, India(BLR)', 'Bangalore, India(BLR)'), ('Pune, India(PNQ)', 'Pune, India(PNQ)'), ('Hyderabad, India(HYD)', 'Hyderabad, India(HYD)'), ('Kolkata, India(CCU)', 'Kolkata, India(CCU)'), ('Chennai, India(MAA)', 'Chennai, India(MAA)'), ('Goa, India(GOI)', 'Goa, India(GOI)'), ('New York, United State(NYC)', 'New York, United State(NYC)'), ('Bankkok, Thailand(BKK)', 'Bankkok, Thailand(BKK)'), ('Singapore, Singapore(SIN)', 'Singapore, Singapore(SIN)'), ('Kathmandu, Nepal(KTM)', 'Kathmandu, Nepal(KTM)'), ('Varansi, India (VNS)', 'Varansi, India (VNS)')], default='Varansi, India (VNS)', max_length=30),
        ),
    ]