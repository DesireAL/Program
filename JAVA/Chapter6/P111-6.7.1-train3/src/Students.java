public class Students {
    int number;
    String name;
    float chinese;
    float math;
    float english;
    float avg;

    public Students(int number,String name, float chinese, float math, float english){
        this.number=number;
        this.name=name;
        this.chinese=chinese;
        this.math=math;
        this.english=english;
        this.avg=(chinese+math+english)/3;
    }

    public void Grade(){
        System.out.println(number + "\t\t" + name + "\t\t" + chinese + "\t" + math + "\t" + english + "\t" + avg);
    }

    public static void main(String[] args) {
        System.out.println("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t平均分");
        System.out.println("——————————————————————————————————————————————————————————————————————————————");

        Students number1 = new Students(1,"张三",91.5f,98.0f,89.0f);
        number1.Grade();


    }


}