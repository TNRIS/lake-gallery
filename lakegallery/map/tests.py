# from django.test import Client, TestCase
# from django.urls import reverse
# from django.conf import settings
# from django.core.exceptions import ValidationError
# from bs4 import BeautifulSoup
# from django.http import HttpRequest

# from django.contrib.staticfiles import finders

# from django.contrib.gis.geos import Point, Polygon, MultiPolygon

# from .models import (MajorReservoirs, RWPAs, HistoricalAerialLinks,
#                      StoryContent, LakeStatistics, SignificantEvents,
#                      BoatRamps, ChannelMarkers, Hazards, Parks,
#                      get_upload_path)
# from .views import (get_region_header_list, get_lake_header_list)
# from .config import overlays
# from .validators import validate_past_dates

# from middleware import MobileDetectionMiddleware

# import string
# import os
# import datetime

# test_point = Point((1, 1), (1, 2))
# p1 = Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))
# p2 = Polygon(((1, 1), (1, 2), (2, 2), (1, 1)))
# test_geom = MultiPolygon(p1, p2)


# class MajorReservoirsModelTests(TestCase):

#     def test_string_representation(self):
#         """
#         Test the string representation of the model return the Reservoir Label
#         """
#         response = MajorReservoirs(res_lbl="Brand New Reservoir")
#         self.assertEqual(str(response), response.res_lbl)

#     def test_verbose_name_representations(self):
#         """
#         Test the name representations are formatted correctly
#         """
#         self.assertEqual(str(MajorReservoirs._meta.verbose_name),
#                          "Major Reservoir")
#         self.assertEqual(str(MajorReservoirs._meta.verbose_name_plural),
#                          "Major Reservoirs")


# class HistoricalAerialLinksModelTests(TestCase):

#     def test_string_representation(self):
#         """
#         Test the string representation of the model returns the link URL
#         """
#         response = HistoricalAerialLinks(link="http://google.com")
#         self.assertEqual(str(response), response.link)

#     def test_verbose_name_representations(self):
#         """
#         Test the name representations are formatted correctly
#         """
#         self.assertEqual(str(HistoricalAerialLinks._meta.verbose_name),
#                          "Historical Aerial Link")
#         self.assertEqual(str(HistoricalAerialLinks._meta.verbose_name_plural),
#                          "Historical Aerial Links")

#     def test_dictionary_method(self):
#         """
#         Test the dictionary method as a response with the link & year
#         """
#         response = HistoricalAerialLinks(link="http://google.com", year=1970)
#         dictionary = response.as_dict()
#         self.assertIs(isinstance(dictionary, dict), True)
#         self.assertIs(isinstance(dictionary['link'], str), True)
#         self.assertIs(isinstance(dictionary['year'], int), True)
#         self.assertEqual(response.link, "http://google.com")
#         self.assertEqual(response.year, 1970)

#     def test_field_types(self):
#         """
#         Test the fields will error if not the correct types
#         """
#         MajorReservoirs(res_lbl="Lake Travis", geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl="Lake Travis")
#         response = HistoricalAerialLinks(link="not a URL",
#                                          year="string", lake=m)
#         try:
#             response.full_clean()
#         except ValidationError as e:
#             error = dict(e)
#             self.assertEqual(error['year'], ["'string' value must be an "
#                                              "integer."])
#             self.assertEqual(error['link'], ['Enter a valid URL.'])

#     def test_key_relationship_requirement(self):
#         """
#         Test the 'lake' ForeignKey field requirement
#         """
#         with self.assertRaises(ValueError) as e:
#             HistoricalAerialLinks(link='http://google.com', year=1970,
#                                   lake="lake")
#         assert ('"HistoricalAerialLinks.lake" must be a "MajorReservoirs"'
#                 ' instance' in str(e.exception))


# class StoryContentModelTests(TestCase):

#     def test_string_representation(self):
#         """
#         Test the string representation of the model return the Lake name
#         """
#         lake_name = "Lake Travis"
#         MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)
#         response = StoryContent(lake=m)
#         self.assertEqual(str(response), lake_name)

#     def test_verbose_name_representations(self):
#         """
#         Test the name representations are formatted correctly
#         """
#         self.assertEqual(str(StoryContent._meta.verbose_name),
#                          "Story Content")
#         self.assertEqual(str(StoryContent._meta.verbose_name_plural),
#                          "Story Content")

#     def test_tags(self):
#         """
#         Test the photo tag image sources
#         """
#         lake_name = "Lake Travis"
#         MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)

#         test_file = 'test.png'
#         good_url = settings.MEDIA_URL + os.path.join(lake_name, test_file)
#         s = StoryContent(lake=m)

#         # summary main tag
#         s.summary_photo_main = get_upload_path(s, test_file)
#         soup = BeautifulSoup(s.summ_main_tag(), "html.parser")
#         src = soup.findAll('img')[0]['src']
#         self.assertEqual(src, good_url)

#         # history main tag
#         s.history_photo_main = get_upload_path(s, test_file)
#         soup = BeautifulSoup(s.hist_main_tag(), "html.parser")
#         src = soup.findAll('img')[0]['src']
#         self.assertEqual(src, good_url)

#         # history tag
#         s.history_photo = get_upload_path(s, test_file)
#         soup = BeautifulSoup(s.hist_tag(), "html.parser")
#         src = soup.findAll('img')[0]['src']
#         self.assertEqual(src, good_url)

