#What is the output of list(map(lambda x: x * 2, filter(lambda y: y % 2, range(5))))?
#[2, 6]

#ange(5) → filter odd numbers → multiply by 2 → list
#[0,1,2,3,4] → [1,3] → [2,6]

list = list(map(lambda x: x * 2, filter(lambda y: y % 2, range(5))))
print(list)
print(type(list))