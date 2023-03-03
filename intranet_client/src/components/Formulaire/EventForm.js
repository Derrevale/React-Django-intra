import React, { useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import "../../styles/Formulaire/EventForm.css";

const EventForm = ({ onSubmit }) => {
  const [title, setTitle] = useState('');
  const [start, setStart] = useState('');
  const [end, setEnd] = useState('');
  const [location, setLocation] = useState('');
  const [description, setDescription] = useState('');
  const [calendar, setCalendar] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    const event = {
      title,
      debut: start,
      fin: end,
      location,
      description,
      category: calendar,
    };

    axios.post('http://localhost:8002/api/event/', event)
      .then(() => {
        setTitle('');
        setStart('');
        setEnd('');
        setLocation('');
        setDescription('');
        setCalendar('');
        onSubmit();
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <form onSubmit={handleSubmit} className="event-form">
      <label htmlFor="title" className="event-form__label">Title</label>
      <input
        id="title"
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="event-form__input"
        required
      />

      <label htmlFor="start" className="event-form__label">Start</label>
      <input
        id="start"
        type="datetime-local"
        value={start}
        onChange={(e) => setStart(e.target.value)}
        className="event-form__input"
        required
      />

      <label htmlFor="end" className="event-form__label">End</label>
      <input
        id="end"
        type="datetime-local"
        value={end}
        onChange={(e) => setEnd(e.target.value)}
        className="event-form__input"
        required
      />

      <label htmlFor="location" className="event-form__label">Location</label>
      <input
        id="location"
        type="text"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
        className="event-form__input"
        required
      />

      <label htmlFor="description" className="event-form__label">Description</label>
      <textarea
        id="description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        className="event-form__textarea"
        required
      />

      <label htmlFor="calendar" className="event-form__label">Calendar</label>
      <select
        id="calendar"
        value={calendar}
        onChange={(e) => setCalendar(e.target.value)}
        className="event-form__select"
        required
      >
        <option value="">Select a calendar</option>
        <option value="1">Calendar 1</option>
        <option value="2">Calendar 2</option>
        <option value="3">Calendar 3</option>
      </select>

      <button type="submit" className="event-form__submit-btn">Submit</button>
    </form>
  );
};

EventForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
};

export default EventForm;
