class Solution {
    public String longestCommonPrefix(String[] strs) {
       int minLength = Integer.MAX_VALUE;
       int ind = 0;
       for (int i = 0; i < strs.length; i++) {
           if(strs[i].length() < minLength) {
               minLength = strs[i].length();
               ind = i;
           }
       }
       System.out.println(minLength);
       
       for(int i = 0; i < minLength; i++) {
           char c = strs[0].charAt(i);
           for(int j = 0; j < strs.length; j++) {
               if(strs[j].charAt(i) != c && i != 0) {
                   return strs[0].substring(0, i); 
               } else if(strs[j].charAt(i) != c) {
                   System.out.println("Here");
                   return "";
               }
           }
       }
       return strs[ind]; 
    }
}
