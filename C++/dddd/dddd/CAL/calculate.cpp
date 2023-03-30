#include "calculate.h"
#include "ui_calculate.h"

calculate::calculate(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::calculate)
{
    ui->setupUi(this);
    resize(400,400);
    VerticalLayout = new QVBoxLayout(this);

    R_and_edit1 = new QHBoxLayout();
    S_and_edit2 = new QHBoxLayout();

    label1 = new QLabel();
    label1->setText(tr("请输入半径:"));

    lineEdit1 = new QLineEdit();
    lineEdit2 =new QLineEdit();
    lineEdit2->setReadOnly(true);
    label2 = new QLabel();
    label2->setText(tr("      面积:"));

    button = new QPushButton();
    button->setText(tr("计算"));

    R_and_edit1->addWidget(label1);
    R_and_edit1->addWidget(lineEdit1);

    S_and_edit2->addWidget(label2);
    S_and_edit2->addWidget(lineEdit2);

    VerticalLayout->addLayout(R_and_edit1);
    VerticalLayout->addLayout(S_and_edit2);
    VerticalLayout->addWidget(button);


    //计算,①点击按钮计算  ②实时计算
//    connect(button,&QPushButton::clicked,this,&calculate::calculate_S);
    connect(lineEdit1,&QLineEdit::textChanged,this,&calculate::calculate_S);
}

calculate::~calculate()
{
    delete ui;
}

void calculate::calculate_S()
{
    double round_S;
    double number = lineEdit1->text().toDouble();
    round_S = number * number * PI;
    lineEdit2->setText(QString::number(round_S));
}

