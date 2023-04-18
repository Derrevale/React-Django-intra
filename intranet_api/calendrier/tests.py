from django.test import TestCase
from .models import Calendar, Event, DAILY
from datetime import datetime

# Classe de test pour le modèle Calendar
class CalendarModelTestCase(TestCase):

    # Méthode setUp exécutée avant chaque test
    def setUp(self):
        self.calendar = Calendar.objects.create(
            name='Test Calendar',
            description='This is a test calendar.',
            slug='test-calendar'
        )

    # Test pour vérifier la création d'un objet Calendar
    def test_calendar_creation(self):
        self.assertIsInstance(self.calendar, Calendar)
        self.assertEqual(self.calendar.__str__(), 'Test Calendar')

# Classe de test pour le modèle Event
class EventModelTestCase(TestCase):

    # Méthode setUp exécutée avant chaque test
    def setUp(self):
        self.calendar = Calendar.objects.create(
            name='Test Calendar',
            description='This is a test calendar.',
            slug='test-calendar'
        )

        self.event = Event.objects.create(
            title='Test Event',
            Debut=datetime(2023, 4, 17, 10, 0, 0),
            Fin=datetime(2023, 4, 17, 12, 0, 0),
            location='Test Location',
            description='This is a test event.',
            category=self.calendar,
            recurrency=False,
            frequency=DAILY,
            count=1,
            interval=1
        )

    # Test pour vérifier la création d'un objet Event
    def test_event_creation(self):
        self.assertIsInstance(self.event, Event)
        self.assertEqual(self.event.__str__(), 'Test Event')

    # Test pour vérifier la relation entre les objets Event et Calendar
    def test_event_calendar_relation(self):
        self.assertEqual(self.event.category, self.calendar)
