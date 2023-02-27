import Calendar from '@toast-ui/react-calendar';
import '@toast-ui/calendar/dist/toastui-calendar.min.css';
import React, { useState, useEffect } from 'react';
import moment from 'moment';
import 'tui-date-picker/dist/tui-date-picker.css';
import 'tui-time-picker/dist/tui-time-picker.css';
export function MyCalendar() {
  const calendars = [{ id: 'cal1', name: 'Personal' }];
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8002/api/event/')
      .then(response => response.json())
      .then(data => {
        const convertedEvents = data.map(event => {
          return {
            id: event.id,
            calendarId: 'cal1',
            title: event.title,
            category: event.category,
            start: moment(event.start_date + ' ' + event.start_time).format(),
            end: moment(event.end_date + ' ' + event.end_time).format(),
          };
        });
        setEvents(convertedEvents);
      });
  }, []);
  console.log(events);
  return (
    <div>
      <Calendar
        height="900px"
        view="month"
        month={{
          dayNames: ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'],
          visibleWeeksCount: 3,
        }}
        calendars={calendars}
        events={events}
      />
    </div>
  );
}
