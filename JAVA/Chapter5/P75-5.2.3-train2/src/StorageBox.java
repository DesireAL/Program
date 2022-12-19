
public class StorageBox {
	public static void main(String[] args) {
		int[] totalNum = new int[20];
		int[] emptyNum = {2, 3, 5, 8, 12, 13, 16, 19, 20};
		System.out.println("超市中有储物箱" + totalNum.length + "个。");
		System.out.println("超市中尚未被使用的储物箱有" + emptyNum.length + "个。");
		System.out.println("超市中已经被使用的储物箱有" + (totalNum.length - emptyNum.length) + "个。");
	}
}
