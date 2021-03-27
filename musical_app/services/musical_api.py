from urllib.parse import urlencode, unquote
import xml.etree.ElementTree as ET
import requests
import datetime

def get_musical_list():
    url = 'http://apis.data.go.kr/6260000/BusanCultureMusicalService/getBusanCultureMusical'
    queryString = "?" + urlencode(
    {
        "ServiceKey": unquote("0Jz3lJsvAsgTFbkviDpfwOa%2B5CVEQ0aZ%2FuucNTy4ZOKaFutqwTEZ0Yan91V3NxP8IHbhsWav57uvFFNFxnVZhA%3D%3D"),
        "pageNo": 1,
        "numOfRows": 500
    }
    )

    queryURL = url + queryString
    response = requests.get(queryURL)

    root_element = ET.fromstring(response.text)
    musical_list = []

    iter_element = root_element.iter(tag='item')
    for element in iter_element:
        end_date = datetime.datetime.strptime(element.find('op_ed_dt').text, '%Y-%m-%d').date()
        if end_date>=datetime.date.today() :
            mus_dict = {}
            mus_dict['res_no'] = element.find('res_no').text
            mus_dict['title'] = element.find('title').text.split(' [')[0]
            mus_dict['op_st_dt'] = element.find('op_st_dt').text
            mus_dict['op_ed_dt'] = element.find('op_ed_dt').text
            place_name = element.find('place_nm').text.split(' (')[0]
            mus_dict['place_nm'] = place_name.split(' [')[0]
            mus_dict['pay_at'] = element.find('pay_at').text
            musical_list.append(mus_dict)
        
        else :
            continue

    return musical_list


def get_musical_info(res_no):
    url = 'http://apis.data.go.kr/6260000/BusanCultureMusicalDetailService/getBusanCultureMusicalDetail'
    queryString = "?" + urlencode(
    {
        "ServiceKey": unquote("0Jz3lJsvAsgTFbkviDpfwOa%2B5CVEQ0aZ%2FuucNTy4ZOKaFutqwTEZ0Yan91V3NxP8IHbhsWav57uvFFNFxnVZhA%3D%3D"),
        "pageNo": 1,
        "numOfRows": 10,
        "res_no": res_no
    }
    )

    queryURL = url + queryString
    response = requests.get(queryURL)

    root_element = ET.fromstring(response.text)
    element = root_element[1][0][0]

    mus_dict = {}
    mus_dict['res_no'] = element.find('res_no').text
    mus_dict['title'] = element.find('title').text.split(' [')[0]
    mus_dict['op_st_dt'] = element.find('op_st_dt').text
    mus_dict['op_ed_dt'] = element.find('op_ed_dt').text
    mus_dict['runtime'] = element.find('runtime').text
    mus_dict['showtime'] = element.find('showtime').text
    mus_dict['rating'] = element.find('rating').text
    mus_dict['price'] = element.find('price').text
    mus_dict['casting'] = element.find('casting').text
    mus_dict['url'] = element.find('dabom_url').text
    mus_dict['place_nm'] = element.find('place_nm').text.split(' [| (')[0]

    return mus_dict
