import java.util.Scanner;

public class Main {
    public static int pay(int a){
        int x = 580;
        return x;
    }

    public static double pay2(double a){
        double x = 0;
        x = a*580*0.8;
        return x;
    }

    public static void main(String args[]){
        double price;
        System.out.println("请输入你想购买的商品数量");
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        if(x==1){
            price = pay(x);
        }
        else if(x>1){
            double y = x;
            price = pay2(y);
        }
        else{
            price = 0;
        }
        System.out.println("商品的价格为" + price);
    }
}