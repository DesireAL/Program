/********************************************************************************
** Form generated from reading UI file 'widget.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WIDGET_H
#define UI_WIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_widget
{
public:
    QWidget *layoutWidget;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *horizontalLayout_5;
    QLabel *label_6;
    QSpacerItem *horizontalSpacer_3;
    QTextEdit *textEditSend_JD;
    QSpacerItem *verticalSpacer_5;
    QHBoxLayout *horizontalLayout_6;
    QLabel *label_7;
    QSpacerItem *horizontalSpacer_4;
    QTextEdit *textEditSend_WD;
    QWidget *layoutWidget_3;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QComboBox *CboxSerialport;
    QPushButton *ButtonSwitch;
    QPushButton *Button_Send;
    QWidget *layoutWidget_4;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_4;
    QSpacerItem *horizontalSpacer;
    QTextEdit *textEdiReceive_JD;
    QSpacerItem *verticalSpacer;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_5;
    QSpacerItem *horizontalSpacer_2;
    QTextEdit *textEdiReceive_WD;
    QWidget *layoutWidget1;
    QVBoxLayout *verticalLayout_4;
    QSpacerItem *verticalSpacer_6;
    QHBoxLayout *horizontalLayout_4;
    QSpacerItem *horizontalSpacer_5;
    QVBoxLayout *verticalLayout_3;
    QSpacerItem *verticalSpacer_3;
    QLabel *label_3;
    QSpacerItem *verticalSpacer_2;
    QSpacerItem *horizontalSpacer_6;
    QSpacerItem *verticalSpacer_4;
    QWidget *layoutWidget2;
    QVBoxLayout *verticalLayout_6;
    QSpacerItem *verticalSpacer_9;
    QHBoxLayout *horizontalLayout_7;
    QSpacerItem *horizontalSpacer_7;
    QVBoxLayout *verticalLayout_5;
    QSpacerItem *verticalSpacer_8;
    QLabel *label_2;
    QSpacerItem *verticalSpacer_7;
    QSpacerItem *horizontalSpacer_8;
    QSpacerItem *verticalSpacer_10;

    void setupUi(QWidget *widget)
    {
        if (widget->objectName().isEmpty())
            widget->setObjectName(QString::fromUtf8("widget"));
        widget->resize(1150, 600);
        widget->setMinimumSize(QSize(1150, 598));
        widget->setMaximumSize(QSize(1150, 600));
        layoutWidget = new QWidget(widget);
        layoutWidget->setObjectName(QString::fromUtf8("layoutWidget"));
        layoutWidget->setGeometry(QRect(10, 340, 341, 116));
        verticalLayout_2 = new QVBoxLayout(layoutWidget);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setSpacing(6);
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        label_6 = new QLabel(layoutWidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        horizontalLayout_5->addWidget(label_6);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_3);

        textEditSend_JD = new QTextEdit(layoutWidget);
        textEditSend_JD->setObjectName(QString::fromUtf8("textEditSend_JD"));

        horizontalLayout_5->addWidget(textEditSend_JD);


        verticalLayout_2->addLayout(horizontalLayout_5);

        verticalSpacer_5 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer_5);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setSpacing(6);
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        label_7 = new QLabel(layoutWidget);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        horizontalLayout_6->addWidget(label_7);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_4);

        textEditSend_WD = new QTextEdit(layoutWidget);
        textEditSend_WD->setObjectName(QString::fromUtf8("textEditSend_WD"));

        horizontalLayout_6->addWidget(textEditSend_WD);


        verticalLayout_2->addLayout(horizontalLayout_6);

        layoutWidget_3 = new QWidget(widget);
        layoutWidget_3->setObjectName(QString::fromUtf8("layoutWidget_3"));
        layoutWidget_3->setGeometry(QRect(10, 20, 311, 41));
        horizontalLayout = new QHBoxLayout(layoutWidget_3);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        label = new QLabel(layoutWidget_3);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        CboxSerialport = new QComboBox(layoutWidget_3);
        CboxSerialport->setObjectName(QString::fromUtf8("CboxSerialport"));

        horizontalLayout->addWidget(CboxSerialport);

        ButtonSwitch = new QPushButton(layoutWidget_3);
        ButtonSwitch->setObjectName(QString::fromUtf8("ButtonSwitch"));

        horizontalLayout->addWidget(ButtonSwitch);

        Button_Send = new QPushButton(widget);
        Button_Send->setObjectName(QString::fromUtf8("Button_Send"));
        Button_Send->setGeometry(QRect(10, 470, 181, 41));
        layoutWidget_4 = new QWidget(widget);
        layoutWidget_4->setObjectName(QString::fromUtf8("layoutWidget_4"));
        layoutWidget_4->setGeometry(QRect(10, 140, 341, 116));
        verticalLayout = new QVBoxLayout(layoutWidget_4);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_4 = new QLabel(layoutWidget_4);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        horizontalLayout_2->addWidget(label_4);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        textEdiReceive_JD = new QTextEdit(layoutWidget_4);
        textEdiReceive_JD->setObjectName(QString::fromUtf8("textEdiReceive_JD"));

        horizontalLayout_2->addWidget(textEdiReceive_JD);


        verticalLayout->addLayout(horizontalLayout_2);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_5 = new QLabel(layoutWidget_4);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        horizontalLayout_3->addWidget(label_5);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_2);

        textEdiReceive_WD = new QTextEdit(layoutWidget_4);
        textEdiReceive_WD->setObjectName(QString::fromUtf8("textEdiReceive_WD"));

        horizontalLayout_3->addWidget(textEdiReceive_WD);


        verticalLayout->addLayout(horizontalLayout_3);

        layoutWidget1 = new QWidget(widget);
        layoutWidget1->setObjectName(QString::fromUtf8("layoutWidget1"));
        layoutWidget1->setGeometry(QRect(10, 260, 341, 71));
        verticalLayout_4 = new QVBoxLayout(layoutWidget1);
        verticalLayout_4->setSpacing(6);
        verticalLayout_4->setContentsMargins(11, 11, 11, 11);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        verticalLayout_4->setContentsMargins(0, 0, 0, 0);
        verticalSpacer_6 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_4->addItem(verticalSpacer_6);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_5);

        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_3->addItem(verticalSpacer_3);

        label_3 = new QLabel(layoutWidget1);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        QFont font;
        font.setFamily(QString::fromUtf8("AcadEref"));
        font.setPointSize(22);
        label_3->setFont(font);

        verticalLayout_3->addWidget(label_3);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_3->addItem(verticalSpacer_2);


        horizontalLayout_4->addLayout(verticalLayout_3);

        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_6);


        verticalLayout_4->addLayout(horizontalLayout_4);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_4->addItem(verticalSpacer_4);

        layoutWidget2 = new QWidget(widget);
        layoutWidget2->setObjectName(QString::fromUtf8("layoutWidget2"));
        layoutWidget2->setGeometry(QRect(10, 70, 341, 61));
        verticalLayout_6 = new QVBoxLayout(layoutWidget2);
        verticalLayout_6->setSpacing(6);
        verticalLayout_6->setContentsMargins(11, 11, 11, 11);
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        verticalLayout_6->setContentsMargins(0, 0, 0, 0);
        verticalSpacer_9 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_6->addItem(verticalSpacer_9);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setSpacing(6);
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        horizontalSpacer_7 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_7->addItem(horizontalSpacer_7);

        verticalLayout_5 = new QVBoxLayout();
        verticalLayout_5->setSpacing(6);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        verticalSpacer_8 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_5->addItem(verticalSpacer_8);

        label_2 = new QLabel(layoutWidget2);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setFont(font);

        verticalLayout_5->addWidget(label_2);

        verticalSpacer_7 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_5->addItem(verticalSpacer_7);


        horizontalLayout_7->addLayout(verticalLayout_5);

        horizontalSpacer_8 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_7->addItem(horizontalSpacer_8);


        verticalLayout_6->addLayout(horizontalLayout_7);

        verticalSpacer_10 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_6->addItem(verticalSpacer_10);


        retranslateUi(widget);

        QMetaObject::connectSlotsByName(widget);
    } // setupUi

    void retranslateUi(QWidget *widget)
    {
        widget->setWindowTitle(QCoreApplication::translate("widget", "widget", nullptr));
        label_6->setText(QCoreApplication::translate("widget", "\351\243\236\350\241\214\345\231\250\347\233\256\346\240\207\347\273\217\345\272\246:", nullptr));
        label_7->setText(QCoreApplication::translate("widget", "\351\243\236\350\241\214\345\231\250\347\233\256\346\240\207\347\272\254\345\272\246:", nullptr));
        label->setText(QCoreApplication::translate("widget", "\347\253\257\345\217\243\345\217\267\357\274\232", nullptr));
        ButtonSwitch->setText(QCoreApplication::translate("widget", "\346\211\223\345\274\200", nullptr));
        Button_Send->setText(QCoreApplication::translate("widget", "\345\217\221\351\200\201", nullptr));
        label_4->setText(QCoreApplication::translate("widget", "\351\243\236\350\241\214\345\231\250\345\275\223\345\211\215\347\273\217\345\272\246:", nullptr));
        label_5->setText(QCoreApplication::translate("widget", "\351\243\236\350\241\214\345\231\250\345\275\223\345\211\215\347\272\254\345\272\246:", nullptr));
        label_3->setText(QCoreApplication::translate("widget", "\351\243\236\350\241\214\345\231\250\347\233\256\346\240\207\344\275\215\347\275\256", nullptr));
        label_2->setText(QCoreApplication::translate("widget", "\351\243\236\350\241\214\345\231\250\345\275\223\345\211\215\344\275\215\347\275\256", nullptr));
    } // retranslateUi

};

namespace Ui {
    class widget: public Ui_widget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WIDGET_H
