from django.test import TestCase
from django.urls import reverse
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


class ViewTests(TestCase):

    def test_index_context(self):
        """
        Test the layer config object in context
        """
        response = self.client.get(reverse('map:index'))
        config = response.context['layers']
        check_layers = ['rwpas', 'reservoirs']
        check_keys = ['table_name', 'label_field', 'carto_css',
                      'interactivity']

        # check that the 2 layers are in config with proper keys
        for layer in check_layers:
            self.assertIs(layer in config.keys(), True)
            # check the keys of those 2 layers
            layer_info = config[layer]
            for key in check_keys:
                self.assertIs(key in layer_info.keys(), True)
            # check the value type for each key
            self.assertIs(isinstance(layer_info['table_name'], str), True)
            self.assertIs(isinstance(layer_info['label_field'], str), True)
            self.assertIs(isinstance(layer_info['carto_css'], str), True)
            self.assertIs(isinstance(layer_info['interactivity'], list), True)
            # verify 2 layer fields: 1 for region letter, 1 for name
            self.assertEqual(len(layer_info['interactivity']), 2)

    def test_index_templates(self):
        """
        Test the index view templates include required leaflet
        """
        leaflet_templates = ['leaflet/js.html', 'leaflet/css.html',
                             'leaflet/_leaflet_map.html']
        index_template = 'map/index.html'

        response = self.client.get('/')
        template_names = []
        for t in response.templates:
            template_names.append(t.name)

        for lt in leaflet_templates:
            self.assertIs(lt in template_names, True)
        self.assertIs(index_template in template_names, True)
