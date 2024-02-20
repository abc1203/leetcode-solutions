class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] nums3 = new int[m];
        for(int i = 0; i < m; i++) nums3[i] = nums1[i];

        int i = 0; int ind1 = 0; int ind2 = 0;
        while(ind1 < m || ind2 < n) {
            if(ind1 < m && ind2 < n) {
                if(nums3[ind1] < nums2[ind2]) {
                    nums1[i] = nums3[ind1];
                    ind1++;
                } else {
                    nums1[i] = nums2[ind2];
                    ind2++;
                }
            } else if(ind1 == m) {
                nums1[i] = nums2[ind2];
                ind2++;
            } else if(ind2 == n) {
                nums1[i] = nums3[ind1];
                ind1++;
            }
            i++;
        }
    }
}
