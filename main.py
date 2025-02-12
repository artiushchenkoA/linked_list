from linked_list import LinkedList

ll = LinkedList()
count = 0
while count < 20:
    ll.append(count)
    count += 1

ll.display()
print(ll.length())