import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi import status

from PostApi.data import exceptions
from PostApi.data.datatypes.posts import PostData

from PostApi.data.database import db_session
from PostApi.data.database.posts import Post
from PostApi.data.database.db_session import get_session

# Endpoints
# 1. GET /: Retrieves a simple message indicating the root of the API.
# 2. GET /posts: Retrieves all posts from the database.
# 3. GET /posts/{post_id:int}: Retrieves a post by its ID.
# 4. DELETE /posts/{post_id:int}: Deletes a post by its ID.
# 5. POST /posts: Creates a new post with data provided.
# 6. PUT /posts/{post_id:int}: Updates an existing post with new data.

@asynccontextmanager
async def lifespan(instance: FastAPI):
    dotenv_path = os.path.join(os.path.dirname(__file__), 'env.env')
    if not os.path.exists(dotenv_path):
        raise Exception("[ERROR] File env.env is missing!")
    load_dotenv(dotenv_path)
    from PostApi.data import config

    db_session.global_init(database=config.database_name,
                           user=config.database_user,
                           password=config.database_pass,
                           host=config.database_host)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "root"}


@app.get("/posts")
async def get_all_posts():
    sess = get_session()
    posts = sess.query(Post).all()
    return {"amount": len(posts),
            "data": posts}


@app.get("/posts/{post_id:int}")
async def get_post_byid(post_id: int):
    sess = get_session()
    post = sess.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise exceptions.PostNotExist
    return {'data': post}


@app.delete("/posts/{post_id:int}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post_byid(post_id: int):
    sess = get_session()
    post = sess.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise exceptions.PostNotExist
    sess.delete(post)
    sess.commit()


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(data: PostData):
    sess = get_session()
    sess.add(Post(data))
    sess.commit()


@app.put("/posts/{post_id:int}")
async def update_post(post_id: int, data: PostData):
    sess = get_session()
    post = sess.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise exceptions.PostNotExist
    post.title = data.title
    post.published = data.published
    post.content = data.content
    sess.commit()
    return {'message': 'Post was successfully updated!'}
