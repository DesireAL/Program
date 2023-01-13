class YHK{
    public YHK(){
        System.out.println("银行卡可以存钱");
    }
}

class CXK extends YHK{
    public CXK(){
        System.out.println("银行卡中的储蓄卡不可以借钱");
    }
}

class XYK extends YHK{
    public XYK(){
        System.out.println("银行卡中的信用卡可以借钱");
    }
}


public class Main {
    public static void main(String[] args) {
        new CXK();
        new XYK();
    }
}