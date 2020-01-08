import sys
import os
import string

def int_input():
    string = input()
    if not string:
        return (-10)
    elif (len(string) == 1) and (string[0] == '0'):
        return (0)
    else:
        try:
            numb = int(string)
            return (numb)
        except ValueError:
            return (-10)

psql = 'psql '
location = '-h localhost '
db_name = 'test_db '
user = 'test_user '

team=''

main_query = psql + location + db_name + user


'''
    list of standard queries
    they will be called  from func 'out_std_queries'
'''

std_queries = {
    1 : '../sql/std_queries/out_devices.sql',
    2 : '../sql/std_queries/out_employees.sql',
    3 : '../sql/std_queries/out_instrument.sql',
    4 : '../sql/std_queries/out_laptops.sql',
    5 : '../sql/std_queries/out_printers.sql',
    6 : '../sql/std_queries/out_projects.sql',
    7 : '../sql/std_queries/out_team_info.sql',
    8 : '../sql/std_queries/out_team_members.sql'
}


'''
    list of special queries
    they will be called  from func 'out_spec_queries'


    WARNING: printer query must added with parameters ':palette' and ':format'
'''

spec_queries = {
    1 : '''psql -h localhost test_db test_user -f ../sql/spec_queries/out_my_team_members.sql -v team_name="\'''',
    2 : '''psql -h localhost test_db test_user -f ../sql/spec_queries/out_next_deadlines.sql -v team_name="\'''',
    3 : '''psql -h localhost test_db test_user -f ../sql/spec_queries/out_all_team_projects.sql -v team_name="\'''',
    4 : '''psql -h localhost test_db test_user -f ../sql/spec_queries/out_free_laptops.sql''',
    5 : '''psql -h localhost test_db test_user -f ../sql/spec_queries/out_free_instrument.sql''',
    6 : '''psql -h localhost test_db test_user -f ../sql/spec_queries/out_var_printers.sql '''
}


'''
    This function get users query-choice between all standard queries
'''  

def out_std_queries():
    os.system('clear')
    print(
'''   list of tables
-------------------------
 1 | devices
 2 | employees
 3 | instrument
 4 | laptops
 5 | printers
 6 | projects
 7 | team_info
 8 | team_members
 
 print '9' for exit
 print '-1' for exit from this menu
    ''')
    choice = -10
    while  choice == -10:
        choice = int_input()
        if (choice == -10):
            print('''Invalid Number
 Press ENTER to coninue''')
            input()
    if choice == 9:
        raise SystemExit
    if choice == -1:
        return
    if (choice < 1) or (choice > 8):
        print('''There no choice like this
 Press ENTER to coninue''')
        input()
        out_std_queries()
        return 
    minor_query = main_query + '-f ' + std_queries[choice]
    os.system(minor_query)
    print(''' Press ENTER to coninue''')
    input()
    out_std_queries()

palette = {
    'RGB',
    'CMYK',
    'WB',
    'other'
}

paper_format={
    'A1',
    'A2',
    'A3',
    'A4',
    'A5',
    'custom'
}


'''
    This function get users choices about printers paper format and color palette
'''  

def out_print():
    os.system('clear')
    print(''' Enter the paper format (A1, A2, A3, A4, A5, custom):''')
    format = input()
    if (format not in paper_format):
        print ("    There is no paper like this\n Press ENTER to coninue")
        input()
        return
    
    print(''' Enter the color palette (RGB, CMYK, WB, other):''')
    palette = input()
    if (palette not in palette):
        print ("    There is no palette like this\n Press ENTER to coninue")
        input()
        return
    minor_query = spec_queries[6] + '-v format="\'' + format + '\'"' + ' -v palette="\'' + palette + '\'"'
    print(minor_query)
    os.system(minor_query)
    print(''' Press ENTER to coninue''')
    input()


'''
    This function get users query-choice between all special queries
    If user choose printer-query, this function call out_print function
'''    

def out_spec_queries():
    os.system('clear')
    print(
'''   list of special queries
-----------------------------------------------------
 1 | information about your teammates
 2 | information about next deadlines of your team
 3 | information about all projects of your team
 4 | information about free laptops, you can use
 5 | information about free instruments, you can use
 6 | information about printers in office
 
 print '9' for exit
 print '-1' for exit from this menu
    ''')
    choice = -10
    while  choice == -10:
        choice = int_input()
        if (choice == -10):
            print('''Invalid Number
 Press ENTER to coninue''')
            input()
    if choice == 9:
        raise SystemExit
    if choice == -1:
        return
    if (choice < 1) or (choice > 6):        
        print('''There no choice like this
 Press ENTER to coninue''')
        input()
    else:
        if choice == 6:
            out_print()
        else :
            minor_query = spec_queries[choice]
            os.system(minor_query)
            print(''' Press ENTER to coninue''')
            input()
    out_spec_queries()

'''
    This function get users query-choice between std and spec queries (look in the head of document)
'''

def main_choice():
    os.system('clear')
    print('''   Choose queries you want to display:
-------------------------
 1 | standard queries (all information without redaction)
 2 | special queries (special redacted information)
 
 print '9' for exit
''')
    choice = -10
    while  choice == -10:
        choice = int_input()
        if (choice == -10):
            print('''Invalid Number
 Press ENTER to coninue''')
            input()
    if choice == 9:
        raise SystemExit
    if (choice < 1) or (choice > 2):
        print('''There no choice like this
 Press ENTER to coninue''')
        input()
        main_choice()
        return
    if choice == 1:
        out_std_queries()
    if choice == 2:
        out_spec_queries()
    main_choice()

'''
    This function get name of team, check it, fill call of sql-query and call main_choice function
'''

def main_info():
    os.system('psql -h localhost test_db test_user -f ../sql/std_queries/out_team_info.sql > .team_base')
    os.system('clear')
    f = open('.team_base')
    all_file = f.read()
    f.close()
    print(all_file)
    print(''' Enter your team''')
    team = input()
    if all_file.find('| ' + team + '''
''') == -1:
        print('ERROR: There is no team with this name')
        exit()
#adding team_name to sql_scripts
    spec_queries[1] +=  team + '\'"'
    spec_queries[2] +=  team + '\'"'
    spec_queries[3] +=  team + '\'"'
    main_choice()
    
main_info()