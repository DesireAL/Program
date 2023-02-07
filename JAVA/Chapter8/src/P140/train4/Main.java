package P140.train4;

class Animal1 {
    void eat(){
    }
}

public class Main {
    public static void main(String[] args){
        Animal1 a = new Animal1(){
            @Override
            void eat(){
                System.out.println("猫吃鱼，狗吃肉");
            }
        };
        a.eat();
    }
}
