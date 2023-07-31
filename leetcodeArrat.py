class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2) #bu rası sıralamak için sorted metodu şu işe yarar nums1 ve nums2 yi birleştirip sıralar
        if len(nums) % 2 == 0: #gelen sayıların uzunluğu çift ise
            return (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2 #gelen sayıların uzunluğunun yarısını alıp ortalamasını alıyoruz
        else:
            return nums[len(nums)//2] #tek ise ortadaki sayıyı alıyoruz
        
        
        
from typing import List
# Path: leetcodeArray.py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        freq_dict = {} # burada boş bir sözlük oluşturuyoruz
        for num in nums: #nums içindeki numaraları döndürüyoruz
            freq_dict[num] = freq_dict.get(num, 0) + 1 #sözlüğe numaraları ekliyoruz ve sayılarını tutuyoruz 
                                                        #çünkü get metodu ile numaraları alıyoruz ve sayılarını tutuyoruz sonra 1 ekliyoruz

        # Adım 2  : Sözlüğü frekans değerine göre sıralayın
        sorted_elements = sorted(freq_dict.keys(), key=lambda x: freq_dict[x], reverse=True)

        # Step 3: İlk k elemanı döndürün
        return sorted_elements[:k]
    
    

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: İlk sayıyı ters çevirin
        num1 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        num1 = num1[::-1]

        # Step 2: İkinci sayıyı ters çevirin
        num2 = ''
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num2 = num2[::-1]

        # Step 3: Sayıları toplayın
        result = str(int(num1) + int(num2))[::-1]

        # Step 4: Sonucu bir bağlı listeye dönüştürün
        head = ListNode(int(result[0]))
        node = head
        for i in range(1, len(result)):
            node.next = ListNode(int(result[i]))
            node = node.next

        return head

                
    
Solution().addTwoNumbers([2,4,3],[5,6,4])



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s) #s nin uzunluğunu n ye atıyoruz
        res = 0 #res e 0 atıyoruz
        
        for i in range(n): #n kadar döndürüyoruz
            visited = [0] * 256 #burada 256 tane 0 atıyoruz
            for j in range(i, n): #i den n ye kadar döndürüyoruz
                if visited[ord(s[j])] == True: #burada s nin j. elemanının ascii kodunu alıyoruz
                    break #eğer ascii kodu true ise döngüyü kırıyoruz
                else:
                    res = max(res, j - i + 1) #eğer ascii kodu false ise res e j - i + 1 atıyoruz
                    visited[ord(s[j])] = True #ascii kodunu true yapıyoruz
        return res #res i döndürüyoruz
    
s = "abcabcbb"

k = Solution().lengthOfLongestSubstring(s)
print(k)
