import React, { Component, useState } from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import 'moment/locale/fr'; // Importe les fichiers de localisation français de Moment.js
import "../../../styles/Calendar/Calendar.css";
import "react-big-calendar/lib/css/react-big-calendar.css";
import getEvents from "./EventsCFS";
import Popup from "../Popup";

moment.locale('fr'); // Définit la langue de Moment.js sur français

const localizer = momentLocalizer(moment);

class CalendarCFS extends Component {
  state = {
    events: [],
    showPopup: false,
    selectedEvent: null
  };

  async componentDidMount() {
    const events = await getEvents();
    this.setState({ events });
  }

  handleSelectEvent = (event) => {
    this.setState({
      selectedEvent: event,
      showPopup: true
    });
  };

  handleClosePopup = () => {
    this.setState({
      showPopup: false
    });
  };

  render() {
    const { events, selectedEvent, showPopup } = this.state;
    return (
      <div className="Calendar">
        <Calendar
          localizer={localizer}
          defaultDate={new Date()}
          defaultView="month"
          events={events}
          style={{ height: "100vh" }}
          onSelectEvent={this.handleSelectEvent}
        />
        {showPopup && (
          <Popup
            title={selectedEvent.title}
            start={selectedEvent.start}
            end={selectedEvent.end}
            description={selectedEvent.description}
            handleClosePopup={this.handleClosePopup}
          />
        )}
      </div>
    );
  }
}

export default CalendarCFS;