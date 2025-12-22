# Itaú Unibanco - Backend Challenge (Python Edition)

This project is a solution for the backend coding challenge provided by the Itaú Unibanco hiring team.

Although the original challenge suggests Java/Kotlin, I implemented this solution using **Python** and **Flask** to demonstrate proficiency in this stack, while strictly adhering to all architectural constraints, logic requirements, and performance patterns (Thread Safety).

## 📋 The Challenge

The goal was to build a REST API that receives transactions and returns statistics based on them in real-time.

### Constraints & Rules
* hosted on GitHub/GitLab.
* **No Database allowed:** All data must be stored in memory.
* **No Cache allowed:** (e.g., Redis).
* State must be managed safely across concurrent requests.
* Standard JSON responses.

## 🚀 Technologies

* **Python 3.x**
* **Flask** (Web Framework)
* **Pytest** (Automated Testing)

## 🏗 Architecture

The project follows a Service-Controller pattern to separate business logic from HTTP routing:
* **Controller:** Handles incoming HTTP requests and responses.
* **Service/Repository:** Manages the in-memory data storage using **Thread Locking** to ensure data integrity during concurrent access.

## 🛠 How to Run

1. **Clone the repository**
   git clone https://github.com/Vlencio/desafio-itau.git
   cd [FOLDER CONTAINING THE CLONE]

2. **Create virtual enviroment**
   python -m venv venv
   #Windows
   .\venv\Scripts\activate
   #Linux
   source venv/bin/activate

3. **Install the requirements**
   pip install -r requirements

4. **Run the application**
   python -m controler.controler

Extra. **Tests**
   If you want to test the application, the folder tests is designed specifically for that.
   You can run it by typing on your terminal:
      pytest -v

🔌 API Endpoints
1. POST /transacao

Adds a new transaction to the memory.

Body:
JSON

{
    "valor": 123.45,
    "dataHora": "2023-12-19T10:00:00.000Z"
}

Validations:

    Fields valor and dataHora are mandatory.

    Transaction cannot be in the future.

    valor must be equal to or greater than 0.

Responses:

    201 Created: Transaction accepted (Empty body).

    422 Unprocessable Entity: Business rule validation failed (e.g., date in the future).

    400 Bad Request: Invalid JSON format.

2. DELETE /transacao

Clears all transactions stored in memory.

Responses:

    200 OK: Memory cleared successfully.

3. GET /estatistica

Returns statistics of transactions that happened in the last 60 seconds.

Response:
JSON

{
    "count": 10,
    "sum": 1234.56,
    "avg": 123.456,
    "min": 12.34,
    "max": 123.56
}

If no transactions occurred in the last 60 seconds, all values return 0.
