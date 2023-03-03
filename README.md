# Flight-deal-finder

This is a Python project that helps users find flight deals by searching for the cheapest flights to their desired destination.

This is a Python project that helps users find flight deals by searching for the cheapest flights to their desired destination.
Features

    Searches for flight deals using the Kiwi Tequila API
    Retrieves flight data from the Sheety API
    Notifies users via email when a deal is found
    Uses OOP principles to organize code and improve maintainability
    Implements error handling to gracefully handle exceptions

Getting Started

1. To get started with this project, follow these steps:

   Clone the repository to your local machine:

   ```bash

   git clone https://github.com/tt-ishere/Flight-deal-finder.git
   ```

2. Create a virtual environment:

   ```bash

   python3 -m venv env
   ```

3. Activate the virtual environment:

```bash

source env/bin/activate
```

4.  Set up your environment variables:

    Create a .env file in the root directory of the project
    Add the following variables to the .env file:

    ```makefile

    SHEETY_ENDPOINT=<YOUR SHEETY ENDPOINT>
    SHEETY_AUTHORIZATION=<YOUR SHEETY AUTHORIZATION TOKEN>
    TEQUILA_ENDPOINT=<YOUR TEQUILA ENDPOINT>
    TEQUILA_API_KEY=<YOUR TEQUILA API KEY>
    ```

    Replace the values in angle brackets with your own values.

5.  Run the program:

    ```python

    python main.py
    ```

    Usage

To use this program, you will need to add the cities you are interested in to the FlightDeals sheet in your Sheety account. The program will search for the cheapest flights to these cities using the Kiwi Tequila API.

If a flight deal is found for any of the cities in the FlightDeals sheet, an email notification will be sent to all the email addresses listed in the users sheet in your Sheety account.
Contributing

Contributions are welcome! If you have any ideas for improvements or bug fixes, please submit a pull request.

Credits

This project was created Enoch Tetteh Amanor as part of the Python Developer Bootcamp by Dr. Angela Yu.
