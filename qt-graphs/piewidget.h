#ifndef PIEWIDGET_H
#define PIEWIDGET_H

#include <QHBoxLayout>
#include <QPushButton>
#include <QQmlContext>
#include <QQuickWidget>
#include <QWidget>

class PieGraph;

class PieWidget : public QWidget {
    Q_OBJECT
  public:
    explicit PieWidget(QWidget *parent = nullptr);
    ~PieWidget();

    void initializeButtons();
    void initializeQuickWidget();

    QWidget *containerWidget() const;

  private:
    QWidget *m_widget;
    QQuickWidget *m_quickWidget;
    QVBoxLayout *m_vLayout;
    QHBoxLayout *m_hLayout;

    PieGraph *m_pieGraph;
};

#endif // PIEWIDGET_H
