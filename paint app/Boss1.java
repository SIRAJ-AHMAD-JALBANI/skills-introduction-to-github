public class Boss1 {
    public static void main(String[] args) {
        // Father father = new Father();
        // System.out.println(father.hear());
        A a = new A();
        a.speak();
    }
}

public class Father {
    void speak() {
        System.out.println("I can speak");
    }

    void run() {
        System.out.println("I can run");
    }

    void hear() {
        System.out.println("I can hear");
    }

}

public class A extends Father {

    void speak() {
        System.out.println("I cannot speak");
    }
}

public class B extends Father {
    void run() {
        System.out.println("I cannot run");
    }
}

public class C extends Father {
    System.out.println("I cannot hear");

}