#         # section one main tag
#         s.section_one_photo_main = get_upload_path(s, test_file)
#         soup = BeautifulSoup(s.one_main_tag(), "html.parser")
#         src = soup.findAll('img')[0]['src']
#         self.assertEqual(src, good_url)

#         # section one tag
#         s.section_one_photo = get_upload_path(s, test_file)
#         soup = BeautifulSoup(s.one_tag(), "html.parser")
#         src = soup.findAll('img')[0]['src']
#         self.assertEqual(src, good_url)

#         # section two main tag
#         s.section_two_photo_main = get_upload_path(s, test_file)
#         soup = BeautifulSoup(s.two_main_tag(), "html.parser")
#         src = soup.findAll('img')[0]['src']
#         self.assertEqual(src, good_url)

#         # section two tag
#         s.section_two_photo = get_upload_path(s, test_file)
#         soup = BeautifulSoup(s.two_tag(), "html.parser")
#         src = soup.findAll('img')[0]['src']
#         self.assertEqual(src, good_url)

#         # section three main tag
#         s.section_three_photo_main = get_upload_path(s, test_file)
#         soup = BeautifulSoup(s.three_main_tag(), "html.parser")
#         src = soup.findAll('img')[0]['src']
#         self.assertEqual(src, good_url)

#         # section three tag
#         s.section_three_photo = get_upload_path(s, test_file)
#         soup = BeautifulSoup(s.three_tag(), "html.parser")
#         src = soup.findAll('img')[0]['src']
#         self.assertEqual(src, good_url)

#     def test_key_relationship_requirement(self):
#         """
#         Test the 'lake' OneToOne relationship field requirement
#         """
#         with self.assertRaises(ValueError) as e:
#             StoryContent(summary="text here", history="text there",
#                          lake="lake")
#         assert ('"StoryContent.lake" must be a "MajorReservoirs" instance' in
#                 str(e.exception))


# class LakeStatisticsModelTests(TestCase):

#     def test_string_representation(self):
#         """
#         Test the string representation of the model return the Lake name
#         """
#         lake_name = "Lake Travis"
#         MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)
#         response = LakeStatistics(lake=m)
#         self.assertEqual(str(response), lake_name)

#     def test_verbose_name_representations(self):
#         """
#         Test the name representations are formatted correctly
#         """
#         self.assertEqual(str(LakeStatistics._meta.verbose_name),
#                          "Lake Statistics")
#         self.assertEqual(str(LakeStatistics._meta.verbose_name_plural),
#                          "Lake Statistics")

#     def test_lake_only_requirement(self):
#         """
#         Test the lake property will error if not designated
#         """
#         response = LakeStatistics()
#         try:
#             response.full_clean()
#         except ValidationError as e:
#             error = dict(e)
#             self.assertEqual(error['lake'], ['This field cannot be null.'])

#     def test_key_relationship_requirement(self):
#         """
#         Test the 'lake' OneToOne relationship field requirement
#         """
#         with self.assertRaises(ValueError) as e:
#             LakeStatistics(lake="lake")
#         assert ('"LakeStatistics.lake" must be a "MajorReservoirs" instance' in
#                 str(e.exception))

#     def test_string_numbers_method(self):
#         """
#         Test the float numbers to strings method
#         """
#         lake_name = "Lake Travis"
#         MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)
#         response = LakeStatistics(lake=m, dam_height=4.3)
#         str_res = response.string_numbers()
#         flds = str_res._meta.get_fields()
#         for f in flds:
#             attr = getattr(response, f.name)
#             attr_type = type(attr)
#             self.assertNotEqual(str(attr_type), 'float')
#             self.assertNotEqual(str(attr)[-2:], '.0')

#     def test_set_displays_method(self):
#         """
#         Test the set displays formatting method
#         """
#         lake_name = "Lake Travis"
#         MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)
#         # test display no statistics
#         response = LakeStatistics(lake=m)
#         dis_res = response.set_displays()
#         self.assertIs(dis_res.general_stats, False)
#         self.assertIs(dis_res.dam_stats, False)
#         self.assertEqual(type(dis_res.primary_purposes), str)
#         minimum_defaults = [0.0, 0, "0", "0.0", "", None, "None"]
#         for s in dis_res.stat_defaults:
#             self.assertTrue(s in minimum_defaults)
#         # test display only general stats
#         response = LakeStatistics(lake=m, original_name="Lake Water")
#         dis_res = response.set_displays()
#         self.assertIs(dis_res.general_stats, True)
#         self.assertIs(dis_res.dam_stats, False)
#         # test display dam stats also displays general stats header
#         response = LakeStatistics(lake=m, top_of_dam=32.4)
#         dis_res = response.set_displays()
#         self.assertIs(dis_res.general_stats, True)
#         self.assertIs(dis_res.dam_stats, True)


# class SignificantEventsModelTests(TestCase):

#     def test_string_representation(self):
#         """
#         Test the string representation of the model returns the binary
#         event type with the date
#         """
#         lake_name = "Lake Travis"
#         MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)

#         today = datetime.datetime.today()
#         dt = str(today.year) + "-" + str(today.month) + "-" + str(today.day)
#         response = SignificantEvents(lake=m, event_type='High',
#                                      date=dt, height=99.99)
#         expected = lake_name + " " + response.event_type + " " + dt
#         self.assertEqual(str(response), expected)

