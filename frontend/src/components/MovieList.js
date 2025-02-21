import React, { useEffect, useState } from "react";
import { getMovies } from "../api";
import { Link } from "react-router-dom";

const MovieList = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchMovies = async () => {
      const data = await getMovies();
      setMovies(data);
    };
    fetchMovies();
  }, []);

  return (
    <div>
      <h2 className="text-xl font-bold">🎬 Movie List</h2>
      <ul>
        {movies.map((movie) => (
          <li key={movie.movieId}>
            <Link to={`/movie/${movie.movieId}`} className="text-blue-500">
              {movie.title}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MovieList;
