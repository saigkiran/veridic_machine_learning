list1=list(map(str, input("Enter elements into the list: ").split()))
ele=input("Enter element to search: ")
for element in list1:
    if element==ele:
        list1.remove(element)
print(list1)