from functions import salary, hello_who

assert hello_who("Max") == "Hello,Max", "hello_who error:1"
assert hello_who("Leo") == "Hello,Leo", "hello_who error:2"
assert hello_who("Nikita") == "Hello,Nikita", "hello_who error:3"
assert salary(2,1) == 4 , "salary error:1"
assert salary(2,2) == 8, "salary error:2"