from requests import Session

class NightWavePlaza:
    def __init__(self) -> None:
        self.api = "https://api.plaza.one"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "NightwavePlaza/1.4.1 (Android: SM-G9880; samsung z3q; ru)",
            "Np-User-Agent": "Nightwave Plaza Axios"
        }

    def get_status(self) -> dict:
        return self.session.get(f"{self.api}/status").json()

    def get_random_background(self) -> dict:
        return self.session.get(
            f"{self.api}/backgrounds/random").json()

    def get_captcha(self) -> dict:
        return self.session.get(f"{self.api}/captcha").json()

    def login(self, username: str, password: str) -> dict:
        data = {
            "username": username,
            "password": password
        }
        response = self.session.post(
            f"{self.api}/user/auth", data=data).json()
        if "token" in response:
            self.token = response["token"]
            self.session.headers["Authorization"] = f"Bearer {self.token}"
        return response

    def register(
            self,
            email: str,
            captcha: str,
            username: str,
            password: str,
            captcha_key: str) -> dict:
        data = {
            "captcha": captcha,
            "email": email,
            "key": captcha_key,
            "password": password,
            "username": username
        }
        return self.session.post(
            f"{self.api}/user/register", data=data).json()

    def set_reaction(self, reaction: int) -> dict:
        data = {
            "reaction": reaction
        }
        return self.session.post(
            f"{self.api}/reactions", data=data).json()

    def get_backgrounds_list(self) -> dict:
        return self.session.get(f"{self.api}/backgrounds").json()

    def get_play_history(self, page: int = 1) -> dict:
        return self.session.get(
            f"{self.api}/history/{page}").json()

    def get_ratings(self, type: str = "overtime", page: int = 1) -> dict:
        return self.session.get(
            f"{self.api}/ratings/{type}/{page}").json()

    def get_news(self, page: int = 1) -> dict:
        return self.session.get(
            f"{self.api}/news/{page}").json()

    def get_song_favorites(self, page: int = 1) -> dict:
        return self.session.get(
            f"{self.api}/user/favorites/{page}").json()

    def change_password(
            self,
            current_password: str,
            new_password: str) -> dict:
        data = {
            "current_password": current_password,
            "password": new_password
        }
        return self.session.put(
            f"{self.api}/user", data=data).json()

    def change_email(self, email: str, password: str) -> dict:
        data = {
            "current_password": password,
            "email": email
        }
        return self.session.put(
            f"{self.api}/user", data=data).json()

    def reset_password(
            self,
            email: str,
            captcha: str,
            captcha_key: str) -> dict:
        data = {
            "captcha": captcha,
            "email": email,
            "key": captcha_key
        }
        return self.session.post(
            f"{self.api}/user/reset", data=data).json()

    def get_song_info(self, song_id: str) -> dict:
        return self.session.get(
            f"{self.api}/songs/{song_id}").json()

    def get_account_info(self) -> dict:
        return self.session.get(f"{self.api}/user").json()

    def add_song_to_favorites(self, song_id: str) -> dict:
        data = {"song_id": song_id}
        return self.session.post(
            f"{self.api}/user/favorites", data=data).json()
    
    def get_on_screen_data(self) -> dict:
        return self.session.get(
            f"{self.api}/status/on-screen-data").json()
    
    def get_background_info(self, background_id: str) -> dict:
        return self.session.get(
            f"{self.api}/backgrounds/{background_id}").json()
