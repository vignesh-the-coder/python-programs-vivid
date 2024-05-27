def join_middle(join_name,finish_name):
    return join_name[0:len(join_name)//2]+finish_name+join_name[len(join_name)//2:]

def main():
    # testcase input
    testcases = int(input())
    
    # looping through testcases
    while(testcases > 0):
        string = input().split()
        bound_by = string[0]
        tag_name = string[1]
        
        testcases -= 1
        
        print (join_middle(bound_by, tag_name))

if __name__ == '__main__':
    main()
    