package P140.ex1;

interface Light {
	void light();
}

public class Match {
	public static void main(String[] args) {
		new Match() {
			void light() {
				System.out.println("火柴在燃烧");
			}
		}.light();

		new Match(){
			void light(){
				System.out.println("火柴在燃烧2");
			}
		}.light();
	}
}
