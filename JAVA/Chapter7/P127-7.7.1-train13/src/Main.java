class People{}
class Teacher extends People{}
class Student extends People{}

public class Main {
    public static void draw(People p){
        if(p instanceof Student){
            System.out.println("学生要好好学习");
        }
        else if(p instanceof Teacher){
            System.out.println("教师要认真授课");
        }
        else{
            System.out.println("每个人都要工作");
        }
    }
    public static void main(String[] args) {
        draw(new People());
        draw(new Teacher());
        draw(new Student());
    }
}