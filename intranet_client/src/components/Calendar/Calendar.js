import React, { Component } from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";

import "../../styles/Calendar.css";
import "react-big-calendar/lib/css/react-big-calendar.css";
import getEvents from "./Events";

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
