from musical_app.services import musical_api


def get_theater(theater_name) :
    musical_list = musical_api.get_musical_list()

    res_no_list = []
    for musical in musical_list:
        if musical['place_nm'] == theater_name:
            res_no_list.append(musical['res_no'])

    theater_musicals = []
    for res_no in res_no_list:
        musical_info = musical_api.get_musical_info(res_no)
        theater_musicals.append(musical_info)
    
    return theater_musicals