from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = "./.env",
        env_file_encoding="utf-8",
        case_sensitive= False
    )
    bot_token : str
    admin_id : str
    name_pack : str
    
@lru_cache(typed = True)
def load_config() -> Config:
    return Config()