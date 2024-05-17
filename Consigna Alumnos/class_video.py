from datetime import datetime

class Video:
    def __init__(self, titulo: str, vistas: int, tiempo: int, url_youtube: str, fecha_lanzamiento: str) -> None:
        self.titulo: str = titulo
        self.vistas: int = vistas
        self.tiempo: int = tiempo
        self.url_youtube: str = url_youtube
        self.fecha_lanzamiento: str = fecha_lanzamiento
        self.sesion = None
        self.colaborador = None
        self.codigo_url = None
    
    def __lt__(self, item):
        return self.sesion < item.sesion
    
    def __gt__(self, item):
        return self.sesion > item.sesion

        
    def mostrar_tema(self) -> None:
        #Agregar los datos pertinentes para que a la hora de mostrar se vean los datos completos del video
        print(f"Titulo: {self.titulo}")
        print(f"Sesión: {self.sesion}")
        print(f"Colaborador: {self.colaborador}")
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Código de URL: {self.codigo_url}")
        print(f"Fecha de Lanzamiento: {self.fecha_lanzamiento.strftime("%d-%m-%Y")}")
        print("*"*30)

    def dividir_titulo(self) -> None:
        #Debe setear el atributo sesion y colaborador con los datos obtenidos del 
        #titulo del video
        titulo_lista: list[str] = self.titulo.split(" | ")
        self.colaborador: str = titulo_lista[0]
        self.sesion: str = titulo_lista[1]
    
    def obtener_codigo_url(self) -> None:
        #Debe setear el atributo codigo_url con el codigo obtenido del atributo url_youtube
        #Por ej: si la url es https://www.youtube.com/watch?v=nicki13 
        #el codigo seria nicki13
        self.codigo_url: str = self.url_youtube.split("=")[1]
    
    def formatear_fecha(self) -> None:
        #Necesitamos que la fecha de lanzamiento sea un objeto de la clase datetime (investigar).
        #Para ello deberán dividir la fecha (en formato string) en dia, mes y año y a partir de 
        #esos datos, crear la nueva fecha. 
        lista_fecha: list[str] = self.fecha_lanzamiento.split("-")
        self.fecha_lanzamiento: datetime = datetime(int(lista_fecha[0]), int(lista_fecha[1]), int(lista_fecha[2]))
        
    def normalizar_objetos(self, lista_videos: list) -> None:
        for video in lista_videos:
            video.dividir_titulo()
            video.obtener_codigo_url()
            video.formatear_fecha()
            self.normalizado = True
        
    def mostrar_lista_temas(self, lista_videos: list) -> None:
        for video in lista_videos:
            video.mostrar_tema()
        
            
    def ordenar_temas(self, lista_videos: list) -> None:
        for video in lista_videos:
            lista_videos.sort()
        
            
    def promedio_vistas(self, lista_videos: list) -> None:
        suma_vistas = 0
        for video in lista_videos:
            suma_vistas += video.vistas
        promedio: float = suma_vistas / len(lista_videos)
        promedio = promedio / 1000
        promedio = round(promedio)
        print(f"El promedio de las vistas de los videos es: {promedio}k vistas")
        
            
    def maxima_reproduccion(self, lista_videos: list) -> None:
        lista_maximos: list[Video] = []
        lista_maximos.append(lista_videos[0])
        maximo = lista_videos[0].vistas
        for video in lista_videos:
            if video.vistas > maximo:
                maximo = video.vistas
                lista_maximos.clear()
                lista_maximos.append(video)
            elif video.vistas == maximo:
                lista_maximos.append(video)
            
        print("Los videos con mayor cantidad de reproducciones son: ")
        self.mostrar_lista_temas(Video, lista_maximos)
            
    def busqueda_por_codigo(self, lista_videos: list, codigo: str) -> None:
        for video in lista_videos:
            if video.codigo_url.count(codigo) > 0:
                video.mostrar_tema()
            
            
    def listar_por_colaborador(self, lista_videos: list, colaborador: str) -> None:
        for video in lista_videos:
            if video.colaborador == colaborador:
                video.mostrar_tema()
            
            
    def listar_por_mes(self, lista_videos: list, mes: str) -> None:
        match mes.lower():
            case "enero":
                mes = 1
            case "febrero":
                mes = 2
            case "marzo":
                mes = 3
            case "abril":
                mes = 4
            case "mayo":
                mes = 5
            case "junio":
                mes = 6
            case "julio":
                mes = 7
            case "agosto":
                mes = 8
            case "septiembre":
                mes = 9
            case "octubre":
                mes = 10
            case "noviembre":
                mes = 11
            case "diciembre":
                mes = 12
            case _:
                mes = 0
        for video in lista_videos:
            if mes == video.fecha_lanzamiento.month:
                video.mostrar_tema()
            