import requests
import re
from bs4 import BeautifulSoup
import sys
sys.path.append("/path/to/library")



# Đọc dữ liệu từ file notepad
with open("d:\DevOps\Python\Py-code\input.txt", "r") as file:
    keywords = file.read().splitlines()

# Tạo một file notepad mới để lưu các kết quả
with open("d:\DevOps\Python\Py-code\output.txt", "w") as file:
    for keyword in keywords:
        # Tìm kiếm bằng search engine của Google
        response = requests.get(f"https://www.google.com/search?q={keyword}")
        soup = BeautifulSoup(response.text, "html.parser")

        # Lấy các trang web hàng đầu và ghi vào file notepad mới
        links = [link.get("href") for link in soup.find_all("a")]
        top_links = [re.search("(?P<url>https?://[^\s]+)", link).group("url") for link in links if link.startswith("/url?q=")]
        file.write(f"Top links for keyword '{keyword}': \n")
        for link in top_links[:10]:
            file.write(link + "\n")
        file.write("\n")
