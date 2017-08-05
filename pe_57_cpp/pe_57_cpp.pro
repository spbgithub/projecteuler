TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt
unix:LIBS += -L/usr/lib -lgmp
SOURCES += main.cpp
QMAKE_CXXFLAGS += -lgmpxx -lgmp -std=c++11
