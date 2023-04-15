#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{

    infoLabel->setText("请在下方输入想要设置的经纬度");
    xLabel->setText("经度");
    yLabel->setText("纬度");
    commitButton->setText("确定");
    cancelButton->setText("取消");

    QHBoxLayout *xLayout = new QHBoxLayout;     //纬度水平布局对象
    xLayout->addWidget(xLabel);
    xLayout->addWidget(xLineEdit);      //添加控件

    QHBoxLayout *yLayout = new QHBoxLayout;     //经度水平布局对象
    yLayout->addWidget(yLabel);
    yLayout->addWidget(yLineEdit);

    QHBoxLayout *buttonLayout = new QHBoxLayout;      //按钮布局
    buttonLayout->addWidget(commitButton);
    buttonLayout->addWidget(cancelButton);

    QVBoxLayout *lnglatLayout = new QVBoxLayout;
    lnglatLayout->addWidget(infoLabel);
    lnglatLayout->addLayout(xLayout);     //布局中加布局(小布局进大布局)
    lnglatLayout->addLayout(yLayout);
    lnglatLayout->addLayout(buttonLayout);

    delete ui;
}