#     def test_verbose_name_representations(self):
#         """
#         Test the name representations are formatted correctly
#         """
#         self.assertEqual(str(SignificantEvents._meta.verbose_name),
#                          "Significant Event")
#         self.assertEqual(str(SignificantEvents._meta.verbose_name_plural),
#                          "Significant Events")

#     def test_key_relationship_requirement(self):
#         """
#         Test the 'lake' ForeignKey field requirement
#         """
#         today = datetime.datetime.today()
#         dt = str(today.year) + "-" + str(today.month) + "-" + str(today.day)
#         with self.assertRaises(ValueError) as e:
#             SignificantEvents(lake="lake", event_type='High',
#                               date=dt, height=99.99)
#         assert ('"SignificantEvents.lake" must be a "MajorReservoirs"'
#                 ' instance' in str(e.exception))

#     def test_requirements(self):
#         """
#         Test the lake, event type, date, and height required
#         """
#         response = SignificantEvents()
#         try:
#             response.full_clean()
#         except ValidationError as e:
#             error = dict(e)
#             self.assertEqual(error['lake'], ['This field cannot be null.'])
#             self.assertEqual(error['date'], ['This field cannot be null.'])
#             self.assertEqual(error['height'], ['This field cannot be null.'])

#     def test_dictionary_method(self):
#         """
#         Test the dictionary method as a response with date, height, and drought
#         """
#         today = datetime.datetime.today()
#         dt = str(today.year) + "-" + str(today.month) + "-" + str(today.day)

#         lake_name = "Lake Travis"
#         MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)

#         response = SignificantEvents(lake=m, date=dt, height=99.99)
#         dictionary = response.as_dict()
#         self.assertIs(isinstance(dictionary, dict), True)
#         self.assertIs(isinstance(dictionary['date'], str), True)
#         self.assertIs(isinstance(dictionary['height'], float), True)
#         self.assertIs(isinstance(dictionary['drought'], str), True)
#         self.assertEqual(dictionary['date'], dt)
#         self.assertEqual(dictionary['height'], 99.99)
#         self.assertEqual(dictionary['drought'], "")
#         # since we're here, might as well test event_type defaults to 'High'
#         self.assertEqual(response.event_type, 'High')


# class BoatRampsModelTests(TestCase):

#     def test_string_representation(self):
#         """
#         Test the string representation of the model return boat ramp name
#         """
#         lake_name = "Lake Travis"
#         MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)

#         response = BoatRamps(lake=m, name="Rampage")
#         self.assertEqual(str(response), response.name)

#     def test_verbose_name_representations(self):
#         """
#         Test the name representations are formatted correctly
#         """
#         self.assertEqual(str(BoatRamps._meta.verbose_name), "Boat Ramp")
#         self.assertEqual(str(BoatRamps._meta.verbose_name_plural),
#                          "Boat Ramps")

#     def test_key_relationship_requirement(self):
#         """
#         Test the 'lake' ForeignKey field requirement
#         """
#         with self.assertRaises(ValueError) as e:
#             BoatRamps(lake="lake", geom=test_point)
#         assert ('"BoatRamps.lake" must be a "MajorReservoirs"'
#                 ' instance' in str(e.exception))


# class ChannelMarkersModelTests(TestCase):

#     def test_string_representation(self):
#         """
#         Test the string representation of the model return lake & marker id
#         """
#         lake_name = "Lake Travis"
#         MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)

#         marker_id = 21
#         response = ChannelMarkers(lake=m, marker_id=marker_id)
#         expected = str(response.lake) + " " + str(response.marker_id)
#         self.assertEqual(str(response), expected)

#     def test_verbose_name_representations(self):
#         """
#         Test the name representations are formatted correctly
#         """
#         self.assertEqual(str(ChannelMarkers._meta.verbose_name),
#                          "Channel Marker")
#         self.assertEqual(str(ChannelMarkers._meta.verbose_name_plural),
#                          "Channel Markers")

#     def test_key_relationship_requirement(self):
#         """
#         Test the 'lake' ForeignKey field requirement
#         """
#         with self.assertRaises(ValueError) as e:
#             ChannelMarkers(lake="lake", geom=test_point)
#         assert ('"ChannelMarkers.lake" must be a "MajorReservoirs"'
#                 ' instance' in str(e.exception))


# class HazardsModelTests(TestCase):

#     def test_string_representation(self):
#         """
#         Test the string representation of the model return lake & hazard type
#         """
#         lake_name = "Lake Travis"
#         MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)

#         hzd = 'No Wake'
#         response = Hazards(lake=m, hazard_type=hzd)
#         expected = str(response.lake) + " " + response.hazard_type
#         self.assertEqual(str(response), expected)

#     def test_verbose_name_representations(self):
#         """
#         Test the name representations are formatted correctly
#         """
#         self.assertEqual(str(Hazards._meta.verbose_name), "Hazard")
#         self.assertEqual(str(Hazards._meta.verbose_name_plural),
#                          "Hazards")

#     def test_key_relationship_requirement(self):
#         """
#         Test the 'lake' ForeignKey field requirement
#         """
#         with self.assertRaises(ValueError) as e:
#             Hazards(lake="lake", geom=test_point)
#         assert ('"Hazards.lake" must be a "MajorReservoirs"'
#                 ' instance' in str(e.exception))


