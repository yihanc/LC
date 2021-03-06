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


# 2018.02.26
# Similar to 157 except saving buf4, wordRead and j into instance var
#
# 
# i for buf counter
# j for buf4 counter
# for i < n: Read from buf4 only when self.j == self.wordRead
# Then copy char one by one
# if wordRead < 4, break and return i

class Solution(object):
    def __init__(self):
        self.buf4 = [ "", "", "", "" ]
        self.wordRead = 0
        self.j = 0
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        buf4 = self.buf4
        i = 0
        while i < n:
            if self.j == self.wordRead: 
                self.wordRead = read4(buf4) 
                self.j = 0
            
            while self.j < self.wordRead and i < n:
                buf[i] = buf4[self.j]
                i, self.j = i + 1, self.j + 1
            if self.wordRead < 4: break
        return i

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
        
# Rewrite online
class Solution(object):
    def __init__(self):
        self.buff4 = [ "" for x in xrange(4) ]
        self.buff4_ptr = 0
        self.buff4_cnt = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.buff4_ptr == 0:
                self.buff4_cnt = read4(self.buff4)
            
            if self.buff4_cnt == 0: break

            while i < n and self.buff4_ptr < self.buff4_cnt:
                buf[i] = self.buff4[self.buff4_ptr]
                i, self.buff4_ptr = i + 1, self.buff4_ptr + 1

            if self.buff4_ptr >= self.buff4_cnt:
                self.buff4_ptr = 0

        return i
            
            





# Self write. Too bad
class Solution2(object):
    def __init__(self):
        self.buff4 = [ "" for x in xrange(4) ]
        self.buff4_ptr = 0
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0

        print("-----", self.buff4_ptr, self.buff4)
        # Handle left
        if self.buff4_ptr > 0:
            while self.buff4_ptr < 4 and i < n:
                buf[i] = self.buff4[self.buff4_ptr]
                self.buff4_ptr += 1
                i += 1

        if i == n: return n

        # Same as call once
        while i < n:
            buff4_cnt = read4(self.buff4)
            
            self.buff4_ptr = 0
            while i + self.buff4_ptr < n and self.buff4_ptr < buff4_cnt:
                buf[i+self.buff4_ptr] = self.buff4[self.buff4_ptr]
                self.buff4_ptr += 1

            if i + self.buff4_ptr == n: return n
            if buff4_cnt < 4: return i + self.buff4_ptr
            
            i += self.buff4_ptr
            
        
if __name__ == "__main__":
    global file_content
    buf = ['' for _ in xrange(100)]
    # file_content = "a"
    # file_content = "abcdefghijklmnop"

    # Case 1
    print("---- Case 1 ---")
    file_content = "abcd"
    obj = Solution()
    obj.read(buf, 1)
    print buf[:30]
    obj.read(buf, 2)
    print buf[:30]
    obj.read(buf, 2)
    print buf[:30]

    # Case 2
    print("")
    print( "---- Case 2 ----" )
    file_content = "abcdefghijklmnopqrstuvwxyz"
    obj = Solution()
    obj.read(buf, 3)
    print buf[:30]
    obj.read(buf, 2)
    print buf[:30]
    obj.read(buf, 3)
    print buf[:30]
    obj.read(buf, 2)
    print buf[:30]
    obj.read(buf, 5)
    print buf[:30]
    obj.read(buf, 6)
    print buf[:30]

