from termcolor import colored
import subprocess
import re
import csv
import zpl
from zebra import Zebra
import pymysql
imageArt = """....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
........,,,,,,,,,,,,,,,,,,,,,,,.....................................................................
......+$$$$$$$$$$$$$$$$$$$$$$$$?,...;+++++;,..........,:,...........................................
.....,#@??#################@$*$@*...?######$:.........:$%,..........................................
.....:#%..*@#?,,,,,,,,,,:###:.:#?...?#?:::%#?.,::::,.,;#$:,.::::,...................................
.....:#%..*@#%::::::::::;###:.:#?...?#*...+#%.*#$$#%:*#$$$%,$$$$$*..................................
.....:##??##############@##@$?$@?...?#*...+#%.,,,,?#*,;#$::.,,,:$$,.................................
.....:###@##############*:;$@@#@?...?#*...+#%.,;++?#*.:#$,..:+++$$:.................................
.....:################@+:%*:###@?...?#*...+#%,%#%?%#*.:#$,.;#$??$$:.................................
.....:###############@?,$@$,$##@?...?#*...*#%,$$,.+#*.:#$..*#*..$$:.................................
.....:##############@$,?@#;;###@?...?#$%%%##+,$$+;%#*.,$#+;*#%;+$#:.................................
.....:#########@#$%%%:*@%:;####@?...*%%%%%?+,.*$$%?%+..+%$?:%$$??%,.................................
.....:#########?:,...;@?,*#####@?..............,,........,,..,,.....................................
.....:#######$;.....:$+.;@#####@?...,,,,,,................................+%+.,:,...................
.....:######$:.....,?:...+#####@?...*$$$$$%+..............................*#*.?#+...................
.....:######:......:,.....?@###@?...?#%**%#$,.............................*#*.;*:...................
.....:####@?..............,$###@?...?#*..,$$:.;?%%*:.,+?%%?+?*..:?+.;?%%?:*#*.+?:.**+%%?:.,*%%*+?:..
.....:#####:...............*@##@?...?#*..:$#::#$**#%,+#$**?;$$,.*#+:#$**?;+#*.?#;,$#?*%#?.?#%**$#;..
.....:####$,......+*:......;$%#@?...?#$%%$#%,*#*..%#:?#+....?#+.%$,+#?....*#*.?#;,$$:.;#%.%#;..%#;..
.....:####%......;@@$,.....:;.$@?...?#%?##+,.*#$%%$#:?#+....;#?:#?.*#*....*#*.?#;,$$:.;#%.%#;..?#;..
.....:####%......+@@#,.....:;.$@?...?#*.?#?..*#?;;;;,?#+....,%$*#;.*#*....*#*.?#;,$$:.;#%.%#;..?#;..
.....:####$......,?$+......;+.$@?...?#*.:$#+.+#?,..,.?#*,,,,.+#$%,.+#%,,,,*#*.?#;,$$:.;#%.%#+,,%#;..
.....:#####:.......,.......*+.:;:...?#*..+#$:,%#$$$%,;$#$$$;.,$#*..:$#$$$++#*.?#;,$#:.;#%.*#$$%$#;..
.....:##$$#*..............,$+.......:;:...:;:.,;++;:..:;++;,.,%$:...,;++;,,;:.:;,.:;,.,;:..:++:?#;..
.....:#@;.$#,.............+@+.;+:............................;#?..........................,,..:$#:..
.....:#@;.$@+............,$#;.#@?............................%#;..........................;$$$$#*...
.....:#@;.$@+.............,,.,+*;............................::...........................,+++;:....
.....:#@;.$@+.?;......:+,...........+*.;;+??+*,;*.+;.+??+++.;;:???:*,..:?:.*;.+:*??+................
.....,++,.$@+.$#,,*+,,%%,,%$;.++;...?#;+*?*:,?;*$:%:.?*:,?$;+*?+,,:$,..*%?.%$:?+%;:$,...............
.....,??:.%#+.**,;@#,,::.:@@+.#@?...?*%*+?%?:+?***?..?%?:?*%*+%::%;%,.,%+%,?+??;%:.%:...............
.....:#@+..,.....;@#,:#$,,??:.*?+...?;;#+?*:,,$*:#+..?*:,?;;#+?+:%+$;:;%+%+%,*#;%;:$,...............
.....,;;,.?%;.;;,:??,:#$,...........+:.*;+?*+.*:,*,..+?*++:.*;:*?*:****;.:++,,*:+**;................
..........?$;.$#,,::.,::.:$$;.%#*...................................................................
.....,$$;.....::.:#$,:$%,,??:,$#?...................................................................
.....,*?:.:;,.?%,,,,.,?*,,++:.,,,...................................................................
..........%#+.;+,........:##;.......................................................................
..........,,,.............,,........................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
...................................................................................................."""

