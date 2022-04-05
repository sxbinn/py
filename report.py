import turtle as t
from importlib import reload
t.title('국기 그리기')

while True:
    flag=input('국기를 그릴 국가를 입력하세요: ')
    
    if flag=='호주':
        import AUS
        continue
    elif flag=='인도':
        import INDIA
        continue
    elif flag=='대한민국':
        import KOREA
        continue
    elif flag=='말레이시아':
        import MALAYSIA
        continue
    elif flag=='영국':
        import UK
        continue
    elif flag=='미국':
        import USA
        continue
    elif flag=='고수빈':
        import ME
        continue
    elif flag=='전부':
        reload(AUS)
        reload(INDIA)
        reload(KOREA)
        reload(MALAYSIA)
        reload(UK)
        reload(USA)
        reload(ME)
        continue
    else:
        print('다시 입력해주세요.')