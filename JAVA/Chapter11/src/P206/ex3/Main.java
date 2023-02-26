package P206.ex3;

public class Main {
    public static void main(String[] args) {
        double distance = 100;
        int x1 = 15, y1 = 4;
        int angle = 30;
        double distance_H = distance * Math.sin(Math.toRadians(angle));
        double distance_V = distance * Math.cos(Math.toRadians(angle));
        double x2 = x1 + distance_H;//(int) Math.round(distance_H);
        double y2 = y1 + distance_V;//(int) Math.round(distance_V);
        System.out.println("新坐标(" + x2 + "," + y2 + ")");
    }
}
