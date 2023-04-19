﻿import QtQuick 2.0
import QtQuick.Window 2.14
import QtLocation 5.6
import QtPositioning 5.6


Window {
    id: root
    title: "地图界面"
    width: 1200
    height: 800
    visible: true
    property double longitude: lnglatWindow.longitude
    property double latitude: lnglatWindow.latitude
    Plugin {
        id: mapPlugin
//        name: "osm"
        // "mapboxgl", "esri", ...
        name:"mapboxgl"
    }
    //修改经纬度后
    onLongitudeChanged: map.update()
    Map {
        id: map
        //锚(位置)
        anchors.left: parent
        x:0; y:0
        width: 1200
        height: 800
        //插件
        plugin: mapPlugin
        //学校坐标
        center: QtPositioning.coordinate(longitude,latitude)
        //缩放大小
        zoomLevel: 17
    }

    //经纬度界面实例化
    Lnglat {
        id:lnglatWindow
    }
    //经纬度设置按钮
    Rectangle {
        x:1075; y:200
        width:100
        height:50
        border.color: "slategrey"
        color: "lightblue"
        radius: 3
        Text {
            anchors.centerIn: parent
            text: "经纬度设置"
            font.pixelSize: 18
        }
        MouseArea {
            anchors.fill: parent
            onClicked:{
                lnglatWindow.show()
            }
        }
    }

    //时间查询界面实例化
    Timequery {
        id:timequeryWindow
    }
    //时间查询按钮
    Rectangle {
        x:1075; y:350
        width:100
        height:50
        border.color: "slategrey"
        color: "lightblue"
        radius: 3
        Text{
            anchors.centerIn: parent
            text: "时间查询"
            font.pixelSize: 18
        }
        MouseArea {
            anchors.fill: parent
            onClicked:{
                timequeryWindow.show()
            }
        }
    }

    //路径显示界面实例化
    Path{
        id:pathWindow
    }
    //路径显示按钮
    Rectangle {
        x:1075; y:500
        width:100
        height:50
        border.color: "slategrey"
        color: "lightblue"
        radius: 3
        Text{
            anchors.centerIn: parent
            text: "路径显示"
            font.pixelSize: 18
        }
        MouseArea {
            anchors.fill: parent
            onClicked:{
                pathWindow.show()
            }
        }
    }
}

