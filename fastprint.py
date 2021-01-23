import time
def pr(st, delay=1):
	for line in st.splitlines():
	    print(line)
	    time.sleep(delay)

