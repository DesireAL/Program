#ifndef CALCULATE_H
#define CALCULATE_H

#include <QWidget>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>
QT_BEGIN_NAMESPACE
namespace Ui { class calculate; }
QT_END_NAMESPACE

class calculate : public QWidget
{
    Q_OBJECT

public:
    calculate(QWidget *parent = nullptr);
    ~calculate();

    //控件
    QLabel *label1, *label2;
    QLineEdit *lineEdit1,*lineEdit2;
    QPushButton *button;

    //布局
    QHBoxLayout *R_and_edit1;
    QHBoxLayout *S_and_edit2;
    QVBoxLayout *VerticalLayout;

    //计算函数(作为槽函数)
    void calculate_S();

private:
    Ui::calculate *ui;
    double PI =3.14;
};
#endif // CALCULATE_H
