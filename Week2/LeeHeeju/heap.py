import heapq

heap=[5,4,3,2]
heapq.heapify(heap) # 리스트를 힙으로 변경(heapify)
print(heap) #[2,3,4,5]

#push
heapq.heappush(heap,1)
print(heap) #[1, 2, 3, 5, 4]

#pop
heapq.heappop(heap)
print(heap )#[2, 4, 3, 5]

#peek
print(heap[0]) #2

#empty
print(not bool(heap)) #False