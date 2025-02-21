# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
# 🎬 Movie Recommendation System

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
3. **Enter a movie name** and get personalized recommendations 🎥



## 🎯 Future Improvements
- ✅ **User Authentication** (Login & Save Favorites)
- 🎭 **Collaborative Filtering** for user-based recommendations
- 📊 **Interactive UI Enhancements**

## 💡 Contributing
Want to improve this project? Feel free to fork the repository and submit a pull request. 🚀

