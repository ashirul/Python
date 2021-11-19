def main():
    x,y = 1000,100
    if(x<y):
        st = "x is less than y"
    elif(x==y):
        st = "x is same as y"
    else:
        st = "x is greater than y"
    print(st)

    st1 = "x is less than y" if(x<y) else "x is greater or as same as y"
    print(st1)

if __name__ == "__main__":
    main()

