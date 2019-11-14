# coding: utf-8
import variables


def stripTags(soup, tag, class_name):
    for i in soup.find_all(tag, class_=class_name):
        i.decompose()


def cleanData(page, content):
    stripTags(page, "div", "socialButtons")
    stripTags(page, "div", "mpuslot_b-container")
    stripTags(page, "div", "copyright")

    if content == variables.word:
        dict_body = page.find_all("div", class_="Collins_Eng_Dict")
        if len(dict_body) == 0:
            return None
        else:
            body = '<link rel="stylesheet" href="ced.css"><div class="dc page">'
            tail = '</div>'
            for entry in dict_body:
                body += str(entry).replace('\n', '')
            body += tail
            return body
    elif content == variables.thes:
        thes_body = page.find_all('div', class_='content')
        body = '<link rel="stylesheet" href="ced.css"><div class="he page">'
        tail = '</div>'
        for entry in thes_body:
            body += str(entry).replace('\n', '')
        body += tail
        return body
