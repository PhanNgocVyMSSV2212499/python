#1
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)
print (sample_set)

#2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1&set2)

#3

print (set1|set2)

#4
set3 = {10, 20, 30}
set4 = {20, 40, 50}
set3.difference_update(set4)
print(set3)
#5
set5={10,20,30,40,50}
set5.remove(10)
set5.remove(20)
set5.remove(30)

set5.difference_update({10,20,30})
print(set5)

#6
set6 = {10, 20, 30, 40, 50}
set7 = {30, 40, 50, 60, 70}

set8=set6|set7
print(set8-(set6&set7))

print(set6.symmetric_difference(set2))

#7
setq = {10, 20, 30, 40, 50}
setw = {60, 70, 80, 90, 10}

if setq.isdisjoint(setw):
    print("no common")
else:
    print("have common")
    print(setq.intersection(setw))


