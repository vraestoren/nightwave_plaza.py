# <img src="https://plaza.one/icons/apple-touch-icon.png?v=2208042" width="50" style="vertical-align:middle;" /> nightwave_plaza.py

> Mobile-API for [NightWave Plaza](https://play.google.com/store/apps/details?id=one.plaza.nightwaveplaza) an online vaporwave radio to indulge yourself with the top aesthetic musical talents of the genre

## Quick Start

```python
from nightwave_plaza import NightWavePlaza

plaza = NightWavePlaza()
plaza.login(username="Hero", password="secret")
```

## Usage

### Authentication

```python
# Login
plaza.login(username="Hero", password="secret")

# Register (requires captcha)
captcha = plaza.get_captcha()
plaza.register(
    email="you@example.com",
    username="Hero",
    password="secret",
    captcha=captcha["captcha"],
    captcha_key=captcha["key"]
)

# Reset password
plaza.reset_password(email="you@example.com", captcha="...", captcha_key="...")

# Change password
plaza.change_password(current_password="old", new_password="new")

# Change email
plaza.change_email(email="new@example.com", password="secret")
```

### Player

```python
plaza.get_account_info()
```

### Radio

```python
# Current status
plaza.get_status()
plaza.get_on_screen_data()

# React to the current song
plaza.set_reaction(reaction=1)

# Play history
plaza.get_play_history(page=1)
```

### Songs

```python
plaza.get_song_info(song_id="abc123")
plaza.add_song_to_favorites(song_id="abc123")
plaza.get_song_favorites(page=1)
```

### Backgrounds

```python
plaza.get_backgrounds_list()
plaza.get_background_info(background_id="abc123")
plaza.get_random_background()
```

### Ratings & News

```python
plaza.get_ratings(type="overtime", page=1)
plaza.get_news(page=1)
```

## API Reference

| Method | Description |
|---|---|
| `login(username, password)` | Login to your account |
| `register(email, username, password, captcha, captcha_key)` | Register a new account |
| `reset_password(email, captcha, captcha_key)` | Send a password reset email |
| `change_password(current_password, new_password)` | Change your password |
| `change_email(email, password)` | Change your email |
| `get_account_info()` | Get your account info |
| `get_status()` | Get current radio status |
| `get_on_screen_data()` | Get current on-screen data |
| `set_reaction(reaction)` | React to the current song |
| `get_play_history(page)` | Get radio play history |
| `get_song_info(song_id)` | Get song details |
| `add_song_to_favorites(song_id)` | Add a song to favorites |
| `get_song_favorites(page)` | Get your favorite songs |
| `get_backgrounds_list()` | Get all backgrounds |
| `get_background_info(background_id)` | Get background details |
| `get_random_background()` | Get a random background |
| `get_ratings(type, page)` | Get leaderboard ratings |
| `get_news(page)` | Get plaza news |
| `get_captcha()` | Get a captcha challenge |
