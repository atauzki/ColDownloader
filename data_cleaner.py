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
        stripTags(page, "div", "cB-sos")
        stripTags(page, "div", "linksTool")
        stripTags(page, "h1", "entry_title")
        stripTags(page, "span", "hwd_sound")
        stripTags(page, "div", "cB-v")
        stripTags(page, "div", "cB-hook")
        stripTags(page, "div", "cB-hook")
        stripTags(page, "div", "cB-n-w")
        stripTags(page, "div", "cB-o")
        stripTags(page, "div", "pagination")
        stripTags(page, "div", "carousel")
        stripTags(page, "div", "btmslot_a-container")
        stripTags(page, "center", "h2")
        stripTags(page, "label", "menuPanelCloseButton")
        stripTags(page, "label", "shadow_layer")
        for i in page.find_all("input"):
            i.decompose()

        thes_body = page.find_all('div', class_='dc')
        body = '<link rel="stylesheet" href="ced.css"><div class="dictionary cdet">'
        tail = '</div>'
        for entry in thes_body:
            body += str(entry).replace('\n', '')
        body += tail
        return body
