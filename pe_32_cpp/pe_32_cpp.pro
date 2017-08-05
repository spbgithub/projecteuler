QT += core
QT -= gui

TARGET = pe_32_cpp
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

SOURCES += main.cpp

QMAKE_CXXFLAGS += -std=c++11
