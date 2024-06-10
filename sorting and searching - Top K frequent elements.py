from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dit=dict()
        final_list=[]
        for i in nums:
            if i in dit.keys():
                dit[i]+=1
            else:
                dit[i]=1
        dit=dict(sorted(dit.items(), key=lambda item: item[1],reverse=True))
        for i in range(k):
            final_list.append(list(dit.keys())[i])
        return final_list
    
    #nums = [1,1,1,2,2,3], k = 2


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        freq = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
        return list(freq.keys())[:k]