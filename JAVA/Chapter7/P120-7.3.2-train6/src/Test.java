
public class Test {//创建一个Test类
	public static void main(String[] args) {
		Animal animal1 = new Eagle();
		animal1.setName("鹰");
		System.out.print(animal1.getName());
		((Eagle) animal1).eat();
		
		Animal animal2 = new Frog();
		animal2.setName("青蛙");
		System.out.print(animal2.getName());
		((Frog) animal2).eat();
		
		Animal animal3 = new Grasshopper();
		animal3.setName("蝗虫");
		System.out.print(animal3.getName());
		((Grasshopper) animal3).eat();
	}
}
