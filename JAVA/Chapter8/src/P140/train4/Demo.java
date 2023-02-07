package P140.train4;

class Animal {
	void eat() {

	}
}

public class Demo {

	public static void main(String[] args) {
		Animal a = new Animal() {
			void eat() {
				System.out.println("è���㣬������");
			}
		};
		a.eat();
	}
}
