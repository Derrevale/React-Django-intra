import React, { Component } from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import 'moment/locale/fr'; // Importe les fichiers de localisation français de Moment.js

import "../../styles/Calendar/Calendar.css";
import "react-big-calendar/lib/css/react-big-calendar.css";
import getEvents from "./Events";

moment.locale('fr'); // Définit la langue de Moment.js sur français

const localizer = momentLocalizer(moment);

class MyCalendar extends Component {
  state = {
    events: [],
  };

  async componentDidMount() {
    const events = await getEvents();
    this.setState({ events });
  }

  render() {
    return (
      <div className="Calendar">
        <Calendar
          localizer={localizer}
          defaultDate={new Date()}
          defaultView="month"
          events={this.state.events}
          style={{ height: "100vh" }}
        />
      </div>
    );
  }
}

export default MyCalendar;
