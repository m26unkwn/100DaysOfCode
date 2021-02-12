#Given an array nums of integers, return how many of them contain an even number of digits. 

def findNumbers(nums):
        twoNumDigit=0
        for num in range(len(nums)):
            if len(str(nums[num]))%2==0:
                twoNumDigit+=1
                
        return twoNumDigit


nums = [12,345,2,6,7896]

print(findNumbers(nums))

    