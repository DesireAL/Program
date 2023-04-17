#ifndef LNGLAT_H
#define LNGLAT_H

#include <QWidget>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>

#include <lnglat_menu.h>

QT_BEGIN_NAMESPACE
namespace Ui { class LngLat; }
QT_END_NAMESPACE

class LngLat : public QWidget
{
    Q_OBJECT

public:
    LngLat(QWidget *parent = nullptr);
    ~LngLat();

    //按钮
    QPushButton *lnglatButton;      //经纬度按钮
    QPushButton *queryButton;
    QPushButton *pathButton;
    //布局
//    QHBoxLayout *lnglatLayout;      //经纬度按钮水平布局
//    QVBoxLayout *menuLayout;        //主界面布局

private slots:
    void lnglat_open();
    void time_query();
    void path_display();

private:
    Ui::LngLat *ui;

};
#endif // LNGLAT_H
