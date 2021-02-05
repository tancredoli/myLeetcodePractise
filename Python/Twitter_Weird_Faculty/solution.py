def weirdFaculty(v:list):
    rs_me = 0
    rs_fd = 2 * sum(v)-len(v)
    if rs_me > rs_fd:
        return 0

    for i in range(len(v)):
        if v[i] == 0:
            rs_me -=1
            rs_fd +=1
        else:
            rs_me +=1
            rs_fd -=1
        if rs_me > rs_fd:
            return i + 1

if __name__ == '__main__':
    print(weirdFaculty( [1, 0, 0, 1, 0]))
    print(weirdFaculty( [1, 0, 0, 1, 1]))
    print(weirdFaculty( [1, 1, 1, 0, 1]))