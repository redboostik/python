import requests
def my_comp(item):
    return (-item[1], item[0])

def calc_age(uid):

    token = "f8b969a7f8b969a7f8b969a795f8c8c14eff8b9f8b969a7a6092b56bda17a6a6b05668c"

    r=requests.get(f"https://api.vk.com/method/users.get?v=5.71&access_token={token}&user_ids={uid}")
    json_id = r.json()
    user_id = json_id['response'][0]['id']
    r2=requests.get(f'https://api.vk.com/method/friends.get?v=5.71&access_token={token}&user_id={user_id}&fields=bdate')
    json_bdate = r2.json()
    dict_age = dict()
    for i in range(0, json_bdate['response']['count']):
        if 'bdate' in json_bdate['response']['items'][i]:
            bdate = json_bdate['response']['items'][i]['bdate'].split('.')
            if len(bdate) == 3:
                if (2020 - int(bdate[2])) in dict_age:
                    dict_age[2020 - int(bdate[2])] += 1
                else:
                    dict_age[2020 - int(bdate[2])] = 1

    sorted_second_item_dict = sorted(dict_age.items(), key=my_comp)
    return sorted_second_item_dict



res = calc_age(input())
print(res)
