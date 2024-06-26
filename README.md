# StellarApi
> Welcome to StellarApi, a Django Rest Framework project designed for managing Planetarium Services.

## Features

Experience the universe with these stellar features:

* **Order Creation:** Authenticated users effortlessly create orders to secure their stellar experiences.
* **Astronomy Show Viewing:** Exclusive access for authenticated users to explore a captivating array of astronomy shows, complete with detailed information.
* **Advanced Filtering:** Customize your astronomy show experience with precision by filtering shows based on title and theme.
* **Admin Privileges:** Admins wield the power to curate the cosmos, creating astronomy shows, managing the Planetarium Dome, and crafting show themes.
* **Comprehensive Documentation:** Conveniently located at /api/doc/swagger, find comprehensive documentation to guide you through your celestial adventures.
* **Pagination:** Navigate through reservation lists seamlessly with pagination.
* **Docker Support:** Easily deploy and manage StellarApi using Docker for a streamlined development and production environment.
* **API Testing:**  StellarApi comes equipped with a suite of tests to ensure the reliability and functionality of its API endpoints, providing peace of mind during development and deployment.
* **Database Initialization Script:**   A script is included to facilitate Docker startup, ensuring seamless database initialization before the application launches, guaranteeing a smooth user experience.
* **Django Debug Toolbar:** Optimize performance.
* **Strong Admin Panel:** Effortless data management.
## Quick Start:

Make sure Python3 is installed on your system, then follow these steps:

```shell
git clone https://github.com/Anna728560/StellarApi
cd config
source venv/bin/activate # or venv\Scripts\activate in Windows
python -m venv venv
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


## Check It Out!

Ready to dive in?

To begin, you need to obtain an access token. Please use the following credentials to acquire admin access. Once you have done this, you will be able to enjoy the interface seamlessly.

* Email: `tom_readme@email.com`
* Password: `123admin123`



Let's embark on a journey through the cosmos together! 🌌✨

## Available urls:

* `http://127.0.0.1:8000/api/planetarium/show_themes`
* `http://127.0.0.1:8000/api/planetarium/planetarium_domes`
* `http://127.0.0.1:8000/api/planetarium/astronomy_shows`
* `http://127.0.0.1:8000/api/planetarium/show_sessions`
* `http://127.0.0.1:8000/api/planetarium/reservations`

## JWT endpoints:

Unlock the power of JWT with these endpoints:

* **create user:**
  * `http://127.0.0.1:8000/api/user/register`
* **get access token:**
  * `http://127.0.0.1:8000/api/user/token`
* **verify access token:**
  * `http://127.0.0.1:8000/api/user/token/verify`
* **refresh token:**
  * `http://127.0.0.1:8000/api/user/token/refresh`
* **manage user:**
  * `http://127.0.0.1:8000/api/user/me`

## Run with docker:

```shell
docker-compose build
```
```shell
docker-compose up
```

## Technologies Used:

* **Python**: Backend programming language
* **Django Rest Framework**: Framework utilized for development
* **JWT**: Authentication mechanism
* **Docker**: Containerization tool for deployment
* **Swagger**: API documentation tool

## DataBase Structure:

![img.png](/images/img.png)


## Demo:
Explore the sleek interface of StellarApi in the demo images provided:

![img_1.png](/images/img_1.png)
![img_2.png](/images/img_2.png)
![img_3.png](/images/img_3.png)
![img_4.png](/images/img_4.png)

## Documentation:
![img_5.png](/images/img_5.png)
![img_6.png](/images/img_6.png)
