package arrays;

import java.util.Arrays;

public class MoveZeros {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {0,1,0,3,12};
		int zeros = 0;
        
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != 0){
                zeros++;
                int swapnum = nums[zeros];
                nums[zeros] = nums[i];
                nums[i] = swapnum;
            }
            System.out.println(Arrays.toString(nums));
        }
        System.out.println(Arrays.toString(nums));
	}

}
