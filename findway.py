#%%
import pyautogui as pag
from PIL import ImageGrab
import keyboard
import time

# %%
# 좌표찾기

x, y = pag.position()
print(x,y)

# 스킬 2번창 (1529,956), 비영사천문(1755,732), 북쪽(1673,507)
# 국내성 지도(1708,188), 마이너스(143,403), 백륜동 클릭(380,248)
# 스페이스 이후, 백륜동 6층 이동클릭(1750,822)
#%%
# 백륜동 6층 이동메크로

while 1:
    pag.click((1529,956)) # 스킬2번창 클릭
    time.sleep(0.5)       #0.5초 대기
    pag.click((1755,732))
    time.sleep(0.5)
    pag.click()
    break 

#%%
# 좌표리스트에 등록된 좌표 만큼 클릭하기

position_dict = {"skwindow_change" : (1529,956),"moveskill" : (1755,732), 
"north":(1673,507), "map" :(1708,188),"zoomout":(143,403),"dungeon":(380,248),
"backryun":(1764,827) }

def position_click(pos_dict):
    pag.click(664,1065)
    counts = 0
    for i in pos_dict:
        if counts == 6 :
            pag.press('space')
            pag.click(pos_dict[i])
            time.sleep(1)
            counts += 1
            print(counts)
            print("yes")
          
        else :
            pag.click(pos_dict[i])
            time.sleep(1)
            counts += 1
            print(counts)

#%%
# 실행시켜보기

position_click(position_dict)

# %%

# this is test
position_clicl(position_dict)