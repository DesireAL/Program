
public class Cramer {
	public static void main(String[] args) {
		double a = 21.8;
		int b = 2;
		int e = 28;
		int c = 7;
		int d = 8;
		int f = 62;
		double x = (e * d - b * f)/(a * d - b * c);
		double y = (a * f - e * c)/(a * d - b * c);
		System.out.println("该二元一次方程组中的x = " + x);
		System.out.println("该二元一次方程组中的y = " + y);
	}
}
