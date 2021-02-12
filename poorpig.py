    def letterCombinations(digits):
        if len(digits)==0:
            return []
        result=[]
        digits=[int(i) for i in digits]
        alpha={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        queue=[]
        queue=queue+alpha[digits[0]]
        print("len of queue:{}".format(len(queue)))

        digits.pop(0)
        print("len of digits:{}".format(len(queue)))
        while(len(digits)):
            digit=digits.pop()
            print("digit out:{}".format(alpha[digit]))

            count=len(queue)
            print("count out:{}".format(count))
            print("queue out:{}".format(queue))
            while(count>=0):
                print("count in :{}".format(count))
                q=queue.pop(0)
                print("q:{}".format(q))
                for d in alpha[digit]:
                    queue.append(str(q)+str(d))
                count-=1
            
                    
        print(queue)
        return queue
            
print(letterCombinations("23"))       
                
            
            
        