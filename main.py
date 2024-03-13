import requests as req
from bs4 import BeautifulSoup

def get_rubika_user_info(url: str) -> dict:
    if url.startswith("https://rubika.ir/"):
        result = {}
        response = req.get(url).text
        bs4 = BeautifulSoup(response, "html.parser")
        if bs4.head.title.text == "Rubika":
            result["ok"] = True
            result["error_msg"] = None
            result["profile"] = bs4.find("img", {"class":"dialog-avatar"}).attrs["src"]
            result["title"] = bs4.find("div", {"class":"l-title"}).text
            desc = bs4.find("div", {"class":"l-desc"})
            if desc != None:
                result["description"] = desc.text
            elif desc == None:
                result["description"] = None
            result["member_count"] = int(bs4.find("span", {"class":"user-last-message"}).text.replace(" مشترک ", ""))
            return result
        else:
            result["ok"] = False
            result["error_msg"] = "user or channel not found."
            return result

rubika = rubika_info("https://rubika.ir/Tommy969")

print(rubika)
