from django.test import TestCase
import datetime
from . import models

class ProductTestCase(TestCase):
    def setUp(self):
        self.description = 'hello world'
        models.Product.objects.create(description=self.description)

    def testStr(self):
        ''' test that __str()__ uses description field '''
        product = models.Product.objects.get()
        self.assertEqual(product.__str__(), self.description)

class BreadcrumbTestCase(TestCase):
    def setUp(self):
        self.product = models.Product.objects.create(description='prod')
        self.datetime = datetime.datetime.fromtimestamp(0)
        self.longitude = 'long'
        self.latitude = 'lat'
        self.elevation = 'el'
        models.Breadcrumb.objects.create(
            product=self.product,
            datetime=self.datetime,
            longitude=self.longitude,
            latitude=self.latitude,
            elevation=self.elevation,
        )

    def testStr(self):
        '''
        test that __str()__ uses fields to create
        a human-readable string
        '''
        breadcrumb = models.Breadcrumb.objects.get()
        expected = 'prod | 1970-01-01 00:00:00+00:00 | long | lat | el'
        self.assertEqual(
            breadcrumb.__str__(),
            expected
        )
