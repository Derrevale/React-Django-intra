import { RRule } from 'rrule';

const API_URL = "http://localhost:8002/api/EventManager Event/";

const getEvents = async (category) => {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    const events = [];

    data.forEach((event) => {
      if (event.category === category) { // filter events with matching category
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
