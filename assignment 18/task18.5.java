class Car {
    String brand;
    String model;
    int year;

    Car(String brand, String model, int year) {   // constructor
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    void displayDetails() {
        System.out.println("Car Details:");
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
    }
}

public class Main {
    public static void main(String[] args) {
        Car c = new Car("Toyota", "Corolla", 2020);
        c.displayDetails();
    }
}




