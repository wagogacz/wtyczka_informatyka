import os
from qgis.PyQt import uic 
from qgis.PyQt import QtWidgets
from qgis.utils import iface
import numpy as np

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'moja_wtyczka_proj_3_dialog_base.ui'))

class Projekt_3Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Projekt_3Dialog, self).__init__(parent)
       
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clear)
        self.pushButton_2.clicked.connect(self.przewyzszenie)
        self.pushButton_3.clicked.connect(self.pole_gauss)
        self.pushButton_4.clicked.connect(self.ilosc_punktow)
   
    def wsp_punktow(self):
        aktywna_warstwa = iface.activeLayer()
        punkty_wsp = ""
        for i in aktywna_warstwa.getSelectedFeatures():
            g = i.geometry()
            punkty_wsp += 'X: %i, Y: %i' % (g.asPoint().x(), g.asPoint().y())
        iface.messageBar().pushMessage("Współrzędne punktów to", punkty_wsp)
    
   
    def clear(self):
        self.textBrowser.setText('')
  
    
    def przewyzszenie(self):
        active_Layer = iface.activeLayer()
        l_obiekty = active_Layer.selectedFeatureCount()
        self.wsp_punktow()
        
        if l_obiekty == 2:
            H = []
            for punkt in active_Layer.selectedFeatures():
                H.append(punkt[3])
            
            dH = abs(H[1]-H[0])
            self.textBrowser.setText(f'Róznica wysokoci między punktami o numerach PKT1 a PKT2 wynosi: {round(dH,3)}[m]')
            iface.messageBar().pushMessage(f'Liczba wybranych obiektów: {l_obiekty}', f'Róznica wysokoci między dwoma punkami: {round(dH,3)}m')
        else:
            self.textBrowser.setText(f'Nieprawidłowa liczba punktów! Wybierz 2 punkty!')
            iface.messageBar().pushMessage(f'Nieprawidłowa liczba punktów! Wybierz 2 punkty!')
   
    
    def pole_gauss(self):
        active_Layer = iface.activeLayer()
        l_obiekty = active_Layer.selectedFeatureCount()
        self.wsp_punktow()
        
        if l_obiekty >= 3:
            pkt = []
            for punkt in active_Layer.selectedFeatures():
                geom = punkt.geometry()
                x, y = geom.asPoint()
                pkt.append([x, y])
            
            pkt_array = np.array(pkt)
            suma = 0
        
            for i in range(len(pkt_array)):
                x1, y1 = pkt_array[i]
                if i == len(pkt_array) - 1:
                    x2, y2 = pkt_array[0]
                else:
                    x2, y2 = pkt_array[i+1]
                
                suma += (x1+x2)*(y2-y1)
            
            pole_w_metrach = abs(suma / 2)            
            
            if self.radioButton_4.isChecked():
                self.textBrowser.setText(f'Pole powierzchni figury o wierzchołkach w {l_obiekty} punktach o wynosi: {round(pole_w_metrach,4)} [m^2]')
                iface.messageBar().pushMessage(f'Liczba wybranych obiektów: {l_obiekty}', f'Pole powierzchni figury o wierzchołkach w punktach o numerach: PKT1, PKT2, PKT3 wynosi: {round(pole_w_metrach,4)} [m^2]')
            elif self.radioButton_3.isChecked():
                ary = pole_w_metrach/100
                self.textBrowser.setText(f'Pole powierzchni figury o wierzchołkach w {l_obiekty} punktach o wynosi: {round(ary,4)} [ary]')
                iface.messageBar().pushMessage(f'Liczba wybranych obiektów: {l_obiekty}', f'Pole powierzchni figury o wierzchołkach w punktach o numerach: PKT1, PKT2, PKT3 wynosi: {round(ary,4)} [ary]')
            elif self.radioButton_5.isChecked():
                ha = pole_w_metrach/10000
                self.textBrowser.setText(f'Pole powierzchni figury o wierzchołkach w {l_obiekty} punktach o wynosi: {round(ha,4)} [hektary]')
                iface.messageBar().pushMessage(f'Liczba wybranych obiektów: {l_obiekty}', f'Pole powierzchni figury o wierzchołkach w punktach o numerach: PKT1, PKT2, PKT3 wynosi: {round(ha,4)} [hektary]')
            else:
                self.textBrowser.setText(f'Wybierz jednostki!')
                iface.messageBar().pushMessage(f'Wybierz jednostki!')
        else:
            iface.messageBar().pushMessage(f'Nieprawidłowa liczba punktów! Aby obliczyć pole powierzchni wybierz minimum 3 punkty!')
            self.textBrowser.setText(f'Nieprawidłowa liczba punktów! Wybierz minimum 3 punkty!')


    def ilosc_punktow (self):
        active_Layer = iface.activeLayer()
        zaznaczone_obiekty = active_Layer.selectedFeatureCount()
        self.textBrowser.setText(f'Liczba zaznaczonych punktów to: {zaznaczone_obiekty}')
        
