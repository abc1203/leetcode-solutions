class Solution {
    // set up hashmap
    static HashMap<String, List<String>> hmap = new HashMap();
    static boolean flag = false;

    public void fillHashMap() {
        for(int i = 2; i <= 9; ++i) {
            Integer id = new Integer(i);
            ArrayList<String> l = new ArrayList<String>();

            switch(id.toString()) {
                case "2":
                    l.add("a"); l.add("b"); l.add("c"); break;
                case "3":
                    l.add("d"); l.add("e"); l.add("f"); break;
                case "4":
                    l.add("g"); l.add("h"); l.add("i"); break;
                case "5":
                    l.add("j"); l.add("k"); l.add("l"); break;
                case "6":
                    l.add("m"); l.add("n"); l.add("o"); break;
                case "7":
                    l.add("p"); l.add("q"); l.add("r"); l.add("s"); break;
                case "8":
                    l.add("t"); l.add("u"); l.add("v"); break;
                case "9":
                    l.add("w"); l.add("x"); l.add("y"); l.add("z"); break; 
            }

            hmap.put(id.toString(), l);
        }
    }
        

    public List<String> letterCombinations(String digits) {
        if(flag == false) {
            fillHashMap();
            flag = true;
        }
        
        if(digits.length() == 0) return new ArrayList<String>();
        else if(digits.length() == 1) return hmap.get(digits);
        
        List<String> list = new ArrayList<String>();
        List<String> oldList = letterCombinations(digits.substring(1));

        for(String letter : hmap.get(digits.substring(0, 1))) {
            for(String letterComb : oldList) {
                list.add(letter + letterComb);
            }
        }

        return list;
    }
}
