import QtQuick 2.0
import QtQuick.Window 2.14

Window {
    id: root
    title: "经纬度设置"
    visible: false
    width: 300
    height: 200
    property double longitude: 39.7468
    property double latitude: 116.3196
    //输入框
    Rectangle{
        anchors.fill: parent
        width: 280
        height: 180
        color: "whitesmoke"
        //经度输入框
        Rectangle{
            id:lnginput
            x:55
            y:50
            width: 230
            height: 20
            border.color: "lightgrey"
            TextInput{
                id: lng
                anchors.fill: parent
                verticalAlignment: TextInput.AlignVCenter
                selectByMouse: true
                anchors.margins: 5
            }
        }
        Text {
            x:25
            y:54
            text: ("经度")
        }
        //纬度输入框
        Rectangle{
            id:latinput
            x:55
            y:90
            width: 230
            height: 20
            border.color: "lightgrey"
            TextInput{
                id:lat
                anchors.fill: parent
                verticalAlignment: TextInput.AlignVCenter
                selectByMouse: true
                anchors.margins: 5
            }
        }
        Text {
            x:25
            y:94
            text: ("纬度")
        }
    }

    //确定
    Rectangle{
        x:75; y:150
        width:60
        height:25
        border.color: "slategrey"
        color: "white"
        radius: 3
        Text{
            anchors.centerIn: parent
            text: "确定"
            font.pixelSize: 18
        }
        MouseArea{
            anchors.fill: parent
            onClicked:{
                longitude = Number(lng.toString())
                latitude = Number(lat.toString())
                root.close()
            }
        }
    }
    //取消
    Rectangle{
        x:165; y:150
        width:60
        height:25
        border.color: "slategrey"
        color: "white"
        radius: 3
        Text{
            anchors.centerIn: parent
            text: "取消"
            font.pixelSize: 18
        }
        MouseArea{
            anchors.fill: parent
            onClicked:{
                root.close()
            }
        }
    }

}
