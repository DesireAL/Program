package P140.ex4;

interface Moveable{
    void run();
}

public class Main {
    public static void main(String[] args){
        Moveable m = new Moveable(){
            public void run(){
                System.out.println("小狗向前跑");
            }
        };
        m.run();
    }
}
