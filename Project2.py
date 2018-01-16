from PyQt4 import QtGui
import sys
app = QtGui.QApplication(sys.argv)
print (QtGui.QImageReader.supportedImageFormats())
