st = [0,1, '', 2, ' ', 3, ' ', 4, ' ', 5, ' ', 6, ' ', 7, ' ', 8, ' ', 9, ' ', 10, ""]
t = 0
b = 1

print(st)
for l in range(10):
    st.clear()
    for i in range(10):
        t += 1
        st.append(t * b)
        e = t * b
        if e < 10:
            st.append(" ")
        else:
            st.append("")
    t = 0
    print(b,st)
    b += 1