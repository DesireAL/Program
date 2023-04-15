#include "lnglat.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    LngLat w;

    w.show();
    return a.exec();
}
