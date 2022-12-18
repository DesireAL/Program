//中断外层循环
public class Main {
    public static void main(String[] args) {
        Loop:for(int i=1;i<=3;i++){
            for(int j=1;j<=5;j++){
                System.out.println("i="+i+" j="+j);
                if(j==3){
                    break Loop;
                }
            }
        }
    }
}