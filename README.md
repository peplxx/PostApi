## PostApi FastAPI Application

This repository contains a FastAPI application for managing posts in a database through a RESTful API.

### Setup

1. Clone the repository:
      git clone <repository_url>
   

2. Install dependencies:
      pip install -r requirements.txt
   

3. Create an env.env file at the root with the following format:
   
   PASSWORD = 'password for database'

   ...
   

5. Run the application:
      uvicorn main:app --reload
   

### Features

1. Endpoints:
   - GET /: Retrieves a simple message indicating the root of the API.
   - GET /posts: Retrieves all posts from the database.
   - GET /posts/{post_id:int}: Retrieves a post by its ID.
   - DELETE /posts/{post_id:int}: Deletes a post by its ID.
   - POST /posts: Creates a new post with data provided.
   - PUT /posts/{post_id:int}: Updates an existing post with new data.

2. Data Models:
   - PostData: Data type for representing post information.
   - Post: Represents a post entity in the database.

3. Exceptions:
   - PostNotExist: Custom exception raised when a post does not exist.

4. Database Interaction:
   - Uses SQLAlchemy for interacting with the database.
   - SQLAlchemy session works over PostgresSQL connection.

### Usage

- The application provides basic CRUD functionalities for managing posts in a database.
- Use appropriate HTTP methods to interact with the API endpoints.

### Additional Information

- Ensure to handle the env.env file securely to protect sensitive database information.
- For detailed API documentation, access the application through a web browser or API client.

Repository was created for FastApi practise.
