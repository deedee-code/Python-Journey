# Import necessary modules from FastAPI
from fastapi import FastAPI, Body, Query
from validators import CreateUserDTO, UpdateUserInfoDto
from data import UsersDetails

# Create an instance of FastAPI
app = FastAPI()

# Define a simple GET endpoint
@app.get('/')
async def first_api():
    return {'message': 'Hello, there! 🌟'}

# Define a GET endpoint to return all users
@app.get('/users')
async def get_all_users():
    return UsersDetails

# Define a GET endpoint to return all users by gender using query parameters
@app.get("/users/")
async def get_users_by_gender(gender: str = Query(...)):
    users_to_return = []
    for user in UsersDetails:
        if user.get("gender").casefold() == gender.casefold():
            users_to_return.append(user)
    return users_to_return


# Define a GET endpoint to return a user by their age
@app.get("/users/{user_age}")
async def get_user_by_age(user_age: int):
    for user in UsersDetails:
        if user.get("age") == user_age:
            return user
    return {"message": "User not found"}


# Define a POST endpoint to create a new user using a Pydantic model
@app.post("/create-user")
async def create_user(user_request: CreateUserDTO):
    new_user = user_request.model_dump()
    UsersDetails.append(new_user)
    return new_user


# Define a PATCH endpoint to update user details
@app.patch("/users/{user}")
async def update_user(user_name: str, updated_user: UpdateUserInfoDto):
    for i in range(len(UsersDetails)):
        if UsersDetails[i].get("name").casefold() == user_name.casefold():
            UsersDetails[i]["name"] = updated_user.name
            UsersDetails[i]["gender"] = updated_user.gender
            UsersDetails[i]["age"] = updated_user.age
            return UsersDetails[i]
    return {"message": f"User with name {name} not found"}


# Define a DELETE endpoint to delete a user
@app.delete("/users/delete_user/{user_name}")
async def delete_user(user_name: str):
    for i in range(len(UsersDetails)):
        if UsersDetails[i].get("name").casefold() == user_name.casefold():
            UsersDetails.pop(i)
            return {"message": f"user with name {user_name} has been deleted"}
    return {"message": f"User with name {user_name} not found"}


# Define an endpoint to search user by Keyword
@app.get('/users/search/')
async def search_users_by_keyword(keyword : str = Query(...)):
    users_to_return = []
    for user in UsersDetails:
        if keyword.casefold() in user.get('name').casefold() or keyword.casefold() in user.get('gender').casefold():
            users_to_return.append(user)
    return users_to_return

# Define an endpoint to create multiple users
@app.post('/users/create_user')
async def create_multiple_users(create_users: list[CreateUserDTO] = Body(...)):
    users = []
    for user in create_users:
        new_user = user.dict()
        UsersDetails.append(new_user)
        users.append(new_user)
    return users


# Define an endpoint to count users
@app.get('/users/count/')
async def count_users(gender : str = Query(...)):
    count = 0
    for user in UsersDetails:
        if user.get('gender').casefold() == gender.casefold():
            count += 1
    return { 'count': count }