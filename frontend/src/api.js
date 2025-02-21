import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:5000"; 

export const getMovies = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/movies`);
    return response.data;
  } catch (error) {
    console.error("Error fetching movies:", error);
    return [];
  }
};

export const getRecommendations = async (movieId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/recommend?movie=${encodeURIComponent(movieId)}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching recommendations:", error);
    return [];
  }
};
