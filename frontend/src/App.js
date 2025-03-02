import { useEffect, useState } from "react";
import axios from "axios";
import Home from "./Pages/Home";

function App() {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/events/")
            .then(response => setEvents(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
            </Routes>
        </Router>
    );
}

export default App;
