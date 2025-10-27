# This entire file will be ignored by Pylint. pylint: skip-file

"""
შექმენით პროგრამა რომელიც წაიკითხავს ორ ფაილს ამ ჩანაწერებს გააერთიანებს და ჩაწერს მესამე ფაილში
"""

with open("task10/file1.txt", "r") as file1, open(
    "task10/file2.txt", "r"
) as file2, open("task10/merged_file.txt", "w") as merged_file:
    content1 = file1.read()
    content2 = file2.read()

    merged_file.write(content1 + content2)
