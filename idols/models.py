import datetime
from django.db import models

class MurtiImage(models.Model):

    idol_image = models.FileField(upload_to='idol-images', default='idol-images/None/no-img.png')

    class Meta:
        verbose_name = "Murti Image"
        verbose_name_plural = "MurtiImages"

    def __str__(self):
        return self.idol_image.name

    def image_tag(self):
        if self.idol_image:
            return '<a href="%s"><img src="%s" height="100" /></a>' % (self.idol_image.url, self.idol_image.url)
        # else:
        #     return self.idol_image.name            

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class MurtiCategory(models.Model):
    '''Main category includes:
    dagdusheth, titawala etc.
    '''

    murti_category_name = models.CharField(max_length=50, unique=True)
    category_code = models.CharField(max_length=4, unique=True)
    feature = models.TextField(blank=True, default='')
    images = models.ForeignKey(MurtiImage, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "MurtiCategory"
        verbose_name_plural = "MurtiCategorys"

    def __str__(self):
        return self.murti_category_name


class Ingredient(models.Model):
    ''' example:
    e.g: clay, paper, glue, mud etc.
    '''

    ingredient_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "composition"
        verbose_name_plural = "compositions"

    def __str__(self):
        return self.ingredient_name


class MaterialCategory(models.Model):
    ''' example:
    POP, eco-friendly, paper-mache etc.
    '''

    material_category_name  = models.CharField(max_length=50)
    dissolution_time_per_kg = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    ingredients             = models.ManyToManyField(Ingredient)
    # tests_passed  = [char]  # e.g: t1, t2, t3
    # weight_per_kg = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    class Meta:
        verbose_name = "MaterialCategory"
        verbose_name_plural = "MaterialCategorys"

    def __str__(self):
        return self.material_category_name
    

class MurtiTag(models.Model):
    '''
    for tags
    '''

    tag = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "MurtiTag"
        verbose_name_plural = "MurtiTags"

    def __str__(self):
        return self.tag


class Status:
    AVAILABLE = 'Available'
    BOOKED = 'Booked'
    CHOICES = (
      (AVAILABLE, 'Available'),
      (BOOKED, 'Booked'),
    )

# class MurtiStatus(models.Model):
#     '''Following are possible options:
#     Available, booked, under_development etc.
#     '''
#     murti_status = models.CharField(max_length=20)

#     class Meta:
#         verbose_name = "MurtiStatus"
#         verbose_name_plural = "MurtiStatus"

#     def __str__(self):
#         return self.murti_status
    

class Buyer(models.Model):

    buyer_name = models.CharField(max_length=50)
    phone_no   = models.CharField(max_length=14, blank=True, default='')
    address    = models.TextField(blank=True, default='') 

    class Meta:
        verbose_name = 'Buyer'
        verbose_name_plural = 'Buyers'
        ordering = ['buyer_name']

    def __str__(self):
        return self.buyer_name
    

class Murti(models.Model):

    murti_name  = models.CharField(max_length=50)
    murti_id    = models.CharField(max_length=20, unique=True)
    altname     = models.CharField(max_length=50, blank=True, default='')
    sp_feature  = models.TextField(blank=True, default='')
    height      = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    weight      = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price       = models.PositiveIntegerField(blank=True, null=True)
    category    = models.ForeignKey(MurtiCategory, on_delete=models.CASCADE, null=True)
    material    = models.ForeignKey(MaterialCategory, on_delete=models.CASCADE, null=True)
    status      = models.CharField(max_length=10, choices=Status.CHOICES, default=Status.AVAILABLE)
    note        = models.TextField(blank=True, default='')
    tags        = models.ManyToManyField(MurtiTag)
    images      = models.ManyToManyField(MurtiImage)
    featured    = models.BooleanField(default=False)
    year = models.IntegerField(choices=((2017, 2017), (2016, 2016)), default=datetime.datetime.now().year)

    sold_price  = models.PositiveIntegerField(blank=True, null=True)
    buyer       = models.ForeignKey(Buyer, on_delete=models.CASCADE, blank=True, null=True)
    booked_at   = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Murti"
        verbose_name_plural = "Murtis"

    def __str__(self):
        return self.murti_name + ' (' + self.murti_id + ')'
