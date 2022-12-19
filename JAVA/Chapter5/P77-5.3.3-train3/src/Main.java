public class Main {
    public static void main(String[] args) {
        String bookshelf[][] = new String[3][2];
        bookshelf[0][0]="历史类读物";
        bookshelf[1][0]="经济类读物";
        bookshelf[1][1]="现代科学类读物";
        for(int i=0;i<3;i++){
            for(int j=0;j<2;j++){
                System.out.print(bookshelf[i][j]);
            }
            System.out.println();
        }
    }
}