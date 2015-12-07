all:
	gcc -shared -fpic floyd.cpp -o floyd.so -I/usr/include/python3.4m -L/usr/lib/python3.4/config-3.4m-x86_64-linux-gnu -lpython3.4 -lstdc++
