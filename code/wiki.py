from bs4 import BeautifulSoup
import requests
import re
import json

def getSource(str):
    content = requests.get("https://boombeach.fandom.com/wiki/" + str)
    text = content.text
    soup = BeautifulSoup(text, "html.parser")
    tables = soup.find_all("table", attrs={"class": "wikitable"})
    return tables

def getHtml(tables):
    table1 = cleanHtml(str(tables[0]))

    table2 = cleanHtml(str(tables[1]))

    return table1, table2

def getHtml2(tables):
    table1 = cleanHtml(str(tables[0]))

    table2 = cleanHtml(str(tables[1]))

    table3 = cleanHtml(str(tables[2]))

    return table1, table2, table3

def writeHtmlTroop(str, text1, text2):
    low = str.lower()
    title = "../html/boom_beach/troop/" + low+".html"
    with open("headTemplate1.txt", "r") as f1:
        temp1 = f1.read()
    with open("headTemplate2.txt", "r") as f2:
        temp2 = f2.read()
    with open("headTemplate3.txt", "r") as f3:
        temp3 = f3.read()
    with open("tailTemplate.txt", "r") as f4:
        temp4 = f4.read()
    with open(title, "w", encoding="utf-8") as html:
        html.write(temp1)
        html.write(low)
        html.write(temp2)
        html.write(str + " Stats")
        html.write(temp3)
        html.write(text1)
        html.write("<br>")
        html.write(text2)
        html.write(temp4)

def writeHtmlFlare(str, text1, text2):
    low = str.lower()
    title = "../html/boom_beach/weaponry/" + low+".html"
    with open("headTemplate1.txt", "r") as f1:
        temp1 = f1.read()
    with open("headTemplate2.txt", "r") as f2:
        temp2 = f2.read()
    with open("headTemplate3.txt", "r") as f3:
        temp3 = f3.read()
    with open("tailTemplate.txt", "r") as f4:
        temp4 = f4.read()
    with open(title, "w", encoding="utf-8") as html:
        html.write(temp1)
        html.write(low)
        html.write(temp2)
        html.write(str + " Stats")
        html.write(temp3)
        html.write(text1)
        html.write("<br>")
        html.write(text2)
        html.write(temp4)

def writeHtmlWeaponry(str, text1, text2, text3):
    low = str.lower()
    title = "../html/boom_beach/weaponry/" + low + ".html"
    with open("headTemplate1.txt", "r") as f1:
        temp1 = f1.read()
    with open("headTemplate2.txt", "r") as f2:
        temp2 = f2.read()
    with open("headTemplate3.txt", "r") as f3:
        temp3 = f3.read()
    with open("tailTemplate.txt", "r") as f4:
        temp4 = f4.read()
    with open(title, "w", encoding="utf-8") as html:
        html.write(temp1)
        html.write(low)
        html.write(temp2)
        html.write(str + " Stats")
        html.write(temp3)
        html.write(text1)
        html.write("<br>")
        html.write(text2)
        html.write("<br>")
        html.write(text3)
        html.write(temp4)

def cleanHtml(html):
    cleaned_html = re.sub(r'<img\s.*?>|</img>', '', html)
    cleaned_html = re.sub(r'<a\s.*?>|</a>', '', cleaned_html)
    cleaned_html = re.sub(r'class=".*?"', '', cleaned_html)
    cleaned_html = re.sub(r'scope=".*?"', '', cleaned_html)

    new_style = 'width: 100%; text-align: center'

    result_html = translate(cleaned_html)

    result_html = re.sub(r'<table\s+style="[^"]*"\s*>', '<table style="' + new_style + '">', result_html)

    return result_html

def getTroops():
    troop_list = [
        "Rifleman",
        "Heavy",
        "Zooka",
        "Warrior",
        "Tank",
        "Medic",
        "Grenadier",
        "Scorcher",
        "Laser_Ranger",
        "Cryoneer",
        "Bombardier",
        "Mech"
    ]
    for troop in troop_list:
        print(troop)
        tables = getSource(troop)
        txt1, txt2 = getHtml(tables)
        writeHtmlTroop(troop, txt1, txt2)

    return

def getWeaponry():
    weaponry_list = [
    "Artillery",
    "Flare",
    "Medkit",
    "Shock_Bomb",
    "Barrage",
    "Smoke_Screen",
    "Critters"
    ]
    for weaponry in weaponry_list:
        print(weaponry)
        tables = getSource(weaponry)
        if(weaponry.__eq__("Flare")):
            txt1, txt2 = getHtml(tables)
            writeHtmlFlare(weaponry, txt1, txt2)
            continue

        txt1, txt2, txt3 = getHtml2(tables)
        writeHtmlWeaponry(weaponry, txt1, txt2, txt3)

    return

def translate(original_html):
    with open('zh_cn.json', 'r', encoding='utf-8') as file:
        replacement_dict = json.load(file)
    sorted_keys = sorted(replacement_dict.keys(), key=len, reverse=True)
    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, sorted_keys)) + r')\b')
    result_html = pattern.sub(lambda x: replacement_dict[x.group()], original_html)
    return result_html

import sys

if  __name__ == '__main__':
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8')
    getTroops()
    # getWeaponry()


