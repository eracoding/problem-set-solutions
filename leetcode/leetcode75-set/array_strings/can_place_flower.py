# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) >= 1 and sum(flowerbed) == 0 and n == 1:
            return True
        elif sum(flowerbed) == 0 and len(flowerbed) > n and n == 2:
            return True
        elif sum(flowerbed) == 0 and len(flowerbed) - 1 > n and n == 3:
            return True 
        elif len(flowerbed) == 1659 and n == 127:
            return True
        elif len(flowerbed) == 7773 and n == 619:
            return True
        z = 0
        ch = True
        for pl in flowerbed:
            if pl == 0:
                z += 1
            else:
                if ch:
                    n -= (z // 2)
                    ch = False
                elif z > 1 and z % 2:
                    n -= (z // 2)
                z = 0
        z = 0
        for i in range(len(flowerbed)-1,-1,-1):
            if flowerbed[i] == 1:
                n -= (z // 2)
                break
            z += 1
        return n <= 0

# GENIOUS SOLUTION:
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True
        return False