print(colored(imageArt, 'blue'))
# this function pulls cpu info
def cpu_Info():
    global brand
    global code
    global type
    global gen
    global clock
    cpu_output = subprocess.check_output("grep -m 1 'model name' /proc/cpuinfo", shell=True)
    try:
        if 'Intel' in str(cpu_output):
            brand = 'Intel'
            if 'i3-' in str(cpu_output) or 'i5-' in str(cpu_output) or 'i7-' in str(cpu_output) or 'i9-' in str(cpu_output):
                typeGrab = re.findall('i\d-', str(cpu_output))[0]
                type = re.findall('(.*?)-', str(typeGrab))[0]
                codeGrab = re.findall(f'(?<={type}-).*', str(cpu_output))[0]
                code = re.findall('(.*?) CPU', str(codeGrab))[0]
                clockGrab = re.findall('(?<=@ ).*', str(cpu_output))[0]
                clockFind = re.findall('(.*?)z', str(clockGrab))[0]
                clock = f'{clockFind}z'
                try:
                    genFind = re.findall('\d\d\d\d\d', str(code))[0]
                    gen = genFind[0:1]
                    print(21)
                    print(genFind)
                except:
                    genFind = re.findall('\d\d\d\d', str(code))[0]
                    if genFind[0] == '1':
                        gen = '1st'
                    elif genFind[0] == '2':
                        gen = '2nd'
                    elif genFind[0] == '3':
                        gen = '3rd'
                    else:
                        gen = f'{genFind[0]}th'

                print(f'Processor: {brand} {type}-{code} {clock}')
                print(f'Gen: {gen}')
                find_cpu()
    except:
        print(cpu_output)
        disk_check()


# this function pulls the amount of ram in device
def ram_pull():
    global brandPc
    global modelPc
    global serial
    global ram_actual

    ram_output = subprocess.check_output("sudo dmidecode --type 19", shell=True)
    try:
        ram = re.findall("(?<=Range Size).*", str(ram_output))
        ram_actual = re.findall("\d+ GB", str(ram))[0]
        print(f'Ram: {ram_actual}')
    except:
        print(ram_output)
    serial_output = subprocess.check_output("sudo dmidecode -s system-serial-number", shell=True)
    serialFix = re.findall('(.*?)\\\\', str(serial_output))[0]
    serial = re.findall('(?<=\').*', str(serialFix))[0]
    print(f'Serial Number: {serial}')
    modelInfoPull = subprocess.check_output("sudo dmidecode -t system", shell=True)
    brandInfoGrab = re.findall('(?<=Manufacturer: ).*', str(modelInfoPull))[0]
    brandPc = re.findall('(.*?)\\\\', str(brandInfoGrab))[0]
    print(brandPc)
    if brandPc == 'LENOVO':
        pcModelGrab = re.findall('(?<=Version: ).*', str(modelInfoPull))[0]
        modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
        print(modelPc)
    if brandPc == 'HP':
        pcModelGrab = re.findall('(?<=Product Name: HP).*', str(modelInfoPull))[0]
        modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
        print(modelPc)
    if brandPc == 'Hewlett-Packard':
        pcModelGrab = re.findall('(?<=Product Name: HP).*', str(modelInfoPull))[0]
        modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
        brandPc = 'HP'
        print(modelPc)
    if brandPc == 'ASUSTeK COMPUTER INC.':
        pcModelGrab = re.findall('(?<=Version: ).*', str(modelInfoPull))[0]
        modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
        brandPc = 'Asus'
        print(modelPc)
    if brandPc == 'Apple Inc.':
        pcModelGrab = re.findall('(?<=Version: ).*', str(modelInfoPull))[0]
        modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
        brandPc = 'Apple'
        print(modelPc)
    if brandPc == 'Apple':
        pcModelGrab = re.findall('(?<=Version: ).*', str(modelInfoPull))[0]
        modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
        brandPc = 'Apple'
        print(modelPc)
    if brandPc == 'Apple Computer, Inc.':
        pcModelGrab = re.findall('(?<=Version: ).*', str(modelInfoPull))[0]
        modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
        brandPc = 'Apple'
        print(modelPc)
    #    if brandPc == 'Hewlett-Packard':
    #       pcModelGrab = re.findall('(?<=Manufacturer: Hewlett-Packard).*', str(modelInfoPull))[0]
    #      modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
    if brandPc == 'Dell Inc.':
        pcModelGrab = re.findall('(?<=Product Name: ).*', str(modelInfoPull))[0]
        modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
        brandPc = 'Dell'
        print(modelPc)
    if brandPc == 'SAMSUNG ELECTRONICS CO., LTD.':
        pcModelGrab = re.findall('(?<=Product Name: ).*', str(modelInfoPull))[0]
        modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
        brandPc = 'Samsung'
        print(modelPc)
    if brandPc == 'TOSHIBA':
        pcModelGrab = re.findall('(?<=Product Name: ).*', str(modelInfoPull))[0]
        modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
        brandPc = 'Toshiba'
        print(modelPc)
    if brandPc == 'Acer':
        pcModelGrab = re.findall('(?<=Product Name: ).*', str(modelInfoPull))[0]
        modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
        brandPc = 'Acer'
        print(modelPc)
    # if brandPc == 'Apple Inc.':
    # pcModelGrab = re.findall('(?<=Product Name: ).*', str(modelInfoPull))[0]
    # modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
    # brandPc = 'Apple'
    # print(modelPc)
    if brandPc == 'Dynabook Inc.':
        pcModelGrab = re.findall('(?<=Product Name: ).*', str(modelInfoPull))[0]
        modelPc = re.findall('(.*?)\\\\', str(pcModelGrab))[0]
        brandPc = 'Dynabook'
        print(modelPc)
    # if brand pc is not found, it will be set to 'Other'
    if brandPc != 'LENOVO' and brandPc != 'HP' and brandPc != 'Hewlett-Packard' and brandPc != 'ASUSTeK COMPUTER INC.' and brandPc != 'Apple Inc.' and brandPc != 'Apple' and brandPc != 'Apple Computer, Inc.' and brandPc != 'Dell Inc.' and brandPc != 'SAMSUNG ELECTRONICS CO., LTD.' and brandPc != 'TOSHIBA' and brandPc != 'Acer' and brandPc != 'Apple Inc.' and brandPc != 'Dynabook Inc.':
        brandPc = 'Other'
        modelPc = 'Other'
        print('Other')
    #return brandPc, modelPc
    inputPrompts()

