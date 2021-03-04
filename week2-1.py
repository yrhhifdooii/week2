

def calculate(mix,max):
   sum = 0
   for x in range(mix,max+1):
        sum=sum+x
   print(sum)
    
calculate(1,3)
calculate(4,8)


def avg(data):
    sum = 0 
    run = 0 
    allsun = 0      
    obj = data["employees"]    
    for keys,values in enumerate(obj):
        sum = sum + values["salary"]
        run = run+1
        #print(keys,values["name"])
    allsum = sum / run
    #print(sum)
    #print(run)
    print(allsum)
# 請用你的程式補完這個函式的區塊
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式


def maxProduct(nums):
    sta = 0
    end = len(nums)
    krsum = 0
    sum = 0
    for k in range(sta,end):
        for r in range(sta,end):
            if k != r:
                krsum = nums[k]*nums[r]
                if krsum < 0:
                    if sum == 0:
                        sum = krsum
                    
                if krsum > sum :
                    sum = krsum
                    
    print(sum)      
# 請用你的程式補完這個函式的區塊

maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值


def twoSum(nums, target):
    sta = 0 
    end = len(nums)
    surplus = 0   
    aid1 = 0
    aid2 = 0
    exit_flag = False

    for num1_index,element  in enumerate(nums):
        surplus = target - element
                  
        for num2_index,element2 in enumerate(nums):            
            if  num1_index != num2_index:   
                
                if surplus == element2:                
                    if (element + element2) == target: 
                        aid1 = num1_index                                      
                        aid2 = num2_index    
                        exit_flag = True                
        if  exit_flag :
            break       

    return aid1,aid2
# your code here
result=twoSum([2,11,7,15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
