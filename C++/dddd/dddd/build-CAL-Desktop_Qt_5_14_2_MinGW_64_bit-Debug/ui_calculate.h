/********************************************************************************
** Form generated from reading UI file 'calculate.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CALCULATE_H
#define UI_CALCULATE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_calculate
{
public:

    void setupUi(QWidget *calculate)
    {
        if (calculate->objectName().isEmpty())
            calculate->setObjectName(QString::fromUtf8("calculate"));
        calculate->resize(568, 400);

        retranslateUi(calculate);

        QMetaObject::connectSlotsByName(calculate);
    } // setupUi

    void retranslateUi(QWidget *calculate)
    {
        calculate->setWindowTitle(QCoreApplication::translate("calculate", "calculate", nullptr));
    } // retranslateUi

};

namespace Ui {
    class calculate: public Ui_calculate {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CALCULATE_H
