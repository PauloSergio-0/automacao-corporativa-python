from service.sistema_corporativo import Sistema

if __name__ == "__main__":
    sistema = Sistema()
    sistema.acessar_site()
    sistema.pagina_consulta()
    
    for i in ('01389187246234', '030158952186','029905612135','029900752119','030158022186','030573652135','030162522119'):
        # Sistema.limpar_Consulta()
        ele = sistema.consultar(i)
        print(ele)

