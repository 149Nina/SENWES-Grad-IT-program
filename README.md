# SENWES-Grad-IT-program

Star Wars API Wrapper
Overview
This project is a straightforward Python Flask framework API wrapper for the Star Wars API (SWAPI). The goal is to offer a RESTful interface that includes caching for optimization, effectively handles error cases, and simplifies some SWAPI capabilities.

Setup and Run Instructions

1.Clone the repository:
	git clone https://github.com/username/star-wars-api-wrapper.git
	cd star-wars-api-wrapper

2.Install dependencies:
	pip install -r requirements.txt

3.Run the application:
	python app.py
	The application will be accessible at http://localhost:5000/.

Endpoints
GET /films: Returns a list of Star Wars films.
GET /films/{id}/characters: Returns a list of characters for the specified film.
GET /films/{id}/starships: Returns a list of starships for the specified film.

Architecture

The application builds a lightweight web server using the Flask framework. Responses and their expiration time are stored in a basic in-memory cache dictionary (cache), which is used to implement caching.

A decorator function called cache_response_time encapsulates the route handler functions as part of the caching scheme. It determines whether a valid cache is present for the request path and parameters provided. The cached response is returned if the cache is valid; if not, the original function is called and the result is cached for later use.

Design Decisions

Caching: To optimize response times in less than five minutes, a simple in-memory cache was implemented. By doing this, the SWAPI is under less stress and can respond to repeated requests more quickly.

Error Handling: Invalid routes and film IDs were taken care of. Returns suitable error messages together with HTTP status codes so that clients can receive insightful feedback.

SWAPI Requests: Used the requests library to make API requests to the SWAPI. The application fetches data from the SWAPI based on the provided film ID and extracts characters or starships information.

Flask Framework: Chose Flask for its simplicity and ease of use. It provides a quick way to set up a RESTful API with minimal boilerplate code.

Documentation: Included comments in the code for better understanding. API endpoints and their functionalities are explained in comments above the respective route handler functions.

README: Provided clear instructions on how to set up and run the application, an overview of the architecture, and explanations of design decisions to facilitate easy understanding for users and developers.
