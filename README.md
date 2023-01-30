# IMDB-DRF
### Introduction
This is a clone of the popular movie database website IMDB, built using the Django Rest Framework (DRF). The application provides a REST API for accessing movie and actor information, as well as user authentication and authorization.

### Features
<ul>
   <li>Movie list and details</li>
   <li>Review list</li>
   <li>User authentication and authorization</li>
   <li>API for accessing movie and actor information</li> 
</ul>

### Status Codes:
200 : Success

204 : No Content

401 : Unauthorized

404 : Error

### The API Routes:
<ul>
  <li> /list/ - Movie List page </li>
  <li> /list/pk/ - Movie detail page </li> 
  
  <li> /stream/ - Streaming Platform  List Page </li>
  <li> /stream/pk/ - Streaming Platform Detail Page  </li>
  
  <li> stream/pk/review-create/ - Review Create for a particular Movie  </li>
  <li> stream/pk/reviews/ - Review Create for a particular Movie  </li>
  <li> /review/id/ - Review Detail Page  </li>
  
  <li> /account/login/ - Login User  </li>
  <li> /account/register/ - Register User  </li>
  <li> /account/logout/ - Logout User  </li>
</ul>  

