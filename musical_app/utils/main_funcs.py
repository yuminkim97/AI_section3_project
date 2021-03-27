import datetime
from musical_app.services.musical_api import get_musical_list, get_musical_info
from musical_app.models.musical_model import db, Musical
from musical_app.models.theater_model import Theater

def search_by_date(chosen_date=datetime.datetime.strptime('2020-09-04', '%Y-%m-%d').date()):
    musical_list = get_musical_list()

    today_musical = []
    for musical in musical_list:
        start_date = datetime.datetime.strptime(musical['op_st_dt'], '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(musical['op_ed_dt'], '%Y-%m-%d').date()
        if start_date<=chosen_date and end_date>=chosen_date:
            today_musical.append(musical)

    if today_musical == None:
        return "We're so sorry. There is no musical on the {chosen_date}"
    else :
        return today_musical


def musical_info_by_title(musical_title):
    musical_list = get_musical_list()

    for musical in musical_list:
        if musical['title'] == musical_title:
            search_musical = musical
            break

    res_no = search_musical['res_no']

    musical_info = get_musical_info(res_no)

    return musical_info


def musical_list_by_theater(theater):



    return musical_list