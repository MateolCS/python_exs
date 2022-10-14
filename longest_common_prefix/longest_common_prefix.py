
test_input = ["flower","flow","flight"]

def longest_common_prefix( strs ):
    if len(strs) == 0:
        return ""
    longest_prefix = strs[0]
    for item in strs: 
        while item.find(longest_prefix) != 0:
            longest_prefix = longest_prefix[:-1]
    return longest_prefix

print(longest_common_prefix(test_input))