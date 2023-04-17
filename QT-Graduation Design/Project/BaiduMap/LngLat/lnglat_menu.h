#ifndef LNGLAT_MENU_H
#define LNGLAT_MENU_H

#include <QWidget>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>

namespace Ui {
class lnglat_menu;
}

class lnglat_menu : public QWidget
{
    Q_OBJECT

public:
    explicit lnglat_menu(QWidget *parent = nullptr);
    ~lnglat_menu();

    //标签
    QLabel *infoLabel;       //info为提示信息 label为控件名
    QLabel *xLabel;      //纬度提示语
    QLabel *yLabel;      //经度提示语
    //输入框
    QLineEdit *xLineEdit;     //纬度(横)
    QLineEdit *yLineEdit;     //经度(竖)
    //按钮
    QPushButton *commitButton;      //确定按钮
    QPushButton *cancelButton;      //取消按钮
    //布局
    QHBoxLayout *xLayout;     //纬度水平布局对象
    QHBoxLayout *yLayout;     //经度水平布局对象
    QHBoxLayout *buttonLayout;      //按钮布局
    QVBoxLayout *lnglat_manu_Layout;      //整体布局

private slots:
    void cancelButton_clicked();
    void commitButton_clicked();

private:
    Ui::lnglat_menu *ui;
};

#endif // LNGLAT_MENU_H
