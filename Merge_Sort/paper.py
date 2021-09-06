N = 8
num_list = [
    [1,1,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1],
    [0,0,0,0,1,1,0,0],
    [0,0,0,0,1,1,0,0],
    [1,0,0,0,1,1,1,1],
    [0,1,0,0,1,1,1,1],
    [0,0,1,1,1,1,1,1],
    [0,0,1,1,1,1,1,1]
]

# num = [white_num, blue_num]
def blue_white(l_x,r_x,u_y,d_y,num, num_list):
    
    if (r_x - l_x) == 1:
        num[num_list[u_y][l_x]] += 1

        print(l_x,r_x,u_y,d_y,num)
        return num
    
    temp = num_list[u_y][l_x]

    for i in range(u_y, d_y):
        for j in range(l_x,r_x):
            if temp != num_list[i][j]:
                num_1 = blue_white(l_x,(r_x+l_x)//2,u_y,(u_y+d_y)//2,num, num_list)
                num_2 = blue_white((r_x+l_x)//2,r_x,u_y,(u_y+d_y)//2,num, num_list)
                num_3 = blue_white((r_x+l_x)//2,r_x,(u_y+d_y)//2,d_y,num, num_list)
                num_4 = blue_white(l_x,(r_x+l_x)//2,(u_y+d_y)//2,d_y,num, num_list)

                num[0] += (num_1[0] + num_2[0] + num_3[0] + num_4[0])
                num[1] += (num_1[1] + num_2[1] + num_3[1] + num_4[1])
                
                print(l_x,r_x,u_y,d_y,num)
                return num 

    num[num_list[u_y][l_x]] += 1
    print(l_x,r_x,u_y,d_y,num)
    return num

print(blue_white(0,N,0,N,[0,0], num_list))