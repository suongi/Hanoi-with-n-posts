disk = int(input("Please input the number of disks: "))
post = int(input("Please input the number of posts: "))
bits = premask = 0
m = post - 1
while m > 0:
    m = m >> 1
    bits += 1
    premask = (premask << 1) + 1
message = []
lenth_message_item = post * (post - 1) // 2 + 4
""" message_item=message[step]=[status, next-step should be, the choices of next-step from this status,
all choice*[post_f, post_t], the moved into this status] """

def set_top(status, top):
    posts = []
    for i in range(post):
        top.append(disk + 1)
        posts.append(i)
    i = 0
    while i < disk:
        disk_post = status & premask
        if disk_post in posts:
            top[disk_post] = i + 1
            posts.remove(disk_post)
        status = status >> bits
        i += 1

def rightset(status):
    top = []
    set_top(status, top)
    feature_post = {}
    for i in range(1, disk + 1):
        if i in top:
            feature_post[status >> (i - 1) * bits & premask] = 0
            top.remove(i)
    for i in range(1, disk + 1):
        post_number = status >> (i - 1) * bits & premask
        if post_number in feature_post:
            feature_post[post_number] += (1 << (i - 1) * bits)
    feature_sorted = sorted(list(feature_post.values()))
    status1 = 0
    post_index = post - 1
    while feature_sorted != []:
        apost_feature = feature_sorted.pop()
        status1 += apost_feature * post_index
        post_index -= 1
    if status >> (disk - 1) * bits & premask == 0:
        status1 += 1 << disk * bits
    return status1
    
def set_message(step, status):
    message_templet = []
    for i in range(lenth_message_item):
        message_templet.append([])
    if step >= len(message):
        message.append(message_templet)
    top = []
    set_top(status, top)
    message[step][0] = status
    message[step][1] = 0
    movable = 0
    for i in range(post):
        for j in range(1, post):
            k = (i + j) % post
            if top[i] < top[k]:
                movable += 1
                message[step][2 + movable] = [i, k]
    message[step][2] = movable

def finish(status):
    compare = status & premask
    ret = True
    for i in range(1, disk):
        status = status >> bits
        if status & premask != compare:
            ret = False
            break
    return ret

def printway(step, post_d):
    def swap_post(k_0):
        if k_0 == post_d:
            k_0 = post - 1
        elif k_0 == post - 1:
            k_0 = post_d
        return k_0
    _post = []
    for i in range(post):
        _post.append([])
    for i in range(post):
        _post[i].append(disk + 1)
    for i in range(disk):
        _post[0].append(disk - i)
    print("at begining:")
    for i in range(post):
        print(_post[i][1:], end='  ')
    print()
    for i in range(step):
        moved = message[i][message[i][1] + 2]
        print("%3dfrom%dto%d:"%(_post[moved[0]][len(_post[moved[0]]) - 1], (swap_post(moved[0]) + 1), (swap_post(moved[1]) + 1)), end=' ')
        _post[moved[1]].append(_post[moved[0]].pop())
        for j in range(post):
            if j != post_d:
                print(_post[j][1:], end='  ')
        print(_post[post_d][1:])

def forward():
    step = 0
    min_step = 10000
    status = 0
    statuslist = [rightset(status)]
    income = []
    newstep = True
    while step > -1:
        if newstep:
            set_message(step, status)
            message[step][lenth_message_item - 1] = income
            newstep = False
        elif message[step][1] == message[step][2]:
            step -= 1
            statuslist.pop()
            continue
        message[step][1] += 1
        post_f = message[step][message[step][1] + 2][0]
        post_t = message[step][message[step][1] + 2][1]
        income = [post_f, post_t]
        top_f = 1
        status = message[step][0]
        while True:
            if status & premask == post_f:
                break
            status = status >> bits
            top_f += 1
        mask = premask << ((top_f - 1) * bits)
        bit_change = post_t << ((top_f - 1) * bits)
        status = (message[step][0] & ~mask) + bit_change
        if rightset(status) not in statuslist:
            if finish(status):
                printway(step + 1, post_t)
                if step < min_step - 1:
                    min_step = step + 1
                step -= 1
                statuslist.pop()
            elif step < min_step - 2:
                statuslist.append(rightset(status))
                step += 1
                newstep = True
    print("min_step=", min_step)

import time
begintime = time.time()
forward()
usetime = time.time() - begintime
print("usetime: {:.3f} seconds".format(usetime))