class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> container = {};

        // loop over the nums
        for(int x : nums){
            if (container.contains(x)){
                return true;
            }
            container.insert(x);
        }

        return false;        
    }
};