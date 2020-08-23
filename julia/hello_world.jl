# This calls the function with "Hello, World!" amd prints the first arg supplied via terminal cmd line. 

function f(str)
    println(str)
end

f("Hello, World!")

print("Also print the following from the command line \n")

try 
    println(ARGS[1])
catch x
    println("ERROR! The script expects one command line argument!")
end
