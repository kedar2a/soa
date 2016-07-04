from django.db import models


class MurtiCategory(models.Model):
    '''Main category includes:
    dagdusheth, titawala etc.
    '''

    murti_category_name = models.CharField(max_length=50, unique=True)
    category_code = models.CharField(max_length=2)
    feature = models.TextField(null=True)  # max_length=5000

    class Meta:
        verbose_name = "MurtiType"
        verbose_name_plural = "MurtiTypes"

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
    dissolution_time_per_kg = models.DecimalField(max_digits=4, decimal_places=2, null=True)
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


class MurtiImage(models.Model):

    idol_image = models.FileField(upload_to='idol-images/', default='idol-images/None/no-img.jpg')

    class Meta:
        verbose_name = "MurtiImage"
        verbose_name_plural = "MurtiImages"

    def __str__(self):
        return self.idol_image.name


class Status:
    AVAILABLE = 'Available'
    BOOKED = 'Booked'
    CHOICES = (
      (AVAILABLE, 'Available'),
      (BOOKED, 'Booked'),
    )


class MurtiStatus(models.Model):
    '''Following are possible options:
    Available, booked, under_development etc.
    '''
    murti_status = models.CharField(max_length=20)

    class Meta:
        verbose_name = "MurtiStatus"
        verbose_name_plural = "MurtiStatus"

    def __str__(self):
        return self.murti_status
    

class Murti(models.Model):

    murti_name  = models.CharField(max_length=50)
    murti_id    = models.CharField(max_length=2, unique=True)
    altname     = models.CharField(max_length=50, null=True)
    sp_feature  = models.TextField(null=True)
    height      = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    weight      = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    price       = models.PositiveIntegerField(null=True)
    category    = models.ForeignKey(MurtiCategory, on_delete=models.CASCADE, null=True)
    material    = models.ForeignKey(MaterialCategory, on_delete=models.CASCADE, null=True)
    status      = models.CharField(max_length=10, choices=Status.CHOICES, default=Status.AVAILABLE)
    note        = models.TextField(null=True)
    tags        = models.ManyToManyField(MurtiTag)
    images      = models.ManyToManyField(MurtiImage)

    class Meta:
        verbose_name = "Murti"
        verbose_name_plural = "Murtis"

    def __str__(self):
        return self.murti_name + ' (' + self.murti_id + ')'
