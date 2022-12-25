import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int x=1,y=1;
        int boxx=2,boxy=2;
        char box[][] = new char[8][10];
        while(true){
            box[x][y]='&';
            box[boxx][boxy]='o';
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 10; j++) {
                    if(i == 0 || j == 0 || i == 7 || j == 9) {
                        box[i][j] = 'H';
                    }else if(i == 6 && j == 5) {
                        box[i][j] = '*';
                    }else if(i==x && j==y)
                    ;else if(i==boxx && j==boxy)
                    ;else{
                        box[i][j] = ' ';
                    }
                    System.out.print(box[i][j] + " ");
                }
                System.out.println();
            }
            Scanner sc = new Scanner(System.in);
            char input = sc.next().charAt(0);
            if(input == 'D' && y!=9){
                y++;
                if(x==boxx && y==boxy){
                    boxy++;
                    if(boxy==9){
                        boxy--;
                        y--;
                    }
                }
            }else if(input == 'A' && y!=1){
                y--;
                if(x==boxx && y==boxy){
                    boxy--;
                    if(boxy==0){
                        boxy++;
                        y++;
                    }
                }
            }else if(input == 'W' && x!=1){
                x--;
                if(x==boxx && y==boxy){
                    boxx--;
                    if(boxx==0){
                        boxx++;
                        x++;
                    }
                }
            }else if(input == 'S' && x!=6){
                x++;
                if(x==boxx && y==boxy){
                    boxx++;
                    if(boxx==7){
                        boxx--;
                        x--;
                    }
                }
            }else{
                System.out.println("当前箱子坐标为 "+boxx+" "+boxy);
            }
            if(boxx==6 && boxy==5){
                System.out.println("游戏成功！");
                break;
            }
        }
    }
}
