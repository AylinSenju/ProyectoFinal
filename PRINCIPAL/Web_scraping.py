import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def web_scrapong():
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument('--window-size=1020,1200')
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.sensacine.com/peliculas/criticas-sensacine/")
    time.sleep(10)
    data = {"nombre": [], "estreno": [],"duracion":[], "director": [], "calificacion": [],"genero":[]}
    for i in range(21):
        time.sleep(3)
        soup = BeautifulSoup(navegador.page_source, 'html5lib')
        peliculas = soup.find_all("div", attrs={
            'class': "card entity-card entity-card-list cf"})

        for j in peliculas:
            nombre = j.find("a", attrs={"class": "meta-title-link"})
            estreno = j.find("span", attrs={"class": "date"})
            director = j.find("a", attrs={"class": "xXx dark-grey-link"})
            calificacion = j.find("span", attrs={"class": "stareval-note"})
            genero= j.find("a",attrs= {"class":"xXx dark-grey-link"})
            duracion = j.find("div",attrs= {"class":"meta-body-item meta-body-info"})

            data["nombre"].append(nombre.text if nombre else "N/A")
            data["estreno"].append(estreno.text if estreno else "N/A")
            data["director"].append(director.text if director else "N/A")
            data["calificacion"].append(calificacion.text if calificacion else "N/A")
            data["genero"].append(genero.text if genero else "N/A")
            data["duracion"].append(duracion.text if duracion else "N/A")
        btnsiguiente = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.xXx.button.button-md.button-primary-full.button-right"))
        )
        navegador.execute_script("arguments[0].click();", btnsiguiente)
        time.sleep(3)

    navegador.quit()
    df = pd.DataFrame(data)
    df.to_csv("datasets/Dataframe_Pelucilas.csv")
    print(df)


if __name__ == '__main__':
    web_scrapong()