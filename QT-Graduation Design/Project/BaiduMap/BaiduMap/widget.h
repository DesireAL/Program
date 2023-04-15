#ifndef WIDGET_H
#define WIDGET_H
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>

#include <QWidget>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();

private:
    Ui::Widget *ui;

    QLabel *infoLabel = new QLabel;       //info为提示信息 label为控件名
    QLabel *xLabel = new QLabel;      //纬度提示语
    QLabel *yLabel = new QLabel;      //经度提示语
    QLineEdit *xLineEdit = new QLineEdit;     //纬度(横)
    QLineEdit *yLineEdit = new QLineEdit;     //经度(竖)
    QPushButton *commitButton = new QPushButton;      //确定按钮
    QPushButton *cancelButton = new QPushButton;      //取消按钮
};

#endif // WIDGET_H

