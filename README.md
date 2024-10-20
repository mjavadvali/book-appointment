<h1>Book appointment</h1>
This project is built using Django and Vue.js, and runs in a Dockerized environment.

<h3>Prerequisites</h3>
<ul>
	<li>Docker</li>
	<li>Docker Compose</li>
</ul>

<h3>Installation</h3>

``` git clone https://github.com/mjavadvali/book-appointment.git ```

```cd book-appointment```

<h3>Generate a Django Secret Key:</h3>

Inside a Python shell, run:

```from django.core.management.utils import get_random_secret_key ```

```get_random_secret_key()```


<p>
	Open your .env file located inside the env/.env directory and replace the SECRET_KEY value with the generated key
</p>

<h3>
	Build and run the Docker containers
</h3>

```docker-compose up --build```
<h3>
Create a Django superuser	
</h3>


Once the containers are up and running, create a superuser by executing the following command. Replace <backend-container> with the name of your backend container (usually based on your service name from docker-compose.yml):
```
docker exec -it <backend-container> python manage.py createsuperuser
```
You can find the exact container name by running docker ps if you're unsure.

<h3>
Usage
</h3>
Access the frontend: 

http://localhost:5173

Access the backend (Django admin): 
http://localhost:8000/admin
