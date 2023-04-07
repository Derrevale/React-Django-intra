from django.shortcuts import render
from dateutil.rrule import rrule, DAILY, WEEKLY, MONTHLY
from rest_framework.response import Response

from .models import Calendar
from .models import Event
from .serializers import CalendarSerializer
from .serializers import EventSerializer

from rest_framework import viewsets



# Create your views here.
class CalendarysViewset(viewsets.ModelViewSet):
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()
    tags = ['EventManager - Calendrier']


class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    tags = ['EventManager - Event']

    def get_recurrent_events(self, request, *args, **kwargs):
        events = self.queryset.filter(rrule__isnull=False)
        recurrent_events = []
        for event in events:
            rule = rrule.rrulestr(event.rrule)
            for date in rule:
                recurrent_event = event
                recurrent_event.start_date = date
                recurrent_events.append(recurrent_event)
        serializer = self.serializer_class(recurrent_events, many=True)
        return Response(serializer.data)