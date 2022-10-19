
from Menu import Menu
from Quadrante import Quadrante


menu = Menu()

while True:

   if (menu.mostrar_menu() == True):

       break
    
   cordenadas = menu.cordenadas

   main_quadrante = Quadrante(cordenadas)
   print(f"{main_quadrante.obter_cordenadas_quadrante()}")
   




    
