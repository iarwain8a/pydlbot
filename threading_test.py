import threading

def f(id):
    print ("thread function",id)
    return
def e():
	print ("a")
	return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f,args=(i,))
        p = threading.Thread(target=e)
        t.start()
        p.start()