# class ParksModelTests(TestCase):

#     def test_string_representation(self):
#         """
#         Test the string representation of the model returns park name
#         """
#         lake_name = "Lake Travis"
#         MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)

#         park_type = 'Preserve'
#         nm = "Parky-Park"
#         response = Parks(lake=m, park_type=park_type, name=nm)
#         self.assertEqual(str(response), response.name)

#     def test_verbose_name_representations(self):
#         """
#         Test the name representations are formatted correctly
#         """
#         self.assertEqual(str(Hazards._meta.verbose_name), "Hazard")
#         self.assertEqual(str(Hazards._meta.verbose_name_plural),
#                          "Hazards")

#     def test_key_relationship_requirement(self):
#         """
#         Test the 'lake' ForeignKey field requirement
#         """
#         with self.assertRaises(ValueError) as e:
#             Hazards(lake="lake", geom=test_point)
#         assert ('"Hazards.lake" must be a "MajorReservoirs"'
#                 ' instance' in str(e.exception))


# class functionTests(TestCase):

#     def test_upload_path(self):
#         """
#         Test the upload path generator function
#         """
#         lake_name = "Lake Travis"
#         MajorReservoirs(res_lbl=lake_name, geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)
#         response = StoryContent(lake=m)
#         path = get_upload_path(response, "photo.png")
#         self.assertEqual(path, os.path.join(lake_name, "photo.png"))

#     def test_date_validator(self):
#         """
#         Test the past date validator function doesn't allow future dates
#         """
#         # past date should pass
#         yesterday = datetime.date.today() - datetime.timedelta(days=1)
#         self.assertEqual(validate_past_dates(yesterday), yesterday)
#         # current date should pass
#         today = datetime.date.today()
#         self.assertEqual(validate_past_dates(today), today)
#         # future date should fail
#         tomorrow = datetime.date.today() + datetime.timedelta(days=1)
#         with self.assertRaises(ValidationError) as e:
#             validate_past_dates(tomorrow)
#         assert ('The date cannot be in the future!' in str(e.exception))


# class URLTests(TestCase):

#     def test_homepage(self):
#         """
#         Test the homepage URL
#         """
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

#     def test_region_pages(self):
#         """
#         Test the correct region URLs /A - /P
#         """
#         good_letters = string.ascii_uppercase[:16]
#         for l in good_letters:
#             response = self.client.get('/' + l)
#             self.assertEqual(response.status_code, 301)

#         """
#         Test the incorrect region URLs /Q - /Z
#         """
#         bad_letters = string.ascii_uppercase[16:]
#         for l in bad_letters:
#             response = self.client.get('/' + l)
#             self.assertEqual(response.status_code, 404)

#         """
#         Test the correct region redirect URLs /a - /p
#         """
#         good_letters = string.ascii_lowercase[:16]
#         for l in good_letters:
#             response = self.client.get('/' + l)
#             self.assertEqual(response.status_code, 301)

#         """
#         Test the incorrect region redirect URLs /q - /z
#         """
#         bad_letters = string.ascii_lowercase[16:]
#         for l in bad_letters:
#             response = self.client.get('/' + l)
#             self.assertEqual(response.status_code, 404)

#     def test_story_pages(self):
#         """
#         Test lake story page urls
#         """
#         lake_name = "Lake Travis"
#         lake_region = "K"
#         MajorReservoirs(res_lbl=lake_name, region=lake_region,
#                         geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)
#         StoryContent(lake=m)
#         # test successful query for lake
#         response = self.client.get('/' + lake_region + '/' + lake_name)
#         self.assertEqual(response.status_code, 200)
#         # test bad region for lake in URL
#         response = self.client.get('/A/' + lake_name)
#         self.assertEqual(response.status_code, 404)
#         # test redirect if lowercase region supplied
#         response = self.client.get('/' + lake_region.lower() + '/' + lake_name)
#         self.assertEqual(response.status_code, 302)

#     def test_about(self):
#         """
#         Test the about page URL
#         """
#         response = self.client.get('/about/')
#         self.assertEqual(response.status_code, 200)
#         response = self.client.get('/about')
#         self.assertEqual(response.status_code, 301)


# class ViewTests(TestCase):

#     def test_header_lists(self):
#         """
#         Test the header lists generated
#         """
#         region_nm_1, region_lt_1 = 'rwpa 1', 'A'
#         region_nm_2, region_lt_2 = 'rwpa 2', 'B'
#         RWPAs(objectid=1, reg_name=region_nm_1, letter=region_lt_1,
#               shape_leng=10, shape_area=2, geom=test_geom).save()
#         RWPAs(objectid=2, reg_name=region_nm_2, letter=region_lt_2,
#               shape_leng=10, shape_area=2, geom=test_geom).save()
#         res_nm_1, res_lt_1 = 'mr 1', 'A'
#         res_nm_2, res_lt_2 = 'mr 2', 'B'
#         MajorReservoirs(res_lbl=res_nm_1, region=res_lt_1,
#                         geom=test_geom).save()
#         MajorReservoirs(res_lbl=res_nm_2, region=res_lt_2,
#                         geom=test_geom).save()

