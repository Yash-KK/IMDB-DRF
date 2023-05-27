# IMDB-DRF Application
### Technologies used: Django, Django Rest Framework, Docker.
<hr>
<br>

## Description
The IMDB-DRF clone is a web application built using Django and Django REST Framework (DRF) that replicates the functionality of the popular IMDB website. 
It provides endpoints to manage a watchlist of movies, view movie details, explore streaming platforms, and interact with movie reviews.

<br>

## Key Features
<ul>
  <li> <strong> Movie List and Detail Pages: </strong>  Browse and view details of movies in the watchlist.</li> <br>
  <li> <strong> Streaming Platform List and Detail Pages:  </strong> Explore various streaming platforms and their details. </li> <br>
  <li> <strong> Review Creation and Listing: </strong> Create and view reviews for specific movies. </li> <br>
  <li> <strong> User Authentication: </strong> Register, login, and logout functionality for users. </li> <br>
</ul>

 <br>
 
 <strong> Clone the git repository locally: </strong> <br>
```
https://github.com/Yash-KK/IMDB-DRF.git
```

 <strong> Create and activate a Virtual Envionment: </strong> <br>
```
 virtualenv venv
 source venv/bin/activate
```

 <strong> Install Dependencies: </strong> <br>
```
pip install -r requirements.txt
```

 <strong> Setup Database and Run the Development Server </strong> <br>
```
python manage.py migrate
python manage.py runserver
```

<br>

## API
After successfull deployment of the image containers our backend is up and running on : <br>
* [localhost:8000](http://127.0.0.1:8000/) <br>

<br>

The IMDB-DRF clone application provides the following endpoints:

* **Movie List Page**: View all existing movies and create a new movie instance.
  - Endpoint: `/watch-list/`
  - HTTP Methods: GET, POST

* **Movie Detail Page**: View a particular movie, update its details, or delete it.
  - Endpoint: `/watch-list/{movie_id}/`
  - HTTP Methods: GET, PUT, PATCH, DELETE

* **Streaming Platform List Page**: Browse all streaming platforms and their details.
  - Endpoint: `/platform-list/`
  - HTTP Methods: GET

* **Streaming Platform Detail Page**: View details of a specific streaming platform.
  - Endpoint: `/platform-list/{platform_id}/`
  - HTTP Methods: GET

* **Review Create**: Create a review for a particular movie.
  - Endpoint: `/watch-list/{movie_id}/review-create/`
  - HTTP Methods: POST

* **Review List**: List all reviews for a particular movie.
  - Endpoint: `/watch-list/{movie_id}/reviews/`
  - HTTP Methods: GET

* **Review Detail**: View details of a specific review for a movie.
  - Endpoint: `/watch-list/{movie_id}/review-detail/{review_id}/`
  - HTTP Methods: GET

* **User Authentication**
  - Login User: `/accounts/login/`
  - Register User: `/accounts/register/`
  - Logout User: `/accounts/logout/`














