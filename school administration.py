import csv
def write_into_csv(info_list):
    with open('student_infi_csv', 'a' , newline='') as csv_files:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name" , "Age" ,"Contact Number" , "Email"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while(condition):
        student_info = input("Enter student's info for student #{} in following format(Name Age Contact_Number Email):".format(student_num))

        student_info_list = student_info.split(' ')

        print("\n The entered info is -\n Name: {} \n Age: {} \n Contact_number: {} \n Email: {}"
              .format(student_info_list[0] , student_info_list[1] , student_info_list[2] , student_info_list[3]))

        choice_check = input(" Is entered info correct ?  (yes/no): ")

        if choice_check == "yes":
            condition = True
            student_num = student_num + 1

        elif choice_check == "no":
            print("\n Please re-enter the values!!")
            
                                                                                                                               
                                                                                                                               

                                                                                                                               
