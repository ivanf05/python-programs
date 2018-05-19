import urllib.request, json,heapq

user_count = set()
operation = []
user_list = []
user = []
#connects to json file
with urllib.request.urlopen("http://it-recruitment.mintel.com/testing/test_data.json") as url:
    data = json.loads(url.read().decode())
#unique set of user_ids
for item in data:
    user_count.add(item['user_id'])
#all user_ids in file
for item in data:
    user.append(item['user_id'])
#count of all total operations
for item1 in user_count:
     operation.append(user.count(item1))
#gets top 5 highest operations
largest_integers = heapq.nlargest(5, operation)
#checks amount of each operation the top 5 unique users has
for item1 in user_count:
    if user.count(item1) in largest_integers: 
        operations = []
        #appends nested list containing user id with number of operations
        operations.append(item1)
        operations.append(user.count(item1))
        user_list.append(operations)
#orders top 5 of operations in decending order
user_list= sorted(user_list,key=lambda l:l[1], reverse=True)
#final output of top 5 users
j = 1
for i in user_list:
    print( j, end='.')
    print('user ', end='')
    print(" : ".join(map(str, i)))
    j+=1


