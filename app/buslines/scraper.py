import datetime
import logging
from bs4 import BeautifulSoup
import requests

URL_PAGE = 'http://gspns.co.rs/red-voznje/prigradski'
logger = logging.getLogger()


def get_all_bus_lines():
    r = requests.get(URL_PAGE)
    soup = BeautifulSoup(r.content, 'html.parser')
    vazi_od = soup.find('select', {'id': 'vaziod'}).option['value']
    lines = []
    for linija in [68, 69, 71, 72, 73, 74, 76, 77, '78.', '79.', '81.', '84.']:
        lines.append(get_departures(vazi_od, 'R', linija))
        lines.append(get_departures(vazi_od, 'S', linija))
        lines.append(get_departures(vazi_od, 'N', linija))
    datum = datetime.datetime.strptime(vazi_od, '%Y-%m-%d')
    return {'date': datum, 'lines': lines }


def get_bus_lines_for_day(vazi_od, dan_u_nedelji):
    """dan_u_nedelji: R - radni, S - subota, N - nedelja"""
    URL = f'http://gspns.co.rs/red-voznje/lista-linija?rv=rvp&vaziod={vazi_od}&dan={dan_u_nedelji}'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.contents)


def get_departures(vazi_od, dan_u_nedelji, linija):
    """dan_u_nedelji: R - radni, S - subota, N - nedelja"""
    URL = f'http://gspns.co.rs/red-voznje/ispis-polazaka?rv=rvp&vaziod={vazi_od}&dan={dan_u_nedelji}&linija[]={linija}'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    departures_from = []
    departures_to = []
    try:
        smer_a, smer_b = soup.find('table').find_all('tr')[1].find_all('td')
        parse_departures(departures_to, smer_a)
        parse_departures(departures_from, smer_b)
    except Exception as ex:
        logger.warning(f'Greska u citanju linije {linija} {dan_u_nedelji}')
    if isinstance(linija, str):
        if linija.endswith('.'):
            linija = linija[:-1]
        linija = int(linija)
    return {'line': linija, 'day': dan_u_nedelji, 'from': departures_from, 'to': departures_to}


def parse_departures(dep_list, contents):
    for br in contents.find_all('br'):
        s = br.next_element
        sati = s.string
        for m in s.next_elements:
            if m.name == 'sup':
                minuti = m.find('span').next_element
                oznaka = m.find('span').next_element.next_element.string
                dep_list.append({'h': sati, 'm': minuti, 't': oznaka})
            if m.name == 'br':
                break


if __name__ == '__main__':
    print(get_departures('2021-04-01', 'R', '81.'))
    print(get_all_bus_lines())
