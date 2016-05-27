

with open("/tmp/123", "r") as f:
   # print("\n".join(f.read().split("\n")[-5:]))
    print("\n".join(f.read().split("\n")[-3:]))
