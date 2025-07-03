# Coffee-Project-in-Python-Django

This is a Django-based web application for managing and browsing information about different coffee varieties, reviews, and stores.

## Features

*   **Browse Coffee Varieties:** View a list of all available coffee varieties with their details.
*   **View Coffee Details:** See more information about a specific coffee, including its description, type, and price.
*   **Find Coffee Stores:** Search for stores that carry a specific coffee variety.
*   **Coffee Reviews:** Users can add reviews and ratings for different coffees.
*   **Coffee Certificates:** Each coffee has a unique certificate of authenticity.

## Models

The application uses the following models to structure its data:

*   **CoffeeVariety:** The core model, representing a single type of coffee. It includes fields for name, image, description, type, price, and more.
*   **CoffeeReview:** A one-to-many relationship with `CoffeeVariety`, allowing multiple reviews per coffee.
*   **Store:** A many-to-many relationship with `CoffeeVariety`, as each store can sell multiple coffee varieties, and each variety can be sold in multiple stores.
*   **CoffeeCertificate:** A one-to-one relationship with `CoffeeVariety`, providing a unique certificate for each coffee.

## Getting Started

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/coffee_python.git
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the migrations:**
    ```bash
    python manage.py migrate
    ```
4.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.