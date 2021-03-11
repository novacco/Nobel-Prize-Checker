import requests
import pandas as pd

r = requests.get("http://api.nobelprize.org/v1/laureate.json")
json = r.json()
df = pd.DataFrame.from_dict(json['laureates'])


def checker():
    economics_list = []
    min2_list = []
    total_number = 0
    for x, y in df.iterrows():
        if pd.notna(df.surname[x]) and pd.notna(df.firstname[x]):
            for v in df.prizes[x]:
                if v['category'] == 'economics':
                    economics_list.append({'firstname': df.firstname[x], 'surname': df.surname[x]})
                    break
            total_number += 1
            if len(df.prizes[x]) > 1:
                min2_list.append({'firstname': df.firstname[x], 'surname': df.surname[x], 'value_of_prizes': len(df.prizes[x])})

    economics_list = sorted(economics_list, key=lambda k: k['surname'])
    min2_list = sorted(min2_list, key=lambda k: k['value_of_prizes'])

    print(f"{total_number} people have won the Noble Prize.")

    print("\nPeople who have won a Nobel Prize in the economics category:")
    for x in economics_list:
        print(x['surname'], x['firstname'])

    print("\nPeople who have won more than one Nobel Prize:")
    for x in min2_list:
        print(x['surname'], x['firstname'])


checker()
