import java.util.Arrays;

public class PackagedEggs {
	public static void main(String[] args) {	//ʾ���Ĵ���̫�鷳��,�Լ�����һ��
		int[] boxes = new int[10];
		Arrays.fill(boxes, 0, 4, 60);
		Arrays.fill(boxes, 4, 10, 58);
		for (int i = 0; i < boxes.length; i++) {
			System.out.println("��" + (i + 1) + "��װ��" + boxes[i] + "ö����");
		}
	}
}
