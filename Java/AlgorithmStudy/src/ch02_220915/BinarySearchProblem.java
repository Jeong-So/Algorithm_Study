package ch02_220915;

public class BinarySearchProblem {

	public static void main(String[] args) {
		
		int[] numbers = {12, 25, 31, 48, 54, 66, 70, 83, 95, 108};
		
		int pos = (numbers.length)/2;
		
		int searchNum = 25;
		
		int searchPos = 0;
		
		if(numbers[pos] > searchNum) {
			for(int i = 0; i < pos; i++) {
				if(numbers[i] == searchNum) {
					searchPos = i;
				}
			}
		}
		else if(numbers[pos] <= searchNum){
			for(int i = pos; i < numbers.length; i++) {
				if(numbers[i] == searchNum) {
					searchPos = i;
				}
			}	
		}
		
		if (searchPos == 0 && numbers[0] != searchNum) {
			System.out.println("찾고있는 " + searchNum + "값이 없습니다.");
		}
		else {
			System.out.println("찾고있는 " + searchNum + "값의 위치는 " + (searchPos+1) + "번째 입니다.");
		}
		
		
		

	}

}
