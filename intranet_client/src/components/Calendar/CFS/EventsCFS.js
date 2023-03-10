import { RRule } from 'rrule';

const API_URL = "http://localhost:8002/api/event/";

const getEvents = async () => {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    const events = [];

    data.forEach((event) => {
      if (event.category === 2) { // filter events with category 2 --> CFS
        if (!event.recurrency) {
          events.push({
            id: event.id,
            title: event.title,
            start: new Date(event.Debut),
            end: new Date(event.Fin),
            allDay: false,
            description: event.description,
            location: event.location,
            category: event.category,
          });
        } else {
          const rule = event.rrule;
          const ruleObj = RRule.fromString(rule);
          const allOccurrences = ruleObj.all((date, i) => i < event.count);
          allOccurrences.forEach((occurrence) => {
            events.push({
              id: event.id,
              title: event.title,
              start: occurrence,
              end: new Date(occurrence.getTime() + (new Date(event.Fin).getTime() - new Date(event.Debut).getTime())),
              allDay: false,
              description: event.description,
              location: event.location,
              category: event.category,
            });
          });
        }
      }
    });

    return events;
  } catch (error) {
    console.error(error);
    return [];
  }
};


export default getEvents;
