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
		
		System.out.println("numbers�迭�� �ּڰ��� " + min + ", " + numbers[minIndex] + " �̸�, �迭�� " + (minIndex+1) + "��° �Դϴ�.");
		System.out.println("numbers�迭�� �ִ��� " + max + ", " + numbers[maxIndex] + " �̸�, �迭�� " + (maxIndex+1) + "��° �Դϴ�.");

	}

}