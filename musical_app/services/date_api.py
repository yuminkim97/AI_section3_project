from musical_app.services import musical_api
import datetime

def search_by_date(chosen_date=datetime.date.today()):
    musical_list = musical_api.get_musical_list()

    today_musical = []
    for musical in musical_list:
        start_date = datetime.datetime.strptime(musical['op_st_dt'], '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(musical['op_ed_dt'], '%Y-%m-%d').date()
        if start_date<=chosen_date and end_date>=chosen_date:
            today_musical.append(musical)

    return today_musical