#         reg_list = get_region_header_list()
#         self.assertEqual(reg_list, [{'name': region_nm_1,
#                                      'letter': region_lt_1},
#                                     {'name': region_nm_2,
#                                      'letter': region_lt_2}])
#         res_list = get_lake_header_list()
#         self.assertEqual(res_list, [{'name': res_nm_1,
#                                      'region': res_lt_1,
#                                      'class': 'disabled'},
#                                     {'name': res_nm_2,
#                                      'region': res_lt_2,
#                                      'class': 'disabled'}])

#     def test_index_context(self):
#         """
#         Test the index template context; config & header lists
#         """
#         response = self.client.get(reverse('map:index'))
#         config = response.context['layers']
#         check_layers = ['rwpas', 'reservoirs']
#         check_keys = ['table_name', 'label_field', 'carto_css',
#                       'carto_lbl', 'interactivity']

#         # check that the 2 layers are in config with proper keys
#         for layer in check_layers:
#             self.assertIs(layer in config.keys(), True)
#             # check the keys of those 2 layers
#             layer_info = config[layer]
#             for key in check_keys:
#                 self.assertIs(key in layer_info.keys(), True)
#             # check the value type for each key
#             self.assertIs(isinstance(layer_info['table_name'], str), True)
#             self.assertIs(isinstance(layer_info['label_field'], str), True)
#             self.assertIs(isinstance(layer_info['carto_css'], str), True)
#             self.assertIs(isinstance(layer_info['carto_lbl'], str), True)
#             self.assertIs(isinstance(layer_info['interactivity'], list), True)
#             # verify 2 layer fields: 1 for region letter, 1 for name
#             self.assertEqual(len(layer_info['interactivity']), 2)

#         # although the header functions are tested above, we will retest them
#         # here to verify they are in the context
#         region_nm_1, region_lt_1 = 'rwpa 1', 'A'
#         region_nm_2, region_lt_2 = 'rwpa 2', 'B'
#         RWPAs(objectid=1, reg_name=region_nm_1, letter=region_lt_1,
#               shape_leng=10, shape_area=2, geom=test_geom).save()
#         RWPAs(objectid=2, reg_name=region_nm_2, letter=region_lt_2,
#               shape_leng=10, shape_area=2, geom=test_geom).save()
#         res_nm_1, res_lt_1 = 'mr 1', 'A'
#         res_nm_2, res_lt_2 = 'mr 2', 'B'
#         MajorReservoirs(res_lbl=res_nm_1, region=res_lt_1,
#                         geom=test_geom).save()
#         MajorReservoirs(res_lbl=res_nm_2, region=res_lt_2,
#                         geom=test_geom).save()
#         response = self.client.get(reverse('map:index'))
#         hdr_reg = response.context['header_regions']
#         self.assertEqual(hdr_reg, [{'name': region_nm_1,
#                                     'letter': region_lt_1},
#                                    {'name': region_nm_2,
#                                     'letter': region_lt_2}])
#         hdr_lks = response.context['header_lakes']
#         self.assertEqual(hdr_lks, [{'name': res_nm_1,
#                                     'region': res_lt_1,
#                                     'class': 'disabled'},
#                                    {'name': res_nm_2,
#                                     'region': res_lt_2,
#                                     'class': 'disabled'}])
#         # check the version number in the context
#         self.assertIs('version' in response.context, True)
#         self.assertEqual(response.context['version'], settings.VERSION)

#     def test_region_context(self):
#         """
#         Test the region template context; config & header lists
#         """
#         # although the header functions are tested above, we will retest them
#         # here to verify they are in the context
#         region_nm_1, region_lt_1 = 'rwpa 1', 'A'
#         region_nm_2, region_lt_2 = 'rwpa 2', 'B'
#         RWPAs(objectid=1, reg_name=region_nm_1, letter=region_lt_1,
#               shape_leng=10, shape_area=2, geom=test_geom).save()
#         RWPAs(objectid=2, reg_name=region_nm_2, letter=region_lt_2,
#               shape_leng=10, shape_area=2, geom=test_geom).save()
#         res_nm_1, res_lt_1 = 'mr 1', 'A'
#         res_nm_2, res_lt_2 = 'mr 2', 'B'
#         MajorReservoirs(res_lbl=res_nm_1, region=res_lt_1,
#                         geom=test_geom).save()
#         MajorReservoirs(res_lbl=res_nm_2, region=res_lt_2,
#                         geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl='mr 1')
#         StoryContent(lake=m, summary="text here", history="text there").save()

#         request_region = 'A'
#         response = self.client.get(reverse('map:region',
#                                    args=[request_region]))
#         hdr_reg = response.context['header_regions']
#         self.assertEqual(hdr_reg, [{'name': region_nm_1,
#                                     'letter': region_lt_1},
#                                    {'name': region_nm_2,
#                                     'letter': region_lt_2}])
#         hdr_lks = response.context['header_lakes']
#         # this also doubles down by testing the 'post_save' signal sent by
#         # editing a StoryContent record and it auto editing the associated
#         # major reservoir to be class=enabled
#         self.assertEqual(hdr_lks, [{'name': res_nm_1,
#                                     'region': res_lt_1,
#                                     'class': 'enabled'},
#                                    {'name': res_nm_2,
#                                     'region': res_lt_2,
#                                     'class': 'disabled'}])

