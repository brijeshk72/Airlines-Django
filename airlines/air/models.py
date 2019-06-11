from django.db import models
import datetime

class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pwd = models.CharField(max_length=10)

    def __str__(self):
        return self.fname

# choice=(
#     ('DEL','Delhi, India(DEL)'),
#     ('BOM','Mumbai, India(BOM)'),
#     ('BLR','Bangalore, India(BLR)'),
#     ('PNQ','Pune, India(PNQ)'),
#     ('HYD','Hyderabad, India(HYD)'),
#     ('CCU','Kolkata, India(CCU)'),
#     ('MAA','Chennai, India(MAA)'),
#     ('GOI','Goa, India(GOI)'),
#     ('NYC','New York, United State(NYC)'),
#     ('BKK','Bankkok, Thailand(BKK)'),
#     ('SIN','Singapore, Singapore(SIN)'),
#     ('KTM','Kathmandu, Nepal(KTM)'),
#     ('VNS','Varansi, India (VNS)'),
# )

choice=(
    ('Delhi, India(DEL)','Delhi, India(DEL)'),
    ('Mumbai, India(BOM)','Mumbai, India(BOM)'),
    ('Bangalore, India(BLR)','Bangalore, India(BLR)'),
    ('Pune, India(PNQ)','Pune, India(PNQ)'),
    ('Hyderabad, India(HYD)','Hyderabad, India(HYD)'),
    ('Kolkata, India(CCU)','Kolkata, India(CCU)'),
    ('Chennai, India(MAA)','Chennai, India(MAA)'),
    ('Goa, India(GOI)','Goa, India(GOI)'),
    ('New York, United State(NYC)','New York, United State(NYC)'),
    ('Bankkok, Thailand(BKK)','Bankkok, Thailand(BKK)'),
    ('Singapore, Singapore(SIN)','Singapore, Singapore(SIN)'),
    ('Kathmandu, Nepal(KTM)','Kathmandu, Nepal(KTM)'),
    ('Varansi, India (VNS)','Varansi, India (VNS)'),
)

choiceclass = (
    ('Echonomy','Echonomy'),
    ('Premium Echonomy','Premium Echonomy'),
    ('Business','Business'),
)

class AddPlane(models.Model):
    planename = models.CharField(max_length=20)
    echonomy= models.CharField(max_length=30, choices= choiceclass, default='Echonomy')
    source = models.CharField(max_length=30, choices= choice, default= 'Varansi, India(VNS)')
    destination = models.CharField(max_length=30, choices= choice, default= 'Varansi, India (VNS)')
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    price = models.IntegerField()

    def __str__(self):
        return self.planename

class ConfirmTicket(models.Model):
    cname = models.CharField(max_length=25)
    start = models.CharField(max_length=25)
    end   = models.CharField(max_length=25)
    dtime = models.CharField(max_length=25)
    atime = models.CharField(max_length=25)
    payprice = models.CharField(max_length=20)
    category = models.CharField(max_length=25)
    mail = models.EmailField(max_length=25)
    def __str__(self):
        return self.cname