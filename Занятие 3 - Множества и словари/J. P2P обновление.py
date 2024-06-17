n, k = map(int, input().split())

timeslots = [0]*(n) # таймслоты по устройствам для ответа, нулевое устр-во удалить перед ответом
obnov_v_seti = {}  # {0:1, 1:1, 2:1} изначально все части по одной, все на нулевом устройстве
obnov_na_ustr_list = {}  # {устр-во: [колич, set(0, 1, 2, 3)]} словарь с множ-м номеров обнов не на устройстве
prioriteti = {} # {устр-во: {устр. приоритета: приоритет}}

for i in range(n):
    if i == 0:
        obnov_na_ustr_list[i] = [k, {}]
    else:
        obnov_na_ustr_list[i] = [0, set(i for i in range(k))]
                                
    for j in range(n):
        if i != j:
            if i in prioriteti:  # заполняем приоритеты нулевыми знач-ми
                prioriteti[i][j] = 0
            else:
                prioriteti[i] = {j:0}

for i in range(k):  # заполняем боновления в сети
    obnov_v_seti[i] = 1

final_marker = k*n

while sum(obnov_v_seti.values()) < final_marker: # пока в сети колич обн < n*k
    # ФОРМИРОВАНИЕ ЗАПРОСОВ
    obnov_v_seti_work = sorted(obnov_v_seti.items(), key=lambda t: t[1]) # сортировка для перебора
    obnov_na_ustr_list_work = sorted(obnov_na_ustr_list.items(), key=lambda t: t[1][0]) # сортировка для выбора в запросах
    zaprosi = {} # {донор: (реципиент, обнова, приоритет, колич обн)}

    for i in obnov_na_ustr_list:
        if obnov_na_ustr_list[i][0] < k:
            for j in obnov_v_seti_work:
                if j[0] in obnov_na_ustr_list[i][1]:
                    for m in obnov_na_ustr_list_work:
                        if m[1][0] > 0:
                            if j[0] not in m[1][1]:
                                timeslots[i] += 1
                                if m[0] not in zaprosi:
                                    zaprosi[m[0]] = (i, j[0], prioriteti[m[0]][i], obnov_na_ustr_list[i][0])
                                else:
                                    if zaprosi[m[0]][2] < prioriteti[m[0]][i]:
                                        zaprosi[m[0]] = (i, j[0], prioriteti[m[0]][i], obnov_na_ustr_list[i][0])
                                    elif zaprosi[m[0]][2] == prioriteti[m[0]][i]:
                                        if zaprosi[m[0]][3] > obnov_na_ustr_list[i][0]:
                                            zaprosi[m[0]] = (i, j[0], prioriteti[m[0]][i], obnov_na_ustr_list[i][0])
                                break
                    else:
                        continue
                    break

    # ЗАПРОСЫ СФОРМИРОВАНЫ
    # УДОВЛЕТВОРЕНИЕ ЗАПРОСОВ
    for z in zaprosi:
        ustroistvo = zaprosi[z][0]
        obnova = zaprosi[z][1]
        prir = zaprosi[z][2]
        obnov_cnt = zaprosi[z][3]

        
        obnov_v_seti[zaprosi[z][1]] +=1
        obnov_na_ustr_list[ustroistvo][0] += 1
        obnov_na_ustr_list[ustroistvo][1].remove(obnova)
        prioriteti[ustroistvo][z] += 1

timeslots.pop(0)

print(*timeslots)

'''
Суть:
1. ЗАПРОСЫ ОБНОВЛЕНИЙ
    1) количество обнов на устройствах и в сети
    2) устр-во выбирает отсутств обнову(Приоритет: меньше в сети => номер обновы(min))
    3) устр-во запрашивает выбр обновуу устр-ва, которое его имеет (Приоритет: устр-во с наим колич обновлений => номер устр-ва (min))
2. УДОВЛЕТВОРЕНИЕ ЗАПРОСОВ УСТРОЙСТВАМИ
    Устр-во выбирает кому дать обнову. Приоритеты:
    1. Более ценное устройство (Дало донору больше обновлений)
    2. Устр-во с наименьшим колич обнов
    3. наименьший номер устройства
'''
