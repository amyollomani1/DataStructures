import collections 

class Solution:
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #hasmap: key : list of anagrams
        m: dict[str,list[str]] = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in m:
                m[key].append(s)
            else:
                m[key] = [s]

        res = []
        for k in m.keys():
            res.append(m[k])
        return res

    if __name__ == '__main__':
        print(groupAnagrams(6, ["eat","tea","tan","ate","nat","bat"]))
      

