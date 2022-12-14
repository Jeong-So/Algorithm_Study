package ch01_220915;

public class MinMaxProblem {

	public static void main(String[] args) {

		int[] numbers = {10, 55, 23, 2, 79, 101, 16, 82, 30, 45};
		
		int min = numbers[0];
		int max = numbers[0];
		int minIndex = 0;
		int maxIndex = 0;
		
//		System.out.println(numbers.length);
		
		for (int i = 1 ; i < numbers.length ; i++ ) {
			if(min > numbers[i]) {
				min = numbers[i];
				minIndex = i;
			}
			else if(max < numbers[i]) {
				max = numbers[i];
				maxIndex = i;
			}
		}
		
		System.out.println("numbers배열의 최솟값은 " + min + ", " + numbers[minIndex] + " 이며, 배열의 " + (minIndex+1) + "번째 입니다.");
		System.out.println("numbers배열의 최댓값은 " + max + ", " + numbers[maxIndex] + " 이며, 배열의 " + (maxIndex+1) + "번째 입니다.");

	}

}
