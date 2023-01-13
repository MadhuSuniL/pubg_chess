
def id_to_num(id):
    return int(id.replace('#c',''))

def num_to_id(num):
    return str("#c"+str(num))

def reverse_id(id):
    try:
        cell = id_to_num(id)
        id = num_to_id(101-cell)
        return id
    except ValueError:
        return 'none'


def make_none(ids1,ids2):
    all = ids1 + ids2
    none_list = []
    for i in range(1,101):
        id = num_to_id(i)
        if id not in all:
            none_list.append(id)
    return none_list        



def m4_blinks(id):
    blinks = {'up':[],
              'down':[],
              'left':[],
              'right':[],
              'left_up':[],
              'left_down':[],
              'right_up':[],
              'right_down':[]
              }
    cell = id_to_num(id)
    
    cell_var = cell
    # for up cells
    while cell_var > 10:
        cell_var -= 10
        blinks['up'].append(cell_var)
    
    cell_var = cell
    # for down cells
    while cell_var < 91:
        cell_var += 10
        blinks['down'].append(cell_var)
    
    cell_var = cell
    # for left cells
    while True:
        cell_var -= 1
        if cell_var%10 == 0:
            break
        blinks['left'].append(cell_var)
    
    cell_var = cell
    # for right cells
    while True:
        if cell_var%10 == 0:
            break
        cell_var += 1
        blinks['right'].append(cell_var)
    
    cell_var = cell
    not_allowed_cells = (1,11,21,31,41,51,61,71,81,91,2,3,4,5,6,7,8,9,10)
    # for cross up left cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['left_up'].append(cell_var)
            break
        blinks['left_up'].append(cell_var)
        cell_var -= 11
    
    
    cell_var = cell
    not_allowed_cells = (10,20,30,40,50,60,70,80,90,
                         91,92,93,94,95,96,97,98,99,100)
    # for cross down right cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['right_down'].append(cell_var)
            break
        blinks['right_down'].append(cell_var)
        cell_var += 11
 
    cell_var = cell
    not_allowed_cells = (10,20,30,40,50,60,70,80,90,100,
                         1,2,3,4,5,6,7,8,9)
    # for cross up right cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['right_up'].append(cell_var)
            break
        blinks['right_up'].append(cell_var)
        cell_var -= 9
 
    cell_var = cell
    not_allowed_cells = (1,11,21,31,41,51,61,71,81,
                         91,92,93,94,95,96,97,98,99,100)
    # for cross down left cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['left_down'].append(cell_var)
            break
        blinks['left_down'].append(cell_var)
        cell_var += 9
    
    # blinks = list(set(blinks))
    # final_blinks = []
    # for num in blinks:
    #     id = num_to_id(num)
    #     final_blinks.append(id)
    
    for key in blinks:
        try:
            blinks[key].remove(cell)
        except:
            pass
        
    for key in blinks:
        if len(blinks[key]) > 7:
            blinks[key] = blinks[key][0:7]
            
    
    return blinks

# print(m4_blinks('#c1'))

def awm_blinks(id):
    blinks = {'up':[],
              'down':[],
              'left':[],
              'right':[],
              'left_up':[],
              'left_down':[],
              'right_up':[],
              'right_down':[]
              }
    cell = id_to_num(id)
    
    cell_var = cell
    # for up cells
    while cell_var > 10:
        cell_var -= 10
        blinks['up'].append(cell_var)
    
    cell_var = cell
    # for down cells
    while cell_var < 91:
        cell_var += 10
        blinks['down'].append(cell_var)
    
    cell_var = cell
    # for left cells
    while True:
        cell_var -= 1
        if cell_var%10 == 0:
            break
        blinks['left'].append(cell_var)
    
    cell_var = cell
    # for right cells
    while True:
        if cell_var%10 == 0:
            break
        cell_var += 1
        blinks['right'].append(cell_var)
    
    cell_var = cell
    not_allowed_cells = (1,11,21,31,41,51,61,71,81,91,2,3,4,5,6,7,8,9,10)
    # for cross up left cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['left_up'].append(cell_var)
            break
        blinks['left_up'].append(cell_var)
        cell_var -= 11
    
    
    cell_var = cell
    not_allowed_cells = (10,20,30,40,50,60,70,80,90,
                         91,92,93,94,95,96,97,98,99,100)
    # for cross down right cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['right_down'].append(cell_var)
            break
        blinks['right_down'].append(cell_var)
        cell_var += 11
 
    cell_var = cell
    not_allowed_cells = (10,20,30,40,50,60,70,80,90,100,
                         1,2,3,4,5,6,7,8,9)
    # for cross up right cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['right_up'].append(cell_var)
            break
        blinks['right_up'].append(cell_var)
        cell_var -= 9
 
    cell_var = cell
    not_allowed_cells = (1,11,21,31,41,51,61,71,81,
                         91,92,93,94,95,96,97,98,99,100)
    # for cross down left cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['left_down'].append(cell_var)
            break
        blinks['left_down'].append(cell_var)
        cell_var += 9
    
    # blinks = list(set(blinks))
    # final_blinks = []
    # for num in blinks:
    #     id = num_to_id(num)
    #     final_blinks.append(id)
    
    for key in blinks:
        try:
            blinks[key].remove(cell)
        except:
            pass        
    
    return blinks

