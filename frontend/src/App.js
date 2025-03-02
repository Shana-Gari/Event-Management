import { useEffect, useState } from "react";
import axios from "axios";

function App() {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/events/")
            .then(response => setEvents(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h1>Upcoming Events</h1>
            {events.map(event => (
                <div key={event.id}>
                    <h2>{event.title}</h2>
                    <p>{event.description}</p>
                </div>
            ))}
        </div>
    );
}

export default App;
