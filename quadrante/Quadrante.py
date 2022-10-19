class Quadrante:

    def __init__ (self, cordenadas):

        self.cordenadas = cordenadas
    

    def obter_cordenadas_quadrante(self):

        cordenadaX = self.cordenadas.cordenadaX
        cordenadaY = self.cordenadas.cordenadaY

        if(cordenadaX > 0 and cordenadaY > 0 ):
            
            return "Primeiro"

        elif(cordenadaX < 0 and cordenadaY > 0):

            return "Segundo"

        elif(cordenadaX < 0 and cordenadaY < 0):

            return "Terceiro"

        elif(cordenadaX > 0 and cordenadaY < 0):

            return "Quarto"

        else:
            return ""            

              

