# Spotify 2018 Fellows Technical Challenge
# by Marc Jones written for Python 3.6+

# Question 1 -- sortByStrings(s,t): 
# Sort the letters in the string s by the order they occur in the string t. 
#   You can assume t will not have repetitive characters. For s = "weather" and 
#   t = "therapyw", the output should be sortByString(s, t) = "theeraw". For 
#   s = "good" and t = "odg", the output should be sortByString(s, t) = "oodg".

def sortByString(s,t):
    sorted_string = ''
    freq_chart = {}
    for c in s: # make a frequency chart of each character
        if c in freq_chart:
            freq_chart[c] = freq_chart[c]+1
        else:
            freq_chart[c] = 1    
    for c in t: # assemble new string from 't' & the frequency chart
        if c in freq_chart:
            for _ in range(freq_chart[c]):
                sorted_string += c
    return sorted_string # above algorithm runs in O(len(S)+len(T)) = O(N)

# example 1
print(sortByString('weather','therapyw'))
# example 2
print(sortByString('good','odg'))
# unspecified edge case: if a character in string 'S' does not exist in 'T' it is not included
print(sortByString('weather','therapy')) # no 'w'


# Question 2 -- decodeString(s): 
# Given an encoded string, return its corresponding decoded string. The encoding 
#   rule is: k[encoded_string], where the encoded_string inside the square brackets 
#   is repeated exactly k times. Note: k is guaranteed to be a positive integer. 
#   For s = "4[ab]", the output should be decodeString(s) = "abababab" 
#   For s = "2[b3[a]]", the output should be decodeString(s) = "baaabaaa"

def decodeString(s):
    # alpha-numeric lookup tables and helper variables
    numbers = {'0','1','2','3','4','5','6','7','8','9'}
    decoded = ''
    encoded = ''
    k = ''
    stack = [c for c in s]
    
    while(len(stack)>0):
        c = stack.pop() # take the top of the stack
        if c not in numbers and c != '[' and c != ']':
            # put together encoded string
            encoded = c + encoded
            # find rest of the alpha chars in the encoded substring 
            i = len(stack)-1
            while(i >= 0 and stack[i] not in numbers and stack[i] != '['):
                encoded = stack.pop() + encoded
                i -= 1  
        elif c == '[':
            # find the numeric chars to multiply encoded 
            i = len(stack)-1
            while(i >= 0 and stack[i] in numbers):
                k = stack.pop() + k
                i -= 1       
        if k != '':
            # copy the encoded string k times
            k = int(k)
            if decoded == '': # decoding the inner most nested
                while(k > 0):
                    decoded = encoded + decoded # MAYBE USE SPACE AS INDICATOR TO ENTER NEXT STR ADDITION
                    k -= 1
            else: # decoded outer nested by multiplying the previous inner nested 
                tmp = []
                for _ in range(k):
                    tmp.append(encoded + decoded)
                decoded = ''
                for i in tmp:
                    decoded += i
            k = ''
            encoded = ''    
    return decoded # above algorithm O(len(S) + # of nested substrings) = O(N) 
     
# example 1
print(decodeString('4[ab]'))
# example 2
print(decodeString('2[b3[a]]'))
# unspecified edge case: format of input string has a substring after a closing bracket the
print(decodeString('1[b3[a]2[c]]')) # numerical value before the preceeding substring is applied 
                                    # instead to their combination, not the preceeding substring


# Question 3 -- changePossibilities(amount,denom): 
# Your quirky boss collects rare, old coins. They found out you're a programmer and asked  
#   you to solve something they've been wondering for a long time. Write a function that,  
#   given an amount of money and an array of coin denominations, computes the number of  
#   ways to make the amount of money with coins of the available denominations. 
#   Example: for amount=4 (4cents) and denominations=[1,2,3] (1cent, 2cents and 3cents), your program 
#   would output 4 the number of ways to make 4cent with those denominations: 
#   1cent, 1cent, 1cent, 1cent  ;  1cent, 1cent, 2cents  ;  1cent, 3cents  ;  2cents, 2cents

def changePossibilities(amount,denom):    
    # using a dynamic programming approach by creating a table (of lengnth one size 
    # larger than the target amount) to hold possible coin combination values
    counting_list = [1 if i == 0 else 0 for i in range(amount+1)]
    
    # iterate through list for each 'coin denomination'
    for i in range(len(denom)):
        # add all possibilities within the range of the 'coin denomination' 
        # value and the target value + 1
        for k in range(denom[i],amount+1):
            counting_list[k] += counting_list[k-denom[i]]
            
    # after adding up all the coin combinations the resulting number of 
    # possibilities is conveniently in the last element of the list
    return counting_list[amount] # algorithm runs in O(len(denom) * amount+1) = O(N)

    
# example 1
print(changePossibilities(4,[1,2,3]))

# example with unsorted input
print(changePossibilities(4,[3,1,2]))