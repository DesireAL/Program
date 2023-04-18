#include "lnglat_menu.h"
#include "ui_lnglat_menu.h"

#include <QGuiApplication>
#include <QQmlApplicationEngine>

lnglat_menu::lnglat_menu(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::lnglat_menu)
{
    ui->setupUi(this);
    resize(300,200);

    QWidget w;
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
    infoLabel->setText(QStringLiteral("请在下方输入想要设置的经纬度"));
    xLabel->setText(QStringLiteral("经度"));
    yLabel->setText(QStringLiteral("纬度"));
    commitButton->setText(QStringLiteral("确定"));
    cancelButton->setText(QStringLiteral("取消"));
    //布局实例
    xLayout = new QHBoxLayout();
    yLayout = new QHBoxLayout();
    buttonLayout = new QHBoxLayout();
    lnglat_manu_Layout = new QVBoxLayout(this);
    //界面布局
    xLayout->addWidget(xLabel);
    xLayout->addWidget(xLineEdit);
    yLayout->addWidget(yLabel);
    yLayout->addWidget(yLineEdit);
    buttonLayout->addWidget(commitButton);
    buttonLayout->addWidget(cancelButton);

    lnglat_manu_Layout->addWidget(infoLabel);
    lnglat_manu_Layout->addLayout(xLayout);
    lnglat_manu_Layout->addLayout(yLayout);
    lnglat_manu_Layout->addLayout(buttonLayout);

    //连接信号与槽
    connect(cancelButton, &QPushButton::clicked, this, &lnglat_menu::cancelButton_clicked);     //关闭界面
    connect(commitButton, &QPushButton::clicked, this, &lnglat_menu::commitButton_clicked);     //经纬度确定
}

void lnglat_menu::cancelButton_clicked()
{
    //关闭界面
    this->close();
}

void lnglat_menu::commitButton_clicked()
{
    //获取输入
    double longitude;
    double latitude;
    longitude = yLineEdit->text().toDouble();       //获取纬度
    latitude = xLineEdit->text().toDouble();        //获取经度
    this->close();

}

lnglat_menu::~lnglat_menu()
{
    delete ui;
}
