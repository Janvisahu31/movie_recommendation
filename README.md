# movie_recommendation# 🎬 Movie Recommendation System

## 🌟 Overview
The **Movie Recommendation System** is an AI-powered application that suggests movies based on user preferences. It uses **TF-IDF Vectorization** and **Cosine Similarity** to recommend movies similar to the one provided by the user. The system is built using **Python (Flask, Pandas, Scikit-learn)** for the backend and **React.js** for the frontend.

## 🚀 Features
- 🔍 **Search for a Movie** – Enter a movie name to get personalized recommendations.
- 🎞 **AI-Powered Recommendations** – Uses **natural language processing (NLP)** to find similar movies.
- 📜 **Genre & Tag-Based Suggestions** – Enhances recommendations using movie genres and user tags.
- 📈 **Optimized Performance** – Uses **Pickle** to save the trained model for fast execution.
- 🌐 **Interactive Web Interface** – Built with **React.js** for a modern and user-friendly experience.

## 🛠 Tech Stack
### **Backend (Machine Learning & API)**
- **Python** – Main programming language
- **Flask** – Backend framework for API
- **Pandas** – Data handling & preprocessing
- **Scikit-learn** – ML model (TF-IDF & Cosine Similarity)
- **Pickle** – Model serialization for faster loading

### **Frontend (Web UI)**
- **React.js** – Frontend framework
- **Axios** – API requests to Flask backend
- **Tailwind CSS** – Styling and responsiveness

### **Database & Storage**
- **CSV Dataset** – Movies, ratings, and tags datasets
- **Pickle Files** – Stores precomputed similarity matrices

## 📂 Folder Structure
```
📂 movie-recommendation-system
│── 📁 backend
│   ├── app.py  # Flask API
│   ├── recommender.py  # ML Model
│   ├── model.pkl  # Pretrained Model
│   ├── requirements.txt  # Dependencies
│── 📁 frontend
│   ├── src
│   │   ├── components
│   │   │   ├── Home.js
│   │   │   ├── Recommend.js
│   │   ├── App.js
│   │   ├── index.js
│   ├── package.json
│── 📁 datasets
│   ├── movies.csv
│   ├── ratings.csv
│   ├── tags.csv
│── README.md  # Project Documentation
```

## 🏗 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/movie-recommendation.git
cd movie-recommendation
```

### **2️⃣ Backend Setup (Flask API)**
```sh
cd backend
pip install -r requirements.txt
python app.py
```

### **3️⃣ Frontend Setup (React.js)**
```sh
cd frontend
npm install
npm start
```

## 🔥 Usage
1. **Run the backend** (`python app.py`)
2. **Run the frontend** (`npm start`)


## 🎯 Future Improvements
- ✅ **User Authentication** (Login & Save Favorites)
- 🎭 **Collaborative Filtering** for user-based recommendations
- 📊 **Interactive UI Enhancements**

## 💡 Contributing
Want to improve this project? Feel free to fork the repository and submit a pull request. 🚀


---
💡 *Star ⭐ this repository if you found it useful!*

