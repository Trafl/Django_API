
# FullStack Project - Car Resale Website

This project was developed with the goal of creating a platform for car resale, allowing administrators and customers to manage and view vehicle models. Utilizing the power of **Python** and **Django**, the system provides a user-friendly interface for both administrators and end users. Additionally, an integration with **OpenAI API (ChatGPT)** was implemented to automatically generate car model descriptions.

## Technologies Used

- **Django Templates**: For rendering dynamic pages.
- **Django Forms**: For simplified form creation.
- **Django ORM**: For performing database interactions in an objective way.
- **Docker-Compose**: Used to manage the **PostgreSQL** container.
- **Class-Based Views**: To facilitate code reuse in views.
- **Django Signals**: For creating interactions between system parts, such as automations when saving data.
- **OpenAI API (ChatGPT)**: Integration for automatically generating vehicle descriptions.
- **HTML and CSS**: For front-end construction and styling.

## How to Use

### Step 1: Install Dependencies

After downloading the project, open the terminal in the root folder and run the command to install the project dependencies:

```bash
pip install -r requirements.txt
```

### Step 2: Configure the `.env` File

Create a `.env` file in the root of the project containing the following environment variables:

```
API_IA_KEY=Your OpenAI API key
DB_NAME=Database name
DB_USER=Database user name
DB_PASSWORD=Database user password
DB_HOST=Database host (e.g., db)
DB_PORT=Database port (e.g., 5432)
```

### Step 3: Start the Database

Use **Docker Compose** to start the container with the **PostgreSQL** database:

```bash
docker-compose up
```

### Step 4: Create the Database Tables

With the database running, run the migrations to create the project tables in the database:

```bash
python manage.py migrate
```

### Step 5: Create Superuser

Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

After creating the superuser, you can access the Django administration panel at:

```
http://127.0.0.1:8000/admin/
```

### Step 6: Run the Server

Finally, run the Django development server:

```bash
python manage.py runserver
```

Now, access the website at:

```
http://127.0.0.1:8000/cars/
```
- Start Page

![](https://github.com/Trafl/assets/blob/main/DjangoFront.png)

- Details

![](https://github.com/Trafl/assets/blob/main/carDetail.png)

- Registry

![](https://github.com/Trafl/assets/blob/main/image.png)

