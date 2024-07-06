import jwt
from datetime import datetime, timedelta
from fastapi.security.utils import get_authorization_scheme_param

def create_access_token(username: str, expires_delta: timedelta = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode = {"exp": expire, "username": username}
    encoded_jwt = jwt.encode(to_encode, "SECRET_KEY", algorithm="HS256")
    return encoded_jwt

def get_current_user(token: str = Depends()):
    scheme, token = get_authorization_scheme_param(token)
    if scheme.lower()!= "bearer":
        raise HTTPException(status_code=403, detail="Invalid authentication scheme")
    try:
        payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
        username = payload.get("username")
        if not username:
            raise HTTPException(status_code=403, detail="Invalid token")
        user = session.query(User).filter_by(username=username).first()
        if not user:
            raise HTTPException(status_code=403, detail="User not found")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")
