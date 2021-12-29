times = int(input('Для перевода в формат ЧЧ:ММ:СС введите количество секунд - '))
hour: int = 0
mim: int = 0
if times >= 60:
    mim = times // 60
    sec = times % 60
    if mim >= 60:
        hour = mim // 60
        mim = mim % 60
        print(f'Время - {hour}:{mim}:{sec}')
    else:
        print(f'Время - {hour}:{mim}:{sec}')
else:
    sec = times % 60
    print(f'Время - {hour}:{mim}:{sec}')
