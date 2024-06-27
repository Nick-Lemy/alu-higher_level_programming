#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i}{j}", end=", " if int(f"{i}{j}") < 89 else "\n")
