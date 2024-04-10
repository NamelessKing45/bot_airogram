from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    bot_token: str = "7113779368:AAEB4N8mlaalE10L_Mfi5-Nx4EqfLdXe7FY"
    admin_ids: frozenset[int] = frozenset({42, 3595399})


settings = Settings()
