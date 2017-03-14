# Read N Characters Given Read4 II - Call multiple times (158)
# Loop
# 
# The API: int read4(char[] buf) reads 4 characters at a time from a file.
# 
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
# 
# By using the read4 API, implement the function int read(char[] buf, int n) that reads n characters from the file.
# 
# Note: The read function may be called multiple times.
# The API: int read4(char *buf) reads 4 characters at a time from a file.
# 
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
# 
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
# 
# Note:
# The read function will only be called once for each test case.

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1
    
    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i
        
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """



if __name__ == "__main__":
    global file_content
    buf = ['' for _ in xrange(100)]
    # file_content = "a"
    # file_content = "abcdefghijklmnop"

    # Case 1
    print("---- Case 1 ---")
    file_content = "abcd"
    obj = Solution()
    print(obj.read(buf, 1))
    print buf[:30]
    print(obj.read(buf, 2))
    print buf[:30]
    print(obj.read(buf, 2))
    print buf[:30]

    # Case 2
    print("")
    print( "---- Case 2 ----" )
    file_content = "abcdefghijklmnopqrstuvwxyz"
    obj = Solution()
    print(obj.read(buf, 3))
    print buf[:30]
    print(obj.read(buf, 2))
    print buf[:30]
    print(obj.read(buf, 3))
    print buf[:30]
    print(obj.read(buf, 2))
    print buf[:30]
    print(obj.read(buf, 5))
    print buf[:30]
    print(obj.read(buf, 6))
    print buf[:30]

