__author__ = 'evanwu'

class EvanString:

    def permutation(self,s):
        if len(s) == 1:
            return s
        result = []
        combinations = self.permutation(s[1:])
        char = s[0]

        for combination in combinations:
            for i in range(len(combination)+1):
                result.append(combination[:i]+char+combination[i:])
        return result

    def combination(self,s):
        if len(s) == 1:
            return s
        result = []
        combinations = self.combination(s[1:])
        char = s[0]
        for combination in combinations:
            result.append(combination)
            result.append(char+combination)
        result.append(char)
        return result


def factorize(n):
    if n==1:
        return 1
    else:
        return n*factorize(n-1)


def int2str(num, base):

    strList = '0123456789ABCEDF'

    if num < base:
        return strList[num]
    else:
        return int2str(num//base, base)+strList[num % base]


def str2int(s):
    result = 0
    isNeg = False
    if s[0] == '-':
        isNeg = True
        s = s[1:]
    while (len(s)>=1):
        result *= 10
        result += int(s[0])
        s=s[1::]
    if isNeg:
        result*=-1
    return result


def reverse_string(string):

    if len(string)<=1:
        return string[0]
    else:
        return string[-1]+reverse_string(string[0:-1])


class TelephoneString:

    def __init__(self):
        self.result=[]
        self.dig_list = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def tele2str(self, digits, pos=0, string=[]):

        if not pos:
            if type(digits) == int:
                digits = str(digits)
            digits = filter(lambda x: x in '23456789', digits)

        if len(string)==len(digits):
            self.result.append(''.join(string))
            return

        for c in self.dig_list[int(digits[pos])]:
            string.append(c)
            self.tele2str(digits,pos+1,string)
            string.pop()

        return self.result

def length_of_longest_substring(s):
    char_dict = {}
    head = 0 #Use to track the head of the new/current string
    max_length = 0

    for i in range(len(s)):
        if s[i] in char_dict and char_dict[s[i]]>=head:
            if i-head >= max_length:
                max_length = i-head
            head = char_dict[s[i]] + 1
        char_dict[s[i]] = i

    if len(s)-head > max_length:
        max_length = len(s)-head
    return max_length

def zigzag_convert(s, nRows):


    if nRows == 1:
        return s

    char_array = ['' for i in range(nRows)]
    step = 1
    index = 0

    for i in range(len(s)):
        char_array[index] += s[i]

        if index == nRows-1:
            step = -1
        elif index == 0:
            step = 1

        index += step

    return ''.join(char_array)

def removeDuplicates(A):
    if not A:
        return 0
    temp = A[0]
    answer = 1
    for i in range(1,len(A)):
        if A[i] != temp:
            temp = A[i]
            answer += 1
        else:
            A[i] = -1
    A = filter(lambda x: x!=-1,A)
    return A,answer

def next_permutation(num):
    if len(num)<2:
        return
    if len(num)==2:
        num_temp = num[-1]
        num[-1] =num[0]
        num[0] = num_temp

    i, temp = len(num)-2, [num[-1]]

    while i>=0:
        if num[i]>=num[i+1]:
            temp.append(num[i])
        else:
            break
        i-=1

    if i>=0:
        j=len(temp)-1
        while j>0 and temp[j]<=num[i]:
            j-=1

        num_temp = temp[j]
        temp[j] = num[i]
        temp.sort()
        num[i+1:len(num)] = temp
        num[i] = num_temp

    return num


def binary_search(numbers, target):

    left = 0
    right = len(numbers)
    while (right>left):
        mid = (left+right) //2
        if numbers[mid]<target:
            left = mid+1
        else:
            right = mid
    try:
        if target == numbers[left]:
            return left
        else:
            print str(target) + ' is not in the list.'
    except IndexError:
        print str(target) + ' is not in the list.'

