import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Window 2.12
import QtQuick.Layouts 1.12
import QtQuick.Controls.Material 2.3
import QtCharts 2.3

ApplicationWindow {
    id: app_window
    title: qsTr("Simple Graph Example")

    width: 800
    height: 600

    // Sets the default colors to be used for Style
    Material.theme: Material.Dark
    Material.accent: Material.Teal

    // default visibility is false so need to set it here
    visible: true

    Rectangle {
        id: graphScreen
        width: 800
        height: 600 
        color: Material.background

        function generateData() {
            var line = line_graph.series("data_series")
            dataGenerator.generatePlotData(line)
        }

        function generateDataFromLibrary() {
            var line = line_graph.series("data_series")
            dataGenerator.generateLibPlotData(line)
        }

        function fitWithScipy() {
            var data_line = line_graph.series("data_series")
            var fit_line = line_graph.series("fit_series")
            scipyFit.createFit(data_line,fit_line)
        }

        function fitWithLibrary() {
            var data_line = line_graph.series("data_series")
            var fit_line = line_graph.series("lib_fit_series")
            libraryFit.createFit(data_line,fit_line)
        }

        ColumnLayout {
            anchors.fill: graphScreen

            Item {
                id: lineChartArea
                Layout.fillHeight: true
                Layout.fillWidth: true

                ChartView {
                    id: line_graph
                    anchors.fill: parent
                    legend.visible: false
                    antialiasing: true
                    animationOptions: ChartView.NoAnimation
                    backgroundColor: "transparent"
                    margins.top: 0
                    margins.bottom: 0
                    margins.left: 0
                    margins.right: 0

                    ValueAxis {
                        id: x_axis
                        min: -4
                        max: 4
                        labelsColor: "#41cd52"
                        gridLineColor: "grey"
                        }
                    ValueAxis {
                        id: y_axis
                        min: -1.2
                        max: 1.2
                        labelsColor: "#41cd52"
                        gridLineColor: "grey"
                        }
                    ScatterSeries {
                        axisX: x_axis
                        axisY: y_axis
                        markerSize: 4
                        color: Material.accent
                        name: "data_series"
                        useOpenGL: true
                        }
                    LineSeries {
                        axisX: x_axis
                        axisY: y_axis
                        color: "cyan"
                        name: "fit_series"
                        useOpenGL: true
                        }
                    LineSeries {
                        axisX: x_axis
                        axisY: y_axis
                        color: "#3D5AFE"
                        name: "lib_fit_series"
                        useOpenGL: true
                        }
                    }
                }
                Item {
                    id: lower__area
                    Layout.preferredHeight: graphScreen.height/4
                    Layout.fillWidth: true

                    RowLayout {
                        anchors.fill: parent
                        spacing: 0

                        Item {
                            Layout.fillWidth: true
                            Layout.fillHeight: true

                            ColumnLayout {
                                anchors.fill: parent

                                Item {
                                    Layout.fillHeight: true
                                    Layout.fillWidth: true

                                    Button {
                                        text: "Data From C++ Library"
                                        anchors.centerIn: parent

                                        onClicked: {
                                            graphScreen.generateDataFromLibrary()

                                        }
                                    }
                                }
                                Item {
                                    Layout.fillHeight: true
                                    Layout.fillWidth: true

                                    Button {
                                        text: "Fit with C++ Library"
                                        anchors.centerIn: parent

                                        onClicked: {
                                            graphScreen.fitWithLibrary()
                                        }
                                    }
                                }
                                
                            }
                        }

                        Item {
                            Layout.fillWidth: true
                            Layout.fillHeight: true

                            ColumnLayout {
                                anchors.fill: parent

                                Item {
                                    Layout.fillHeight: true
                                    Layout.fillWidth: true
                                    visible: false  // Used for testing

                                    Button {
                                        text: "Generate Test Data With NumPy"
                                        anchors.centerIn: parent

                                        onClicked: {
                                            graphScreen.generateData()
                                        }
                                    }
                                }
                                
                                Item {
                                    Layout.fillHeight: true
                                    Layout.fillWidth: true

                                    Button {
                                        text: "Fit With SciPy"
                                        anchors.centerIn: parent

                                        onClicked: {
                                            graphScreen.fitWithScipy()
                                        }
                                    } 
                                }

                            }

                           
                        }
                    }

                    
            }
        }
    }
}
