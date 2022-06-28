import tkinter as tk
import random
import time
from tkinter import messagebox as mb

# 카드 맞추기 게임 (신경쇠약)
게임화면 = tk.Tk()
게임화면.title('카드 맞추기 게임')
게임화면.geometry("400x450")

card1 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card1))
card1.place(x = 0, y = 0, width = 100, height = 100)
card2 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card2))
card2.place(x = 100, y = 0, width = 100, height = 100)
card3 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card3))
card3.place(x = 200, y = 0, width = 100, height = 100)
card4 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card4))
card4.place(x = 300, y = 0, width = 100, height = 100)

card5 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card5))
card5.place(x = 0, y = 100, width = 100, height = 100)
card6 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card6))
card6.place(x = 100, y = 100, width = 100, height = 100)
card7 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card7))
card7.place(x = 200, y = 100, width = 100, height = 100)
card8 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card8))
card8.place(x = 300, y = 100, width = 100, height = 100)

card9 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card9))
card9.place(x = 0, y = 200, width = 100, height = 100)
card10 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card10))
card10.place(x = 100, y = 200, width = 100, height = 100)
card11 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card11))
card11.place(x = 200, y = 200, width = 100, height = 100)
card12 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card12))
card12.place(x = 300, y = 200, width = 100, height = 100)

card13 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card13))
card13.place(x = 000, y = 300, width = 100, height = 100)
card14 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card14))
card14.place(x = 100, y = 300, width = 100, height = 100)
card15 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card15))
card15.place(x = 200, y = 300, width = 100, height = 100)
card16 = tk.Button(master = 게임화면, font = ('Arial', 10), command=lambda:event_open(card16))
card16.place(x = 300, y = 300, width = 100, height = 100)

colors = { 0:'pink', 1:'red', 2:'blue', 3:'green', 4:'yellow', 5:'purple', 6:'orange', 7:'skyblue' }

cards = [
  card1,card2,card3,card4,
  card5,card6,card7,card8,
  card9,card10,card11,card12,
  card13,card14,card15,card16
]

cardInfos = []
def getCardInfo(card) :
  for oneCardInfo in cardInfos:
    if card == oneCardInfo[0]:
      return oneCardInfo

def checkEnd():
  for oneCardInfo in cardInfos :
    if oneCardInfo[2] is False :
      return

  mb.showinfo("클리어!")
  init()

def init() :
  global cardInfos 

  lst = list(range(16))
  random.shuffle(lst) 

  card1.config(bg='gray', activebackground= colors[ lst[0] % 8 ])
  card2.config(bg='gray', activebackground= colors[ lst[1] % 8 ])
  card3.config(bg='gray', activebackground= colors[ lst[2] % 8 ])
  card4.config(bg='gray', activebackground= colors[ lst[3] % 8 ])
  card5.config(bg='gray', activebackground= colors[ lst[4] % 8 ])
  card6.config(bg='gray', activebackground= colors[ lst[5] % 8 ])
  card7.config(bg='gray', activebackground= colors[ lst[6] % 8 ])
  card8.config(bg='gray', activebackground= colors[ lst[7] % 8 ])
  card9.config(bg='gray', activebackground= colors[ lst[8] % 8 ])
  card10.config(bg='gray', activebackground= colors[ lst[9] % 8 ])
  card11.config(bg='gray', activebackground= colors[ lst[10] % 8 ])
  card12.config(bg='gray', activebackground= colors[ lst[11] % 8 ])
  card13.config(bg='gray', activebackground= colors[ lst[12] % 8 ])
  card14.config(bg='gray', activebackground= colors[ lst[13] % 8 ])
  card15.config(bg='gray', activebackground= colors[ lst[14] % 8 ])
  card16.config(bg='gray', activebackground= colors[ lst[15] % 8 ])

  cardInfos.clear()
  # cardInfos = []
  for i in range(16) :
    cardInfos.append([cards[i], lst[i], False])

#####################################################################

work = False
checkingCardInfo = None
def event_open(card) :
  global checkingCardInfo
  global work

  # 카드 정보 확인
  cardInfo = getCardInfo(card)

  #isFind 확인
  if cardInfo[2] : # 예외 : 혹시 모를 체크된 카드를 확인한다.
    return
  elif checkingCardInfo == cardInfo  :
    return
  elif work :
    return

  work = True  
  if checkingCardInfo is None :
    checkingCardInfo = cardInfo
    card.config(bg=colors[cardInfo[1] % 8 ] )
  else : #--- 두번째 카드 선택 ---
    cardInfo[0].config(bg=colors[ cardInfo[1] % 8 ])
    # 카드비교
    if (checkingCardInfo[0] != cardInfo[0]) & (checkingCardInfo[1] % 8 == cardInfo[1] % 8 ) :
      checkingCardInfo[2] = True
      cardInfo[2] = True
      checkEnd()
    else :
      time.sleep(1)
      checkingCardInfo[0].config(bg='gray')  
      cardInfo[0].config(bg='gray')    
    checkingCardInfo = None

  work = False

#####################################################################

init()

게임화면.mainloop()