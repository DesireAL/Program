public class test {
    public static void main(String[] args){
        int x = 3, y = 4;
        boolean ch;
        ch = x < y || ++x == --y;
        System.out.println(ch+ " " + x + " "+ y);
    }
}
