package P151.ex6;

import java.util.Scanner;

public class Demo {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		boolean flag = true;
		while (flag) {
			try {
				System.out.println("������������");
				String name = sc.nextLine();
				System.out.println("���������䣺");
				int age = Integer.parseInt(sc.nextLine());
				System.out.println("������Ϣ¼��ɹ�����˶ԣ�\n������" + name + "\t���䣺" + age );
				flag = false;
			} catch (NumberFormatException e) {
				e.printStackTrace();
				System.err.println("������Ĳ�����Ч���䣬����������");
			}finally {
				sc.reset();
			}
		}
	}
}
