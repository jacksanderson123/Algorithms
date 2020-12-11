sample_str = "Hey jack reverse me"
new_str = ""
for i in range(len(sample_str)):
    pointer = len(sample_str) -i -1
    new_str = new_str + sample_str[pointer]

print(f"Original string {sample_str}")
print(f"Reverse string {new_str}")