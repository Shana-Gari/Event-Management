import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "../Pages/EventDetails.css";  // Custom Styling

const EventDetails = () => {
    const { id } = useParams();
    const [event, setEvent] = useState(null);

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/events/${id}/`)
            .then(response => setEvent(response.data))
            .catch(error => console.error("Error fetching event details:", error));
    }, [id]);

    if (!event) return <div className="loading">Loading event details...</div>;

    return (
        <div className="event-details-container">
            <div className="container">
                <h1 className="event-title">{event.title}</h1>

                <div className="row">
                    {/* Sidebar with event info */}
                    <div className="col-md-4 sidebar">
                        <h4>📆 Event Details</h4>
                        <p><strong>📅 Date:</strong> {new Date(event.date).toLocaleString()}</p>
                        <p><strong>🛑 Last Date to Register:</strong> {new Date(event.date).toLocaleString()}</p>
                        <p><strong>📍 Venue:</strong> {event.venue}</p>
                    </div>

                    {/* Event Poster */}
                    <div className="col-md-8">
                        {event.poster ? (
                            <img src={`http://127.0.0.1:8000/media/${event.poster}`}
                                className="img-fluid event-poster" alt={event.title} />
                        ) : (
                            <div className="no-image">No Image Available</div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default EventDetails;
