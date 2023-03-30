#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    input_r = new QLabel();
    output_s = new QLabel();
    input_r -> setText("请输入圆形半径");
    output_s -> setText("面积为: ");

    l1 = new QLineEdit();
    l2 = new QLineEdit();

    btn_call = new QPushButton();
    btn_call -> setText("计算");

    HBoxLayout1 = new QHBoxLayout();
    HBoxLayout2 = new QHBoxLayout();
    VBoxLayout = new QVBoxLayout(this);

    HBoxLayout1 -> addWidget(input_r);
    HBoxLayout1 -> addWidget(l1);

    HBoxLayout2 -> addWidget(output_s);
    HBoxLayout2 -> addWidget(l2);

    VBoxLayout -> addLayout(HBoxLayout1);
    VBoxLayout -> addLayout(HBoxLayout2);
    VBoxLayout -> addWidget(btn_call);
    //调整大小
    resize(400,400);

    connect(btn_call,&QPushButton::clicked,this,&Widget::Calculate);

}

Widget::~Widget()
{
    delete ui;
}

void Widget::Calculate()
{
    //获取输入
    double R_1;
    R_1 = l1 -> text().toDouble();
    double S_1;
    S_1 = R_1 * R_1 * 3.14;
    //将double类型转换为string
    l2 -> setText(QString::number(S_1));
}

