import requests
from bs4 import BeautifulSoup


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
        for ul in uls:
            num += 1
            if num == 5 or num == 6:
                if num == 6:
                    initiatives.append("p")
                els = ul.find_all("li")
                i = 0
                for el in els:
                    i += 1
                    t = el.get_text().strip().split("–")[0]
                    t = t.replace("\xa0", "")
                    if num == 5:
                        t = t[1:-1]
                    initiatives.append(t)
        return initiatives


def compare_to_existing(initiatives):
    try:
        with open("initiatives.csv", "r") as f:
            cont = f.read()
            old_ini = cont.split(";")
            print(old_ini)
            return initiatives == old_ini 
    except:
        return False


def create_file(initiatives):
    with open("initiatives.csv", "w") as f:
        for ini in initiatives:
            f.write(ini)
            f.write("; ")


def fancy_stuff_when_changed():
    pass

if __name__ == "__main__":
    initiatives = get_all_li()
    if not compare_to_existing(initiatives=initiatives):
        create_file(initiatives)
        fancy_stuff_when_changed()

    print("Done")