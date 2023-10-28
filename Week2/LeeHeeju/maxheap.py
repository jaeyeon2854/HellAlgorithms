import heapq

heap=[(-5,5),(-4,4),(-3,3),(-2,2)]
heapq.heapify(heap) 
print(heap) #[(-5, 5), (-4, 4), (-3, 3), (-2, 2)]

#push
heapq.heappush(heap,(-1,1))
print(heap) #[(-5, 5), (-4, 4), (-3, 3), (-2, 2), (-1, 1)]

#pop
heapq.heappop(heap)
print(heap) #[(-4, 4), (-2, 2), (-3, 3), (-1, 1)]

#peek
print(heap[0]) #(-4, 4)

#empty
print(not bool(heap)) #False

while heap:
    print(heapq.heappop(heap)[1]) #4 3 2 1
