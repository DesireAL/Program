import java.util.Scanner;

public class Shopping {
	public static void main(String[] args) {
		double price = 580;
		double discount = 0.8;
		Scanner sc = new Scanner(System.in);
		System.out.print("����Ҫ������Ʒ��������");
		int number = sc.nextInt();
		sc.close();
		Shopping shopping = new Shopping();
		if (number == 1) {
			shopping.pay(number, price);
		} else {
			shopping.pay2(number, price, discount);
		}
	}

	public void pay(int account, double price) {
		System.out.println("Ӧ����" + price + "Ԫ��");
	}

	public void pay2(int account, double price, double discount) {
		System.out.println("Ӧ����" + (account * price * discount) + "Ԫ��");
	}
}