# print(awm_blinks('#c1'))


def akm_blinks(id):
    blinks = {'up':[],
              'down':[],
              'left':[],
              'right':[],
              'left_up':[],
              'left_down':[],
              'right_up':[],
              'right_down':[]
              }
    cell = id_to_num(id)
    
    cell_var = cell
    # for up cells
    while cell_var > 10:
        cell_var -= 10
        blinks['up'].append(cell_var)
    
    cell_var = cell
    # for down cells
    while cell_var < 91:
        cell_var += 10
        blinks['down'].append(cell_var)
    
    cell_var = cell
    # for left cells
    while True:
        cell_var -= 1
        if cell_var%10 == 0:
            break
        blinks['left'].append(cell_var)
    
    cell_var = cell
    # for right cells
    while True:
        if cell_var%10 == 0:
            break
        cell_var += 1
        blinks['right'].append(cell_var)
    
    cell_var = cell
    not_allowed_cells = (1,11,21,31,41,51,61,71,81,91,2,3,4,5,6,7,8,9,10)
    # for cross up left cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['left_up'].append(cell_var)
            break
        blinks['left_up'].append(cell_var)
        cell_var -= 11
    
    
    cell_var = cell
    not_allowed_cells = (10,20,30,40,50,60,70,80,90,
                         91,92,93,94,95,96,97,98,99,100)
    # for cross down right cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['right_down'].append(cell_var)
            break
        blinks['right_down'].append(cell_var)
        cell_var += 11
 
    cell_var = cell
    not_allowed_cells = (10,20,30,40,50,60,70,80,90,100,
                         1,2,3,4,5,6,7,8,9)
    # for cross up right cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['right_up'].append(cell_var)
            break
        blinks['right_up'].append(cell_var)
        cell_var -= 9
 
    cell_var = cell
    not_allowed_cells = (1,11,21,31,41,51,61,71,81,
                         91,92,93,94,95,96,97,98,99,100)
    # for cross down left cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['left_down'].append(cell_var)
            break
        blinks['left_down'].append(cell_var)
        cell_var += 9
    
    # blinks = list(set(blinks))
    # final_blinks = []
    # for num in blinks:
    #     id = num_to_id(num)
    #     final_blinks.append(id)
    
    for key in blinks:
        try:
            blinks[key].remove(cell)
        except:
            pass        
        
    for key in blinks:
        if len(blinks[key]) > 3:
            blinks[key] = blinks[key][0:3]
    
    
    return blinks

# print(akm_blinks('#c1'))


def shot_blinks(id):
    blinks = {'up':[],
              'down':[],
              'left':[],
              'right':[],
              'left_up':[],
              'left_down':[],
              'right_up':[],
              'right_down':[]
              }
    cell = id_to_num(id)
    
    cell_var = cell
    # for up cells
    while cell_var > 10:
        cell_var -= 10
        blinks['up'].append(cell_var)
    
    cell_var = cell
    # for down cells
    while cell_var < 91:
        cell_var += 10
        blinks['down'].append(cell_var)
    
    cell_var = cell
    # for left cells
    while True:
        cell_var -= 1
        if cell_var%10 == 0:
            break
        blinks['left'].append(cell_var)
    
    cell_var = cell
    # for right cells
    while True:
        if cell_var%10 == 0:
            break
        cell_var += 1
        blinks['right'].append(cell_var)
    
    cell_var = cell
    not_allowed_cells = (1,11,21,31,41,51,61,71,81,91,2,3,4,5,6,7,8,9,10)
    # for cross up left cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['left_up'].append(cell_var)
            break
        blinks['left_up'].append(cell_var)
        cell_var -= 11
    
    
    cell_var = cell
    not_allowed_cells = (10,20,30,40,50,60,70,80,90,
                         91,92,93,94,95,96,97,98,99,100)
    # for cross down right cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['right_down'].append(cell_var)
            break
        blinks['right_down'].append(cell_var)
        cell_var += 11
 
    cell_var = cell
    not_allowed_cells = (10,20,30,40,50,60,70,80,90,100,
                         1,2,3,4,5,6,7,8,9)
    # for cross up right cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['right_up'].append(cell_var)
            break
        blinks['right_up'].append(cell_var)
        cell_var -= 9
 
    cell_var = cell
    not_allowed_cells = (1,11,21,31,41,51,61,71,81,
                         91,92,93,94,95,96,97,98,99,100)
    # for cross down left cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['left_down'].append(cell_var)
            break
        blinks['left_down'].append(cell_var)
        cell_var += 9
    
    # blinks = list(set(blinks))
    # final_blinks = []
    # for num in blinks:
    #     id = num_to_id(num)
    #     final_blinks.append(id)
    
    for key in blinks:
        try:
            blinks[key].remove(cell)
        except:
            pass        
        
    for key in blinks:
        if len(blinks[key]) > 1:
            blinks[key] = blinks[key][0:1]
    
    
    return blinks

