from unittest.mock import patch

from django.test import SimpleTestCase
from django.urls import reverse


class SubmitFeedbackTests(SimpleTestCase):
    @patch('feedbackapp.views.Feedback.objects.create')
    def test_post_saves_feedback_and_redirects_home(self, create_feedback):
        response = self.client.post(
            reverse('submit'),
            {
                'role': 'Student',
                'teacher': 'Teacher A',
                'subject': 'Mathematics',
                'target': 'Teacher A',
                'class_name': 'Computer Science',
                'year': 'Second year',
                'teaching': '5',
                'communication': '4',
                'support': '3',
                'growth': '2',
                'comment': 'Helpful and clear feedback.',
            },
        )

        self.assertRedirects(response, reverse('home'))
        create_feedback.assert_called_once_with(
            role='Student',
            teacher='Teacher A',
            subject='Mathematics',
            target='Teacher A',
            class_name='Computer Science',
            year='Second year',
            teaching=5,
            communication=4,
            support=3,
            growth=2,
            comment='Helpful and clear feedback.',
        )

    def test_get_is_not_allowed(self):
        response = self.client.get(reverse('submit'))

        self.assertEqual(response.status_code, 405)