from django.test import TestCase

from .models import MajorReservoirs, RWPAs
import string


class MajorReservoirsModelTests(TestCase):

    def test_string_representation(self):
        """
        Test the string representation of the model return the Reservoir Label
        """
        response = MajorReservoirs(res_lbl="Brand New Reservoir")
        self.assertEqual(str(response), response.res_lbl)

    def test_verbose_name_representations(self):
        """
        Test the name representations are formatted correctly
        """
        self.assertEqual(str(MajorReservoirs._meta.verbose_name),
                         "Major Reservoir")
        self.assertEqual(str(MajorReservoirs._meta.verbose_name_plural),
                         "Major Reservoirs")


class RWPAsModelTests(TestCase):

    def test_string_representation(self):
        """
        Test the string representation of the model return the Region Name
        """
        response = RWPAs(reg_name="Brand New Region")
        self.assertEqual(str(response), response.reg_name)

    def test_verbose_name_representations(self):
        """
        Test the name representations are formatted correctly
        """
        self.assertEqual(str(RWPAs._meta.verbose_name), "RWPA")
        self.assertEqual(str(RWPAs._meta.verbose_name_plural), "RWPAs")


class URLTests(TestCase):

    def test_homepage(self):
        """
        Test the homepage URL
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_region_pages(self):
        """
        Test the correct region URLs /A - /P
        """
        good_letters = string.ascii_uppercase[:16]
        for l in good_letters:
            response = self.client.get('/' + l)
            self.assertEqual(response.status_code, 301)

        """
        Test the incorrect region URLs /Q - /Z
        """
        bad_letters = string.ascii_uppercase[16:]
        for l in bad_letters:
            response = self.client.get('/' + l)
            self.assertEqual(response.status_code, 404)

        """
        Test the correct region redirect URLs /a - /p
        """
        good_letters = string.ascii_lowercase[:16]
        for l in good_letters:
            response = self.client.get('/' + l)
            self.assertEqual(response.status_code, 301)

        """
        Test the incorrect region redirect URLs /q - /z
        """
        bad_letters = string.ascii_lowercase[16:]
        for l in bad_letters:
            response = self.client.get('/' + l)
            self.assertEqual(response.status_code, 404)
