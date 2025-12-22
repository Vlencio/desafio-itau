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
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPO.git](https://github.com/SEU_USUARIO/SEU_REPO.git)
   cd SEU_REPO
