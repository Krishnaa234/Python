def isBalanced(s):
    stack = []
    # map right bracket (key) to left bracket (value)
    right = {'}':'{',')':'(',']':'['}
    left = ['(','{','[']
  
    for c in s:
    	# push all left brackets to the stack
        if c in left:
            stack.append(c)
        else:
            if len(stack) > 0 and stack[-1] == right[c]:
            	# matches
                stack.pop()
            else:
            	# doesn't match
                return 'NO'
              
    # if anything is still on the stack
    if len(stack) > 0:
        return 'NO'
      
    return 'YES'

s = '{[()]}'
r = '{[(])}'
t = '{{[[(())]]}}'
print(isBalanced(s))
print(isBalanced(r))
print(isBalanced(t))

'''
Output:
Yes
No
Yes
'''
