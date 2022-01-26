disk = int(input("Please input the number of disks: "))
post = int(input("Please input the number of posts: "))
bits = premask = 0
m = post - 1
while m > 0:
    m = m >> 1
    bits += 1
    premask = (premask << 1) + 1

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
    
def printway(status, post_k, statuslist):
    def swap_post(k_0):
        if k_0 == 0:
            k_0 = post_k
        elif k_0 == post - 1:
            k_0 = 0
        elif k_0 == post_k:
            k_0 = post - 1
        return k_0
    _post = []
    for i in range(post):
        _post.append([])
    for i in range(post):
        _post[i].append(disk + 1)
    for i in range(disk):
        _post[post_k].append(disk - i)
    print("at begining:", end=' ')
    for i in range(post):
        print(_post[(post_k + i) % post][1:], end='  ')
    print()
    while status != 0:
        right_status = rightset(status)
        post_f = statuslist[right_status] % post
        post_t = statuslist[right_status] // post
        top_ele = []
        set_top(status, top_ele)
        if post_k == post - 1:
            print("%3dfrom%dto%d:"%(top_ele[post_f], (swap_post(post_f) + 1), (swap_post(post_t) + 1)), end=' ')
        else:
            print("%3dfrom%dto%d:"%(top_ele[post_f], (swap_post(swap_post(post_f)) + 1), (swap_post(swap_post(post_t)) + 1)), end=' ')
        _post[post_t].append(_post[post_f].pop())
        for i in range(post):
            print(_post[swap_post(i)][1:], end='  ')
        print()
        mask = premask << (top_ele[post_f] - 1) * bits
        bit_change = post_t << (top_ele[post_f] - 1) * bits
        status = (status & ~mask) + bit_change

def forward():
    message = []  
    for i in range(post + 1):
        message.append(0)
    message[1] = disk
    message = [message]
    # message-term=message[step]=[status, high-post_0~(post - 1)]
    step = 0
    this_round = 1
    status = 0
    statuslist = {rightset(status): 0}
    notfinish = True
    while notfinish:
        new_round = 0
        while this_round > 0:
            this_round -= 1
            term = message.pop()
            status = term[0]
            top_element = []
            set_top(status, top_element)
            for i in range(post):
                for j in range(1, post):
                    k = (i + j) % post
                    if top_element[i] < top_element[k]:
                        mask = premask << (top_element[i] - 1) * bits
                        bit_change = k << (top_element[i] - 1) * bits
                        new_status = (status & ~mask) + bit_change
                        right_status = rightset(new_status)
                        if right_status not in statuslist:
                            statuslist[right_status] = i * post + k
                            new_round += 1
                            new_term = [new_status]
                            for l in range(1, post + 1):
                                new_term.append(term[l])
                            new_term[i + 1] -= 1
                            new_term[k + 1] += 1
                            message.insert(0, new_term)
                            if new_term[k + 1] == disk:
                                printway(new_status, k, statuslist)
                                notfinish = False
        this_round = new_round
        step += 1
    print("step=", step)

import time
begintime = time.time()
forward()
usetime = time.time() - begintime
print("usetime: {:.3f} seconds".format(usetime))