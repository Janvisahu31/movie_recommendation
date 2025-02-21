import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getRecommendations } from "../api";

const Recommendation = () => {
  const { movieId } = useParams();
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    const fetchRecommendations = async () => {
      const data = await getRecommendations(movieId);
      if (data && Array.isArray(data.recommended_movies)) {
        setRecommendations(data.recommended_movies);
      } else {
        setRecommendations([]); // Handle invalid responses
      }
    };
    fetchRecommendations();
  }, [movieId]);

  console.log(recommendations);

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold">🎬 Recommended Movies</h2>
      {recommendations.length === 0 ? (
        <p>No recommendations found.</p>
      ) : (
        <ul className="mt-4">
          {recommendations.map((movie, index) => (
  <div key={index}>
    <h3>{movie.title}</h3>
    <p>Genres: {movie.genres}</p>
  </div>
))}

        </ul>
      )}
    </div>
  );
};



export default Recommendation;
