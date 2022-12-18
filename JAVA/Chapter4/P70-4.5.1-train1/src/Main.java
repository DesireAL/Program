import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        while(true){
            Scanner sc = new Scanner(System.in);
            System.out.print("请输入要进行判断的数：");
            int number = sc.nextInt();
            if(number % 2 == 0){
                System.out.println("该数为偶数");
            }
            else{
                System.out.println("该数为奇数");
            }
        }
    }
}