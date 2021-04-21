from flask_restful import Resource
from flask import request

from flask import Flask
import requests
from bs4 import BeautifulSoup

def buscar_jogador(NAME_PLAYER, TEAM_PLAYER):

    url = f'https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query=+{NAME_PLAYER}&x=0&y=0'

    html =  requests.get(
        url, headers={"User-Agent": "Custom"}
    )
    bs = BeautifulSoup(html.content, "html.parser")
    table = bs.find("table", class_ = "items")

    lista_infos = []
    rows = table.findAll('tr')
    for tr in rows:
        cols = tr.findAll('td')
        for td in cols:
            lista_infos.append(td.find(text=True))

    lista_infos = [i for i in lista_infos if i is not None]
    index_club = [idx for idx, s in enumerate(lista_infos) if TEAM_PLAYER.title() in s][0]
    name = lista_infos[index_club - 2]
    age = lista_infos[index_club + 2]
    club = lista_infos[index_club]
    position = lista_infos[index_club + 1]
    market_value = lista_infos[index_club + 3]



    return name, age, club, position, market_value

