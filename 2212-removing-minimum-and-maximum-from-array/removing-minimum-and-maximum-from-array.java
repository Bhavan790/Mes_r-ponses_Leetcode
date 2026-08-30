class Solution {
    public int minimumDeletions(int[] nums) {
        int n = nums.length;
        if (n <= 2) {
            return n;
        }

        // Find min and max values
        int a = nums[0];
        int b = nums[0];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < a) {
                a = nums[i];
            }
            if (nums[i] > b) {
                b = nums[i];
            }
        }

        int l = 0;
        int r = n - 1;
        int i = 0;
        int j = 0;
        int p = 0;
        int q = 0;

        // 1. First target from front
        while (nums[l] != a && nums[l] != b) {
            i++;
            l++;
        }
        i++;

        // 2. First target from back
        while (nums[r] != a && nums[r] != b) {
            j++;
            r--;
        }
        j++;

        // 3. Both from front
        int k = 0;
        int s = 2;
        while (s > 0) {
            if (nums[k] == a || nums[k] == b) {
                s--;
            }
            p++;
            k++;
        }

        // 4. Both from back
        k = n - 1;
        s = 2;
        while (s > 0) {
            if (nums[k] == a || nums[k] == b) {
                s--;
            }
            q++;
            k--;
        }

        return Math.min(p, Math.min(q, i + j));
    }
}