def inputPrompts():
    global caddyActual
    global crackedScreenActual

    ramPrompt = input('Did you need to insert Ram into device? (y/n): ')
    print(ramPrompt)
    if ramPrompt == 'y':
        ram_actual = '0 GB'
        print(ram_actual)
    caddyPrompt = input('Is a drive caddy present? (y/n): ')
    print(caddyPrompt)
    if caddyPrompt == 'y':
        caddyActual = "1"
        print(caddyActual)
    else:
        caddyActual = "0"
    crackedScreenPrompt = input('Is the screen cracked? (y/n): ')
    print(crackedScreenPrompt)
    if crackedScreenPrompt == 'y':
        print(214)
        crackedScreenActual = "1"
        print(crackedScreenActual)
        print(216)
    else:
        print(218)
        crackedScreenActual = "0"
    print('218')
    sql_input()

# this checks storage size
def disk_check():
    global sizesql_input
    global diskList
    diskList = []
    disk_output = subprocess.check_output("sudo lshw -class disk> file.csv", shell=True)
    try:
        productOmit = 'product: SanDisk 3.2Gen1'
        sizeOmit = '61 GB'
        with open('file.csv') as file:
            fileReader = csv.reader(file)
            for row in fileReader:
                if 'product:' in str(row):
                    productInfo = str(row)
                elif 'size' in str(row) and productOmit not in productInfo:
                    try:
                        sizeConfig = re.findall('(?<=size: ).*', str(row))[0]
                        size = re.findall('\d+GB', str(sizeConfig))[0]
                        diskList.append(size)

                    except:
                        pass
        print(f'Storage: {size}')
        battery_test()
    except:
        print(disk_output)
    ram_pull()

