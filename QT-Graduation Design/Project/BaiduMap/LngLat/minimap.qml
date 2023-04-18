import QtQuick 2.0
import QtQuick.Window 2.14
import QtLocation 5.6
import QtPositioning 5.6


Window {
    width: 1200
    height: 800
    visible: true

    Plugin {
        id: mapPlugin
//        name: "osm"
        // "mapboxgl", "esri", ...
        name:"mapboxgl"
    }

    Map {
        //锚(位置)
        anchors.left: parent
        x:0; y:0
        width: 1200
        height: 800
        //插件
        plugin: mapPlugin
        //学校坐标
        center: QtPositioning.coordinate(39.7468,116.3196)
        //缩放大小
        zoomLevel: 17
    }

    Rectangle{
        anchors.right: parent
        x:1075; y:200
        width:100
        height:50
        border.color: "slategrey"
        color: "lightblue"
        radius: 3
        Text{
            anchors.centerIn: parent
            text: "经纬度设置"
            font.pixelSize: 18
        }
    }

    Rectangle{
        anchors.right: parent
        x:1075; y:350
        width:100
        height:50
        color: "grey"
        radius: 3
        Text{
            anchors.centerIn: parent
            text: "时间查询"
            font.pixelSize: 18
        }
    }

    Rectangle{
        anchors.right: parent
        x:1075; y:500
        width:100
        height:50
        color: "grey"
        radius: 3
        Text{
            anchors.centerIn: parent
            text: "路径显示"
            font.pixelSize: 18
        }
    }
}

