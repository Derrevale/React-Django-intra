const API_URL = "http://localhost:8002/api/event/";

const getEvents = async () => {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    const events = data.map((event) => ({
      id: event.id,
      title: event.title,
      start: event.start_datetime,
      end: new Date(`${event.start_datetime}Z`),
      allDay: false,
      description: event.description,
      location: event.location,
      category: event.category,
    }));

    return events;
  } catch (error) {
    console.error(error);
    return [];
  }
};

export default getEvents;
