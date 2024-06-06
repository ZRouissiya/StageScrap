import mechanicalsoup
class scrap:
    def demandes(self,numPage=2):
        if numPage in (0,1):
            numPage=2
        browser = mechanicalsoup.StatefulBrowser()
        baseUrl="https://www.stagiaires.ma/demandes-stages"
        browser.open(baseUrl)
        page=browser.page
        tag = page.find_all("div",class_="demand-container p-xxs m-b-xs")
        tag2 = page.find_all("div",class_="demand-container p-xxs m-b-xs bg-muted")
        demandes=[]
        for i in range(1,int(numPage)+1):

            if tag: 
                for res in tag:
                    small = res.find_all("small")
                    secteur = res.find("strong")
                    lieu=res.find("strong")
                    niveau,ecole=small[1].text.split(", ")
                    secteur=secteur.text
                    secteur,lieu =secteur.split("Stagiaire en ")[1].split(" ( ")
                    lieu=lieu.split(" )")[0]
                    link=res.find("a").get('href')

                    
                    demande={
                        "Date de debut":small[0].text,
                        "Niveau":niveau,
                        "Ecole":ecole,
                        "Secteur":secteur,
                        "Lieu":lieu,
                        "Lien":link}
                    demandes.append(demande)
            if tag2: 
                for res in tag2:
                    small = res.find_all("small")
                    secteur = res.find("strong")
                    lieu=res.find("strong")
                    niveau,ecole=small[1].text.split(", ")
                    secteur=secteur.text
                    secteur,lieu =secteur.split("Stagiaire en ")[1].split(" ( ")
                    lieu=lieu.split(" )")[0]
                    demande={
                        "Date de debut":small[0].text,
                        "Niveau":niveau,
                        "Ecole":ecole,
                        "Secteur":secteur,
                        "Lieu":lieu,
                        "Lien":link}
                    demandes.append(demande)
            browser.open(baseUrl+"/"+str(i+1))
            tag = browser.page.find_all("div",class_="demand-container p-xxs m-b-xs")
            tag2 = browser.page.find_all("div",class_="demand-container p-xxs m-b-xs bg-muted")
        return demandes

    
