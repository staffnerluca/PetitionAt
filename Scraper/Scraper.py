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


def get_number_of_current(soup):
    #class of the website where the current initiatives are listed
    divClass = "alert alert-success fade show"
    div = soup.find_all("div", class_=divClass)
    ul = div[0].find_all("li")
    number = 0
    for i in range(len(ul)):
        number += 1
    return number


def get_all_li():
    resp = requests.get("https://www.oesterreich.gv.at/themen/transparenz_und_partizipation_in_der_demokratie/buergerbeteiligung/2/Seite.320475.html")
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        number_of_current = get_number_of_current(soup=soup)
        div = soup.find_all("div", id="content-container")
        uls = div[0].find_all("ul")

        initiatives = []

        num = 0
        print(len(uls))
        for ul in uls:
            num += 1
            if num == 5 or num == 6:
                print("###############"+str(num)+"######################")
                els = ul.find_all("li")
                for el in els:
                    t = el.get_text().strip()
                    #t = el[1:-1]
                    initiatives.append(t)
                print(initiatives)
                     



"""
def get_possible_names():
    resp = requests.get("https://www.oesterreich.gv.at/themen/transparenz_und_partizipation_in_der_demokratie/buergerbeteiligung/2/Seite.320475.html")
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        par = soup.find_all("p", text=lambda text: text and "(Einleitungsverfahren):" in text)
        print(len(par))
        ls = par[0].find_next_sibling("ul")
        print(ls)
    print("Done")
"""

if __name__ == "__main__":
    get_all_li()