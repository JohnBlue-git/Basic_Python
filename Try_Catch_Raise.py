# Auther: John Blue
# Time: 2023/2
# Platform: 
# Object: display how to use try, catch, and raise

def file_func():
    try:
        # reading the file
        fo = open("abc.txt", "r")
        result=list()
        for line in open('test.txt'):
            line = fo.readline().split('\t')
        print(line)
        m = len(line) / 2 + 1
        del line[int(m)]
        print(line)
        result.append(line)
        print(result)
        fo.close()
        
        # writing the file
        fo = open("abc.txt", 'w')
        print ("filename: ", fo.name)
        str = ['a','\t','112','\t','112','\t']
        for i in range(5):
            fo.write(str[i])
        fo.write('\n')
        fo.writelines( str )
        fo.write('\n')
        fo.close()
    except FileNotFoundError:
        raise FileNotFoundError()

if __name__ == "__main__":
    # try block
    print("Try Catch block >>")
    try:
        myNumbers = [1, 2, 3]
        print(myNumbers[10])
    except:    
        print("Something went wrong.")    
    finally:            
        print("The 'try catch' is finished.")

    # try block
    print("Throws >>")
    try:
        file_func();
    except FileNotFoundError:    
        print("File not found.")
    except:
        print("Something went wrong.")    
    #except (RuntimeError, TypeError, NameError):
    finally:            
        print("The 'throw' is finished.")
