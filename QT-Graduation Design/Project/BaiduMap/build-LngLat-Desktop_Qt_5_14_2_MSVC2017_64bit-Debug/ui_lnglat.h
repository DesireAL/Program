/********************************************************************************
** Form generated from reading UI file 'lnglat.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LNGLAT_H
#define UI_LNGLAT_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_LngLat
{
public:

    void setupUi(QWidget *LngLat)
    {
        if (LngLat->objectName().isEmpty())
            LngLat->setObjectName(QString::fromUtf8("LngLat"));
        LngLat->resize(800, 600);

        retranslateUi(LngLat);

        QMetaObject::connectSlotsByName(LngLat);
    } // setupUi

    void retranslateUi(QWidget *LngLat)
    {
        LngLat->setWindowTitle(QCoreApplication::translate("LngLat", "LngLat", nullptr));
    } // retranslateUi

};

namespace Ui {
    class LngLat: public Ui_LngLat {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LNGLAT_H
