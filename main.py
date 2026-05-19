from fastapi import FastAPI

app = FastAPI()

#@app.get("/api")
#def home():
    #return {"message": "Hii this my first API"}

#@app.get("/api/{data_id}")
#def read_data(data_id: int):
    #return {
        #"data_id": data_id,
        #"message": f"my id = {data_id}"
    #}

#@app.get("/def/")
#def search_data(a:str=None):
   # return {"query":a}

 users=[]

   @app.post("add_user")
   def add_user(name:str,email:str):
    user={"id":len(users)+1,"name":name,"email":email}
    users.append(users)
    return {"message":"user added","users":user}

    @app.get("/users"):
    def get_users():
        return users
     