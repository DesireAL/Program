QT       += \
    core gui \
    qml quick

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

DEFINES += QT_DEPRECATED_WARNINGS

SOURCES += \
    lnglat_menu.cpp \
    main.cpp \
    lnglat.cpp

HEADERS += \
    lnglat.h \
    lnglat_menu.h

FORMS += \
    lnglat.ui \
    lnglat_menu.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

#DISTFILES += \
#    qml/nimimap.qml

RESOURCES += \
    qml.qrc

DISTFILES += \
    Lnglat.qml \
    Minimap.qml \
    Pathdisplay.qml \
    Timequery.qml
