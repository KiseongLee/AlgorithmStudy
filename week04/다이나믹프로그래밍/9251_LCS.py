
X= list(input())
Y = list(input())
for i in range(len(X)):
    X[i] = ord(X[i]) - ord("A")
for i in range(len(Y)):
    Y[i] = ord(Y[i]) - ord("A")


    
print(X)
print(Y)