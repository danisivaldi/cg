import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Escalas do objeto
scalex = scaley = scalez = 1.0

# Posicionamento do objeto
x_pos = y_pos = z_pos = 0.0

# Posição e velocidade de rotação
obj = 0.0
obj_speed = 10.0

# Definição dos formatos de objetos
TEAPOT = 1
TORUS = 2
CONE = 3

format = TEAPOT

# Rendering inicial
rendering = GL_SMOOTH

# Propriedades do material
def setMaterial() :
    no_mat = [ 0.0, 0.0, 0.0, 1.0 ]
    mat_diffuse = [ 0.1, 0.5, 0.8, 1.0 ]
    mat_specular = [ 1.0, 1.0, 1.0, 1.0 ]
    high_shininess = [ 100.0 ]

    glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
    glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess);
    glMaterialfv(GL_FRONT, GL_EMISSION, no_mat);


# Inicializa a luz
def initLighting() :
    # Informa que irá utilizar iluminação    
    glEnable(GL_LIGHTING)
    # Liga a luz
    glEnable(GL_LIGHT0)
    # Informa que irá utilizar as cores do material
    glEnable(GL_COLOR_MATERIAL)


# Posição da luz
def setLight() :
    light_position = [10.0, 10.0, -20.0, 0.0]
    ligth_ambient = [0.2, 0.2, 0.2, 1.0]
    light_difuse = [0.7, 0.7, 0.7, 1.0]
    light_specular = [0.7, 0.7, 0.7, 1.0]


    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ligth_ambient)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ligth_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_difuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)


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

    initLighting()

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

    # Definição da projeção ortogonal
    glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0)

    setLight()
    setMaterial()
    glShadeModel(rendering)
    
    # Cores do objeto    
    glColor3f(0.4, 0.9, 0.2)

    glTranslatef(x_pos, y_pos, z_pos)
    glScalef(scalex, scaley, scalez)
    glRotate(obj, 0, 0, 1)

    # Projeta a figura
    if format == TEAPOT:
        glutSolidTeapot(0.5)
    elif format == TORUS:
        glutSolidTorus(0.25, 0.75, 50, 50)
    elif format == CONE:
        glutSolidCone(0.5, 1.5, 50, 25)

    glutSwapBuffers()


def keyPressed(key, x, y):
    
    # Conversão da tecla para UTF8
    key = key.decode("utf-8")
    
    global scalex, scaley, scalez, obj, obj_speed, format
    
    # Saída do programa
    if key == 'q':
        exit()
    
    # Aumenta a escala do objeto
    elif key == 'i':
        scalex = scaley = scalez = scalex+0.1

    # Diminui a escala do objeto
    elif key == 'o':
        if scalex > 0.2:
            scalex = scaley = scalez = scalex-0.1

    # Espelhamento em x, y
    elif key == 'y':
        scalex = scalex * -1
    elif key == 'x':
        scaley = scaley * -1
    
    # Rotação anti-horária
    elif key == 'r':
        obj = obj + obj_speed
        obj =  obj % 360

    # Rotação horária
    elif key == 't':
        obj = obj - obj_speed
        obj =  obj % 360

    # Mudança do formato do objeto
    elif key == '1':
        format = TEAPOT
    elif key == '2':
        format = TORUS
    elif key == '3':
        format = CONE

    elif key == '5':
    	rendering = GL_SMOOTH
    elif key == '6':
    	rendering = GL_FLAT

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

