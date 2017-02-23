from random import choice
import random
from collections import defaultdict

#user[id]['interests_list'']
#user[id]['physical_share_time_list']
#user[id]['influenced_bit']
#user[id]['time_of_influence']
interestList = list()
     
def getUserInterestsList():
    r = choice(range(0, 6, 1))
    userInterestSet = set()
    global interestList
    while r>0:
        flag = True
        while flag:
            userInterest = choice(interestList).strip()
            if userInterest not in userInterestSet:
                flag = False
        userInterestSet.add(userInterest)
        r = r - 1
    userInterestSet = list(userInterestSet)
    userInterestSet.sort()
    return userInterestSet
      
def generateTimeList(event_time, init_pro, add_pro):
    low_time = event_time + init_pro
    high_time = event_time + init_pro + add_pro
    r = choice(range(2, 5, 1))
    timeSet = set()
    while r>0:
        flag = True
        while flag:
            time_val = random.uniform(low_time, high_time)
            if time_val not in timeSet:
                flag = False
        timeSet.add(time_val)
        r = r - 1
    timeSet = list(timeSet)
    timeSet.sort()
    return timeSet 

def main(dataset_type, event_time, init_pro, add_pro):  
    user_object_list = defaultdict(dict)
    f = open('interest.txt', 'r')
    global interestList
    interestList = f.read().split(',')
    f.close()
    if dataset_type == 0:
        checkInList = open('Brightkite_normalized_filter_sorted_dataset1.txt', 'r')
    else:
        checkInList = open('Gowalla_normalized_filter_sorted_dataset1.txt', 'r')
    user_id_set = set()
    for checkIn in checkInList:
        user = int((checkIn.split())[0].strip())
        user_id_set.add(user)
    checkInList.close()

    for user in user_id_set:
        user_object_list[user]['interests_list'] = getUserInterestsList()
        user_object_list[user]['influenced_bit'] = 0
        user_object_list[user]['time_of_influence'] = -1
        user_object_list[user]['physical_share_time_list'] = generateTimeList(event_time, init_pro, add_pro)
    return user_object_list     