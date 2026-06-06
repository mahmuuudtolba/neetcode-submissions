class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string , vector<string> > container;
        for (const auto &s : strs){
            string sortedS = s ;
            sort(sortedS.begin() , sortedS.end());
            container[sortedS].push_back(s);
        }

        vector<vector<string>> results ;

        for (auto& p : container){
            results.push_back((p.second));

        }

        return results;

        }

        
    }
;
