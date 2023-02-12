package P151.train6;
import java.util.Scanner;

/*class MyException extends Exception{
    String message;
    public MyException(String ErrorMessage){
        message = ErrorMessage;
    }

    public String getMessage(){
        return message;
    }
}*/

public class Main {

    static int Exception(float age) throws Exception{
        //float age1 = age;
        int age2 = (int) age;
        if(age != age2){
            throw new Exception("年龄不能为小数");
        }
        return age2;
    }
    public static void main(String[] args){
        try{
            System.out.println("请输入姓名");
            Scanner s1 = new Scanner(System.in);
            String name = s1.next();
            System.out.println("请输入年龄");
            Scanner s2 = new Scanner(System.in);
            float age = s2.nextFloat();
            int age2 = Exception(age);
            System.out.println("姓名:"+ name +" 年龄:"+ age2);
        }catch(Exception e){
            System.out.println(e);
        }

    }
}
