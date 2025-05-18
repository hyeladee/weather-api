# Weather API App

A simple weather dashboard that fetches real-time weather data from the OpenWeather API. Built with **FastAPI** (Python) for the backend and **Vanilla JS + HTML** for the frontend. No frameworks, no fluff—just raw weather power.

## Features

* Real-time weather data via OpenWeather API
* Lightweight and fast FastAPI backend
* Simple HTML + JavaScript frontend
* Caching to reduce unnecessary API calls
* Easy to deploy (Render-ready)

## Demo

**Live URL:** *[Weather API App](https://weather-api-g6rk.onrender.com)*

## Project Structure

```
weather-api/
├── main.py           # FastAPI backend
├── index.html        # Frontend UI
├── .env              # API keys and secrets (not pushed to GitHub)
├── Pipfile           # Project dependencies
├── Pipfile.lock      # Dependency lock file
├── .gitignore        # Git ignore rules
```

## Environment Setup

### 1. Clone the repo

```bash
git clone https://github.com/hyeladee/weather-api.git
cd weather-api
```

### 2. Install dependencies

Using Pipenv:

```bash
pipenv install
pipenv shell
```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

### 4. Run the app

```bash
uvicorn main:app --reload
```

Then visit `http://localhost:8000` in your browser.

## Deployment

This project can be easily deployed to platforms like **Render**, **Railway**, or **Fly.io**.

To deploy on Render:

1. Push your code to GitHub.
2. Create a new Web Service on Render.
3. Set build and start commands:

   * **Build Command:** `pip install pipenv && pipenv install`
   * **Start Command:** `pipenv run uvicorn main:app --host=0.0.0.0 --port=10000`
4. Add your `.env` values in the Render dashboard.

## API Endpoint

### `/weather?city=CityName`

**Example:**

```http
GET /weather?city=lagos
```

**Response:**

```json
{
  "main": {
    "temp": 28.34,
    "humidity": 85
  },
  "weather": [
    {
      "description": "scattered clouds"
    }
  ],
  ...
}
```

## License

MIT License.

---

*Built with love by [@hyeladee](https://github.com/hyeladee)*
