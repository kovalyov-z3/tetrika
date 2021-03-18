
intervals = { 
  'lesson': [1594663200, 1594666800], 
  'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472], 
  'tutor': [1594663290, 1594663430, 1594663443, 1594666473] 
}


def appearance(intervals):
    '''
    Данную задачу я предлагаю решить таким образом:
    1)Получить множества, состоящие из секунд с шагом 1 для времени урока,
    преподавателя и ученика(вместе с последней секундой)
    2)Найти длину пересечения этих множеств
    '''
    lesson = set()
    pupil = set()
    tutor = set()
    # объявляем множества для каждого интервала
    
    lesson = set(range(intervals['lesson'][0], intervals['lesson'][1] + 1))
    # Составляем множество, состоящее из секунд урока (с последней)
    
    for i in range(0, len(intervals['pupil']), 2):
        pupil = pupil | set(range(intervals['pupil'][i], intervals['pupil'][i+1]+1))
        #Составляем множество для секунд присутствия ученика,
        #для этого каждые два интервала загоняем во множество и объединяем их
        
    for i in range(0, len(intervals['tutor']), 2):
        tutor = tutor | set(range(intervals['tutor'][i], intervals['tutor'][i+1]+1))
        #аналогичные действия для преподавателя
        
    
    return len(lesson & pupil & tutor) # возвращаем длину пересечения
    
'''
Проверка:

print(appearance(intervals))
'''
