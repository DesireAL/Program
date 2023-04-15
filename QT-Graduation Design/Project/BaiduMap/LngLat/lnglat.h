#ifndef LNGLAT_H
#define LNGLAT_H

#include <QWidget>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>
//#include <QProcess>

QT_BEGIN_NAMESPACE
namespace Ui { class LngLat; }
QT_END_NAMESPACE

class LngLat : public QWidget
{
    Q_OBJECT

public:
    LngLat(QWidget *parent = nullptr);
    ~LngLat();

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
    QVBoxLayout *lnglatLayout;      //整体布局

private slots:
    void cancelButton_clicked();

private:
    Ui::LngLat *ui;

};
#endif // LNGLAT_H
