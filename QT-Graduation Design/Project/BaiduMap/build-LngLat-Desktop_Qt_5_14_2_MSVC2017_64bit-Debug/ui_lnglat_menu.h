/********************************************************************************
** Form generated from reading UI file 'lnglat_menu.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LNGLAT_MENU_H
#define UI_LNGLAT_MENU_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_lnglat_menu
{
public:

    void setupUi(QWidget *lnglat_menu)
    {
        if (lnglat_menu->objectName().isEmpty())
            lnglat_menu->setObjectName(QString::fromUtf8("lnglat_menu"));
        lnglat_menu->resize(400, 300);

        retranslateUi(lnglat_menu);

        QMetaObject::connectSlotsByName(lnglat_menu);
    } // setupUi

    void retranslateUi(QWidget *lnglat_menu)
    {
        lnglat_menu->setWindowTitle(QCoreApplication::translate("lnglat_menu", "Form", nullptr));
    } // retranslateUi

};

namespace Ui {
    class lnglat_menu: public Ui_lnglat_menu {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LNGLAT_MENU_H
