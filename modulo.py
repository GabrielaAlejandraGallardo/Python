import operaciones as o

def main():
    resSUMA=o.suma(2, 2)
    print(resSUMA)
    res=o.resta(4, 2)
    print(res)
    op=o.Operador()
    print(op.multiplicacion(3,4))



if __name__=="__main__":
    main()