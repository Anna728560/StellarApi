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

Ready to dive in? Use the following credentials to explore:

* Email: `tom_readme@email.com`
* Password: `123admin123`

Let's embark on a journey through the cosmos together! 🌌✨

## Available urls
* `/api/planetarium/show_themes`
* `/api/planetarium/planetarium_domes`
* `/api/planetarium/astronomy_shows`
* `/api/planetarium/show_sessions`
* `/api/planetarium/reservations`

## JWT endpoints:

Unlock the power of JWT with these endpoints:

* **create user:**
  * `/api/user/register`
* **get access token:**
  * `/api/user/token`
* **verify access token:**
  * `/api/user/token/verify`
* **refresh token:**
  * `/api/user/token/refresh`
* **manage user:**
  * `/api/user/me`

## DataBase Structure:
![img.png](img.png)

## Demo:
Explore the sleek interface of StellarApi in the demo images provided:

![img_1.png](img_1.png)
![img_2.png](img_2.png)
![img_3.png](img_3.png)
![img_4.png](img_4.png)
![img_5.png](img_5.png)
![img_6.png](img_6.png)


## Documentation:

![img_7.png](img_7.png)
![img_8.png](img_8.png)
![img_9.png](img_9.png)
![img_10.png](img_10.png)
