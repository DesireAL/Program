public class Cat {
    int number;
    String name;
    int age;
    double weight;
    String color;

    private Cat(int number,String name,int age,double weight, String color){
        this.number = number;
        this.name = name;
        this.age = age;
        this.weight = weight;
        this.color = color;
    }

    public String toString(){
        return "猫咪" + number + "号: 名字: " + name + "\n年龄: " + age + "\n重量: " + weight + "\n颜色: " + color + "\n";
    }
    public static void main(String[] args) {
        Cat c1 = new Cat(1,"Java",12,21.0,"java.awt.Color[r=0,g=0,b=0]");
        Cat c2 = new Cat(2,"C++",12,21.0,"java.awt.Color[r=255,g=255,b=255]");
        Cat c3 = new Cat(1,"Java",12,21.0,"java.awt.Color[r=0,g=0,b=0]");
        System.out.println(c1);
        System.out.println(c2);
        System.out.println(c3);
    }
}