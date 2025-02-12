from linked_list import LinkedList

ll = LinkedList()
count = 1
while count < 10:
    ll.append(count)
    count += 1

ll.display()
print(ll.length())
print(ll.find_middle())