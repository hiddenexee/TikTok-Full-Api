import requests

class TikTokApi:
    def __init__(self, proxy: str):
        self.api_url = 'http://api_url/' # api url change
        self.headers = {'Content-Type': 'application/json'}

        self.proxy = proxy

    def create_device(self):
        response = requests.post(
            f"{self.api_url}create_device",
            headers=self.headers,
            json={"proxy": self.proxy, "app_version": "38.1.1"}
        ).json()

        return response

    def create_account(self, email: str, password: str, device: dict):
        payload = {
            "email": email,
            "password": password,
            "proxy": self.proxy,
            "device": device
        }
        response = requests.post(
            f"{self.api_url}create_account",
            headers=self.headers,
            json=payload
        ).json()

        return response

    def login(self, device: dict):
        payload = {
            "proxy": self.proxy,
            "device": device
        }
        response = requests.post(
            f"{self.api_url}login",
            headers=self.headers,
            json=payload
        ).json()

        return response

    def change_profil(self, name: str, username: str, bio: str, account: dict):
        payload = {
            "opsiyon": "name,username,bio",
            "name": name,
            "username": username,
            "bio": bio,
            "proxy": self.proxy,
            "account": account
        }
        response = requests.post(
            f"{self.api_url}change_profil",
            headers=self.headers,
            json=payload
        ).json()

        return response

    def send_like(self, video_id: str, account: dict):
        payload = {
            "video_id": video_id,
            "proxy": self.proxy,
            "account": account
        }
        response = requests.post(
            f"{self.api_url}send_like",
            headers=self.headers,
            json=payload
        ).json()

        return response

    def send_follow(self, user_id: str, sec_user_id: str, account: dict):
        payload = {
            "user_id": user_id,
            "sec_user_id": sec_user_id,
            "proxy": self.proxy,
            "account": account
        }
        response = requests.post(
            f"{self.api_url}send_follow",
            headers=self.headers,
            json=payload
        ).json()

        return response

    def send_comment(self, video_id: str, comment: str, account: dict):
        payload = {
            "video_id": video_id,
            "comment": comment,
            "proxy": self.proxy,
            "account": account
        }
        response = requests.post(
            f"{self.api_url}send_comment",
            headers=self.headers,
            json=payload
        ).json()

        return response

    def send_view(self, video_id: str, account: dict):
        payload = {
            "video_id": video_id,
            "proxy": self.proxy,
            "account": account
        }
        response = requests.post(
            f"{self.api_url}send_view",
            headers=self.headers,
            json=payload
        ).json()

        return response

    def send_share(self, video_id: str, account: dict):
        payload = {
            "video_id": video_id,
            "proxy": self.proxy,
            "account": account
        }
        response = requests.post(
            f"{self.api_url}send_share",
            headers=self.headers,
            json=payload
        ).json()

        return response

    def send_save(self, video_id: str, account: dict):
        payload = {
            "video_id": video_id,
            "proxy": self.proxy,
            "account": account
        }
        response = requests.post(
            f"{self.api_url}send_save",
            headers=self.headers,
            json=payload
        ).json()

        return response

    def captcha_solver(self, device: dict):
        payload = {
            "proxy": self.proxy,
            "device": device
        }
        response = requests.post(
            f"{self.api_url}captcha_solver",
            headers=self.headers,
            json=payload
        ).json()

        return response


