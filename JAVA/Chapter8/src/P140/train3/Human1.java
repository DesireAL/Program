package P140.train3;

public class Human1 {
    class Heart{
        void main(){
            System.out.println("心脏在跳动");
        }
    }

    Heart heart = new Heart();

    void Walk(){
        System.out.println("人用双脚行走");
        heart.main();
    }
    public static void main(String[] argv){
        Human1 people = new Human1();
        people.Walk();
    }
}
