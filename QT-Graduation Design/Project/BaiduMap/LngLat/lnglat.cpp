#include "lnglat.h"
#include "ui_lnglat.h"
#include <QtWidgets>

LngLat::LngLat(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::LngLat)
{
    ui->setupUi(this);
    resize(1200,800);

    //按钮
    lnglatButton = new QPushButton(QStringLiteral("经纬度修改"),this);
    queryButton = new QPushButton(QStringLiteral("时间查询"),this);
    pathButton = new QPushButton(QStringLiteral("路径显示"),this);
    //按钮布局
//    lnglatLayout = new QHBoxLayout(this);
//    menuLayout = new QVBoxLayout(this);
//    lnglatLayout->addWidget(lnglatButton);
//    menuLayout->addLayout(lnglatLayout);
    //按钮大小与位置
//    lnglatButton->setFixedSize(100,50);
    lnglatButton->resize(100,50);
    lnglatButton->move(1050,200);
    queryButton->resize(100,50);
    queryButton->move(1050,325);
    pathButton->resize(100,50);
    pathButton->move(1050,450);

    connect(lnglatButton, &QPushButton::clicked, this, &LngLat::lnglat_open);

}

void LngLat::lnglat_open()
{

    lnglat_menu *lnglat_m = new lnglat_menu();
    lnglat_m->show();

}

void LngLat::time_query()
{

}

void LngLat::path_display()
{

}
LngLat::~LngLat()
{
    delete ui;
}

