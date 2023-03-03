import { RRule } from 'rrule';

const API_URL = "http://localhost:8002/api/event/";

const getEvents = async () => {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    const events = [];

    data.forEach((event) => {
      console.log(event.recurrency)
      if (!event.recurrency) {
        console.log("pas de récurence")
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
        console.log(occurrence)
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
    });

    return events;
  } catch (error) {
    console.error(error);
    return [];
  }
};

export default getEvents;
