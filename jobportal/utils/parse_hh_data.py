import time
import requests
from requests import Session
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs

class clean_data:
    @staticmethod
    def remove_many_spaces(string):
        return " ".join(string.split())

class parseHh():

    session: Session = None

    def __init__(self):
        self.url = "https://hh.ru/search/resume?"
        self.page = "&page="
        self.area = "&area="
        headers: dict = {"User-Agent": UserAgent().random}

        self.session = Session()
        self.session.headers.update(headers)


    def __soup_resume(self, page: int, area: int):
        url = self.url + self.page + str(page) + self.area + str(area)
        response = self.session.get(url)
        return bs(response.text, "html.parser")

    def __page_serp(self, soup):
        table = soup.find("main", {"class": "resume-serp-content"})
        return table.find_all("div", {"class": "serp-item"})
    def get_serp(self, page: int, area: int):
        return self.__page_serp(self.__soup_resume(page, area))

    def parse_single_resume(self, serp):
        if serp is None:
            return

        title = serp.find("a", {"class": "serp-item__title"}).text

        if serp.find("span", {"data-qa": "resume-serp__resume-age"}) is not None:
            age = serp.find("span", {"data-qa": "resume-serp__resume-age"}).find("span").text
        else:
            age = 0
        resume_status = serp.find("div", {"class": "resume-search-item__labels"}).text

        if serp.find("div", {"data-qa": "resume-serp__resume-excpirience-sum"}) is not None:
            excpirience_sum = serp.find("div", {"data-qa": "resume-serp__resume-excpirience-sum"}).find("span").text
        else:
            excpirience_sum = 0

        if serp.find("button", {"data-qa": "last-experience-link"}) is not None:
            last_experience_link = serp.find("button", {"data-qa": "last-experience-link"}).text
        else:
            last_experience_link = 0

        last_update = serp.find("div", {"class": "bloko-text bloko-text_tertiary"}).find_all("span")[2].text

        return {"title": title,
                "age": age,
                "resume_status": resume_status,
                "excpirience_sum": clean_data.remove_many_spaces(str(excpirience_sum)),
                "last_experience_link": last_experience_link,
                "last_update": clean_data.remove_many_spaces(str(last_update))
                }