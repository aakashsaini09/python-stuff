// Parent class
class Calculator {

    // Method to sum two integers
    int my_Sum(int a, int b){

        System.out.println("Parent class sum method:");
        return a + b;
    }
}

// Child class
class AdvancedCalculator extends Calculator{

    // Overriding the my_Sum method
    @Override int my_Sum(int a, int b){

        System.out.println(
            "Child class overridden sum method:");
        // Adding custom behavior
        return a + b
            + 10; // adds extra 10 for demonstration
    }
}

// Main class
public class Test {
    public static void main(String[] args)
    {
        Calculator calc1 = new Calculator();
        System.out.println("Result: "
                           + calc1.my_Sum(5, 10));

        AdvancedCalculator calc2 = new AdvancedCalculator();
        System.out.println("Result: "
                           + calc2.my_Sum(5, 10));

        // Polymorphism example
        Calculator calc3 = new AdvancedCalculator();
        System.out.println("Result: "
                           + calc3.my_Sum(5, 10));
    }
}