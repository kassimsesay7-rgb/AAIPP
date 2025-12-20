public class Main {

    public static void checkNumber(int num) {
        if (num > 0) {
            System.out.println("Input: " + num + " → Output: The number is positive");
        } else if (num < 0) {
            System.out.println("Input: " + num + " → Output: The number is negative");
        } else {
            System.out.println("Input: " + num + " → Output: The number is zero");
        }
    }

    public static void main(String[] args) {
        checkNumber(-5);
        checkNumber(0);
        checkNumber(7);
    }
}



