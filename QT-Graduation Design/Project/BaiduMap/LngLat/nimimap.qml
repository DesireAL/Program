import QtQuick 2.0
import QtQuick.Window 2.14
import QtLocation 5.6
import QtPositioning 5.6

Window {
    width: 512
    height: 512
    visible: true

    Plugin {
        id: mapPlugin
//        name: "osm" // "mapboxgl", "esri", ...
        name:"mapboxgl"
    }

    Map {
        anchors.fill: parent
        plugin: mapPlugin
        //Oslo Coordinate
//        center: QtPositioning.coordinate(59.91, 10.75)
        //school Coordinate
        center: QtPositioning.coordinate(39.7473,116.3195)
        zoomLevel: 16.5
    }
}
