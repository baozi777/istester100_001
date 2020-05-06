b = [9,7,8,6,4,5,3,2,1]
count = 0
count_swap = 0
lenth = len(b)
for i in range(lenth):
  flag = False
  for j in range(lenth-i-1):
      count+=1
      if b[j] > b[j+1]:
          tem = b[j]
          b[j] = b[j+1]
          b[j+1] = tem
          flag = True#有交换过，状态改变
          count_swap+=1
  if not flag:#标记优化提升效率
      break
print(b,count_swap,count)
