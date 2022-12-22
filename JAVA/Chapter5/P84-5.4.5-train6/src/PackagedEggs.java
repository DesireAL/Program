import java.util.Arrays;

public class PackagedEggs {
	public static void main(String[] args) {	//示例的代码太麻烦了,自己改了一下
		int[] boxes = new int[10];
		Arrays.fill(boxes, 0, 4, 60);
		Arrays.fill(boxes, 4, 10, 58);
		for (int i = 0; i < boxes.length; i++) {
			System.out.println("第" + (i + 1) + "箱装了" + boxes[i] + "枚鸡蛋");
		}
	}
}
