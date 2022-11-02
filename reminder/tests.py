from django.test import TestCase , SimpleTestCase

from .forms import ReminderForm


class TestForm(SimpleTestCase):

    def test_reminder_form_valid_data(self):
        form = ReminderForm ( data={
            'title' : 'testcase1',
            'message' :'this is a testcase',
            'reminder_date' : '11/10/2022',
            'show_date' : '11/2/2022',
        })

        self.assertTrue(form.is_valid())

       

