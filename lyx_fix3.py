import os
def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))


width_percent=input("Choose width as % of page:  ")
override_current=input("Would you like to over-ride current formatting? reply with Y or N    ")
trim_path=input("Would you like to trim images full path? reply with Y or N    ")
path_to_file=input("Paste path to your .lyx file here:  ")

f = open(path_to_file, "r")

contents = f.readlines()
f.close()

lyx_filename_path, lyx_filename_tail=os.path.split(path_to_file)
curr_dir = os.listdir(os.getcwd())

if path_to_file.endswith('.lyx'):

    for num, line in enumerate(contents, 1):

    #for line in contents:
        if "filename" in line:
            # this is the graphic's line
            # trim path of object if it is in the same dir
            if trim_path=="Y":
                words_of_line=line.split(" ")
                for index,word in enumerate(line,1):
                    if word=="filename":
                        #check if it's long path or not
                        if str(curr_dir) in words_of_line[index+1]:
                            obj_path= words_of_line[index+1]
                            head, tail = os.path.split(obj_path)
                            #change full path to filename only, assuming it is in the same folder!!
                            words_of_line[index+1]=tail

            if override_current=="N":
                if "width" not in contents[num+1]:
                    # means it is NOT already formatted
                    print(contents[num])
                    contents.insert(num, "	width {}page%\n".format(width_percent))
                # else:
                #     # add comment to show you have been there
                #     contents[num+1]="% SKIPPED	width {}page%\n".format(width_percent)

            # OVER RIDING EXISTING FORMATTING
            else:
                if "width" in contents[num+1]:
                    # means it is not already formatted
                    contents.insert(num, "	width {}page%\n".format(width_percent))
                else:
                    # replace current with new settings
                    contents[num]="	width {}page%\n".format(width_percent)

else:
    print("It isn't a .lyx file\n")
    f.close()
    exit(1)

f = open(path_to_file, "w")
contents = "".join(contents)
#f.writelines(contents)  #possible improvement
print("{} was handled successfully ".format(lyx_filename_tail))
f.write(contents)
f.close()
