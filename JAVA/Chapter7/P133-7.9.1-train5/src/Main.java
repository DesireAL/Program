abstract class Graph{
    String color;
    public Graph(String color){
        this.color = color;
    }
    abstract void area();
}

class Rectangle extends Graph{
    int length;
    int width;
    public Rectangle(String color){
        super(color);
        System.out.println("长方形的颜色为"+color);
    }

    @Override
    void area(){
        System.out.println("长方形的面积为: "+ (length*width));
    }


}

public class Main {
    public static void main(String[] args) {
        Rectangle r1 = new Rectangle("蓝色");
        r1.length = 8;
        r1.width = 6;
        r1.area();
    }
}