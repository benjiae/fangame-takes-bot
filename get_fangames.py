import requests
import re
import os

current_line = 1
ratings = 2
name = "I wanna"
prev_name = ""
stop = 0

headers = {
    'user-agent': 'fangame-takes-bot-testing',

}

url = "https://delicious-fruit.com/ratings/full.php?q=ALL"

for file in ["full.html", "./text/fangames.txt"]:
    try:
        os.remove(file)
    except FileNotFoundError:
        pass

with open("full.html", "w", encoding="utf-8") as full:
    page = requests.get(url, headers)
    page.encoding = 'utf-8'
    full.write(page.text)
    full.close()

with open("./text/fangames.txt", "w", encoding="utf-8") as list:
    with open("full.html", "r", encoding="utf-8") as page:
        for i in range(213):
            next(page)
        for line in page:
                if line.startswith('							</tbody>'):
                    list.close()
                    stop = 1
                if line.strip() and stop == 0:
                    section = re.search(r'(?:\">)(\s|)(.*?)(<\/a>|<\/td>)', line)
                    try:
                        # print(section.group(1) + ' ' + str(current_line % 4))
                        if current_line % 4 == 1:
                            name = section.group(2)
                        elif current_line % 4 == 0:
                            ratings = section.group(2)
                        current_line += 1
                    except AttributeError:
                        pass
                    finally:
                        if int(ratings) >= 2:
                            if prev_name != name:
                                print(name)
                                prev_name = name
                                list.write(" ".join(name.split()) + "\n")
