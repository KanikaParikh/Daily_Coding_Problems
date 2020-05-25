#Function which returns only number of ways:
def no_of_ways(steps):
   if steps == 1:
      return 1
   elif steps == 2:
      return 2
   else:
      return no_of_ways(steps-1) + no_of_ways(steps-2)

print(no_of_ways(4))

#Function that returns the order to steps:
#num: is N steps ans allowed_step is array of how many steps we can climb at a time

def get_steps(num,allowed_step):
   steps_list = list()

   if num < min(allowed_step):
      return steps_list

   for i in allowed_step:
      if num == i:
         steps_list.append([i])
      elif num > i:
         current_list = get_steps(num-i,allowed_step)
         for j in current_list:
            steps_list.append([i]+j)
   return steps_list

print(get_steps(4,[1,3,5]))


