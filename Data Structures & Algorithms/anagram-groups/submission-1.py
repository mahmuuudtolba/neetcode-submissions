class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I need to check all the character of each words
        # Or there is a way to compare the whole word
        # If there is a way to compare the whole word so i can classifiy


        # What if i loop over these strs and for each one i made a set(str)
        # then ckeck if it's exist add the str[i] else create a str[i]
        container = {}
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in container:
                container[sorted_str].append(strs[i])
            else:
                container[sorted_str] = [strs[i]]

        return list(container.values())


        