from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
import os 


api_key_header = APIKeyHeader(name="Kestrel-API-Key", auto_error=False)

def check_key(api_key_header: str = Security(api_key_header)):
    api_key = os.getenv("API_KEY")
    if api_key_header == api_key:
        return "Authorized"
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")