import java.util.Scanner;

public class ArithmeticOperator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);    //创建扫描器，获取控制台输入的值
        System.out.print("请输入两个数字，用空格分开(num1 num2): ");
        double num1 = sc.nextDouble();          //记录输入的第一个数字
        double num2 = sc.nextDouble();          //记录输入的第二个数字
        System.out.print("你输入的两个数分别是: "+num1+"和"+num2);
        sc.close();
    }
}