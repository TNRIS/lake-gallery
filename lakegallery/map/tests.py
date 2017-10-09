from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
from bs4 import BeautifulSoup

from django.contrib.gis.geos import Polygon, MultiPolygon

from .models import (MajorReservoirs, RWPAs, HistoricalAerialLinks,
                     StoryContent, LakeStatistics, get_upload_path)
from .views import (get_region_header_list, get_lake_header_list)
import string
import os

p1 = Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))
p2 = Polygon(((1, 1), (1, 2), (2, 2), (1, 1)))
test_geom = MultiPolygon(p1, p2)


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


class HistoricalAerialLinksModelTests(TestCase):

    def test_string_representation(self):
        """
        Test the string representation of the model returns the link URL
        """
        response = HistoricalAerialLinks(link="http://google.com")
        self.assertEqual(str(response), response.link)

    def test_verbose_name_representations(self):
        """
        Test the name representations are formatted correctly
        """
        self.assertEqual(str(HistoricalAerialLinks._meta.verbose_name),
                         "Historical Aerial Link")
        self.assertEqual(str(HistoricalAerialLinks._meta.verbose_name_plural),
                         "Historical Aerial Links")

    def test_dictionary_method(self):
        """
        Test the dictionary method as a response with the link & year
        """
        response = HistoricalAerialLinks(link="http://google.com", year=1970)
        dictionary = response.as_dict()
        self.assertIs(isinstance(dictionary, dict), True)
        self.assertIs(isinstance(dictionary['link'], str), True)
        self.assertIs(isinstance(dictionary['year'], int), True)
        self.assertEqual(response.link, "http://google.com")
        self.assertEqual(response.year, 1970)

    def test_field_types(self):
        """
        Test the fields will error if not the correct types
        """
        MajorReservoirs(res_lbl="Lake Travis", geom=test_geom).save()
        m = MajorReservoirs.objects.get(res_lbl="Lake Travis")
        response = HistoricalAerialLinks(link="not a URL",
                                         year="string", lake=m)
        try:
            response.full_clean()
        except ValidationError as e:
            error = dict(e)
            self.assertEqual(error['year'], ["'string' value must be an "
                                             "integer."])
            self.assertEqual(error['link'], ['Enter a valid URL.'])

    def test_key_relationship_requirement(self):
        """
        Test the 'lake' ForeignKey field requirement
        """
        with self.assertRaises(ValueError) as e:
            HistoricalAerialLinks(link='http://google.com', year=1970,
                                  lake="lake")
        assert ('"HistoricalAerialLinks.lake" must be a "MajorReservoirs"'
                ' instance' in str(e.exception))


class StoryContentModelTests(TestCase):

    def test_verbose_name_representations(self):
        """
        Test the name representations are formatted correctly
        """
        self.assertEqual(str(StoryContent._meta.verbose_name),
                         "Story Content")
        self.assertEqual(str(StoryContent._meta.verbose_name_plural),
                         "Story Content")

    def test_tags(self):
        """
        Test the photo tag image sources
        """
        lake_name = "Lake Travis"
        MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
        m = MajorReservoirs.objects.get(res_lbl=lake_name)

        test_file = 'test.png'
        good_url = settings.MEDIA_URL + os.path.join(lake_name, test_file)
        s = StoryContent(lake=m)

        # history tag
        s.history_photo = get_upload_path(s, test_file)
        soup = BeautifulSoup(s.hist_tag(), "html.parser")
        src = soup.findAll('img')[0]['src']
        self.assertEqual(src, good_url)

        # section one tag
        s.section_one_photo = get_upload_path(s, test_file)
        soup = BeautifulSoup(s.one_tag(), "html.parser")
        src = soup.findAll('img')[0]['src']
        self.assertEqual(src, good_url)

        # section two tag
        s.section_two_photo = get_upload_path(s, test_file)
        soup = BeautifulSoup(s.two_tag(), "html.parser")
        src = soup.findAll('img')[0]['src']
        self.assertEqual(src, good_url)

        # section three tag
        s.section_three_photo = get_upload_path(s, test_file)
        soup = BeautifulSoup(s.three_tag(), "html.parser")
        src = soup.findAll('img')[0]['src']
        self.assertEqual(src, good_url)

    def test_key_relationship_requirement(self):
        """
        Test the 'lake' OneToOne relationship field requirement
        """
        with self.assertRaises(ValueError) as e:
            StoryContent(summary="text here", history="text there",
                         lake="lake")
        assert ('"StoryContent.lake" must be a "MajorReservoirs" instance' in
                str(e.exception))


