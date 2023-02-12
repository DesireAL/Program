package P151.train3;

public class Main {
    public static void main(String args[]) {
        int a[] = { 1, 2, 3, 4 };
        for (int i = 0; i < 5; i++) {
            try {
                System.out.print("当i="+i+" "+i+"<5时，a["+i+"]="+a[i]+"；");
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("当i="+i+" "+i+"<5时，a["+i+"]不存在，会引起"
                        + e.toString().substring(10, e.toString().indexOf(':'))
                        + "异常，\n该异常为数组越界异常，主要是由于索引超出了数组的长度范围引起的");
            }
            if (i != 4) {
                System.out.println("执行i++，" + "i = " + (i + 1) + "。");
            }
        }
    }
}
