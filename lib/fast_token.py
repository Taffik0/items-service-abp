"""Эта библиотека отвечает за работу с токенами авторизации"""
from fastapi import Request, HTTPException, Depends
from jose import jwt

SECRET_KEY = "my_super_secret_key"
ALGORITHM = "HS256"

def authorize_user(request: Request):
    token = request.cookies.get("jwt")
    print(token)
    if not token:
        raise HTTPException(status_code=401, detail="Нет токена")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Нет user_id в токене")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Неверный или просроченный токен")

def get_uuid_of_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            return None
        return user_id
    except Exception as e:
        print(e)