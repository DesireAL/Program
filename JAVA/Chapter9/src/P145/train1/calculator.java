package P145.train1;
import java.util.InputMismatchException;
import java.util.Scanner;

public class calculator {
    public static void main(String[] args){
        System.out.println("请输入两个整数，用空格分离");
        Scanner s = new Scanner(System.in);
        try{
            int a = s.nextInt();
            int b = s.nextInt();
            System.out.println("输入的两个 整数 为:"+a+"和"+b);
        }
        catch(InputMismatchException e){
            e.printStackTrace();
            String a = s.next();
            String b = s.next();
            System.out.println("控制台输入数据错误");
            System.out.println("输入的两个 字符串 为:"+a+"和"+b);
        }
        finally{
            System.out.println("try语句块结束");
        }
    }
}
