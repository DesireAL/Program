package P140.ex2;

class Human{
    class Heart{
        public void beating(){
            System.out.println("心脏在跳动");
        }
    }
    Heart h1 = new Heart();
    public Human(){
        h1.beating();
    }
}

public class Main{
    public static void main(String[] args){
        new Human();
    }
}
