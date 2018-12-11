# -*- coding: utf-8 -*-
from git import Repo
import datetime, time

#リポジトリのパスを指定
repo = Repo('/Users/murabayashi/code/testq')
branch_name = "master"

#コミット頻度を出力
# with open("csv/" + branch_name + "_commit_frequency.csv", "w") as file:
#     print('hexsha,messege_summary,author,author_mail,authored_day,committer,committer_mail,committed_day',file=file)
#     for item in repo.iter_commits(branch_name, max_count=1000 ,max_parents=1): #直近の件数を指定
#         dt_author = datetime.datetime.fromtimestamp(item.authored_date).strftime("%Y-%m-%d")
#         dt_commit = datetime.datetime.fromtimestamp(item.committed_date).strftime("%Y-%m-%d")
#         message = item.summary
#         message = message.replace('\n', '').replace('\r', '').replace(',', '')
#         print("%s, %s, %s, %s, %s, %s, %s, %s " % (item.hexsha, message, item.author, item.author.email, dt_author, item.committer, item.committer.email, dt_commit),file=file)


#コミット毎のファイル変更量を出力
with open("csv/" + branch_name + "_file_modify_line.csv", "w") as file:
    print('hexsha,author,author_mail,committer,committer_mail,authored_date,file_name,insertions,deletions,lines,messege_summary',file=file)
    for item in repo.iter_commits(branch_name,'src/', max_count=1000, max_parents=0): #直近の件数を指定
        file_list = item.stats.files
        for file_name in file_list:
            dt = datetime.datetime.fromtimestamp(item.authored_date).strftime("%Y-%m-%d") #日付の形式を指定
            insertions = file_list.get(file_name).get('insertions')
            deletions = file_list.get(file_name).get('deletions')
            lines = file_list.get(file_name).get('lines')
            message = item.summary
            message = message.replace('\n', '').replace('\r', '').replace(',', '')
            print("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (item.hexsha, item.author, item.author.email, item.committer, item.committer.email,dt, file_name, insertions, deletions, lines,message),file=file)

#ファイル毎の変更頻度を出力
# with open("csv/" + branch_name + "_file_modify_frequency.csv", "w") as file:
#     print('file_name,commit_count',file=file)
#     file_list = {}
#     for item in repo.iter_commits(branch_name, since='6 months ago' ,max_parents=1): #直近のコミット時期を指定
#         for fileName in item.stats.files:
#             if fileName not in file_list:
#                 file_list[fileName] = []
#             author = {}
#             author[item.author] = datetime.datetime.fromtimestamp(item.authored_date).strftime("%Y-%m-%d %H:%M:%S")
#             file_list[fileName].append(author)

#     for fileName in file_list:
#         print("%s,%d" % (fileName, len(file_list[fileName])),file=file)
