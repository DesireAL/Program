#include "lnglat.h"
#include <QApplication>

#include <QGuiApplication>
#include <QQmlApplicationEngine>

int main(int argc, char *argv[])
{
//    QApplication a(argc, argv);
//    LngLat w;

    QGuiApplication a(argc, argv);

    QQmlApplicationEngine engine;
    engine.load(QUrl(QStringLiteral("nimimap.qml")));

//    w.show();
    return a.exec();
}
