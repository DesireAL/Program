
public class Test {//����һ��Test��
	public static void main(String[] args) {
		Animal animal1 = new Eagle();
		animal1.setName("ӥ");
		System.out.print(animal1.getName());
		((Eagle) animal1).eat();
		
		Animal animal2 = new Frog();
		animal2.setName("����");
		System.out.print(animal2.getName());
		((Frog) animal2).eat();
		
		Animal animal3 = new Grasshopper();
		animal3.setName("�ȳ�");
		System.out.print(animal3.getName());
		((Grasshopper) animal3).eat();
	}
}
