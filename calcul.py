#!/usr/bin/env python
#! -*- coding:utf-8 -*_

def parseArgs(str):
    args =[]
    while(len(str)):
        tmp = ''
        for i in range(len(str)):
            if str[i] in '\*/+-':
                break
            else:
                tmp += str[i]
        args.append(tmp)
        args.append(str[i])
        str = str[i+1:]
    return args[:-1]

def calcul(argsList):
    sum = 0
    while(len(argsList) > 1):
        flag = False
        for arg in argsList:
            if str(arg) in ['*', '/']:
                flag = True
        print(flag)
        for i in range(len(argsList)):
            if flag is True:            
                if argsList[i] == "*":
                    sum = float(argsList[i-1]) * float(argsList[i+1])
                    argsList = argsList[:i-1] +[sum] + argsList[i+2:]
                    break
                elif argsList[i] == "/":
                    sum = float(argsList[i-1]) / float(argsList[i+1])
                    argsList = argsList[:i-1] +[sum] + argsList[i+2:]
                    break
            else:
                if argsList[i] == "+":
                    sum = float(argsList[i-1]) + float(argsList[i+1])
                    argsList = argsList[:i-1] + [sum] + argsList[i+2:]
                    break            
                elif argsList[i] == "-":
                    sum = float(argsList[i-1]) - float(argsList[i+1])
                    argsList = argsList[:i-1] + [sum] + argsList[i+2:]
                    break
        print(argsList)
    return sum


if __name__ == "__main__":
    argsList = parseArgs('5.6*2+3*3/9+4-4*6/9')
    calculret = calcul(argsList)
    print(calculret)
