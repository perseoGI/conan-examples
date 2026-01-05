#include <QApplication>
#include <QtQml/qqmlengine.h>

#include "piewidget.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    PieWidget graph;
    graph.containerWidget()->show();

    return app.exec();
}
