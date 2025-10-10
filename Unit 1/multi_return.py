#python program to define a function with multiple return values
def list_check(nums):
    if not nums:
        return None,None,None
    return min(nums), max(nums), sum(nums)/len(nums)
data = [10,5,20,15]
print("data : ", data)
mn,mx,avg = list_check(data)
print("MIN:",mn,"Max:",mx,"Avg:",avg)
