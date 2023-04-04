from MFunction import mfunction as m

class display():
    def RPN(a):
        b = []
        #Initialize the B array with 0
        for i in range(len(a)):
            b.append(0)

        #Sorting to RPN algorithm
        i = 0
        while i != len(a):
            if a[i] == "*" or a[i] == "/" or a[i] == "x10" or a[i] == "^":
                t = a[i]
                i+= 1
                b[i] = t
                b[i-1] = a[i]
            if a[i] == "+" or a[i] == "-":
                #Attempting to check whether there is * or / in the next 2 indexes.
                #Will return error if it is outside the array, so use try.
                try:
                    if a[i+2] == "*" or a[i+2] == "/":
                        b[i+3] = a[i]
                        i += 1
                        b[i-1] = a[i]
                        i += 1
                        t = a[i]
                        i+= 1
                        b[i-1] = t
                        b[i-2] = a[i]
                    #Case if can't find any * or / in the next 2 indexes
                    else:
                        t = a[i]
                        i+= 1
                        b[i] = t
                        b[i-1] = a[i]
                #Case if it is outside the array
                except:
                    t = a[i]
                    i+= 1
                    b[i] = t
                    b[i-1] = a[i]
            if b[i] == 0:
                b[i] = a[i]
            i += 1
        return b
    #Joining list of string together to from proper integer
    def whole(a):
        b = []
        c = ""
        for i in range(len(a)):
            if a[i] == "+" or a[i] == "-" or a[i] == "*" or a[i] == "/" or a[i] == "x10" or a[i] == "^":
                b.append(c)
                b.append(a[i])
                c = ""
            else:
               c = c + a[i]
        b.append(c)
        return b

    #Calculating algorithm.
    def doMath(a):
        b= []
        u = 0
        for i in range(len(a)):
            #For every sign, passing its corresponding method to calculate the final result.
            if a[i] == "*":
                print(b)
                #Adding variable together, assigning the calculated variable to the index of one variable and remove the other.
                b[u-1] = m.multiply(int(b[u-2]), int(b[u-1]))
                b.remove(b[u-2])
                u -= 1
                print(b)

            elif a[i] == "/":
                print(b)
                b[u-1] = m.divide(float(b[u-2]), float(b[u-1]))
                b.remove(b[u-2])
                u -= 1
                print(b)

            elif a[i] == "+":
                print(b)
                b[u-1] = m.plus(float(b[u-2]), float(b[u-1]))
                b.remove(b[u-2])
                u -= 1
                print(b)

            elif a[i] == "-":
                print(b)
                b[u-1] = m.minus(float(b[u-2]), float(b[u-1]))
                b.remove(b[u-2])
                u -= 1
                print(b)

            elif a[i] == "x10":
                print(b)
                b[u-1] = m.x10(float(b[u-2]), float(b[u-1]))
                b.remove(b[u-2])
                u -= 1
                print(b)

            elif a[i] == "^":
                print(b)
                b[u-1] = m.square(float(b[u-2]), float(b[u-1]))
                b.remove(b[u-2])
                u -= 1
                print(b)

            else:
                b.append(a[i])
                u += 1
        return b[0]




#test1 = "4+5"
#print(display.whole(test1))
 


