
class Pig {
	public boolean equals(Object obj) {
		return true;
	}
}

class Dog{}

public class RidiculousResult {
	public static void main(String[] args) {
		Pig pig = new Pig();
		if (pig.equals(new Dog())) {
			System.out.println("��͹���ͬ�࣡����");
		} else {
			System.out.println("��͹�����ͬ�ࡣ");
		}
	}
}
