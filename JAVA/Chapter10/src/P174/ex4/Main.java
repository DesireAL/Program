package P174.ex4;

public class Main {
    public static void main(String[] args) {
        String str[] = {"张三", "李四", "王五", "赵六", "周七", "王哲", "白浩", "贾蓉", "慕容阿三", "黄蓉"};
        System.out.println("最后一个字相同的名字有");
        for (int i = 0; i < str.length; i++) {              //遍历str
            for (int j = i + 1; j < str.length; j++) {
                int len = str[i].length();
                //System.out.println("str["+i+"]="+str[i]);
                char endChar = str[i].charAt(len - 1);      //str[i].length()-1
                String strEC = endChar + "";
                if (str[j].endsWith(strEC)) {
                    System.out.println(str[i] + "和" + str[j]);
                }
            }
        }
    }
}
