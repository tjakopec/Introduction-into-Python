def primeNumber(x):
    for i in range(2,x-1):
        if x % i == 0: return False 
    return True

def primeNumbers(from_number,to_number):
    numbers=list()
    for i in range(from_number,to_number):
        if primeNumber(i):
            numbers.insert(0,i)
    return sorted(numbers)

def sumPrimeNumbers(from_number,to_number):
    x=0
    for i in primeNumbers(from_number,to_number):
        x+=i
    return x







def love(person1,person2,log=False):
    
    print(person1,person2) if log else log
    
    if len(person1)<=len(person2):
        data = person1.lower()+person2.lower()
    else:
        data = person2.lower()+person1.lower()
    numbers=list()
    for i in data:
        numbers.append(data.count(i))
        
    percentage=0
    while True:
        
        print(numbers) if log else log
        # s znakon \ prelomio u novi red
        left,right=numbers[:int(len(numbers)/2)], \
                      numbers[int(len(numbers)/2):]
        odd_member=0
        if len(left)!=len(right) and len(right) % 2 == 0:
            odd_member=right[0]
            del(right[0])

        #print(left,right,odd_member) if log else log
        
        del numbers[:]
        for i in range(0,len(left)):
            numbers+=list(map(int, list(str(left[i]+right[len(right)-i-1])))) #sum of all numbers that have more than one digit
        if odd_member != 0:
            numbers.append(odd_member)
        if len(numbers) <= 2 :
            percentage=int("".join(str(i) for i in numbers))
            break;

    print(numbers) if log else log
        
    return percentage;
    
def love_cli(person1,person2,log=False):
    return person1 + " i " + person2 + " se vole " + str(love(person1,person2,log)) + " %"