class LakeStatisticsModelTests(TestCase):

    def test_verbose_name_representations(self):
        """
        Test the name representations are formatted correctly
        """
        self.assertEqual(str(LakeStatistics._meta.verbose_name),
                         "Lake Statistics")
        self.assertEqual(str(LakeStatistics._meta.verbose_name_plural),
                         "Lake Statistics")

    def test_lake_only_requirement(self):
        """
        Test the lake property will error if not designated
        """
        response = LakeStatistics()
        try:
            response.full_clean()
        except ValidationError as e:
            error = dict(e)
            self.assertEqual(error['lake'], ['This field cannot be null.'])

    def test_key_relationship_requirement(self):
        """
        Test the 'lake' OneToOne relationship field requirement
        """
        with self.assertRaises(ValueError) as e:
            LakeStatistics(lake="lake")
        assert ('"LakeStatistics.lake" must be a "MajorReservoirs" instance' in
                str(e.exception))

    def test_string_numbers_method(self):
        """
        Test the float numbers to strings method
        """
        lake_name = "Lake Travis"
        MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
        m = MajorReservoirs.objects.get(res_lbl=lake_name)
        response = LakeStatistics(lake=m, dam_height=4.3)
        str_res = response.string_numbers()
        flds = str_res._meta.get_fields()
        for f in flds:
            attr = getattr(response, f.name)
            attr_type = type(attr)
            self.assertNotEqual(str(attr_type), 'float')
            self.assertNotEqual(str(attr)[-2:], '.0')

    def test_set_displays_method(self):
        """
        Test the set displays formatting method
        """
        lake_name = "Lake Travis"
        MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
        m = MajorReservoirs.objects.get(res_lbl=lake_name)
        # test display no statistics
        response = LakeStatistics(lake=m)
        dis_res = response.set_displays()
        self.assertIs(dis_res.general_stats, False)
        self.assertIs(dis_res.dam_stats, False)
        self.assertEqual(type(dis_res.primary_purposes), str)
        minimum_defaults = [0.0, 0, "0.0", "", None, "None"]
        for s in dis_res.stat_defaults:
            self.assertTrue(s in minimum_defaults)
        # test display only general stats
        response = LakeStatistics(lake=m, original_name="Lake Water")
        dis_res = response.set_displays()
        self.assertIs(dis_res.general_stats, True)
        self.assertIs(dis_res.dam_stats, False)
        # test display dam stats also displays general stats header
        response = LakeStatistics(lake=m, top_of_dam=32.4)
        dis_res = response.set_displays()
        self.assertIs(dis_res.general_stats, True)
        self.assertIs(dis_res.dam_stats, True)


class functionTests(TestCase):

    def test_upload_path(self):
        """
        Test the upload path generator function
        """
        lake_name = "Lake Travis"
        MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
        m = MajorReservoirs.objects.get(res_lbl=lake_name)
        response = StoryContent(lake=m)
        path = get_upload_path(response, "photo.png")
        self.assertEqual(path, os.path.join(lake_name, "photo.png"))


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

    def test_story_pages(self):
        """
        Test lake story page urls
        """
        lake_name = "Lake Travis"
        lake_region = "K"
        MajorReservoirs(res_lbl=lake_name, region=lake_region,
                        geom=test_geom).save()
        m = MajorReservoirs.objects.get(res_lbl=lake_name)
        StoryContent(lake=m)
        # test successful query for lake
        response = self.client.get('/' + lake_region + '/' + lake_name)
        self.assertEqual(response.status_code, 200)
        # test bad region for lake in URL
        response = self.client.get('/A/' + lake_name)
        self.assertEqual(response.status_code, 404)
        # test redirect if lowercase region supplied
        response = self.client.get('/' + lake_region.lower() + '/' + lake_name)
        self.assertEqual(response.status_code, 302)


