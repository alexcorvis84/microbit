'''<Ejemplo de DADO ELECTrÓNICO que se lanza agitando la placa microbit>
    Copyright (C) <2019>  <@AlexCorvis84>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>'''

from microbit import *
import random

uno = Image('09900:'
            '90900:'
            '00900:'
            '00900:'
            '99999:')
            
dos = Image('99999:'
            '00009:'
            '99999:'
            '90000:'
            '99999:')
            
tres = Image('99999:'
            '00009:'
            '99999:'
            '00009:'
            '99999:')
            
cuatro = Image('90009:'
            '90009:'
            '99999:'
            '00009:'
            '00009:')
            
cinco = Image('99999:'
            '90000:'
            '99999:'
            '00009:'
            '99999:')
              
seis = Image('99999:'
             '90000:'
             '99999:'
             '90009:'
             '99999:')
            

display.scroll('LANZA!')

while True:
    if accelerometer.was_gesture('shake'):
        valor = random.randint(1,6)
        if valor == 1:
            display.show(uno)
        if valor == 2:
            display.show(dos)
        if valor == 3:
            display.show(tres)
        if valor == 4:
            display.show(cuatro)
        if valor == 6:
            display.show(cinco)
        if valor == 6:
            display.show(seis)
    
