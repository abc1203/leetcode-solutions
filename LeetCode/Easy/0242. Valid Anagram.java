class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();

        for(int i = 0; i < s.length(); i++) {
            String key = String.valueOf(s.charAt(i));
            int oldFreq = 0;
            if(map.get(key) != null) { // current val is NULL
                oldFreq = map.get(key);
            }
            map.put(key, oldFreq+1);
        }


        for(int j = 0; j < t.length(); j++) {
            String key = String.valueOf(t.charAt(j));
            if(map.get(key) == null) return false;
            map.put(key, map.get(key)-1);
        }

        for(Integer i : map.values()) {
            if(i != 0) return false;
        }

        return true;
    }
};
