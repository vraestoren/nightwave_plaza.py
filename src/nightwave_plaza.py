from requests import Session

class NightWavePlaza:
	def __init__(self) -> None:
		self.api = "https://api.plaza.one"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "NightwavePlaza/1.4.1 (Android: SM-G9880; samsung z3q; ru)",
			"Np-User-Agent": "Nightwave Plaza Axios"
		}

	def _get(self, endpoint: str, params: dict = {}) -> dict:
		return self.session.get(
			f"{self.api}{endpoint}", params=params).json()


	def _post(self, endpoint: str, data: dict = None) -> dict:
		return self.session.post(
			f"{self.api}{endpoint}", data=data).json()

	def _put(self, endpoint: str, data: dict = None) -> dict:
		return self.session.put(
			f"{self.api}{endpoint}", data=data).json()

	def get_status(self) -> dict:
		return self._get("/status")

	def get_random_background(self) -> dict:
		return self._get("/backgrounds/random")

	def get_captcha(self) -> dict:
		return self._get("/captcha")

	def login(self, username: str, password: str) -> dict:
		data = {
			"username": username,
			"password": password
		}
		response = self._post("/user/auth", data)
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
		return self._post("/user/register", data=data)

	def set_reaction(self, reaction: int) -> dict:
		data = {
			"reaction": reaction
		}
		return self._post("/reactions", data=data)

	def get_backgrounds_list(self) -> dict:
		return self._get("/backgrounds")

	def get_play_history(self, page: int = 1) -> dict:
		return self._get(f"/history/{page}")

	def get_ratings(
			self, type: str = "overtime", page: int = 1) -> dict:
		return self._get(f"/ratings/{type}/{page}")

	def get_news(self, page: int = 1) -> dict:
		return self._get(f"/news/{page}")

	def get_song_favorites(self, page: int = 1) -> dict:
		return self._get(f"/user/favorites/{page}")

	def change_password(
			self,
			current_password: str,
			new_password: str) -> dict:
		data = {
			"current_password": current_password,
			"password": new_password
		}
		return self._put("/user", data)

	def change_email(self, email: str, password: str) -> dict:
		data = {
			"current_password": password,
			"email": email
		}
		return self._put("/user", data)

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
		return self._post("/user/reset", data)

	def get_song_info(self, song_id: str) -> dict:
		return self._get(f"/songs/{song_id}")

	def get_account_info(self) -> dict:
		return self._get("/user")

	def add_song_to_favorites(self, song_id: str) -> dict:
		data = {
			"song_id": song_id
		}
		return self._post("/user/favorites", data)
	
	def get_on_screen_data(self) -> dict:
		return self._get("/status/on-screen-data")
	
	def get_background_info(self, background_id: str) -> dict:
		return self._get(f"/backgrounds/{background_id}")
