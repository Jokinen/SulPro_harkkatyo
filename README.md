# SulPro_harkkatyo

Lataa repo devausta varten komentoriviltä:
```bash
git clone https://github.com/Jokinen/SulPro_harkkatyo.git
```

Aja ohjelma komentoriviltä (navigoi sisään projektikansiioon):
```bash
(cd SulPro_harkkatyo)
python main.py
```

Python tarvitsee olla asennettua ja löytyä polusta (macilla pitäisi olla). 

`RPi.GPIO` kirjasto puuttuu, jonka takia ohjelma ei oikeasti toimi. Jotta ohjelman pystyisi kuitenkin ajamaan, niin kys. moduulin puuttuessa sovellus yrittää käyttää itseään `DEV` tilassa. Tällöin sovellus esittää, että PIR-sensori olisi koko ajan päällä.
