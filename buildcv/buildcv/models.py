from django.db import models

INDUSTRIES = (
    ('industry1', 'Industry 1'),
    ('industry2', 'Industry 2'),
)

COUNTRIES = (
    ('country1', 'Country 1'),
    ('country2', 'Country 2'),
)

REGIONS = (
    ('region1', 'Region 1'),
    ('region2', 'Region 2'),
)

CITIES = (
    ('city1', 'City 1'),
    ('city2', 'City 2'),
)


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    industry_of_work = models.CharField(max_length=255, choices=INDUSTRIES)
    employee_number = models.IntegerField()
    country = models.CharField(max_length=255, choices=COUNTRIES)
    region = models.CharField(max_length=255, choices=REGIONS)
    city = models.CharField(max_length=255, choices=CITIES)
    company_address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    website = models.URLField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20)
    contact_person_name = models.CharField(max_length=255)
    contact_person_surename = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255)
    VAT_number = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    bank_code = models.CharField(max_length=255)
    bank_number = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='company_logos/')
    company_description = models.TextField()

    def __str__(self):
        return self.company_name
