---
# IMAGO Media Search

A fullstack application for searching and securely displaying media items from IMAGO’s Elasticsearch index.
---

## Features

- **Keyword-based Search** using Elasticsearch (title, description, etc.)
- **Secure Thumbnail Access** via time-limited tokenized URLs
- **Image Fallback Mechanism** if thumbnails can't be loaded
- Minimal **React Frontend** to browse media results
- Basic test coverage with `pytest` for core endpoints
- Clean code and CORS support
- Sensitive data secured using `.env` variables
- Modern tooling: FastAPI, Poetry, Vite, React, Pydantic

## Project Structure

```
├── backend/                   # Backend directory
│   ├── api/                   # FastAPI routes
│   ├── config/                # Configuration
│   ├── models/                # Pydantic models
│   ├── repositories/          # Elasticsearch query logic
│   ├── services/              # Business logic layer
│   ├── utils/                 # Secure token utilities
│   ├── tests/                 # Pytest-based tests
├── frontend/                  # Frontend directory (React)
│   ├── src/                   # React components
│   └── index.html             # Entry HTML
├── .env                       # Environment variables including secret key
├── package.json               # Frontend configuration (Vite)
├── pyproject.toml             # Poetry configuration
```

---

## Installation Instructions

### Prerequisites

- Python 3.12
- Node.js 23.1.0
- [Poetry](https://python-poetry.org/docs/#installation) or using pip
- [Vite](https://vitejs.dev)

---

### Backend Setup (Python + Poetry)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mumar090/imago-media-search.git
   cd imago_search
   ```

2. **Install Python dependencies:**

   ```bash
   poetry install
   ```

3. **Activate Poetry virtual environment:**

   ```bash
   poetry shell
   ```

---

### Frontend Setup (React + Vite)

1. **Navigate to the frontend directory:**

   ```bash
   cd frontend
   ```

2. **Install Node dependencies:**

   ```bash
   npm install
   ```

---

### Running Both Backend and Frontend Concurrently

Start both the backend and frontend concurrently using `npm run dev:all`:

```bash
npm run dev:all
```

- **Backend** will run at: `http://localhost:8000`
- **Frontend** will run at: `http://localhost:5173`

---

### Setting Up Environment Variables

Create a `.env` file in the `backend/` directory with the following content:

```dotenv
SECRET_KEY = "your-key"
ES_HOST = "your-ES-host"
ES_USER = "your-username"
ES_PASSWORD = "your-password"
ES_INDEX = "imago"
BASE_URL = "your-base-url"
VERIFY_CERTS = False
FRONTEND_URL = "http://localhost:5173"
```

---

## Testing

1. **Run the tests:**

   From the root directory, run the following command to execute tests:

   ```bash
   poetry run pytest
   ```

---

## Author

**Muhammad Umar**

---
