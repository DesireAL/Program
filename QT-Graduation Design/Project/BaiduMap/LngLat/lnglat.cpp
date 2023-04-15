#include "lnglat.h"
#include "ui_lnglat.h"

LngLat::LngLat(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::LngLat)
{
    ui->setupUi(this);
    resize(300,200);

    //连接信号与槽
//    connect(cancelButton, &QPushButton::clicked, this, &LngLat::cancelButton_clicked);

    //输入框实例
    xLineEdit = new QLineEdit();
    yLineEdit = new QLineEdit();
    //标签与按钮实例
    infoLabel = new QLabel();
    xLabel = new QLabel();
    yLabel = new QLabel();
    commitButton = new QPushButton();
    cancelButton = new QPushButton();
    //标签与按钮内容
    infoLabel->setText("请在下方输入想要设置的经纬度");
    xLabel->setText("经度");
    yLabel->setText("纬度");
    commitButton->setText("确定");
    cancelButton->setText("取消");
    //布局实例
    xLayout = new QHBoxLayout();
    yLayout = new QHBoxLayout();
    buttonLayout = new QHBoxLayout();
    lnglatLayout = new QVBoxLayout(this);
    //界面布局
    xLayout->addWidget(xLabel);
    xLayout->addWidget(xLineEdit);
    yLayout->addWidget(yLabel);
    yLayout->addWidget(yLineEdit);
    buttonLayout->addWidget(commitButton);
    buttonLayout->addWidget(cancelButton);

    lnglatLayout->addWidget(infoLabel);
    lnglatLayout->addLayout(xLayout);
    lnglatLayout->addLayout(yLayout);
    lnglatLayout->addLayout(buttonLayout);

}

void LngLat::cancelButton_clicked()
{
//    this->close();
}

LngLat::~LngLat()
{
    delete ui;
}

