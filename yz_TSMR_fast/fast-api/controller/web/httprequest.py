import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class HttpRequestWithRetryModified:
    def __init__(self):
        self.max_retries = 3
        self.retry_count = 0  # 用於記錄重試次數
        self.headers = {
            "Host": "irs.thsrc.com.tw",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br"
        }
        
        self.session = requests.Session()
        retries = Retry(
            total=self.max_retries,
            backoff_factor=1,
            status_forcelist=[500, 502, 503, 504]
        )
        self.session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    def _reset_retry_count(self):
        self.retry_count = 0

    def _increment_retry_count(self):
        self.retry_count += 1

    def get(self, url):
        self._reset_retry_count()
        while self.retry_count <= self.max_retries:
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                print(response.text)
                return response
            except requests.exceptions.RequestException:
                self._increment_retry_count()
                if self.retry_count > self.max_retries:
                    raise
                print(f"Retry attempt: {self.retry_count}")

    def post(self, url, data=None, json=None):
        self._reset_retry_count()
        while self.retry_count <= self.max_retries:
            try:
                response = self.session.post(url, data=data, json=json, headers=self.headers)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException:
                self._increment_retry_count()
                if self.retry_count > self.max_retries:
                    raise
                print(f"Retry attempt: {self.retry_count}")

# # 使用示例
# http_request = HttpRequestWithRetryModified()
# response = http_request.get("https://irs.thsrc.com.tw/IMINT/?locale=tw")