class ViewTests(TestCase):

    def test_header_lists(self):
        """
        Test the header lists generated
        """
        region_nm_1, region_lt_1 = 'rwpa 1', 'A'
        region_nm_2, region_lt_2 = 'rwpa 2', 'B'
        RWPAs(objectid=1, reg_name=region_nm_1, letter=region_lt_1,
              shape_leng=10, shape_area=2, geom=test_geom).save()
        RWPAs(objectid=2, reg_name=region_nm_2, letter=region_lt_2,
              shape_leng=10, shape_area=2, geom=test_geom).save()
        res_nm_1, res_lt_1 = 'mr 1', 'A'
        res_nm_2, res_lt_2 = 'mr 2', 'B'
        MajorReservoirs(res_lbl=res_nm_1, region=res_lt_1,
                        geom=test_geom).save()
        MajorReservoirs(res_lbl=res_nm_2, region=res_lt_2,
                        geom=test_geom).save()

        reg_list = get_region_header_list()
        self.assertEqual(reg_list, [{'name': region_nm_1,
                                     'letter': region_lt_1},
                                    {'name': region_nm_2,
                                     'letter': region_lt_2}])
        res_list = get_lake_header_list()
        self.assertEqual(res_list, [{'name': res_nm_1,
                                     'region': res_lt_1},
                                    {'name': res_nm_2,
                                     'region': res_lt_2}])

    def test_index_context(self):
        """
        Test the index template context; config & header lists
        """
        response = self.client.get(reverse('map:index'))
        config = response.context['layers']
        check_layers = ['rwpas', 'reservoirs']
        check_keys = ['table_name', 'label_field', 'carto_css',
                      'carto_lbl', 'interactivity']

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
            self.assertIs(isinstance(layer_info['carto_lbl'], str), True)
            self.assertIs(isinstance(layer_info['interactivity'], list), True)
            # verify 2 layer fields: 1 for region letter, 1 for name
            self.assertEqual(len(layer_info['interactivity']), 2)

        # although the header functions are tested above, we will retest them
        # here to verify they are in the context
        region_nm_1, region_lt_1 = 'rwpa 1', 'A'
        region_nm_2, region_lt_2 = 'rwpa 2', 'B'
        RWPAs(objectid=1, reg_name=region_nm_1, letter=region_lt_1,
              shape_leng=10, shape_area=2, geom=test_geom).save()
        RWPAs(objectid=2, reg_name=region_nm_2, letter=region_lt_2,
              shape_leng=10, shape_area=2, geom=test_geom).save()
        res_nm_1, res_lt_1 = 'mr 1', 'A'
        res_nm_2, res_lt_2 = 'mr 2', 'B'
        MajorReservoirs(res_lbl=res_nm_1, region=res_lt_1,
                        geom=test_geom).save()
        MajorReservoirs(res_lbl=res_nm_2, region=res_lt_2,
                        geom=test_geom).save()
        response = self.client.get(reverse('map:index'))
        hdr_reg = response.context['header_regions']
        self.assertEqual(hdr_reg, [{'name': region_nm_1,
                                    'letter': region_lt_1},
                                   {'name': region_nm_2,
                                    'letter': region_lt_2}])
        hdr_lks = response.context['header_lakes']
        self.assertEqual(hdr_lks, [{'name': res_nm_1,
                                    'region': res_lt_1},
                                   {'name': res_nm_2,
                                    'region': res_lt_2}])

    def test_story_context(self):
        """
        Test the story template context; header lists
        """
        # although the header functions are tested above, we will retest them
        # here to verify they are in the context
        region_nm_1, region_lt_1 = 'rwpa 1', 'A'
        region_nm_2, region_lt_2 = 'rwpa 2', 'B'
        RWPAs(objectid=1, reg_name=region_nm_1, letter=region_lt_1,
              shape_leng=10, shape_area=2, geom=test_geom).save()
        RWPAs(objectid=2, reg_name=region_nm_2, letter=region_lt_2,
              shape_leng=10, shape_area=2, geom=test_geom).save()
        res_nm_1, res_lt_1 = 'mr one', 'A'
        res_nm_2, res_lt_2 = 'mr two', 'B'
        MajorReservoirs(res_lbl=res_nm_1, region=res_lt_1,
                        geom=test_geom).save()
        MajorReservoirs(res_lbl=res_nm_2, region=res_lt_2,
                        geom=test_geom).save()
        m = MajorReservoirs.objects.get(res_lbl='mr one')
        StoryContent(lake=m, summary="text here", history="text there").save()

        response = self.client.get(reverse('map:story', args=['A', 'mr one']))
        hdr_reg = response.context['header_regions']
        self.assertEqual(hdr_reg, [{'name': region_nm_1,
                                    'letter': region_lt_1},
                                   {'name': region_nm_2,
                                    'letter': region_lt_2}])
        hdr_lks = response.context['header_lakes']
        self.assertEqual(hdr_lks, [{'name': res_nm_1,
                                    'region': res_lt_1},
                                   {'name': res_nm_2,
                                    'region': res_lt_2}])

        # check the layer info
        config = response.context['layer']
        check_keys = ['table_name', 'label_field', 'carto_css',
                      'carto_lbl', 'interactivity']
        # check the keys of the layer config
        for key in check_keys:
            self.assertIs(key in config.keys(), True)
        # check the value type for each key
        self.assertIs(isinstance(config['table_name'], str), True)
        self.assertIs(isinstance(config['label_field'], str), True)
        self.assertIs(isinstance(config['carto_css'], str), True)
        self.assertIs(isinstance(config['carto_lbl'], str), True)
        self.assertIs(isinstance(config['interactivity'], list), True)
        # verify 2 layer fields: 1 for region letter, 1 for name
        self.assertEqual(len(config['interactivity']), 2)

        # check the story content in context referencing the table
        c = StoryContent.objects.get(lake=m)
        self.assertEqual(response.context['story'], c)

        # check the lake in context is referencing the url lake
        lake_in_url = response.request['PATH_INFO'].split("/")[2]
        self.assertEqual(response.context['lake'], lake_in_url)

        # check that links is a key in the context
        self.assertIs('links' in response.context, True)
        self.assertIs(isinstance(response.context['links'], list),
                      True)

    def test_templates(self):
        """
        Test view templates include required leaflet and html
        """
        leaflet_templates = ['leaflet/js.html', 'leaflet/css.html',
                             'leaflet/_leaflet_map.html']
        base_template = 'map/base.html'
        index_template = 'map/index.html'
        story_template = 'map/story.html'

        # index template
        response = self.client.get('/')
        template_names = []
        for t in response.templates:
            template_names.append(t.name)

        for lt in leaflet_templates:
            self.assertIs(lt in template_names, True)
        self.assertIs(index_template in template_names, True)
        self.assertIs(base_template in template_names, True)

        # story template
        MajorReservoirs(res_lbl='Lake Tester', region='A',
                        geom=test_geom).save()
        m = MajorReservoirs.objects.get(res_lbl='Lake Tester')
        StoryContent(lake=m, summary="text here", history="text there").save()

        response = self.client.get('/A/Lake%20Tester')
        template_names = []
        for t in response.templates:
            template_names.append(t.name)

        for lt in leaflet_templates:
            self.assertIs(lt in template_names, True)
        self.assertIs(story_template in template_names, True)
        self.assertIs(base_template in template_names, True)
