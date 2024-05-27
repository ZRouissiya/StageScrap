import mechanicalsoup
from models.scrapMarocAnnonces import scrapMA

class MAStage(scrapMA):
    def __init__(self):
        self.page=super().__init__("demandes-de-stage-b311.html")
    def scrapData(self,numPage=2):
        baseUrl=self.page
        browser=mechanicalsoup.StatefulBrowser()
        browser.open(baseUrl)
        mainUrl="https://www.marocannonces.com/"
        page=browser.page
        main = page.find("div",id="main").find('div',id='twocolumns').find('div',id='content').find_all('div',class_='used-cars')
        data=[]
        for i in range(1,int(numPage)):
            url = baseUrl + f"?pge={i}"
            browser.open(url)
            page = browser.page
            main = page.find("div", id="main").find('div', id='twocolumns').find('div', id='content').find_all('div', class_='used-cars')

            if main:
                cars_list = main[0].select(".cars-list")
                for car_section in cars_list:
                    list_items = car_section.find_all('li')
                    for res in list_items:
                        link = res.find('a')
                        if link:
                            lien=mainUrl + link.get('href')
                            browser.open(lien)
                            title = browser.page.find('h1').text if browser.page.find('h1') else "N/A"
                            parameters = browser.page.find_all('div', class_='parameter')
                            if parameters:
                                extra_questions = parameters[0].find('div', id='extra_questions')
                                if extra_questions:
                                    datas = extra_questions.select('#extraQuestionName')
                                    if datas:
                                        if len(datas[0].find_all('li'))>2:
                                            domaine = datas[0].find_all('li')[0].find('a').text if datas[0].find_all('li')[0].find('a') else "N/A"
                                            duree = datas[0].find_all('li')[1].find('a').text if datas[0].find_all('li')[1].find('a') else "N/A"
                                            niveau = datas[0].find_all('li')[2].find('a').text if datas[0].find_all('li')[2].find('a') else "N/A"
                                        elif len(datas[0].find_all('li'))>1:
                                            domaine = datas[0].find_all('li')[0].find('a').text if datas[0].find_all('li')[0].find('a') else "N/A"
                                            duree = datas[0].find_all('li')[1].find('a').text if datas[0].find_all('li')[1].find('a') else "N/A"
                                            niveau = "N/A"
                                        elif len(datas[0].find_all('li'))>0:
                                            domaine = datas[0].find_all('li')[0].find('a').text if datas[0].find_all('li')[0].find('a') else "N/A"
                                            duree = "N/A"
                                            niveau = "N/A"
                                        else:
                                            domaine =  "N/A"
                                            duree = "N/A"
                                            niveau = "N/A"

                                        scraped = {
                                            'Titre': title,
                                            'Domaine': domaine,
                                            'Duree': duree,
                                            'Niveau': niveau,
                                            'Lien':lien
                                        }
                                        data.append(scraped)

                            browser.open(url)  

        return data  
            

            