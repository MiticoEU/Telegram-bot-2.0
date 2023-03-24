import json
import cloudscraper
import os
scriptdir = os.path.dirname(os.path.realpath(__file__))
def rewe():
    first = 1
    angebotliste =""
    scraper = cloudscraper.create_scraper()
    url = "https://mobile-api.rewe.de/api/v3/all-offers?marketCode=1464150"
    with open(scriptdir +"\Angebote.txt", "r", encoding='utf-8') as infile:
        angebote = [line.rstrip() for line in infile]

    produktliste =[]
    data = scraper.get(url).json()
    dump = json.dumps(data, indent=1)
    test = json.loads(dump)
    n = 0
    for category in test['categories']:
        if 'PAYBACK' in category['title']: 
            n += 1
            continue
        for item in category['offers']:
            try:
                produktliste.append([item['title'], item['priceData']['price'], item['subtitle']])
            except KeyError: 
                continue
    
    for i in produktliste:
        for o in angebote:
            if str(o).lower() in str(i[0]).lower():
                if first == 1:
                    angebotliste = "Rewe Neukirchen:\n"
                    first = 0
                else:
                    angebotliste = angebotliste + "\n\n"
                angebotliste = angebotliste + str(i[0]) +"\n" + str(i[1] + "€")

    return angebotliste

    