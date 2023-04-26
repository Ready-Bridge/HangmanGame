def solution(L) :
  dic = dict()
  for i in L :
    if i in dic :
      dic[i] += 1
    else :
      dic[i] = 1

  test = max(dic.values())
  l = []

  for key, values in dic.items() :
    if test == values :
      l.append(key)

  if test == 1 or test == len(L) :
    return "최빈값은 없음"
    
              
  else :      
    result = '최빈값은: '
    for re in l :
      result += (str(re) + '! ')
    
    return result
