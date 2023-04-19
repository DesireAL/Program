#include "lnglat.h"
#include <QApplication>

#include <QGuiApplication>
#include <QQmlApplicationEngine>

int main(int argc, char *argv[])
{

//    QApplication app(argc, argv);
//    LngLat w;
//    w.show();
//    return app.exec();


    QGuiApplication a(argc, argv);
    QQmlApplicationEngine engine;
    engine.load(QUrl(QStringLiteral("qrc:/Minimap.qml")));
    return a.exec();

}
