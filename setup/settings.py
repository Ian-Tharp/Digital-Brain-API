from functools import lru_cache
import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
  youtube_api_key: str
  youtube_api_service_name: str
  youtube_api_version: str
  
  class Config:
    extra = "allow"
    profile = os.environ.get(
      "FASTAPI_PROFILE", "local"
    )
    if profile == "local":
      env_file = [".env", ".env.local"]
    elif os.path.exists(f".env.{profile}"):
      env_file = [f".env.{profile}"]
    else:
      env_file = ".env"
  

@lru_cache()
def get_settings():
  return Settings()
