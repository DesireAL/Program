
public final class Moon {
	String name;
	String characteristic;
	
	public Moon(String name, String characteristic) {
		this.name = name;
		this.characteristic = characteristic;
	}

	public String reflect() {
		return this.name + "���������⣬ֻ����̫����";
	}
	
	public static void main(String[] args) {
		Moon moon = new Moon("����", "������Χû�������������������");
		System.out.println(moon.characteristic + "��" + moon.reflect() + "��");
	}
}
