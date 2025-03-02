import React, { useEffect, useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "../Pages/Home.css";  // Import Custom CSS

const Home = () => {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/events/")
            .then(response => setEvents(response.data))
            .catch(error => console.error("Error fetching events:", error));
    }, []);

    const today = new Date();

    const ongoingEvents = events.filter(event => new Date(event.date) > today);
    const upcomingEvents = events.filter(event => event.status === "Upcoming");

    return (
        <div className="home-container">
            <div className="container">
                {/* Ongoing Events Section */}
                <h2 className="home-title">📅 Ongoing Events</h2>
                {ongoingEvents.length > 0 ? (
                    ongoingEvents.map(event => (
                        <div key={event.id} className="card mb-4 shadow-lg event-card">
                            <div className="card-body">
                                <h5 className="card-title">{event.title}</h5>
                                <p className="card-text">{event.description}</p>
                                <p className="card-text"><strong>📍 Venue:</strong> {event.venue}</p>
                                <p className="card-text"><strong>📅 Date:</strong> {new Date(event.date).toLocaleDateString()}</p>
                                <button className="btn register-btn">Register Now</button>
                            </div>
                        </div>
                    ))
                ) : (
                    <p className="no-events">⚠️ No ongoing events found. Check back later!</p>
                )}

                {/* Upcoming Events Section */}
                <h2 className="home-title">🚀 Upcoming Events</h2>
                {upcomingEvents.length > 0 ? (
                    upcomingEvents.map(event => (
                        <div key={event.id} className="card mb-4 shadow-lg event-card">
                            <div className="card-body">
                                <h5 className="card-title">{event.title}</h5>
                                <p className="card-text">{event.description}</p>
                                <p className="card-text"><strong>📍 Venue:</strong> {event.venue}</p>
                                <p className="card-text"><strong>📅 Date:</strong> {new Date(event.date).toLocaleDateString()}</p>
                                <button className="btn register-btn">View Details</button>
                            </div>
                        </div>
                    ))
                ) : (
                    <p className="no-events">⚠️ No upcoming events available.</p>
                )}
            </div>
        </div>
    );
};

export default Home;