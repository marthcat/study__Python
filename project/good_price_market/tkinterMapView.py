import sys
import tkinter
from tkinter import Listbox
from tkinter import constants
from tkintermapview import TkinterMapView
from pymysql_worker import Pymysql_worker


class GoodPriceMarketApp(tkinter.Tk):
  ## https://github.com/TomSchimansky/TkinterMapView/blob/main/examples/map_view_demo.py
  APP_NAME = "map_view_demo.py"
  WIDTH = 800
  HEIGHT = 750


  def __init__(self, *args, **kwargs):
    tkinter.Tk.__init__(self, *args, **kwargs)
    self.title(self.APP_NAME)
    self.geometry("%dx%d" % (self.WIDTH, self.HEIGHT))

    # sql 준비
    self.sql = Pymysql_worker(host = '127.0.0.1', user = 'root', password = '1234', db = 'teamprj', charset='utf8')


    # 종료 버튼 설정
    # 윈도우 창 x 버튼
    self.protocol("WM_DELETE_WINDOW", self.on_closing) # WM Protocol : 윈도우 창 제어 프로토콜

    # 유닉스 상 종료
    if sys.platform == "darwin":  
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)

    # 위젯 그리드 설정
    self.grid_columnconfigure(0, weight=0)
    self.grid_columnconfigure(1, weight=1)
    # self.grid_columnconfigure(2, weight=0)
    self.grid_rowconfigure(1, weight=1)

    # 위젯 설정
    ## 리스트 박스
    self.listbox = Listbox(width=26,height = 6, bd=2)
    self.listbox.grid(row=0, column=0, padx=5, pady=5)
    for i in ['전체보기', '한식','중식','경양식, 일식','기타 외식업(다방, 패스트푸드 등)']:
      self.listbox.insert(constants.END, i)  
    self.listbox.bind('<<ListboxSelect>>', self.event_for_listbox)

    ## 우상단 라벨 영역
    self.label1 = tkinter.Label(fg = 'black', bg = 'white',relief="groove", justify='left', anchor='w',  text = '원하시는 음식점을 골라주세요')
    self.label1.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    ## 중심 맵 
    self.map_widget = TkinterMapView(width=self.WIDTH, height=600, corner_radius=0)
    self.map_widget.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew") ### nsew: 사방으로 고정
    self.map_widget.set_position(37.5560837, 126.9860765)
    self.map_widget.set_zoom(12)
    
    ## 맵 마커 몰고
    self.marker_list = []
    self.marker_path = None

  def event_for_listbox(self, item):
    ## 이전 마커 삭제
    self.clear_marker_list()

    ## 신규 마커 추가


    pass

  def clear_marker_list(self):
      for marker in self.marker_list:
          self.map_widget.delete(marker)

      self.marker_list_box.delete(0, tkinter.END)
      self.marker_list.clear()
      self.connect_marker()


  def start(self):
      self.mainloop()

  def on_closing(self):
    self.destroy()
    exit()

if __name__ == "__main__":
    app = GoodPriceMarketApp()
    app.start()