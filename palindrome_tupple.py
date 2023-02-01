def palindrome(tupple):
    list(tupple)
    stringer = ""
    for i in tupple:
        stringer += i
    counter = 0
    reversed = ""
    for i in stringer:
        counter -= 1
        reversed = reversed + stringer[counter]
    if stringer == reversed:
        return "is a palindrome."
    else:
        return "not a palindrome"

testtupple = ("aa", "bb", "aa")
testtupple2 = ("cci")

print(palindrome(testtupple))
print(palindrome(testtupple2))