#         config = response.context['layers']
#         check_layers = ['rwpas', 'reservoirs']
#         check_keys = ['table_name', 'label_field', 'carto_css',
#                       'carto_lbl', 'interactivity']

#         # check that the 2 layers are in config with proper keys
#         for layer in check_layers:
#             self.assertIs(layer in config.keys(), True)
#             # check the keys of those 2 layers
#             layer_info = config[layer]
#             for key in check_keys:
#                 self.assertIs(key in layer_info.keys(), True)
#             # check the value type for each key
#             self.assertIs(isinstance(layer_info['table_name'], str), True)
#             self.assertIs(isinstance(layer_info['label_field'], str), True)
#             self.assertIs(isinstance(layer_info['carto_css'], str), True)
#             self.assertIs(isinstance(layer_info['carto_lbl'], str), True)
#             self.assertIs(isinstance(layer_info['interactivity'], list), True)
#             # verify 2 layer fields: 1 for region letter, 1 for name
#             self.assertEqual(len(layer_info['interactivity']), 2)

#         # check context region passed through view function
#         self.assertIs('region' in response.context, True)
#         self.assertEqual(response.context['region'], request_region)

#         # check the extent in context
#         self.assertIs('extent' in response.context, True)
#         self.assertIs(isinstance(response.context['extent'], list), True)
#         self.assertEqual(len(response.context['extent']), 4)
#         for coordinate in response.context['extent']:
#             self.assertIs(type(coordinate), float)

#     def test_story_context(self):
#         """
#         Test the story template context; header lists
#         """
#         # although the header functions are tested above, we will retest them
#         # here to verify they are in the context
#         region_nm_1, region_lt_1 = 'rwpa 1', 'A'
#         region_nm_2, region_lt_2 = 'rwpa 2', 'B'
#         RWPAs(objectid=1, reg_name=region_nm_1, letter=region_lt_1,
#               shape_leng=10, shape_area=2, geom=test_geom).save()
#         RWPAs(objectid=2, reg_name=region_nm_2, letter=region_lt_2,
#               shape_leng=10, shape_area=2, geom=test_geom).save()
#         res_nm_1, res_lt_1 = 'mr one', 'A'
#         res_nm_2, res_lt_2 = 'mr two', 'B'
#         MajorReservoirs(res_lbl=res_nm_1, region=res_lt_1,
#                         geom=test_geom).save()
#         MajorReservoirs(res_lbl=res_nm_2, region=res_lt_2,
#                         geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl='mr one')
#         StoryContent(lake=m, summary="text here", history="text there").save()
#         LakeStatistics(lake=m, dam_height=4.3).save()
#         # load up a bunch of significant high and low events
#         # more than the max displayed (10) each
#         today = datetime.datetime.today()
#         dt = str(today.year) + "-" + str(today.month) + "-" + str(today.day)
#         counter = 0
#         while counter < 15:
#             SignificantEvents(lake=m, event_type='High', date=dt,
#                               height=99.99).save()
#             SignificantEvents(lake=m, event_type='Low', date=dt,
#                               drought="1970-71", height=99.99).save()
#             counter += 1

#         response = self.client.get(reverse('map:story', args=['A', 'mr one']))
#         hdr_reg = response.context['header_regions']
#         self.assertEqual(hdr_reg, [{'name': region_nm_1,
#                                     'letter': region_lt_1},
#                                    {'name': region_nm_2,
#                                     'letter': region_lt_2}])
#         hdr_lks = response.context['header_lakes']
#         self.assertEqual(hdr_lks, [{'name': res_nm_1,
#                                     'region': res_lt_1,
#                                     'class': 'enabled'},
#                                    {'name': res_nm_2,
#                                     'region': res_lt_2,
#                                     'class': 'disabled'}])

#         # check the extent in context
#         self.assertIs('extent' in response.context, True)
#         self.assertIs(isinstance(response.context['extent'], list), True)
#         self.assertEqual(len(response.context['extent']), 4)
#         for coordinate in response.context['extent']:
#             self.assertIs(type(coordinate), float)

#         # check the layer info
#         config = response.context['layer']
#         check_keys = ['table_name', 'label_field', 'carto_css',
#                       'carto_lbl', 'interactivity', 'carto_story_css']
#         # check the keys of the layer config
#         for key in check_keys:
#             self.assertIs(key in config.keys(), True)
#         # check the value type for each key
#         self.assertIs(isinstance(config['table_name'], str), True)
#         self.assertIs(isinstance(config['label_field'], str), True)
#         self.assertIs(isinstance(config['carto_css'], str), True)
#         self.assertIs(isinstance(config['carto_lbl'], str), True)
#         self.assertIs(isinstance(config['interactivity'], list), True)
#         self.assertIs(isinstance(config['carto_story_css'], str), True)
#         # verify 2 layer fields: 1 for region letter, 1 for name
#         self.assertEqual(len(config['interactivity']), 2)

#         # check the story content in context referencing the table
#         c = StoryContent.objects.get(lake=m)
#         self.assertEqual(response.context['story'], c)

#         # check the lake in context is referencing the url lake
#         lake_in_url = response.request['PATH_INFO'].split("/")[2]
#         self.assertEqual(response.context['lake'], lake_in_url)

#         # check that links is a key in the context
#         self.assertIs('links' in response.context, True)
#         self.assertIs(isinstance(response.context['links'], list),
#                       True)

