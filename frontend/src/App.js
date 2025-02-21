import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import MovieList from "./components/MovieList";
import Recommendation from "./components/Recommendation";

function App() {
  return (
    <Router>
      <div className="p-4">
        <h1 className="text-2xl font-bold">🍿 Movie Recommender</h1>
        <Routes>
          <Route path="/" element={<MovieList />} />
          <Route path="/movie/:movieId" element={<Recommendation />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
