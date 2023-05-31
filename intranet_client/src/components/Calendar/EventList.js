import {RRule, rrulestr} from 'rrule';
import moment from "moment";
import 'moment-timezone';
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
                        start: moment.utc(event.Debut).toDate(),
                        end: moment.utc(event.Fin).toDate(),
                        allDay: false,
                        description: event.description,
                        location: event.location,
                        category: event.category,
                    });
                } else {
                    const rule = event.rrule.replace(/DTSTART=\d{8}T\d{6}/, match => `DTSTART=${moment.utc(match.slice(8), "YYYYMMDDTHHmmss").format("YYYYMMDDTHHmmss")}Z`);
                    console.log(rule);
                    const ruleObj = rrulestr(rule);
                    console.log("Règle :", ruleObj);
                    console.log("Date de début :", moment.utc(ruleObj.options.dtstart).format('YYYY-MM-DD HH:mm:ss'));
                    const allOccurrences = ruleObj.all((date, i) => i < event.count);
                    allOccurrences.forEach((occurrence) => {
                        events.push({
                            id: event.id,
                            title: event.title,
                            start: moment.utc(occurrence).toDate(),
                            end: moment.utc(occurrence.getTime() + (moment.utc(event.Fin).toDate().getTime() - moment.utc(event.Debut).toDate().getTime())).toDate(),
                            allDay: false,
                            description: event.description,
                            location: event.location,
                            category: event.category,
                        });
                    });

                }
            }
        });
        console.log(events);
        return events;
    } catch (error) {
        console.error(error);
        return [];
    }
};


export default getEvents;