#         # check that stats is a key in the context
#         self.assertIs('stats' in response.context, True)
#         self.assertIs(isinstance(response.context['stats'],
#                       type(LakeStatistics())), True)
#         ls = LakeStatistics.objects.get(lake=m)
#         ls = ls.string_numbers()
#         ls = ls.set_displays()
#         self.assertEqual(response.context['stats'], ls)

#         # check that high events is a key in the context
#         self.assertIs('high_events' in response.context, True)
#         self.assertIs(isinstance(response.context['high_events'], list),
#                       True)
#         # test high events list isn't larger than 10
#         self.assertEqual(len(response.context['high_events']), 10)
#         # test high events list objects don't have drought but does have rank
#         for i in response.context['high_events']:
#             self.assertIs('drought' in i, False)
#             self.assertIs('rank' in i, True)

#         # check that low events is a key in the context
#         self.assertIs('low_events' in response.context, True)
#         self.assertIs(isinstance(response.context['low_events'], list),
#                       True)
#         # test low events list isn't larger than 10
#         self.assertEqual(len(response.context['low_events']), 10)
#         # test low events list objects have drought and rank keys
#         for i in response.context['low_events']:
#             self.assertIs('drought' in i, True)
#             self.assertIs('rank' in i, True)

#         # check that overlays and overlay_order are context keys
#         self.assertIs('overlays' in response.context, True)
#         self.assertIs('overlay_order' in response.context, True)
#         # test that overlay_order list matches keys in overlays
#         self.assertEqual(len(response.context['overlay_order']),
#                          len(response.context['overlays'].keys()))
#         for k in response.context['overlays'].keys():
#             self.assertIs(k in response.context['overlay_order'], True)
#         for k in response.context['overlay_order']:
#             self.assertIs(k in response.context['overlays'].keys(), True)
#         # test each overlay at least has table_name, toc_label, carto_css
#         for k in response.context['overlays'].keys():
#             overlay_config = response.context['overlays'][k]
#             self.assertIs('toc_label' in overlay_config.keys(), True)
#             self.assertIs('table_name' in overlay_config.keys(), True)
#             self.assertIs('carto_css' in overlay_config.keys(), True)
#             # test overlay toc_label matches key name
#             self.assertEqual(k, overlay_config['toc_label'])

#         # check that overlay query in context equaling lake id
#         self.assertIs('overlay_query' in response.context, True)
#         self.assertIs(isinstance(response.context['overlay_query'], int),
#                       True)
#         self.assertEqual(response.context['overlay_query'], m.id)

#     def test_about_context(self):
#         """
#         Test the about template context; config & header lists
#         """
#         # although the header functions are tested above, we will retest them
#         # here to verify they are in the context
#         region_nm_1, region_lt_1 = 'rwpa 1', 'A'
#         region_nm_2, region_lt_2 = 'rwpa 2', 'B'
#         RWPAs(objectid=1, reg_name=region_nm_1, letter=region_lt_1,
#               shape_leng=10, shape_area=2, geom=test_geom).save()
#         RWPAs(objectid=2, reg_name=region_nm_2, letter=region_lt_2,
#               shape_leng=10, shape_area=2, geom=test_geom).save()
#         res_nm_1, res_lt_1 = 'mr 1', 'A'
#         res_nm_2, res_lt_2 = 'mr 2', 'B'
#         MajorReservoirs(res_lbl=res_nm_1, region=res_lt_1,
#                         geom=test_geom).save()
#         MajorReservoirs(res_lbl=res_nm_2, region=res_lt_2,
#                         geom=test_geom).save()
#         response = self.client.get(reverse('map:about'))
#         hdr_reg = response.context['header_regions']
#         self.assertEqual(hdr_reg, [{'name': region_nm_1,
#                                     'letter': region_lt_1},
#                                    {'name': region_nm_2,
#                                     'letter': region_lt_2}])
#         hdr_lks = response.context['header_lakes']
#         self.assertEqual(hdr_lks, [{'name': res_nm_1,
#                                     'region': res_lt_1,
#                                     'class': 'disabled'},
#                                    {'name': res_nm_2,
#                                     'region': res_lt_2,
#                                     'class': 'disabled'}])
#         # check the version number in the context
#         self.assertIs('version' in response.context, True)
#         self.assertEqual(response.context['version'], settings.VERSION)

#     def test_templates(self):
#         """
#         Test view templates include required leaflet and html
#         """
#         leaflet_templates = ['leaflet/js.html', 'leaflet/css.html',
#                              'leaflet/_leaflet_map.html']
#         base_template = 'map/base.html'
#         index_template = 'map/index.html'
#         region_template = 'map/region.html'
#         story_template = 'map/story.html'
#         story_mobile_template = 'map/story_mobile.html'
#         about_template = 'map/about.html'

#         # index template
#         response = self.client.get('/')
#         template_names = []
#         for t in response.templates:
#             template_names.append(t.name)

#         for lt in leaflet_templates:
#             self.assertIs(lt in template_names, True)
#         self.assertIs(index_template in template_names, True)
#         self.assertIs(base_template in template_names, True)

