import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Escalas do objeto
scalex = scaley = scalez = 1.0

# Posicionamento do objeto
x_pos = y_pos = z_pos = 0.0


def main():

	w = h = 3000 # Dimensões da janela

	glutInit() # Inicialização do GLUT
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) # Definição do modo de exibição inicial	
	glutInitWindowPosition(0,0) # Posição da janela de exibição
	glutInitWindowSize(w, h) # Tamanho da janela de exibição
	glutCreateWindow("Visualizacao de objetos 3D") # Criação da janela de exibição
	glutDisplayFunc(display) # Exibição do display
	glutKeyboardFunc(keyPressed) # Manipulação das teclas pressionadas
	glutSpecialFunc(specialKeyPressed) # Manipulação de teclas especiais
	glutMainLoop()

def display():

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpa o buffer
	glEnable(GL_DEPTH_TEST) # Habilitação do teste de profundidade

 	# Define a matriz como model view e carrega
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	# Definição dos pontos de observação
	gluLookAt(1.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
	
	# Define a matriz como projeção e carrega
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	
	glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0) # Definição da projeção ortogonal
	
	glColor3f(0.9, 0.3, 0.2) # Cores do objeto
#	glRotatef(90.0, 0.0, 1.0, 0.0)
	glTranslatef(x_pos, y_pos, z_pos)
	glScalef(scalex, scaley, scalez)

	glutWireTeapot(0.5) # Projeta a figura

#	glutWireTorus(1.0, 3.0, 30, 30) # Projeta a figura

	glutSwapBuffers()

def keyPressed(key, x, y):

	key = key.decode("utf-8") # Conversão da tecla para UTF8

	global scalex, scaley, scalez

	if key == 'q':
		exit() # Saída do programa
	
	# Aumenta a escala do objeto
	elif key == 'i':
		scalex = scaley = scalez = scalex+0.1
	
	# Diminui a escala do objeto
	elif key == 'o':
		if scalex > 0.2: 
			scalex = scaley = scalez = scalex-0.1 

	glutPostRedisplay()

def specialKeyPressed(key, x, y):

	global x_pos, y_pos, z_pos

	if key == GLUT_KEY_LEFT:
		x_pos = x_pos-0.1 # Translação para esquerda
	elif key == GLUT_KEY_RIGHT:
		x_pos = x_pos+0.1 # Translação para direita
	elif key == GLUT_KEY_UP:
		y_pos = y_pos+0.1 # Translação para cima
	elif key == GLUT_KEY_DOWN: 
		y_pos = y_pos-0.1 # Translação para baixo
	elif key == GLUT_KEY_PAGE_UP: 
		z_pos = z_pos+0.1 # Translação para frente
	elif key == GLUT_KEY_PAGE_DOWN:
		z_pos = z_pos-0.1 # Translação para trás

	glutPostRedisplay()


if __name__ == "__main__":
	main()