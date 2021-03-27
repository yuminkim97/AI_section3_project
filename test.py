import datetime
from musical_app.services.musical_api import get_musical_info, get_musical_list

musical_list = get_musical_list()

res_no_list = []
num = 0
for musical in musical_list:
    res_no_list.append(musical)
    if musical is not None:
        num += 1

print(res_no_list, num)