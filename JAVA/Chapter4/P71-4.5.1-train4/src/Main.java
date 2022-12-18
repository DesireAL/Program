public class Main {
    public static void main(String[] args) {
        int i=0;
        for(int x=4;x<=7;x++){
            for(int y=4;y<=7;y++){
                if(y==x){
                    continue;}
                for(int z=4;z<=7;z++){
                    if((z==x)||(z==y)){
                        continue;}
                    String a = String.valueOf(x);
                    String b = String.valueOf(y);
                    String c = String.valueOf(z);
                    i++;
                    System.out.println(a+b+c);
                }
            }
        }
        System.out.println("一共有"+i+"个不重复的数字");
    }
}