# print(shot_blinks('#c1'))

def kar_blinks(id):
    blinks = {'up':[],
              'down':[],
              'left':[],
              'right':[],
              }
    cell = id_to_num(id)
    
    cell_var = cell
    # for up cells
    while cell_var > 10:
        cell_var -= 10
        blinks['up'].append(cell_var)
    
    cell_var = cell
    # for down cells
    while cell_var < 91:
        cell_var += 10
        blinks['down'].append(cell_var)
    
    cell_var = cell
    # for left cells
    while True:
        cell_var -= 1
        if cell_var%10 == 0:
            break
        blinks['left'].append(cell_var)
    
    cell_var = cell
    # for right cells
    while True:
        if cell_var%10 == 0:
            break
        cell_var += 1
        blinks['right'].append(cell_var)
    
    for key in blinks:
        try:
            blinks[key].remove(cell)
        except:
            pass        
        
    
    
    return blinks

# print(kar_blinks('#c1'))


def nade_blinks(id):
    blinks = {'up':[],
              'down':[],
              'left':[],
              'right':[],
              }
    cell = id_to_num(id)
    
    cell_var = cell
    # for up cells
    not_allowed_cells = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
    if cell_var in not_allowed_cells:
        pass
    else:
        blinks['up'].append(cell_var-20) 
    
    
    cell_var = cell
    # for down cells
    not_allowed_cells = (81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100)
    if cell_var in not_allowed_cells:
        pass
    else:
        blinks['down'].append(cell_var+20) 
    
    cell_var = cell
    # for left cells
    not_allowed_cells = (1,11,21,31,41,51,61,71,81,91,2,12,22,32,42,52,62,72,82,92)
    if cell_var in not_allowed_cells:
        pass
    else:
        blinks['left'].append(cell_var-2) 
    
    
    cell_var = cell
    # for right cells
    not_allowed_cells = (9,19,29,39,49,59,69,79,89,99,10,20,30,40,50,60,70,80,90)
    if cell_var in not_allowed_cells:
        pass
    else:
        blinks['right'].append(cell_var+2)
    
    for key in blinks:
        try:
            blinks[key].remove(cell)
        except:
            pass        
    
    
    return blinks

# print(nade_blinks('#c1'))
    

def m24_blinks(id):
    blinks = {'left_up':[],
              'left_down':[],
              'right_up':[],
              'right_down':[]
              }
    cell = id_to_num(id)
    
    
    cell_var = cell
    not_allowed_cells = (1,11,21,31,41,51,61,71,81,91,2,3,4,5,6,7,8,9,10)
    # for cross up left cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['left_up'].append(cell_var)
            break
        blinks['left_up'].append(cell_var)
        cell_var -= 11
    
    
    cell_var = cell
    not_allowed_cells = (10,20,30,40,50,60,70,80,90,
                         91,92,93,94,95,96,97,98,99,100)
    # for cross down right cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['right_down'].append(cell_var)
            break
        blinks['right_down'].append(cell_var)
        cell_var += 11
 
    cell_var = cell
    not_allowed_cells = (10,20,30,40,50,60,70,80,90,100,
                         1,2,3,4,5,6,7,8,9)
    # for cross up right cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['right_up'].append(cell_var)
            break
        blinks['right_up'].append(cell_var)
        cell_var -= 9
 
    cell_var = cell
    not_allowed_cells = (1,11,21,31,41,51,61,71,81,
                         91,92,93,94,95,96,97,98,99,100)
    # for cross down left cells
    while True:
        if cell_var in not_allowed_cells:
            blinks['left_down'].append(cell_var)
            break
        blinks['left_down'].append(cell_var)
        cell_var += 9
    
    for key in blinks:
        try:
            blinks[key].remove(cell)
        except:
            pass        

    return blinks

# print(m24_blinks('#c1'))




def get_blinks(id,img,sur):
    if 'm4.png' in img:
        res = m4_blinks(id)
        for key in sur:
            if sur[key]:
                pass
            else:
                try:
                    del res[key]   
                except:
                    pass    
    elif 'awm.png' in img:
        res = awm_blinks(id)
        for key in sur:
            if sur[key]:
                pass
            else:
                del res[key]   
    elif 'akm.png' in img:
        res = akm_blinks(id)
        for key in sur:
            if sur[key]:
                pass
            else:
                try:
                    del res[key]   
                except:
                    pass
    
    elif 'nade.png' in img:
        res = nade_blinks(id)
        for key in sur:
            if sur[key]:
                pass
            else:
                try:
                    del res[key]   
                except:
                    pass   
    
    elif 'm24.png' in img:
        res = m24_blinks(id)
        for key in sur:
            if sur[key]:
                pass
            else:
                try:
                    del res[key]   
                except:
                    pass
    
    elif 'kar.png' in img:
        res = kar_blinks(id)
        for key in sur:
            if sur[key]:
                pass
            else:
                try:
                    del res[key]   
                except:
                    pass
    else:
        res = shot_blinks(id)
        for key in sur:
            if sur[key]:
                pass
            else:
                try:
                    del res[key]   
                except:
                    pass   
    return res