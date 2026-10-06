# nums=list(map(int,input().split()))
# count={i:nums.count(i) for i in nums}
# for i in count.values():
#     if i>1:
#         print("True")
#         break
# else:
#     print("False")

# nums=list(map(int,input().split()))
# k=int(input())
# l=[]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==k:
#             l.append(i)
#             l.append(j)
# print(l)

# a=input()
# b=input()
# if sorted(a)==sorted(b):
#     print("true")
# else:
#     print("false")

# l=[2,2,1,1,1,2,2]
# c={}
# for i in l:
#     if i not in c.keys():
#         c[i]=1
#     else:
#         c[i]+=1
#     if c[i]>(len(l)/2):
#         print(i)
#         break

# def frequency(s):
#     a={}
#     for i,num in enumerate(s):
#         if num not in a:
#             a[num]=[1,i]
#         else:
#             a[num][0]+=1
#     for j in a.values():
#         if j[0]==1:
#             return j[1]
#     else:
#         return -1
# a="loveleetcode"
# print(frequency(a))

# def anagrams(s):
#     a=[]
#     b=[]
#     c=[]
#     for i in range(len(s)):
#         if sorted(s[i]) not in b:
#             a.append(s[i])
#             b.append(sorted(s[i]))
#             for j in range(i+1,len(s)):
#                 if sorted(s[i])==sorted(s[j]):
#                     a.append(s[j])
#             c.append(a)
#             a=[]
#     return c
#
# s=["eat","tea","tan","ate","nat","bat"]
# print(anagrams(s))


# s="arshad"
# print("".join(sorted(s)))

# l=[1,2,2,1]
# s=[2,2]
# k=set()
# for i in l:
#     if i in s:
#         k.add(i)
# print(list(k))


# n=19
# s=set()
# while(sum!=1):
#     sum=0
#     for i in str(n):
#         sum+=int(i)**2
#     n=sum
#     if sum in s:
#         print("False")
#         break
#     else:
#         s.add(sum)
# else:
#     print("True")

# s="add"
# l="saa"
#
# if len(s)!=len(l):
#     print("False")
# else:
#     iso={}
#     osi={}
#     for i in range(len(s)):
#         if (s[i] in iso and iso[s[i]]!=l[i]) or (l[i] in osi and osi[l[i]]!=s[i]):
#             print("False")
#             break
#         else:
#             iso[s[i]]=l[i]
#             osi[l[i]]=s[i]
#     else:
#         print("True")

nums=[100,4,200,1,3,2]
seen = set()
ans = []

for num in nums:
    if num in seen:
        ans.append(num)
    else:
        seen.add(num)

print(ans)


