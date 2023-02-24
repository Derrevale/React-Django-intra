import React, {useState, useEffect} from 'react';

const Events = () => {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8002/api/event/')
            .then(response => response.json())
            .then(data => setEvents(data));
    }, []);

    return (
        <div>
            {events.map(event => (
                <div key={event.id}>
                    <h3>{event.title}</h3>
                    <p>Calendrier: {event.category}</p>
                    <p>Start Date: {event.start_date}</p>
                    <p>End Date: {event.end_date}</p>
                    <p>Location: {event.location}</p>
                    <p>Description :{}</p>
                    <p>Is Recurent : {event.recurrency}</p>
                    <p>RRule : {event.rrule}</p>
                </div>
            ))}
        </div>
    );
};

export default Events;
