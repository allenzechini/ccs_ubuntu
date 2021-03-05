from django.test import TestCase
from config_compare.forms import CompareConfigForm, UploadConfigForm
from django.conf import settings
from pathlib import PurePath

# upload_path = PurePath(settings.MEDIA_ROOT, 'uploads')

# Create your tests here. 
class ConfigCompareFormTest(TestCase):
    def test_form_field_paths(self):
        form = CompareConfigForm()
        self.assertTrue(form.fields['first_file_field'].path == f'{PurePath(settings.MEDIA_ROOT, "uploads")}/')
        self.assertTrue(form.fields['second_file_field'].path == f'{PurePath(settings.MEDIA_ROOT, "uploads")}/')

    def test_form_field_recursiveness(self):
        form = CompareConfigForm()
        self.assertTrue(form.fields['first_file_field'].recursive == True)
        self.assertTrue(form.fields['second_file_field'].recursive == True)

    def test_form_field_matching(self):
        form = CompareConfigForm()
        self.assertTrue(form.fields['first_file_field'].match == r'\.js(on)?$')
        self.assertTrue(form.fields['second_file_field'].match == r'\.js(on)?$')

class UploadConfigFormTest(TestCase):
    def test_upload_form_label(self):
        form = UploadConfigForm()
        self.assertTrue(
            form.fields['file_field'].label == None or 
            form.fields['file_field'].label == 'New Configuration File'
        )
