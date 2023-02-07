package P140.ex3;

abstract class Fruits{
    public abstract String getName();
}

class People{
    void eat(Fruits fruit){
        System.out.println("吃了一个"+fruit.getName());
    }

    void eat2(String fruit2){
        System.out.println("吃了一个"+fruit2);
    }

}

public class Main {
    public static void main(String[] args){
        People p1 = new People();
        p1.eat(new Fruits(){
            public String getName() {
                return "香蕉";
            }
        });

        p1.eat(new Fruits(){
            public String getName() {
                return "苹果";
            }
        });

        p1.eat2("梨子");
    }
}
