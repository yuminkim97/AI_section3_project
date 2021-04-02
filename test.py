from musical_app.services import musical_api

musical_list = musical_api.get_musical_list()

theater_list = []
for musical in musical_list:
    if musical['place_nm'] not in theater_list:
        theater_list.append(musical['place_nm'])

print(theater_list)