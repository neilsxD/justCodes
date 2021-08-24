from _main_CF import main 

file1 = open("in.txt","r+") 
file1.seek(0)
inputs = file1.readlines()
file2 = open("out.txt","r+") 
file2.seek(0)
outputs = file2.readlines()
outputs = list(map(lambda x : x.split('\n')[0] , outputs))

i=-1
def iterinput(*args):
    global i
    i+=1
    return inputs[i].split('\n')[0]


def test_something_that_involves_user_input(monkeypatch):
    ans = []
    monkeypatch.setattr('builtins.input', iterinput)
    monkeypatch.setattr('builtins.print', lambda x : ans.append(x))
    main()
    ans = list(map(str,ans))
    
    assert ans == outputs
# done

