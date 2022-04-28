from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(0,20,0,20)
    glColor3f(128.0,0.0, 0.0)
    glPointSize(10.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
def bresenham(x1,y1,x2,y2):
    
    #hitung dx dan dy
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    #hitung p 
    p = 2 * dy - dx
    duady = 2 * dy
    duadydx = 2 * (dy - dx)
    
    #tentukan titik awal dan akhir
    if (x1 > x2):
        x = x2
        y = y2
        xend = x1
    else:
        x = x1
        y = y1
        xend = x2
    
    #gambar titik awal
    glBegin(GL_POINTS)
    glVertex2i(x, y)

    #perulangan untuk menggambar titik-titik 
    while (x < xend):
        x = x+1
        if (p < 0):
            p += duady
        else:
            if (y1 > y2):
                y = y-1
            else:
                y = y+1
            p += duadydx
        glVertex2i(x, y

    glEnd()
    glFlush()

def main():
    #Menu pilihan
    pilih = 0
    while (pilih != 2):
        pilih = input("Pilih\n\t1. Baris Baru\n\t2. Keluar\n")
        if int(pilih) == 1: #no 1 berarti untuk mengisi nilai x1,y1,x2,y2
            x1 = int(input("x1: "))
            y1 = int(input("y1: "))
            x2 = int(input("x2: "))
            y2 = int(input("y2: "))
            print("Menampilkan hasil....")
            glutInit(sys.argv)#inisialisasi glut
            glutInitWindowSize(620,460)#inisialisasi ukuran layar glut
            glutInitWindowPosition(0,0)#inisiasliasi posisi layar glut
            glutCreateWindow("Bresenham Algoritma")#inisialisasi pembuatan windo
            glutInitDisplayMode(GLUT_RGB)#inisialisasi tipe display glut
            glutDisplayFunc(lambda: bresenham(x1,y1,x2,y2))
            glutIdleFunc(lambda: bresenham(x1,y1,x2,y2))
            init()
            glutMainLoop()
        else:
            print("Invalid pilih")
            pilih = 0

main()