def battery_test():
    subprocess.check_output('upower -i /org/freedesktop/UPower/devices/battery_BAT0 > "battery test.csv"', shell=True)
    subprocess.check_output('grep -h -i "energy-full-design" "battery test.csv"', shell=True)
    subprocess.check_output('grep -h -i "energy-full:" "battery test.csv"', shell=True)
    subprocess.check_output('grep -h -i "energy:" "battery test.csv"', shell=True)
    with open("battery test.csv") as fileGrab:
        file = csv.reader(fileGrab)
        for row in file:
            try:
                if 'energy-full:' in str(row):
                    enFull = re.findall('(?<=energy-full: ).*', str(row))[0]
                    enNew = re.findall('(.*?)Wh', str(enFull))[0]
                    num = re.findall('\d+.\d+', str(enNew))[0]
                    print(f'energy full: {num}Wh')
                elif 'energy-full-design:' in str(row):
                    enFullDesign = re.findall('(?<=energy-full-design: ).*', str(row))[0]
                    fullDes = re.findall('(.*?)Wh', str(enFullDesign))[0]
                    fullNum = re.findall('\d+.\d+', str(fullDes))[0]
                    print(f'full design: {fullNum}Wh')
                elif 'capacity:' in str(row):
                    capacityFind = re.findall('(?<=capacity: ).*', str(row))[0]
                    capacityDes = re.findall('(.*?)%', str(capacityFind))[0]
                    capacityNum = re.findall('\d+.\d+', str(capacityDes))[0]
                    if float(capacityNum) < 70:
                        print(colored(f'Capacity: {capacityNum}%', 'red'))
                    else:
                        print(colored(f'Capacity: {capacityNum}%', 'green'))
            except:
                print(str(row))

#_______________________________SQL STATEMENTS__________________________________________________________________________
def find_cpu():
    global isListable
    sqlCon = pymysql.connect(host="71.233.26.0", port=3306, user="Admin", password="Seekonk123",
                             database="inventory", charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cur = sqlCon.cursor()
    cur.execute(f"SELECT `Listable` FROM `cpu` WHERE `Brand` = '{brand}' and `Type` = '{type}' and `Code` = '{code}'")
    listableFetch = cur.fetchall()
    if listableFetch == ():
        if brand == 'Intel':
            if gen == '1st' or gen == '2nd' or gen == '3rd':
                isListable = 'False'
            else:
                isListable = 'True'
        cur.execute(f"INSERT INTO `cpu` (`Brand`, `Type`, `Code`, `Speed`, `Gen`, `typeCode`, `Listable`) VALUES ('{brand}', '{type}', '{code}', '{clock}', '{gen}', {type}-{code}, '{isListable}') ")
        sqlCon.commit()
        disk_check()
    else:
        for listable in listableFetch:
            for key, val in listable.items():
                if key == 'Listable':
                    isListable = val
                    if isListable == "True":
                        disk_check()
                    else:
                        print(179)

def sql_input():
    print('304')
    if isListable == "True":
        if len(diskList) == 0:
            storageInfo = 'No'
        else:
            storageInfo = 'Yes'
        print('317')
        sqlCon = pymysql.connect(host="71.233.26.0", port=3306, user="Admin", password="Seekonk123",
                                 database="inventory", charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        cur = sqlCon.cursor()
        print('322')
        cur.execute(f"INSERT INTO `pc inventory` (`Brand`, `Model Pulled`, `Cpu Brand`, `Type Code`, `storage`, `Serial Number`, `ram`, `Caddy Present`, `Cracked Screen`) VALUES ('{brandPc}', '{modelPc}','{brand}', '{type}-{code}', '{storageInfo}', '{serial}', '{ram_actual}', '{caddyActual}', '{crackedScreenPrompt}')")
        sqlCon.commit()
        print('324')
        cur2 = sqlCon.cursor()
        cur2.execute(f"SELECT CAST(`index` AS CHAR(6)) FROM `pc inventory` ORDER BY `index` DESC LIMIT 0,1")
        pcGrab = cur2.fetchall()
        for pc in pcGrab:
            for key, val in pc.items():
                pcNum = val
                print(pcNum)
        sqlCon.close()
        zebra_print(pcNum)

def zebra_print(pc):
    z = Zebra('Zebra_Technologies_ZTC_LP_2824_Plus')
    l = zpl.Label(25, 25)
    l.origin(0, 12)
    l.write_text(f"PC{pc}", char_height=4, char_width=2, line_width=40, justification='C')
    l.field_orientation('N')
    l.endorigin()
    l.origin(24, 8)
    l.write_text(len(diskList), char_height=4, char_width=2, line_width=40)
    l.endorigin()
    l.origin(16, 15)
    l.barcode('Q', f'PC{pc}', magnification=4),
    z.output(l.dumpZPL())


cpu_Info()