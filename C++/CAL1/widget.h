#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
//控件
#include <QLabel>
#include <QPushButton>
#include <QLineEdit>
//布局
#include <QHBoxLayout>
#include <QVBoxLayout>

QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();
    //创建指针
    QLabel *input_r,*output_s;
    QLineEdit *l1,*l2;
    QPushButton *btn_call;
    QHBoxLayout *HBoxLayout1, *HBoxLayout2;
    QVBoxLayout *VBoxLayout;

    void Calculate();


private:
    Ui::Widget *ui;
};
#endif // WIDGET_H
