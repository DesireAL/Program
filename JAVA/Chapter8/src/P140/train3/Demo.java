package P140.train3;

class Human {
	Heart heart = new Heart();

	class Heart {
		void beating() {
			System.out.println("心脏跳动");
		}
	}

	void walk() {
		System.out.println("人走路");
		heart.beating();
	}
}

public class Demo {
	public static void main(String[] args) {
		Human tom = new Human();
		tom.walk();
	}
}
