import csv
import os

def read_csv_demo(file_path):
    if not os.path.exists(file_path):
        print(f"文件{file_path}不存在")
        return
    
    try:
        with open(file_path,mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get('Name','unkonwn')
                age = row.get('Age','unknown')
                print(f"name: {name}, age: {age}")

    except FileNotFoundError:
        print("file not found")
    except UnicodeDecodeError:
        print("编码错误")
    except csv.Error as e:
        print(f"csv处理出错: {e}")
    except Exception as e:
        print(f"未知错误: {e}")

def write_csv_demo(file_path,data):
    if not data:
        print("没有数据可以写入")
        return

    fieldnames = data[0].keys()

    try:
        with open(file_path,mode='w', newline='') as f:
            writer = csv.DictWriter(f,fieldnames=fieldnames)

            # 写入表头
            writer.writeheader()

            writer.writerows(data)
        print(f"数据成功写入到：{file_path}")

    except PermissionError:
        print(f"no permission to write {file_path}")
    except Exception as e:
        print(f"写入过程中发生错误：{e}")

if __name__ == '__main__':
    test_file = 'data_demo.csv'

    sample_data = [
        {"Name":"jojo","Age":26,"City":"AAA"},
        {"Name":"doait","Age":27,"City":"jdiasj"},
        {"Name":"jjdao","Age":28,"City":"fdjoafj"}
    ]

    write_csv_demo(test_file,sample_data)

    read_csv_demo(test_file)