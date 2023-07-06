import unittest
import inventory
import funciones

class TestPrime(unittest.TestCase):
    #titulo,precioC,precioV,Genero,Plataforma,cant
    def test_validar_juego(self):
        self.assertFalse(funciones.validarJuego(["",-1,-1,"","",0]))
        self.assertTrue(funciones.validarJuego([0,1,1,"Aventura","PC",2]))
        self.assertFalse(funciones.validarJuego(["",1,1,"Estrategia","Switch",10]))
        self.assertFalse(funciones.validarJuego(["LOL",10000,10000,"","PC",200]))
        self.assertFalse(funciones.validarJuego(["Minecraft",1.1,1,"Aventura","PS5",10]))
        self.assertFalse(funciones.validarJuego(["Minecraft",-1,-1,"Aventura","",100]))
            
if __name__=='__main__':
	unittest.main()
