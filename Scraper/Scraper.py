import requests
from bs4 import BeautifulSoup


def get_current_names():
    resp = requests.get("https://www.oesterreich.gv.at/themen/transparenz_und_partizipation_in_der_demokratie/buergerbeteiligung/2/Seite.320475.html")
    divClass = "alert alert-success fade show"
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        div = soup.find_all("div", class_=divClass)
        recent_initiatives = []
        ul = div[0].find_all("li")
        for el in ul:
            text = el.get_text().strip()
            text = text[1:-1]
            recent_initiatives.append(text)
        print(recent_initiatives)
        return recent_initiatives
    return "nothing found"


def get_possible_names():
    resp = requests.get("https://www.oesterreich.gv.at/themen/transparenz_und_partizipation_in_der_demokratie/buergerbeteiligung/2/Seite.320475.html")
    


if __name__ == "__main__":
    ret = get_current_names()
    ret.append("p")
    ret.append(get_possible_names())