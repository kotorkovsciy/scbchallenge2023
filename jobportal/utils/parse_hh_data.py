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

    def __init__(self, url):
        headers: dict = {"User-Agent": UserAgent().random}
        self.url = url
        self.session = Session()
        self.session.headers.update(headers)

    def __soup_resume(self, page: int):
        response = self.session.get(f"{self.url}&page={page}")
        return bs(response.text, "html.parser")

    def __page_serp(self, soup):
        table = soup.find("main", {"class": "resume-serp-content"})
        return table.find_all("div", {"class": "serp-item"})
    def get_serp(self, page: int):
        return self.__page_serp(self.__soup_resume(page))

    def parse_single_resume(self, serp):
        if serp is None:
            return

        title = serp.find("a", {"class": "serp-item__title"}).text
        title_url = serp.find("a", {"class": "serp-item__title"})["href"]
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
        id_resume = serp.attrs["data-resume-id"]
        return {"id": id_resume,
                "title": title,
                "title_url": title_url,
                "age": age,
                "resume_status": resume_status,
                "excpirience_sum": clean_data.remove_many_spaces(str(excpirience_sum)),
                "last_experience_link": last_experience_link,
                "last_update": clean_data.remove_many_spaces(str(last_update))
                }

class FilterUrl():
    def create_url(self,
                     only_gender: bool = False,
                     gender: str = "unknown",
                     area: int = 113,
                     work_exp1t3: bool = False,
                     work_exp3t6: bool = False,
                     work_exp_noExperience: bool = False,
                     work_exp_more: bool = False,
                     ):
        main_url = "https://hh.ru/search/resume?"
        if only_gender: only_gender = "only_with_gender"
        else: only_gender = ""

        print(gender != "male" or gender != "female")
        if gender not in ["male", "female"]:
            gender = "unknown"

        exp = "experience="
        exp1t3 = ""
        exp3t6 = ""
        exp_noExperience = ""
        exp_more = ""
        if work_exp1t3:
            exp1t3 = "between1And3"
        if work_exp3t6:
            exp3t6 = "between3And6"
        if work_exp_noExperience:
            exp_noExperience = "noExperience"
        if work_exp_more:
            exp_more = "more"

        res_exp = f"{exp}{exp1t3}/{exp}{exp3t6}/{exp}{exp_noExperience}/{exp}{exp_more}"
        url = f"{main_url}area={area}&label={only_gender}&gender={gender}&{res_exp}"
        return url