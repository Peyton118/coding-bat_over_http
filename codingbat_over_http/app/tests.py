from django.test import SimpleTestCase

# Create your tests here.
class TestNearHundred(SimpleTestCase):
    def test_near_hundred(self):
        response = self.client.get("/warmup_1/near_hundred/93/")
        self.assertContains(response, True)

    def test_near_hundred(self):
        response = self.client.get("/warmup_1/near_hundred/90/")
        self.assertContains(response, True)

    def test_near_hundred(self):
        response = self.client.get("/warmup_1/near_hundred/89/")
        self.assertContains(response, False)

class TestStringSplosion(SimpleTestCase):
    def test_string_splosion(self):
        response = self.client.get("/warmup_2/string-splosion/Code/")
        self.assertContains(response, 'Code')

    def test_string_splosion(self):
        response = self.client.get("/warmup_2/string-splosion/abc/")
        self.assertContains(response, 'abc')

    def test_string_splosion(self):
        response = self.client.get("/warmup_2/string-splosion/ab/")
        self.assertContains(response, 'ab')

class TestCatDog(SimpleTestCase):
    def test_cat_dog(self):
        response = self.client.get("/string_2/cat_dog/catdog/")
        self.assertContains(response, True)
    def test_cat_dog(self):
        response = self.client.get("/string_2/cat_dog/catcat/")
        self.assertContains(response, False)

    def test_cat_dog(self):
        response = self.client.get("/string_2/cat_dog/1cat1cadodog/")
        self.assertContains(response, True)

class TestLoneSum(SimpleTestCase):
    def test_lone_sum(self):
        response = self.client.get("/logic_2/lone_sum/1/2/3/")
        self.assertContains(response, 6)

    def test_lone_sum(self):
        response = self.client.get("/logic_2/lone_sum/3/2/3/")
        self.assertContains(response, 2)

    def test_lone_sum(self):
        response = self.client.get("/logic_2/lone_sum/3/3/3/")
        self.assertContains(response, 0)