#         # region template
#         RWPAs(objectid=1, reg_name='Test Region', letter='A',
#               shape_leng=10, shape_area=2, geom=test_geom).save()
#         response = self.client.get('/A/')
#         template_names = []
#         for t in response.templates:
#             template_names.append(t.name)
#         for lt in leaflet_templates:
#             self.assertIs(lt in template_names, True)
#         self.assertIs(region_template in template_names, True)
#         self.assertIs(base_template in template_names, True)

#         # story template
#         MajorReservoirs(res_lbl='Lake Tester', region='A',
#                         geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl='Lake Tester')
#         StoryContent(lake=m, summary="text here", history="text there").save()

#         response = self.client.get('/A/Lake%20Tester')
#         template_names = []
#         for t in response.templates:
#             template_names.append(t.name)

#         for lt in leaflet_templates:
#             self.assertIs(lt in template_names, True)
#         self.assertIs(story_template in template_names, True)
#         self.assertIs(base_template in template_names, True)

#         # story mobile template
#         ipad_user_agent = ('Mozilla/5.0 (iPad; CPU OS 7_0_6 like Mac OS X) '
#                            'AppleWebKit/537.51.1 (KHTML, like Gecko) Coast/2'
#                            '.0.5.71150 Mobile/11B651 Safari/7534.48.3')
#         response = self.client.get('/A/Lake%20Tester',
#                                    HTTP_USER_AGENT=ipad_user_agent,
#                                    HTTP_ACCEPT="*/*")
#         template_names = []
#         for t in response.templates:
#             template_names.append(t.name)

#         for lt in leaflet_templates:
#             self.assertIs(lt in template_names, True)
#         self.assertIs(story_mobile_template in template_names, True)
#         self.assertIs(base_template in template_names, True)

#         # about template
#         response = self.client.get('/about/')
#         template_names = []
#         for t in response.templates:
#             template_names.append(t.name)
#         self.assertIs(about_template in template_names, True)
#         self.assertIs(base_template in template_names, True)


# class SignalTests(TestCase):

#     def test_story_content_post_save(self):
#         """
#         Test StoryContent post_save enables and post_delete
#         disables MajorReservoir
#         """
#         res_nm_1, res_lt_1 = 'mr 1', 'A'
#         MajorReservoirs(res_lbl=res_nm_1, region=res_lt_1,
#                         geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=res_nm_1)
#         self.assertEqual(m.story, 'disabled')
#         StoryContent(lake=m, summary="text here", history="text there").save()
#         m = MajorReservoirs.objects.get(res_lbl=res_nm_1)
#         self.assertEqual(m.story, 'enabled')
#         s = StoryContent.objects.get(summary="text here")
#         self.assertEqual(s.lake, m)
#         s.delete()
#         m = MajorReservoirs.objects.get(res_lbl=res_nm_1)
#         self.assertEqual(m.story, 'disabled')


# class StaticFileTests(TestCase):

#     def test_legend_images_exist(self):
#         """
#         Test the legend images exist
#         """
#         # iterate the overlays in config, they are the ones to be added
#         # to the map
#         for k in overlays.keys():
#             filename = "map/images/{0}.png".format(k)
#             result = finders.find(filename)
#             self.assertIs(isinstance(result, str), True)
#         # test Lake overlay image as it is not part of the config
#         result = finders.find("map/images/Lake.png")
#         self.assertIs(isinstance(result, str), True)

#     def test_css_exists(self):
#         """
#         Test the css file exists
#         """
#         result = finders.find("map/style.css")
#         self.assertIs(isinstance(result, str), True)

#     def test_base_images(self):
#         """
#         Test the base html images (logos and such)
#         """
#         response = self.client.get('/')
#         soup = BeautifulSoup(response.content, "html.parser")
#         imgs = soup.findAll('img')
#         img_srcs = [i['src'] for i in imgs]
#         for s in img_srcs:
#             fixed_path = s.replace(settings.STATIC_URL, "")
#             result = finders.find(fixed_path)
#             self.assertIs(isinstance(result, str), True)


# class MiddlewareTests(TestCase):

#     def test_mobile_detection(self):
#         """
#         Test the mobile detection middleware for story template
#         """
#         lake_name = "Lake Travis"
#         lake_region = "K"
#         MajorReservoirs(res_lbl=lake_name, region=lake_region,
#                         geom=test_geom).save()
#         m = MajorReservoirs.objects.get(res_lbl=lake_name)
#         StoryContent(lake=m)

#         ipad_user_agent = ('Mozilla/5.0 (iPad; CPU OS 7_0_6 like Mac OS X) '
#                            'AppleWebKit/537.51.1 (KHTML, like Gecko) Coast/2'
#                            '.0.5.71150 Mobile/11B651 Safari/7534.48.3')
#         r = '/' + lake_region + '/' + lake_name

#         req = HttpRequest()
#         req.path = r
#         req.META['HTTP_USER_AGENT'] = ipad_user_agent
#         req.META['HTTP_ACCEPT'] = '*/*'
#         middleware = MobileDetectionMiddleware()
#         req = middleware.process_request(req)
#         self.assertIs(req.is_mobile, True)

#         req = HttpRequest()
#         req.path = r
#         req.META['HTTP_USER_AGENT'] = 'Mozilla/5.0'
#         req.META['HTTP_ACCEPT'] = '*/*'
#         middleware = MobileDetectionMiddleware()
#         req = middleware.process_request(req)
#         self.assertIs(req.is_mobile, False)
