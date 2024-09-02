# redisearch
A simple Flask-based RESTful API for managing brand names using Redisearch.

Getting Started

Prerequisites
- Python 3.x
- Redis with Redisearch module installed

Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/brand-name-api.git
cd brand-name-api
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

3. Ensure Redis is running and has the Redisearch module enabled.

Running the Application
Start the Flask application:
```bash
python app.py
```
The API will be available at http://127.0.0.1:5000.

API Endpoints
- POST /brands: Add a new brand.
- DELETE /brands/<id>: Delete a brand by ID.
- PUT /brands/<id>: Update a brand's name by ID.
- GET /brands/search?q=<query>: Search for brands by name.

Example Requests
- Add a Brand:
```bash
curl -X POST http://127.0.0.1:5000/brands -H "Content-Type: application/json" -d '{"id": "1", "name": "Nike"}'
```
- Search for Brands:
```bash
curl -X GET "http://127.0.0.1:5000/brands/search?q=Nike"
```

License
This project is licensed under the MIT License - see the LICENSE file for details.