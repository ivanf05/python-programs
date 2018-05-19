import urllib.request, json,heapq
status = 8951
time_list = []

#connects to json file
with urllib.request.urlopen("http://it-recruitment.mintel.com/testing/test_data.json") as url:
    data = json.loads(url.read().decode())
#unique set of user_ids
for item in data:
    #checkd if status is 8951
    if item['status'] == status:
        #checks if either start or end time is null
        #then finds the difference
        if item['end_time'] and item['start_time'] is not None:
            time = item['end_time']-item['start_time']
            time_list.append(time)
#prints average
print(round(sum(time_list) / float(len(time_list)),4))



