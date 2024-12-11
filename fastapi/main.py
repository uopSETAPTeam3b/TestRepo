from fastapi import FastAPI, Form, Request, HTTPException, Response, Cookie
from uuid import uuid4
from hashlib import sha256

from fastapi.responses import HTMLResponse

app = FastAPI()

# Simulated database
users = {}  # {username: hashed_password}
sessions = {}  # {session_id: username}


def hash_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()

@app.get("/", response_class=HTMLResponse)
async def main_page():
    return '<a href="/login">Login</a> or <a href="/register">Register</a>'


@app.get("/register", response_class=HTMLResponse)
async def register_page():
    return '''
        <form method="post">
            <label>Username: <input type="text" name="username"></label><br>
            <label>Password: <input type="password" name="password"></label><br>
            <button type="submit">Register</button>
        </form>
    '''

@app.get("/login", response_class=HTMLResponse)
async def login_page():
    return '''
        <form method="post">
            <label>Username: <input type="text" name="username"></label><br>
            <label>Password: <input type="password" name="password"></label><br>
            <button type="submit">Login</button>
        </form>
    '''

@app.post("/register")
async def register(request: Request, username: str = Form(...), password: str = Form(...)):
    if not username or not password:
        raise HTTPException(status_code=400, detail="Username and password are required.")
    if username in users:
        raise HTTPException(status_code=400, detail="User already exists.")

    users[username] = hash_password(password)
    return {"message": "User registered successfully."}


@app.post("/login")
async def login(request: Request, response: Response, username: str = Form(...), password: str = Form(...)):
    if not username or not password:
        raise HTTPException(status_code=400, detail="Username and password are required.")
    if users.get(username) != hash_password(password):
        raise HTTPException(status_code=401, detail="Invalid credentials.")

    session_id = str(uuid4())
    sessions[session_id] = username
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    return {"message": "Login successful."}


@app.post("/logout")
async def logout(session_id: str = Cookie(None)):
    if session_id in sessions:
        del sessions[session_id]
    return {"message": "Logged out successfully."}


@app.get("/profile")
async def profile(session_id: str = Cookie(None)):
    username = sessions.get(session_id)
    if not username:
        raise HTTPException(status_code=401, detail="Not authenticated.")
    return {"username": username}


# Debugging endpoints (not for production)
@app.get("/users")
async def get_users():
    return users

@app.get("/sessions")
async def get_sessions():
    return sessions