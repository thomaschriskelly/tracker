from django.test import TestCase, Client
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


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def testIndex(self):
        '''
        verifies that web app index loads
        '''
        index_response = self.client.get('/')
        self.assertEqual(index_response.status_code, 200)

    def testPostProduct(self):
        '''
        tests POSTing a product creates new db entry
        '''
        self.assertEqual(models.Product.objects.all().count(), 0)
        response = self.client.post('/products/', {'description': 'hello world'})
        self.assertEqual(models.Product.objects.all().count(), 1)
        self.assertEqual(models.Product.objects.get().description, 'hello world')

